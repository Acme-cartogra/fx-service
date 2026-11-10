from fastapi import FastAPI

app = FastAPI(title="fx-service", version="1.0.0")

@app.get("/actuator/health")
def health(): return {"status": "UP"}

@app.get("/fxs")
def route_0(): return {"status": "ok"}

@app.post("/fxs")
def route_1(): return {"status": "ok"}

@app.get("/fxs/{id}")
def route_2(): return {"status": "ok"}
