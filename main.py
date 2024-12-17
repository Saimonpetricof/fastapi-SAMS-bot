from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()


@app.get("/")
async def root():
    return {"message": " Работаем, как - непонятно"}

@app.get("/webhook")
async def webhook(request: Request):
    update =request.get(link + "/sendMessage?chat_id=479761739&text=Привет_медвед")
    return {"привет_медвед"}