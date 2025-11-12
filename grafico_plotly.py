import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import re, unicodedata

FILE_PATH = "produtos_doados0.csv"
df = pd.read_csv(FILE_PATH)

# datas
df["DataDaDoacao_dt"] = pd.to_datetime(df["Data da Doação"], format="%d/%m/%Y", errors="coerce")
df["AnoMes"] = df["DataDaDoacao_dt"].dt.to_period("M").astype(str)

# Parser para nao ter duplicações
def _norm_ascii_upper(s):
    s = str(s or "").strip()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return s.upper()

def parse_produto_tipo(s):
    raw = str(s or "").strip()
    s_bar = re.sub(r"\s*/\s*", "/", raw)
    norm = _norm_ascii_upper(s_bar)
    CLS_PAT = r"(CONVENCIONAL|ORG[ÂA]NICO)"
    SEM_PAT = r"(CLASSIFICA[ÇC][AÃ]O\s*SEM\s*CARACTER[ÍI]STICAS|SEM\s*CARACTER[ÍI]STICAS)"
    cls = ""
    base = raw
    if re.search(SEM_PAT, norm):
        base = re.sub(SEM_PAT, "", base, flags=re.IGNORECASE).strip()
        base = re.sub(r"\(\s*\)", "", base).strip()
        norm2 = _norm_ascii_upper(base)
        m_bar2 = re.search(rf"/\s*{CLS_PAT}\s*$", norm2)
        if m_bar2:
            cls_raw = m_bar2.group(1)
            cls = "CONVENCIONAL" if "CONVENCIONAL" in cls_raw else "ORGÂNICO"
            base = re.sub(r"/\s*"+m_bar2.group(1)+r"\s*$", "", base, flags=re.IGNORECASE).strip()
    else:
        m_bar = re.search(rf"/\s*{CLS_PAT}\s*$", norm)
        if m_bar:
            cls_raw = m_bar.group(1)
            cls = "CONVENCIONAL" if "CONVENCIONAL" in cls_raw else "ORGÂNICO"
            base = re.sub(r"/\s*"+m_bar.group(1)+r"\s*$", "", base, flags=re.IGNORECASE).strip()
        else:
            m_par = re.search(rf"\(\s*{CLS_PAT}\s*\)\s*$", norm)
            if m_par:
                cls_raw = m_par.group(1)
                cls = "CONVENCIONAL" if "CONVENCIONAL" in _norm_ascii_upper(cls_raw) else "ORGÂNICO"
                base = re.sub(r"\(\s*"+re.escape(cls_raw)+r"\s*\)\s*$", "", base).strip()
    base = re.sub(r"\s*\(.*?\)\s*$", "", base).strip()
    base = re.sub(r"\(\s*\)", "", base).strip()
    base = re.sub(r"\s{2,}", " ", base)
    return base, cls

# Parse
df[["ProdutoBase","Classificacao"]] = df["Produto/Tipo"].apply(lambda s: pd.Series(parse_produto_tipo(s)))

df["ProdutoBase"] = (df["ProdutoBase"]
    .str.replace(r"/\s*(CONVENCIONAL|ORG[ÂA]NICO)\s*$", "", regex=True, flags=re.IGNORECASE)
    .str.replace(r"\(\s*\)", "", regex=True)
    .str.replace(r"\s{2,}", " ", regex=True)
    .str.strip()
)

# categoria = produtoBase
df["Categoria"] = df["ProdutoBase"]

# metricas
df["Valor Doado"] = df["Quantidade Entregue"] * df["Preço Unitário R$"]

top10_qtd = (df.groupby("ProdutoBase", as_index=False)["Quantidade Entregue"].sum()
               .nlargest(10, "Quantidade Entregue").sort_values("Quantidade Entregue"))
top10_valor = (df.groupby("ProdutoBase", as_index=False)["Valor Doado"].sum()
                 .nlargest(10, "Valor Doado").sort_values("Valor Doado"))

mensal_qtd = (df.groupby("AnoMes", as_index=False)["Quantidade Entregue"].sum().sort_values("AnoMes"))
mensal_valor = (df.groupby("AnoMes", as_index=False)["Valor Doado"].sum().sort_values("AnoMes"))

mensal_class = (df.loc[df["Classificacao"] != ""]
                  .groupby(["AnoMes","Classificacao"], as_index=False)["Quantidade Entregue"].sum()
                  .sort_values(["AnoMes","Classificacao"]))

diaria_qtd = (df.groupby("DataDaDoacao_dt", as_index=False)["Quantidade Entregue"].sum()
                .sort_values("DataDaDoacao_dt"))
diaria_qtd["Acumulado"] = diaria_qtd["Quantidade Entregue"].cumsum()

base_resample = df.loc[df["DataDaDoacao_dt"].notna()].copy()
semanal_freq = (base_resample.set_index("DataDaDoacao_dt").sort_index()
                .resample("W")["ProdutoBase"].count().reset_index()
                .rename(columns={"ProdutoBase":"Registros"}))

# Treemap
agg_prod = (df.groupby(["Categoria","Classificacao","ProdutoBase"], as_index=False)[["Valor Doado"]].sum())

labels, parents, ids, values = [], [], [], []
root_id = "root"
labels.append("Doações"); parents.append(""); ids.append(root_id); values.append(float(agg_prod["Valor Doado"].sum()))

for _, r in agg_prod.groupby("Categoria", as_index=False)["Valor Doado"].sum().iterrows():
    cat = r["Categoria"]; cat_id = f"cat::{cat}"
    labels += [cat]; parents += [root_id]; ids += [cat_id]; values += [float(r["Valor Doado"])]

mask_cls = agg_prod["Classificacao"] != ""
for _, r in agg_prod.loc[mask_cls].groupby(["Categoria","Classificacao"], as_index=False)["Valor Doado"].sum().iterrows():
    cat, cls = r["Categoria"], r["Classificacao"]
    cls_id = f"cls::{cat}::{cls}"
    labels += [cls]; parents += [f"cat::{cat}"]; ids += [cls_id]; values += [float(r["Valor Doado"])]

for _, r in agg_prod.iterrows():
    cat, cls, prod, val = r["Categoria"], r["Classificacao"], r["ProdutoBase"], float(r["Valor Doado"])
    parent_id = f"cat::{cat}" if cls == "" else f"cls::{cat}::{cls}"
    prod_id = f"prd::{cat}::{cls or 'NOCLS'}::{prod}"
    labels += [prod]; parents += [parent_id]; ids += [prod_id]; values += [val]


text = []
for lbl, pid in zip(labels, parents):
    if pid.startswith("cat::"):
        text.append(lbl)
    elif pid.startswith("cls::"):
        text.append("")
    else:
        text.append(lbl)

# KPIs
kpi_total_qtd = int(df["Quantidade Entregue"].sum())
kpi_total_valor = float(df["Valor Doado"].sum())
kpi_produtos_unicos = int(df["ProdutoBase"].nunique())

# tema claro
C_BG, C_PLOT, C_GRID, C_TEXT, C_MUTE = "#FFFFFF", "#FAFAFC", "#E7EAF0", "#0F172A", "#475569"
C1, C2, C3, C4, C5 = "#3B82F6", "#10B981", "#8B5CF6", "#EC4899", "#059669"
COLS = ["#2563EB","#F59E0B","#10B981","#EF4444","#7C3AED","#14B8A6",
        "#D97706","#3B82F6","#16A34A","#E11D48","#0EA5E9","#A855F7"]

# KPIs lado a lado
fig = make_subplots(
    rows=7, cols=3,
    specs=[
        [{"type":"bar",     "colspan":3}, None, None],
        [{"type":"bar",     "colspan":3}, None, None],
        [{"type":"domain",  "colspan":3}, None, None],
        [{"type":"scatter", "colspan":3}, None, None],
        [{"type":"bar",     "colspan":3}, None, None],
        [{"type":"scatter", "colspan":3}, None, None],
        [{"type":"indicator"}, {"type":"indicator"}, {"type":"indicator"}]
    ],
    subplot_titles=[
        "Top 10 por Quantidade",
        "Top 10 por Valor Doado",
        "Mix por Categoria/Classificação",
        "Acumulado de Quantidade",
        "Registros Semanais",
        "Tendência Mensal de Valor",
        "", "", ""
    ],
    vertical_spacing=0.075,
    horizontal_spacing=0.08,
    row_heights=[0.16,0.16,0.22,0.12,0.12,0.12,0.10]
)

# 1) Top 10 Qtd
fig.add_trace(go.Bar(
    x=top10_qtd["Quantidade Entregue"], y=top10_qtd["ProdutoBase"], orientation="h",
    marker=dict(color=C1, line=dict(color="rgba(0,0,0,0.06)", width=1)),
    text=top10_qtd["Quantidade Entregue"], texttemplate="%{x:,}",
    textposition="inside", insidetextanchor="end", insidetextfont=dict(color="#FFFFFF"),
    hovertemplate="<b>%{y}</b><br>Qtd: %{x:,}<extra></extra>", name="Top 10 Qtd"
), row=1, col=1)

# 2) Top 10 Valor
fig.add_trace(go.Bar(
    x=top10_valor["Valor Doado"], y=top10_valor["ProdutoBase"], orientation="h",
    marker=dict(color=C2, line=dict(color="rgba(0,0,0,0.06)", width=1)),
    text=top10_valor["Valor Doado"].round(0), texttemplate="R$ %{x:,.0f}",
    textposition="outside", constraintext="outside",
    hovertemplate="<b>%{y}</b><br>Valor: R$ %{x:,.2f}<extra></extra>", name="Top 10 Valor"
), row=2, col=1)

# 3) Treemap
fig.add_trace(go.Treemap(
    labels=labels, parents=parents, ids=ids, values=values,
    branchvalues="total", marker=dict(colors=COLS),
    text=text, textinfo="text",
    hovertemplate="<b>%{label}</b><br>Valor: R$ %{value:,.2f}<extra></extra>",
    maxdepth=2
), row=3, col=1)

# 4) Acumulado Qtd
fig.add_trace(go.Scatter(
    x=diaria_qtd["DataDaDoacao_dt"], y=diaria_qtd["Acumulado"],
    mode="lines+markers", line=dict(color=C5, width=3), marker=dict(size=6, color=C5),
    hovertemplate="<b>%{x|%d/%m/%Y}</b><br>Acumulado: %{y:,}<extra></extra>",
    name="Acumulado Qtd"
), row=4, col=1)

# 5) Registros Semanais
fig.add_trace(go.Bar(
    x=semanal_freq["DataDaDoacao_dt"], y=semanal_freq["Registros"],
    marker=dict(color=C3, line=dict(color="rgba(0,0,0,0.06)", width=1)),
    hovertemplate="<b>%{x|%d/%m/%Y}</b><br>Registros: %{y:,}<extra></extra>",
    name="Registros/semana"
), row=5, col=1)

# 6) Tendência Mensal Valor
fig.add_trace(go.Scatter(
    x=mensal_valor["AnoMes"], y=mensal_valor["Valor Doado"],
    mode="lines+markers", line=dict(color=C4, width=3), marker=dict(size=7, color=C4),
    hovertemplate="<b>%{x}</b><br>Valor: R$ %{y:,.2f}<extra></extra>",
    name="Valor Mensal"
), row=6, col=1)

# 7) KPIs
fig.add_trace(go.Indicator(
    mode="number", value=kpi_total_qtd,
    title={"text":"Total Doado (Qtd)"},
    number={"font":{"size":40}, "valueformat":",.0f"}
), row=7, col=1)
fig.add_trace(go.Indicator(
    mode="number", value=kpi_total_valor,
    title={"text":"Valor Total Doado"},
    number={"font":{"size":40}, "valueformat":",.2f", "prefix":"R$ "}
), row=7, col=2)
fig.add_trace(go.Indicator(
    mode="number", value=kpi_produtos_unicos,
    title={"text":"Produtos Únicos"},
    number={"font":{"size":40}, "valueformat":",.0f"}
), row=7, col=3)

# Layout global
TARGET_WIDTH = 1100
PAGE_WIDTH   = 1250
left_pad = max((PAGE_WIDTH - TARGET_WIDTH) // 2, 40)
right_pad = left_pad

fig.update_layout(
    height=2150, width=PAGE_WIDTH, template="plotly_white",
    paper_bgcolor=C_BG, plot_bgcolor=C_PLOT,
    font=dict(family="Inter, Open Sans, Arial, sans-serif", size=13, color=C_TEXT),
    margin=dict(t=150, r=right_pad, b=60, l=left_pad),
    title=dict(
        text="Projeto Big Data",
        x=0.5, xanchor="center",
        y=0.99, yanchor="top",
        pad=dict(b=22)
    ),
    title_automargin=True,
    hoverlabel=dict(bgcolor="#FFFFFF", bordercolor="#CBD5E1", font_size=12, font_color=C_TEXT),
    hovermode="x unified",
    showlegend=False
)

for ann in fig.layout.annotations:
    if ann.text == "Mix por Categoria/Classificação":
        ann.update(
            y=min(ann.y + 0.02, 0.99),
            yshift=16,
            xanchor="center",
            yanchor="bottom"
        )

fig.update_xaxes(showgrid=False, tickfont=dict(color=C_MUTE), title_font=dict(color=C_MUTE), zeroline=False)
fig.update_yaxes(showgrid=True, gridcolor=C_GRID, tickfont=dict(color=C_MUTE), title_font=dict(color=C_MUTE), zeroline=False)
fig.update_yaxes(row=1, col=1, categoryorder="array", categoryarray=list(top10_qtd["ProdutoBase"]))
fig.update_yaxes(row=2, col=1, categoryorder="array", categoryarray=list(top10_valor["ProdutoBase"]))
fig.update_xaxes(row=6, col=1, tickangle=25)

fig.show()
