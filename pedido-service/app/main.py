from fastapi import FastAPI

app = FastAPI(title="Pedido Service")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/pedidos")
def criar_pedido():
    return {
        "mensagem": "Pedido criado com sucesso",
        "status": "CRIADO"
    }
