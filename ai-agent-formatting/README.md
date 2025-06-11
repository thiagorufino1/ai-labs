# AI Code Assistant Agent

## 📋 Sobre
Agente de IA especializado em assistência à documentação e formatação de código, utilizando Azure OpenAI para processamento de linguagem natural e Black para formatação de código Python.

## 🚀 Funcionalidades

### Documentation Tool
- Extração de conteúdo de URLs de documentação
- Processamento de contexto usando Azure OpenAI
- Resposta a perguntas específicas sobre documentação técnica

### Code Formatter
- Formatação automática de código Python usando Black
- Padronização de estilo de código
- Feedback de status da operação

## 🛠️ Tools Implementadas

### documentation_tool
```python
@tool
def documentation_tool(url: str, question: str) -> str:
    """Processa documentação e responde perguntas com base no contexto."""
```

### black_formatter
```python
@tool
def black_formatter(path: str) -> str:
    """Formata arquivos Python usando o Black."""
```

## ⚙️ Configuração

### Pré-requisitos
- Python 3.12+
- Poetry
- Conta Azure com serviço OpenAI

### Variáveis de Ambiente
```properties
AZURE_OPENAI_API_KEY=sua_chave_aqui
AZURE_OPENAI_API_BASE=sua_url_base_aqui
AZURE_OPENAI_API_VERSION=2025-01-01-preview
AZURE_OPENAI_DEPLOYMENT_NAME=seu_deployment
```

## 📦 Dependências
- langchain v0.3.25+
- black v25.1.0+
- beautifulsoup4 v4.13.4+
- langchain-openai v0.3.22+
- load-dotenv v0.1.0+

## 🚀 Instalação e Uso

```bash
# Instalar dependências
poetry install

# Executar o agente
poetry run python agents.py
```

## 📁 Estrutura do Projeto
```
ai-agent-formatting/
├── agents.py         # Implementação dos agentes
├── scrapper.py      # Utilitário de extração web
├── .env             # Configurações
├── pyproject.toml   # Config Poetry
└── README.md        # Documentação
```

## 🔐 Segurança
⚠️ Nunca compartilhe suas credenciais da Azure ou commits com o arquivo .env!

## 📄 Licença
MIT