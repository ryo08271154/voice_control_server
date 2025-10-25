from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pyttsx3
from dotenv import load_dotenv
import os
import requests
import simpleaudio as sa
import io
import wave

engine = pyttsx3.init()

app = FastAPI()


class Voice(BaseModel):
    command: str
    message: str


load_dotenv()
VOICEVOX_URL = os.environ.get("VOICEVOX_URL")
SPEAKER_ID = int(os.environ.get("SPEAKER_ID"))


@app.post("/voice")
async def voice(command: Voice):
    engine.say(command.message)
    engine.runAndWait()
    return {"message": "OK"}


@app.post("/voice_vox")
async def voice_vox(command: Voice):
    if not VOICEVOX_URL or not SPEAKER_ID:
        raise HTTPException(
            status_code=500, detail="URL or SPEAKER_ID not set in environment variables")
    try:
        res_query = requests.post(
            f"{VOICEVOX_URL}/audio_query",
            params={"text": command.message, "speaker": SPEAKER_ID},
        )
        res_query.raise_for_status()
        audio_query = res_query.json()

        res_synth = requests.post(
            f"{VOICEVOX_URL}/synthesis",
            params={"speaker": SPEAKER_ID},
            json=audio_query,
        )
        res_synth.raise_for_status()
        wav_data = res_synth.content

        with io.BytesIO(wav_data) as f:
            with wave.open(f, 'rb') as wf:
                audio_segment = wf.readframes(wf.getnframes())
                play_obj = sa.play_buffer(
                    audio_segment,
                    num_channels=wf.getnchannels(),
                    bytes_per_sample=wf.getsampwidth(),
                    sample_rate=wf.getframerate()
                )
                play_obj.wait_done()  # 再生が終わるまで待機

    except requests.exceptions.RequestException as e:
        print(e)
        raise HTTPException(
            status_code=503, detail=f"Service unavailable: {e}")

    return {"message": "OK"}
