# 🧾 Projeto de Análise de Doações com Pandas e Plotly

## 📘 Descrição Geral

Este projeto simula uma base de **doações de produtos alimentícios** e conduz um fluxo completo de **análise e visualização** usando **Python**.  
Todo o processamento — da geração dos dados ao dashboard interativo — está automatizado em três scripts principais.

---

## 📁 Estrutura de Arquivos

├── dados.py # Geração dos dados simulados
├── app.py # Tratamento/transformação dos dados (data, AnoMes)
├── grafico_plotly.py # Dashboard interativo (Plotly)
├── produtos_doados0.csv # Dados simulados (saída do dados.py)
├── produtos_doados1.csv # Dados tratados e prontos para análise
└── requirements.txt # Lista de dependências do projeto

---

## ⚙️ Como Funciona

### 1. Criação dos dados simulados (`dados.py`)

- Gera o arquivo **`produtos_doados0.csv`**.
- Inclui produtos, datas, preços e quantidades **realistas e fictícios**.
- Garante **≥ 200 linhas** para cumprir requisitos de projeto.

---

### 2. Tratamento dos dados (`app.py`)

- Lê o CSV bruto e converte a coluna de **data** para `datetime`.
- Cria a coluna **"AnoMes"** (formato `AAAA-MM`), útil para análises temporais.
- Salva como **`produtos_doados1.csv`**.

---

### 3. Dashboard Plotly (`grafico_plotly.py`)

- Lê o CSV tratado.
- Gera **cinco gráficos analíticos**:

  1. Top 10 produtos por quantidade doada
  2. Quantidade doada por mês
  3. Distribuição dos produtos (gráfico de pizza)
  4. Quantidade por data
  5. Evolução mensal da quantidade doada

- Adiciona **dois KPIs** no rodapé:
  - Total de quantidade doada
  - Quantidade média por produto

---

## 🧩 Requisitos de Instalação

### 📦 Dependências

Antes de executar o projeto, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

💡 Dica: para manter o ambiente organizado, crie um ambiente virtual:
python -m venv venv
source venv/bin/activate # (Linux/Mac)
venv\Scripts\activate # (Windows)

Ative o ambiente virtual:

# Linux/Mac

source venv/bin/activate

# Windows

venv\Scripts\activate

▶️ Como Executar

Execute os scripts em sequência para gerar os dados, tratá-los e abrir o dashboard:

python dados.py # Gera produtos_doados0.csv
python app.py # Gera produtos_doados1.csv
python grafico_plotly.py # Abre dashboard Plotly
