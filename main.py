from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from token import link
app = FastAPI()


@app.get("/")
async def root():
    return {"message": " Работаем, как непонятно"}

@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()
    return JSONResponse(status_code=200)
