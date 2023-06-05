from fastapi import APIRouter
from fastapi import HTTPException
from models import *
from database import engineconn

router = APIRouter(
    prefix="/api/customer",
)

engine = engineconn()
session = engine.sessionmaker()

@router.get("/")
async def get_all():
    result = session.query(Customer).all()
    return result

@router.get("/{id}")
async def get_customer(id: int):
    customer = session.query(Customer).filter(Customer.id == id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    customer_dict = customer.__dict__
    customer_dict.pop("_sa_instance_state")  # SQLAlchemy 내부 상태 정보 제거

    return customer_dict