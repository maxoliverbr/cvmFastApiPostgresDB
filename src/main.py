import uvicorn
import logging
from fastapi import FastAPI, Depends, status
from routers import router_cad_cia_aberta
from routers import router_cad_cia_estrang

app = FastAPI()

app.include_router(router_cad_cia_aberta.router)
app.include_router(router_cad_cia_estrang.router)


@app.get("/", status_code=status.HTTP_200_OK)
def get_root():
    return {"InfoInvest": "AI2"}


if __name__ == "__main__":
    # app.run(debug=True)

    uvicorn.run("main:app", port=5000, reload=True, access_log=False)
