from fastapi import FastAPI
from pydantic import BaseModel
import pyttsx3
engine = pyttsx3.init()

app = FastAPI()

class Voice(BaseModel):
    command: str
    message: str

@app.post("/voice")
async def voice(command: Voice):
    engine.say(command.message)
    engine.runAndWait()
    return {"message": "OK"}
