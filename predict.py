import joblib
import pandas as pd

# Carregar modelo e encoder
model = joblib.load("modelo_climatico.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Exemplo de nova entrada (nenhum evento específico)
nova_entrada = pd.DataFrame([{
    "latitude": -15.7942,
    "longitude": -47.8822,
    "temperatura": 30.0,
    "umidade": 70.0,
    "precipitacao": 2.0,
    "pressao_ar": 1012.0,
    "velocidade_vento": 5.0
}])

# Exemplo de nova entrada (chuva_torrencial)
# nova_entrada = pd.DataFrame([{
#     "latitude": -15.7942,
#     "longitude": -47.8822,
#     "temperatura": 30.0,
#     "umidade": 100.0,
#     "precipitacao": 100.0,
#     "pressao_ar": 1012.0,
#     "velocidade_vento": 5.0
# }])

# Exemplo de nova entrada (seca)
# nova_entrada = pd.DataFrame([{
#     "latitude": -15.7942,
#     "longitude": -47.8822,
#     "temperatura": 35.0,
#     "umidade": 20.0,
#     "precipitacao": 0.0,
#     "pressao_ar": 1012.0,
#     "velocidade_vento": 5.0
# }])

# Predição
predicao = model.predict(nova_entrada)
classe = label_encoder.inverse_transform(predicao)

# Probabilidades para cada classe
probs = model.predict_proba(nova_entrada)[0]
for class_name, prob in zip(label_encoder.classes_, probs):
    print(f"Probabilidade de '{class_name}': {prob:.2f}")

print("Classificação prevista:", classe[0])