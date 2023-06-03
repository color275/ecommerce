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

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()

@app.get("/")
async def root():    
    # return "Welcome to root page"
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

@app.get("/customers")
async def customers():
    result = session.query(Customer).all()
    return result

@app.get("/customer/{id}")
async def get_customer(id: int):
    # id에 해당하는 고객 정보 가져오기
    customer = session.query(Customer).filter(Customer.id == id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Customer 모델 객체를 딕셔너리로 변환
    customer_dict = customer.__dict__
    customer_dict.pop("_sa_instance_state")  # SQLAlchemy 내부 상태 정보 제거

    return customer_dict


@app.get("/orders")
async def orders():
    result = session.query(Order).all()
    return result

@app.get("/order/{id}")
async def get_order(id: int):
    # id에 해당하는 고객 정보 가져오기
    order = session.query(Order).filter(Order.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    # order 모델 객체를 딕셔너리로 변환
    order_dict = order.__dict__
    order_dict.pop("_sa_instance_state")  # SQLAlchemy 내부 상태 정보 제거

    return order_dict


@app.get("/products")
async def products():
    result = session.query(Product).all()
    return result

@app.get("/product/{id}")    
async def get_product(id: int):
    # id에 해당하는 고객 정보 가져오기
    product = session.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="product not found")

    # product 모델 객체를 딕셔너리로 변환
    product_dict = product.__dict__
    product_dict.pop("_sa_instance_state")  # SQLAlchemy 내부 상태 정보 제거

    return product_dict