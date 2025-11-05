import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_csv("produtos_doados1.csv")
top_10_qtd = df.groupby("Produto/Tipo")["Quantidade Entregue"].sum().nlargest(10).reset_index()
df_mes_qtd = df.groupby("AnoMes")["Quantidade Entregue"].sum().reset_index()
produtos_pizza = df.groupby("Produto/Tipo")["Quantidade Entregue"].sum().nlargest(5).reset_index()
outros = df.groupby("Produto/Tipo")["Quantidade Entregue"].sum().nsmallest(len(df["Produto/Tipo"].unique()) - 5).sum()
produtos_pizza.loc[len(produtos_pizza)] = ["Outros", outros]
qtd_data = df.groupby("Data da Doação")["Quantidade Entregue"].sum().reset_index()

# KPIs
total_qtd = df["Quantidade Entregue"].sum()
media_produto = df.groupby("Produto/Tipo")["Quantidade Entregue"].sum().mean()

# Dashboard
fig = make_subplots(
    rows=3, cols=3,
    specs=[
        [{"type": "bar"}, {"type": "bar"}, {"type": "pie"}],
        [{"type": "bar"}, {"type": "scatter"}, None],
        [{"type": "indicator"}, {"type": "indicator"}, None]
    ],
    subplot_titles=[
        "Top 10 Produtos por Quantidade", "Quantidade por Mês (AnoMes)", "Distribuição dos Produtos (Pizza)",
        "Qtd por Data da Doação", "Evolução Quantidade Doada", "",
    ]
)

fig.add_trace(go.Bar(
    x=top_10_qtd["Produto/Tipo"], y=top_10_qtd["Quantidade Entregue"], name="Top 10 Produtos"
), row=1, col=1)

fig.add_trace(go.Bar(
    x=df_mes_qtd["AnoMes"], y=df_mes_qtd["Quantidade Entregue"], name="Qtd por Mês"
), row=1, col=2)

fig.add_trace(go.Pie(
    labels=produtos_pizza["Produto/Tipo"], values=produtos_pizza["Quantidade Entregue"], name="Distribuição", hole=0, showlegend=True
), row=1, col=3)

fig.add_trace(go.Bar(
    x=qtd_data["Data da Doação"], y=qtd_data["Quantidade Entregue"], name="Qtd por Data"
), row=2, col=1)

fig.add_trace(go.Scatter(
    x=df_mes_qtd["AnoMes"], y=df_mes_qtd["Quantidade Entregue"], mode='lines+markers', name="Evolução"
), row=2, col=2)

fig.add_trace(go.Indicator(
    mode="number",
    value=total_qtd,
    title={"text": "Total de Quantidade Doadas"}
), row=3, col=1)

fig.add_trace(go.Indicator(
    mode="number",
    value=media_produto,
    title={"text": "Quantidade Média por Produto"}
), row=3, col=2)

fig.update_layout(
    height=1300,
    width=1800,
    legend=dict(orientation="h", yanchor="bottom", y=1.08, xanchor="center", x=0.5),
)
fig.update_xaxes(tickangle=45)
fig.show()
