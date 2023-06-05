from fastapi import APIRouter
from fastapi import HTTPException
from models import *
from database import engineconn

router = APIRouter(
    prefix="/api/product",
)

engine = engineconn()
session = engine.sessionmaker()

@router.get("/")
async def get_all():
    result = session.query(Customer).all()
    return result

@router.get("/{id}")
async def get_product(id: int):
    product = session.query(Product).filter(Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_dict = product.__dict__
    product_dict.pop("_sa_instance_state")  # SQLAlchemy 내부 상태 정보 제거

    return product_dict