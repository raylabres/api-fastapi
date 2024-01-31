from fastapi import FastAPI

app = FastAPI()

# Crias rotas o que vai acontecer quando entrar na rota home ou na rota contato

vendas = {1: {'item': 'lata', 'preço_unitário': 4, 'quantidade': 5},
          2: {'item': 'garrafa 1 L', 'preço_unitário': 10, 'quantidade': 13},
          3: {'item': 'garrafa 2 L', 'preço_unitário': 20, 'quantidade': 19},
          4: {'item': 'latinha', 'preço_unitário': 1, 'quantidade': 5}}

@app.get('/')
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas")
def vendas_totais():
    return vendas

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]
