from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import *
from sqlalchemy import text
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse

import socket
import os

from domain.customer import customer_router
from domain.product import product_router

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

app.include_router(customer_router.router)
app.include_router(product_router.router)

@app.get("/")
async def docs():    
    return RedirectResponse(url="/docs")

@app.get("/host")
async def host():    
    container_hostname = socket.gethostname()    
    container_ip = socket.gethostbyname(container_hostname)
    host_ip = os.environ.get('HOST_IP')
    host_name = os.environ.get('HOST_NAME')
    
    return {
            "container_ip": container_ip,
            "container_hostname": container_hostname,
            "host_ip": host_ip,
            "host_name": host_name,
           }
