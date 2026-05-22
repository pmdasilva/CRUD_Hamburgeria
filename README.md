# 🍔 Hamburgaria Manager

**Gerenciador de Hambúrgueres com Python e Streamlit**

'o contexto da pratica envolve uma aula que estava vendo no youtube onde apliquei os conceitos em python.'

Vídeo de Referência: https://www.youtube.com/watch?v=HG1PlFScmRw

## 📋 Funcionalidades

- ✅ **Adicionar** novos hambúrgueres
- 👀 **Listar** todos os hambúrgueres cadastrados
- ✏️ **Atualizar** dados de hambúrgueres existentes
- 🗑️ **Deletar** hambúrgueres
- 📊 **Análise** de dados com gráficos e estatísticas

## 🚀 Como Usar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar a Aplicação

```bash
streamlit run app/front-end/front.py
```

A aplicação será aberta em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
Practica_Humburgueria/
├── app/
│   ├── crud/
│   │   ├── insert.py      # Adicionar hamburguers
│   │   ├── read.py        # Listar hamburguers
│   │   ├── update.py      # Atualizar hamburguers
│   │   ├── delete.py      # Deletar hamburguers
│   │   └── main.py        # Menu principal
│   ├── data/
│   │   └── data.py        # Armazenamento de dados
│   └── front-end/
│       └── front.py       # Interface Streamlit
├── README.md
└── requirements.txt
```

## 🛠️ Tecnologias Utilizadas

- **Python** - Linguagem de programação
- **Streamlit** - Framework para criar interfaces web
- **Pandas** - Manipulação de dados e análise

## 📊 Funcionalidades da Interface

### 📋 Abas Disponíveis:

1. **➕ Adicionar** - Formulário para adicionar novo hambúrguer
2. **📋 Listar** - Visualiza todos os hambúrgueres com estatísticas
3. **✏️ Atualizar** - Modifica dados de hambúrgueres existentes
4. **🗑️ Deletar** - Remove hambúrgueres da lista
5. **📊 Análise** - Gráficos e análise de dados

### 📊 Sidebar com Informações:
- Total de hambúrgueres cadastrados
- Valor total em estoque
- Preço médio dos hambúrgueres

## 💡 Exemplos de Uso

### Adicionar um Hambúrguer:
1. Vá para a aba "➕ Adicionar"
2. Preencha o nome: "X-Burguer"
3. Preencha o preço: "12.50"
4. Clique em "✅ Adicionar Hambúrguer"

### Visualizar Análise:
1. Vá para a aba "📊 Análise"
2. Veja estatísticas e gráficos dos hambúrgueres

## 🎨 Recursos Visuais

- Interface com abas para melhor organização
- Emojis para melhor experiência de usuário
- Gráficos interativos com Pandas
- Sidebar com resumo de dados
- Validação de entrada de dados
- Mensagens de sucesso/erro

## 📝 Notas

- Os dados são armazenados em memória (lista Python)
- Para persistência de dados, considere adicionar um banco de dados (SQLite, MongoDB, etc.)
- A interface é responsiva e funciona em diferentes tamanhos de tela

## 👤 Autor

Desenvolvido como prática de Python e Streamlit

---

**🍔 Divirta-se gerenciando seus hambúrgueres! 🍔**
