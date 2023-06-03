from sqlalchemy import Column, BigInteger, Text, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    promo_id = Column(Text)
    order_cnt = Column(Integer, nullable=False)
    order_price = Column(Integer, nullable=False)
    order_dt = Column(Text, nullable=False)
    last_update_time = Column(DateTime, nullable=False)
    cust_id = Column(BigInteger, nullable=False)
    prd_id = Column(Integer, nullable=False)

class Customer(Base):
    __tablename__ = "customer"

    id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    password = Column(Text, nullable=False)
    last_login = Column(DateTime)
    is_superuser = Column(Integer, nullable=False)
    username = Column(Text, unique=True, nullable=False)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    is_staff = Column(Integer, nullable=False)
    is_active = Column(Integer, nullable=False)
    date_joined = Column(DateTime, nullable=False)
    phone_number = Column(Text)
    age = Column(Integer)
    gender = Column(Text)
    address = Column(Text)
    last_update_time = Column(DateTime, nullable=False)
    name = Column(Text)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    img_path = Column(String(255))
    category = Column(String(255))
    price = Column(Integer, nullable=False)
    last_update_time = Column(DateTime, nullable=False)    