from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

@app.get("/")
def index():
    return{"mensagem": "olá mundo!"}

@app.post("/token")
async def logar(data:OAuth2PasswordRequestForm = Depends()):
    if data.username == "andre" and data.password == "1234":
        return{"acces_token":"supersecreto","token_type":"bearer"}

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credencial invalidaas")
#inicar pelo cmd = uvicorn main:app --reloadGIT