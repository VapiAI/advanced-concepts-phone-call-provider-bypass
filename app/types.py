from pydantic import BaseModel
from typing import Optional

class CallData(BaseModel):
    AccountSid: str
    ApiVersion: str
    Called: str
    CalledCity: Optional[str]
    CalledCountry: str
    CalledState: str
    CalledZip: Optional[str]
    Caller: str
    CallerCity: str
    CallerCountry: str
    CallerState: str
    CallerZip: str
    CallSid: str
    CallStatus: str
    CallToken: str
    Direction: str
    From: str
    FromCity: str
    FromCountry: str
    FromState: str
    FromZip: str
    StirVerstat: str
    To: str
    ToCity: Optional[str]
    ToCountry: str
    ToState: str
    ToZip: Optional[str]

