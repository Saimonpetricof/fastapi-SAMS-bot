from fastapi import FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get("/")
async def root():
    return {"message": " Работаем, как непонятно"}

@app.post("/webhook")
async def webhook():
    return JSONResponse(status_code=200)
