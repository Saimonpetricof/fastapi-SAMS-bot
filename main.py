from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()
token = '7617038367:AAE7aAYV0Ww1E1ZM7Ugggrbgs2BLXrHfmPU'
link = 'https://api.telegram.org/bot' + token

@app.get("/")
async def root():
    return {"message": " Работаем, как - непонятно"}

@app.get("/webhook")
async def webhook(request: Request):
    update =request.get(link + "/sendMessage?chat_id=479761739&text=Привет_медвед")
    return {"привет_медвед"}