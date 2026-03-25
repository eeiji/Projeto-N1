📌 Projeto N1 – Plataforma de Governança de TI com IA
📖 Descrição
Este projeto tem como objetivo desenvolver um microsserviço em Python capaz de analisar dados operacionais e prever riscos em ambientes de tecnologia, utilizando técnicas de Machine Learning.

A proposta está alinhada ao conceito de governança preditiva, permitindo apoiar a tomada de decisão de forma mais eficiente.

🎯 Objetivo
Criar um microsserviço que:

Recebe dados de entrada (tickets e tempo de resolução)

Aplica um modelo de Machine Learning

Retorna uma previsão de risco (baixo ou alto)

🧱 Estrutura do Projeto
/projeto
│
├── main.py              # Microsserviço (FastAPI)
├── Projeto_N1.ipynb    # Análise, gráficos e treino do modelo
⚙️ Tecnologias Utilizadas
Python

FastAPI

Uvicorn

Scikit-learn

Pandas

Matplotlib

🚀 Como Executar o Projeto
1. Instalar dependências
pip install fastapi uvicorn scikit-learn pandas
2. Executar o microsserviço
uvicorn main:app --reload
3. Acessar a API
API: http://127.0.0.1:8000

Documentação Swagger: http://127.0.0.1:8000/docs

🔗 Endpoint Principal
➤ Previsão de Risco
GET /prever

Parâmetros:
tickets (int): quantidade de chamados

tempo (float): tempo de resolução em horas

Exemplo:
/prever?tickets=60&tempo=10
Resposta:
{
  "tickets": 60,
  "tempo": 10,
  "risco": "ALTO"
}
🤖 Modelo de Machine Learning
O modelo foi desenvolvido utilizando:

Algoritmo: Random Forest

Biblioteca: Scikit-learn

Ele analisa:

Volume de tickets

Tempo de resolução

Para prever o nível de risco operacional.

📊 Análise de Dados
O arquivo Projeto_N1.ipynb contém:

Análise exploratória

Gráficos (histograma e scatter)

Treinamento do modelo

🧠 Arquitetura
O projeto segue o conceito de microsserviços, onde:

O notebook realiza análise e treinamento

A API realiza o consumo do modelo

📌 Conclusão
Este projeto demonstra como a aplicação de Inteligência Artificial pode contribuir para:

Antecipação de riscos

Melhoria na tomada de decisão

Otimização de processos em ambientes tecnológicos

