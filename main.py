from fastapi import FastAPI, requests
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import Optional

app = FastAPI()


@app.get("/hello")
def read_hello(name: Optional[str]= None, is_teacher: Optional[bool]= None):
    
    
    if is_teacher is None and name is None :
        return {"message": f"Hello world"}
    
    if is_teacher is None and name is not None :
        is_teacher=False
        
    if is_teacher is not None and name is None :
        name="Not found"

    if is_teacher :
        return {"message" :f"Hello teacher {name}"}
    else :
        return {"message" :f"Hello {name}"}
        

class WelcomeRequest(BaseModel):
    name: str

@app.post("/welcome")
def welcome_user(request: WelcomeRequest):
    return {f"Bienvenue {request.name}"}
