from fastapi import FastAPI
from sklearn.ensemble import RandomForestClassifier
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

# 🔹 Endpoint GET
@app.get("/prever")
def prever(tickets: int, tempo: float):
    pred = model.predict([[tickets, tempo]])[0]
    risco = "ALTO" if pred == 1 else "BAIXO"
    
    return {
        "tickets": tickets,
        "tempo": tempo,
        "risco": risco
    }