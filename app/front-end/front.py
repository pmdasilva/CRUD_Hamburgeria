import streamlit as st
import sys
from pathlib import Path

# Adicionar o diretório pai ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from crud.insert import adding_hamburguers
from crud.read import list_humburguers
from crud.update import update_hamburguer
from crud.delete import delete_hamburguer
from data.data import data_hamburguers

# Configuração da página
st.set_page_config(
    page_title="🍔 Hamburgaria Manager",
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.2em;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
    }
    .error-box {
        padding: 1rem;
        background-color: #f8d7da;
        border-radius: 0.5rem;
        border-left: 4px solid #dc3545;
    }
    .info-box {
        padding: 1rem;
        background-color: #d1ecf1;
        border-radius: 0.5rem;
        border-left: 4px solid #17a2b8;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("🍔 Hamburgaria Manager")
st.markdown("### Gerenciador de Hambúrgueres com Python e Streamlit")
st.markdown("---")

# Sidebar com informações
with st.sidebar:
    st.header("📊 Informações")
    st.metric("Total de Hambúrgueres", len(data_hamburguers))
    
    if data_hamburguers:
        total_value = sum([h['price'] for h in data_hamburguers])
        st.metric("Valor Total em Estoque", f"R$ {total_value:.2f}")
        
        average_price = total_value / len(data_hamburguers)
        st.metric("Preço Médio", f"R$ {average_price:.2f}")
    
    st.markdown("---")
    st.markdown("**Desenvolvido com:**")
    st.markdown("- 🐍 Python")
    st.markdown("- 💫 Streamlit")

# Criar abas
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "➕ Adicionar",
    "📋 Listar",
    "✏️ Atualizar",
    "🗑️ Deletar",
    "📊 Análise"
])

# ==================== TAB 1: ADICIONAR ====================
with tab1:
    st.header("➕ Adicionar Novo Hambúrguer")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome_hamburguer = st.text_input(
            "Nome do Hambúrguer",
            placeholder="Ex: X-Burguer, Hambúrguer Especial...",
            key="nome_add"
        )
    
    with col2:
        preco_hamburguer = st.number_input(
            "Preço (R$)",
            min_value=0.0,
            step=0.50,
            key="preco_add"
        )
    
    col_submit, col_reset = st.columns(2)
    
    with col_submit:
        if st.button("✅ Adicionar Hambúrguer", key="btn_add", use_container_width=True):
            if nome_hamburguer.strip():
                resultado = adding_hamburguers(nome_hamburguer, preco_hamburguer)
                if resultado['status'] == 'sucesso':
                    st.success(f"✅ {resultado['mensagem']}")
                    st.success(f"🍔 {nome_hamburguer} - R$ {preco_hamburguer:.2f}")
                    st.balloons()
                else:
                    st.error(f"❌ {resultado['mensagem']}")
            else:
                st.warning("⚠️ Por favor, preencha o nome do hambúrguer!")

# ==================== TAB 2: LISTAR ====================
with tab2:
    st.header("📋 Lista de Hambúrgueres")
    
    if data_hamburguers:
        # Criar uma tabela melhorada
        st.markdown("#### Todos os Hambúrgueres Cadastrados:")
        
        # Criar colunas para exibição
        col_num, col_nome, col_preco = st.columns([0.5, 2, 1])
        
        with col_num:
            st.markdown("**#**")
        with col_nome:
            st.markdown("**Nome**")
        with col_preco:
            st.markdown("**Preço**")
        
        st.divider()
        
        for i, hamburguers in enumerate(data_hamburguers):
            col_num, col_nome, col_preco = st.columns([0.5, 2, 1])
            
            with col_num:
                st.write(f"{i + 1}")
            with col_nome:
                st.write(f"🍔 {hamburguers['name']}")
            with col_preco:
                st.write(f"R$ {hamburguers['price']:.2f}")
        
        st.divider()
        
        # Resumo
        total_value = sum([h['price'] for h in data_hamburguers])
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info(f"**Total de Itens:** {len(data_hamburguers)}")
        with col2:
            st.info(f"**Valor Total:** R$ {total_value:.2f}")
        with col3:
            st.info(f"**Preço Médio:** R$ {total_value/len(data_hamburguers):.2f}")
    else:
        st.info("📭 Nenhum hambúrguer cadastrado. Adicione um na aba 'Adicionar'!")

# ==================== TAB 3: ATUALIZAR ====================
with tab3:
    st.header("✏️ Atualizar Hambúrguer")
    
    if data_hamburguers:
        # Criar lista de opções para seleção
        opcoes = []
        for i, h in enumerate(data_hamburguers):
            opcoes.append(f"{i} - {h['name']} (R$ {h['price']:.2f})")
        
        indice_selecionado = st.selectbox(
            "Selecione o hambúrguer a atualizar:",
            options=range(len(data_hamburguers)),
            format_func=lambda x: opcoes[x]
        )
        
        st.divider()
        
        hamburguer_atual = data_hamburguers[indice_selecionado]
        
        st.markdown(f"### Hambúrguer Atual: 🍔 {hamburguer_atual['name']}")
        st.write(f"Preço Atual: R$ {hamburguer_atual['price']:.2f}")
        
        st.markdown("### Novos Dados:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            novo_nome = st.text_input(
                "Novo Nome",
                value=hamburguer_atual['name'],
                key="nome_update"
            )
        
        with col2:
            novo_preco = st.number_input(
                "Novo Preço (R$)",
                value=hamburguer_atual['price'],
                min_value=0.0,
                step=0.50,
                key="preco_update"
            )
        
        if st.button("✅ Atualizar Hambúrguer", use_container_width=True):
            if novo_nome.strip():
                # Atualizar manualmente
                data_hamburguers[indice_selecionado] = {
                    'name': novo_nome,
                    'price': novo_preco
                }
                st.success("✅ Hambúrguer atualizado com sucesso!")
                st.success(f"🍔 {novo_nome} - R$ {novo_preco:.2f}")
                st.rerun()
            else:
                st.warning("⚠️ Por favor, preencha o nome do hambúrguer!")
    else:
        st.info("📭 Nenhum hambúrguer cadastrado. Adicione um na aba 'Adicionar' antes de atualizar!")

# ==================== TAB 4: DELETAR ====================
with tab4:
    st.header("🗑️ Deletar Hambúrguer")
    
    if data_hamburguers:
        # Criar lista de opções para seleção
        opcoes = []
        for i, h in enumerate(data_hamburguers):
            opcoes.append(f"{i} - {h['name']} (R$ {h['price']:.2f})")
        
        indice_selecionado = st.selectbox(
            "Selecione o hambúrguer a deletar:",
            options=range(len(data_hamburguers)),
            format_func=lambda x: opcoes[x],
            key="delete_select"
        )
        
        st.divider()
        
        hamburguer_selecionado = data_hamburguers[indice_selecionado]
        
        st.markdown(f"### ⚠️ Hambúrguer a Deletar:")
        st.warning(f"🍔 {hamburguer_selecionado['name']} - R$ {hamburguer_selecionado['price']:.2f}")
        
        st.markdown("**Esta ação não pode ser desfeita!**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗑️ Deletar", use_container_width=True, type="secondary"):
                hamburguer_deletado = data_hamburguers.pop(indice_selecionado)
                st.success("✅ Hambúrguer deletado com sucesso!")
                st.info(f"Deletado: {hamburguer_deletado['name']}")
                st.rerun()
        
        with col2:
            st.button("❌ Cancelar", use_container_width=True, disabled=True)
    else:
        st.info("📭 Nenhum hambúrguer cadastrado para deletar!")

# ==================== TAB 5: ANÁLISE ====================
with tab5:
    st.header("📊 Análise de Dados")
    
    if data_hamburguers:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🍔 Total de Hambúrgueres", len(data_hamburguers))
        
        with col2:
            total_value = sum([h['price'] for h in data_hamburguers])
            st.metric("💰 Valor Total", f"R$ {total_value:.2f}")
        
        with col3:
            average_price = total_value / len(data_hamburguers)
            st.metric("📈 Preço Médio", f"R$ {average_price:.2f}")
        
        st.divider()
        
        # Hambúrguer mais caro e mais barato
        col1, col2 = st.columns(2)
        
        with col1:
            hamburguer_mais_caro = max(data_hamburguers, key=lambda x: x['price'])
            st.info(f"**Mais Caro:** 🍔 {hamburguer_mais_caro['name']}\nR$ {hamburguer_mais_caro['price']:.2f}")
        
        with col2:
            hamburguer_mais_barato = min(data_hamburguers, key=lambda x: x['price'])
            st.info(f"**Mais Barato:** 🍔 {hamburguer_mais_barato['name']}\nR$ {hamburguer_mais_barato['price']:.2f}")
        
        st.divider()
        
        # Gráfico de preços
        st.markdown("### 📊 Distribuição de Preços")
        
        import pandas as pd
        
        df = pd.DataFrame(data_hamburguers)
        
        # Gráfico de barras
        st.bar_chart(df.set_index('name')['price'])
        
        # Tabela de dados
        st.markdown("### 📋 Dados Detalhados")
        st.dataframe(
            df.rename(columns={'name': 'Nome', 'price': 'Preço (R$)'}),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("📭 Nenhum hambúrguer cadastrado. Adicione um para ver a análise!")

# Rodapé
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "🍔 Hamburgaria Manager v1.0 | "
    "Desenvolvido com Python e Streamlit"
    "</p>",
    unsafe_allow_html=True
)
