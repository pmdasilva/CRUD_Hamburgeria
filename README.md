<<<<<<< HEAD
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
=======
# Practica_Humburgueria

Projeto em Python para gerenciamento simples de um cardápio de hambúrgueres pelo terminal. A aplicação oferece cadastro, listagem, atualização e exclusão de hambúrgueres em memória, com interface de menu interativo e comandos claros.

## O que foi feito

- Criação de um menu interativo para o usuário escolher entre adicionar, listar, atualizar e excluir hambúrgueres.
- Implementação das operações básicas de CRUD:
  - `add`: inserir um novo hambúrguer com nome e preço.
  - `list`: exibir a lista de hambúrgueres cadastrados.
  - `update`: alterar o nome e/ou preço de um hambúrguer existente.
  - `delete`: remover um hambúrguer pelo número da lista.
- Uso de terminal limpo antes de cada ação para deixar a interface menos poluída e mais fácil de usar.
- Gestão dos dados em memória usando uma lista Python simples.

## Arquitetura do projeto

- `app/main.py`
  - Ponto de entrada da aplicação.
  - Loop principal que mostra o menu, lê a opção do usuário e chama as funções correspondentes.
  - Chama `utils.clear_terminal.clear_terminal()` para limpar a tela antes de cada ação.

- `app/crud/read.py`
  - Contém a função `show_menu()` responsável por exibir as opções disponíveis.

- `app/crud/insert.py`
  - Função `adding_hamburguers()` para adicionar um novo hambúrguer.
  - Função `list_humburguers()` para exibir todos os hambúrgueres cadastrados.
  - Importa `data_hamburguers` de `app/data/data.py`.

- `app/crud/update.py`
  - Função `update_list_hamburguers()` para atualizar um hambúrguer existente com base no índice.
  - Valida se o número informado está dentro do intervalo válido.

- `app/crud/delete.py`
  - Função `delete_hamburguers()` para excluir um hambúrguer.
  - Exibe a lista atualizada após a exclusão.

- `app/data/data.py`
  - Armazena a lista `data_hamburguers` usada por todo o sistema.

- `app/utils/clear_terminal.py`
  - Função `clear_terminal()` que limpa a tela de terminal de forma compatível com Windows (`cls`) e Linux/Mac (`clear`).

## Linguagem e bibliotecas utilizadas

- Linguagem principal: Python 3
- Não usa bibliotecas externas além da biblioteca padrão do Python.
- Usa o módulo `os` em `app/utils/clear_terminal.py` para executar o comando de limpar terminal.

## Funções e módulos principais

- `application()` em `app/main.py`: loop principal do aplicativo que mostra o menu e chama operações CRUD.
- `show_menu()` em `app/crud/read.py`: exibe o menu de opções para o usuário.
- `adding_hamburguers()` em `app/crud/insert.py`: adiciona um novo hambúrguer à lista.
- `list_humburguers()` em `app/crud/insert.py`: lista os hambúrgueres cadastrados.
- `update_list_hamburguers()` em `app/crud/update.py`: atualiza hambúrguer existente pelo índice.
- `delete_hamburguers()` em `app/crud/delete.py`: remove um hambúrguer pelo índice.
- `data_hamburguers` em `app/data/data.py`: armazenamento em memória dos hambúrgueres.

## Como usar

1. Execute `python app/main.py` ou `python main.py` a partir do diretório principal do projeto.
2. Escolha uma opção do menu digitando o número desejado.
3. Siga as instruções na tela para cadastrar, listar, atualizar ou excluir hambúrgueres.

## Observações

- Os dados são mantidos apenas em memória enquanto o programa estiver em execução.
- Se quiser, posso ajudar a estender o projeto para salvar os dados em arquivo ou banco de dados.

## Nota sobre atualizações de código

- A descrição do projeto no README foi atualizada para explicar melhor o propósito e o funcionamento do sistema.
- Incluí detalhes de arquitetura e fluxo de uso para facilitar a compreensão de quem for revisar o código.
- Esta nota documenta as mudanças recentes feitas na documentação, sem alterar o comportamento do código em si.
>>>>>>> 71b01cb212882e3ffc5d820d419d48c7e9282ca5
