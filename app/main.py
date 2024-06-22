from fastapi import FastAPI, Form
from .types import CallData
import requests
from twilio.twiml.voice_response import VoiceResponse
from fastapi.responses import PlainTextResponse
import os
from dotenv import load_dotenv
from typing import Optional


load_dotenv()

app = FastAPI()
api_key = os.environ["VAPI_PRIVATE_TOKEN"]


@app.post("/twilio/inbound_call", response_class=PlainTextResponse)
async def receive_call_data(
        AccountSid: str = Form(...),
        ApiVersion: str = Form(...),
        Called: str = Form(...),
        CalledCity: Optional[str] = Form(None),
        CalledCountry: str = Form(...),
        CalledState: str = Form(...),
        CalledZip: Optional[str] = Form(None),
        Caller: str = Form(...),
        CallerCity: str = Form(...),
        CallerCountry: str = Form(...),
        CallerState: str = Form(...),
        CallerZip: str = Form(...),
        CallSid: str = Form(...),
        CallStatus: str = Form(...),
        CallToken: str = Form(...),
        Direction: str = Form(...),
        From: str = Form(...),
        FromCity: str = Form(...),
        FromCountry: str = Form(...),
        FromState: str = Form(...),
        FromZip: str = Form(...),
        StirVerstat: str = Form(...),
        To: str = Form(...),
        ToCity: Optional[str] = Form(None),
        ToCountry: str = Form(...),
        ToState: str = Form(...),
        ToZip: Optional[str] = Form(None)
):
    call_data = CallData(
        AccountSid=AccountSid,
        ApiVersion=ApiVersion,
        Called=Called,
        CalledCity=CalledCity,
        CalledCountry=CalledCountry,
        CalledState=CalledState,
        CalledZip=CalledZip,
        Caller=Caller,
        CallerCity=CallerCity,
        CallerCountry=CallerCountry,
        CallerState=CallerState,
        CallerZip=CallerZip,
        CallSid=CallSid,
        CallStatus=CallStatus,
        CallToken=CallToken,
        Direction=Direction,
        From=From,
        FromCity=FromCity,
        FromCountry=FromCountry,
        FromState=FromState,
        FromZip=FromZip,
        StirVerstat=StirVerstat,
        To=To,
        ToCity=ToCity,
        ToCountry=ToCountry,
        ToState=ToState,
        ToZip=ToZip
    )

    r = requests.post("https://api.vapi.ai/call", json={
        "phoneNumberId": "your-phone-number-id",
        "phoneCallProviderBypassEnabled": True,
        "customer": {
            "number": call_data.Caller
        },
        "assistantId": "your-assistant-id"
    }, headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    })

    result = r.json()

    return result["phoneCallProviderDetails"]["twiml"]
