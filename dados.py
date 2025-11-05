import pandas as pd
import random

dados = [
    {"Produto/Tipo": "ABOBORA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.32, "Quantidade Entregue": 200, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "ABOBRINHA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 6.66, "Quantidade Entregue": 39, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "AIPIM/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 3.66, "Quantidade Entregue": 666, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "BANANA D'ÁGUA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.56, "Quantidade Entregue": 30, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "BANANA DA TERRA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 12.65, "Quantidade Entregue": 30, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "BANANA PRATA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.33, "Quantidade Entregue": 420, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "BATATA DOCE/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.33, "Quantidade Entregue": 36, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "BERINJELA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 6.32, "Quantidade Entregue": 90, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "BETERRABA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.99, "Quantidade Entregue": 72, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "CENOURA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.29, "Quantidade Entregue": 72, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "GOIABA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.29, "Quantidade Entregue": 144, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "JILÓ(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 10.32, "Quantidade Entregue": 26, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "LARANJA SELETA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.67, "Quantidade Entregue": 108, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "MAMÃO FORMOSA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.38, "Quantidade Entregue": 45, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "MANGA PALMER/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 8.34, "Quantidade Entregue": 45, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "MARACUJÁ(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 18.43, "Quantidade Entregue": 230, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "PEPINO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 3.66, "Quantidade Entregue": 18, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "PIMENTÃO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 14.32, "Quantidade Entregue": 45, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "TOMATE(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 10.32, "Quantidade Entregue": 180, "Data da Doação": "12/08/2025"},
    {"Produto/Tipo": "ABACAXI(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 6.50, "Quantidade Entregue": 360, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "ABOBORA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.32, "Quantidade Entregue": 450, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "AIPIM/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 3.66, "Quantidade Entregue": 689, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "ALFACE AMERICANA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 3.82, "Quantidade Entregue": 120, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "ALFACE CRESPA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 11.19, "Quantidade Entregue": 10, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "BANANA D'ÁGUA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.56, "Quantidade Entregue": 195, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "BANANA PRATA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.33, "Quantidade Entregue": 1_195, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "BATATA DOCE/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.33, "Quantidade Entregue": 180, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "BATATA INGLESA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 8.29, "Quantidade Entregue": 128, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "BERINJELA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 6.32, "Quantidade Entregue": 30, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "BETERRABA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.99, "Quantidade Entregue": 338, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "CEBOLA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 10.63, "Quantidade Entregue": 150, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "CEBOLINHA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 24.51, "Quantidade Entregue": 75, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "CENOURA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.96, "Quantidade Entregue": 396, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "COUVE(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.90, "Quantidade Entregue": 90, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "GOIABA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.29, "Quantidade Entregue": 702, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "INHAME(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.66, "Quantidade Entregue": 180, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "JILÓ(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 10.32, "Quantidade Entregue": 39, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "LARANJA SELETA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.67, "Quantidade Entregue": 126, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "MAMÃO FORMOSA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.38, "Quantidade Entregue": 45, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "NABO/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 4.10, "Quantidade Entregue": 18, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "PEPINO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 3.66, "Quantidade Entregue": 342, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "PIMENTÃO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 14.32, "Quantidade Entregue": 200, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "QUIABO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 11.43, "Quantidade Entregue": 52, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "RABANETE(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 15.09, "Quantidade Entregue": 62, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "REPOLHO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 6.14, "Quantidade Entregue": 30, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "SALSA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 37.85, "Quantidade Entregue": 45, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "TOMATE(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 10.32, "Quantidade Entregue": 430, "Data da Doação": "08/10/2025"},
    {"Produto/Tipo": "AIPIM/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 3.66, "Quantidade Entregue": 108, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "ALFACE CRESPA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 11.19, "Quantidade Entregue": 145, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BANANA D'ÁGUA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.56, "Quantidade Entregue": 90, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BANANA PRATA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.33, "Quantidade Entregue": 900, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BATATA DOCE/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 5.33, "Quantidade Entregue": 18, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BATATA INGLESA/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 8.29, "Quantidade Entregue": 324, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BATATA YACON/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 14.25, "Quantidade Entregue": 16, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BETERRABA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.99, "Quantidade Entregue": 270, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BRÓCOLIS(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.68, "Quantidade Entregue": 150, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "BRÓCOLIS(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/ORGÂNICO", "Unidade": "Kg", "Preço Unitário R$": 12.00, "Quantidade Entregue": 36, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "CEBOLINHA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 24.51, "Quantidade Entregue": 9, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "CENOURA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.96, "Quantidade Entregue": 252, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "CHUCHU(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 4.32, "Quantidade Entregue": 30, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "COUVE(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 9.90, "Quantidade Entregue": 65, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "COUVE-FLOR(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 11.59, "Quantidade Entregue": 112, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "INHAME(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 7.66, "Quantidade Entregue": 180, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "NABO/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 4.10, "Quantidade Entregue": 360, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "REPOLHO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 6.14, "Quantidade Entregue": 210, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "REPOLHO(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/ORGÂNICO", "Unidade": "Kg", "Preço Unitário R$": 7.98, "Quantidade Entregue": 60, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "SALSA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/ORGÂNICO", "Unidade": "Kg", "Preço Unitário R$": 49.21, "Quantidade Entregue": 10, "Data da Doação": "19/08/2025"},
    {"Produto/Tipo": "SALSA(CLASSIFICAÇÃO SEM CARACTERÍSTICAS)/CONVENCIONAL", "Unidade": "Kg", "Preço Unitário R$": 37.85, "Quantidade Entregue": 5, "Data da Doação": "19/08/2025"}
]

# Lista para dados simulados
produtos_realistas = [
    "ABOBORA(CONVENCIONAL)", "ABOBRINHA(CONVENCIONAL)", "AIPIM(CONVENCIONAL)", "BANANA D'ÁGUA(CONVENCIONAL)",
    "BANANA DA TERRA(CONVENCIONAL)", "BANANA PRATA(CONVENCIONAL)", "BATATA DOCE(CONVENCIONAL)",
    "BERINJELA(CONVENCIONAL)", "BETERRABA(CONVENCIONAL)", "CENOURA(CONVENCIONAL)", "GOIABA(CONVENCIONAL)",
    "JILÓ(CONVENCIONAL)", "LARANJA SELETA(CONVENCIONAL)", "MAMÃO FORMOSA(CONVENCIONAL)", "MANGA PALMER(CONVENCIONAL)",
    "MARACUJÁ(CONVENCIONAL)", "PEPINO(CONVENCIONAL)", "PIMENTÃO(CONVENCIONAL)", "TOMATE(CONVENCIONAL)",
    "ABACAXI(CONVENCIONAL)", "ALFACE AMERICANA(CONVENCIONAL)", "ALFACE CRESPA(CONVENCIONAL)", "BATATA INGLESA(CONVENCIONAL)",
    "CEBOLA(CONVENCIONAL)", "CEBOLINHA(CONVENCIONAL)", "COUVE(CONVENCIONAL)", "INHAME(CONVENCIONAL)", "NABO(CONVENCIONAL)",
    "QUIABO(CONVENCIONAL)", "RABANETE(CONVENCIONAL)", "REPOLHO(CONVENCIONAL)", "SALSA(CONVENCIONAL)",
    "BATATA YACON(CONVENCIONAL)", "BRÓCOLIS(CONVENCIONAL)", "BRÓCOLIS(ORGÂNICO)", "COUVE-FLOR(CONVENCIONAL)",
    "SALSA(ORGÂNICO)", "REPOLHO(ORGÂNICO)", "CHUCHU(CONVENCIONAL)"
]

datas_possiveis = ["12/08/2025", "19/08/2025", "08/10/2025"]
num_minimo = 200

while len(dados) < num_minimo:
    produto = random.choice(produtos_realistas)
    preco = round(random.uniform(3.0, 20.0), 2)
    quantidade = random.randint(10, 1300)
    data = random.choice(datas_possiveis)
    nova = {
        "Produto/Tipo": produto,
        "Unidade": "Kg",
        "Preço Unitário R$": preco,
        "Quantidade Entregue": quantidade,
        "Data da Doação": data
    }
    dados.append(nova)

df = pd.DataFrame(dados)
df.to_csv("produtos_doados0.csv", index=False, encoding='utf-8-sig')
print(f"Arquivo CSV pronto ('produtos_doados0.csv') — com {len(df)} linhas reais e simuladas.")
