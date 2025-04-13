from fastapi import FastAPI
from translatorService import translate

app = FastAPI()

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/translate")
async def translate_endpoint(message: str, language: str = "Spanish"):
    reply = translate(message, language)
    return {"message": reply}



