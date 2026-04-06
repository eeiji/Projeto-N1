from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import requests
import pandas as pd

app = FastAPI()

# 🔹 Treinamento
data = {
    "tickets_abertos": [10, 50, 30, 80],
    "tempo_resolucao": [2, 10, 5, 15],
    "risco": [0, 1, 0, 1]
}

df = pd.DataFrame(data)
X = df[["tickets_abertos", "tempo_resolucao"]]
y = df["risco"]

model = RandomForestClassifier()
model.fit(X, y)

# Integração ITSM
API_TOKEN = "pk_29062*************************************"
LIST_ID = "https://app.clickup.com/***********/v/l/************"

def criar_ticket(titulo, descricao, prioridade = 3):
    url = f"https://api.clickup.com/api/v2/list/{LIST_ID}/task"

    headers = {
        "Autorizathion": API_TOKEN,
        "Content-Type": "aplication/json"
    }

    payload = {
        "name": titulo,
        "description": descricao,
        "status": "to do",
        "priority": prioridade
    }
    

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


# 🔹 Endpoint GET
@app.get("/prever")
def prever_risco(tempo_resolucao: float):
    
    prob = model.predict_proba([[tempo_resolucao]])[0][1]
    
    resposta = {
        "tempo_resolucao": tempo_resolucao,
        "probabilidade_risco": float(prob)
    }
    
    # regra de negócio (threshold)
    if prob > 0.7:
        ticket = criar_ticket(
            titulo="Alerta de Risco Alto (IA)",
            descricao=f"Risco detectado: {prob:.2f} | Tempo: {tempo_resolucao} min",
            prioridade=1
        )
        resposta["ticket_criado"] = ticket
    
    return resposta
