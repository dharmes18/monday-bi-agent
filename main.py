from fastapi import FastAPI
from agent import analyse

app = FastAPI(title="Monday BI Agent")

@app.get("/")
def home():
    return {"status": "Monday BI Agent running 🚀"}

@app.post("/chat")
def chat(q: str):
    answer = analyse(q)
    return {"answer": answer}