import pandas as pd

df = pd.read_csv("produtos_doados0.csv")

# converte a coluna de data para dateTime
df['Data da Doação'] = pd.to_datetime(df['Data da Doação'], format='%d/%m/%Y')

# cria a coluna ano-mes no formato AAAA-MM
df['AnoMes'] = df['Data da Doação'].dt.strftime('%Y-%m')

# salva o novo csv com essas colunas adicionais
df.to_csv("produtos_doados1.csv", index=False, encoding='utf-8-sig')
