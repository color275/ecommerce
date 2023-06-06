import socket
import os

# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     username: str
#     password: str
#     host: str
#     port: int
#     dbname: str

#     class Config:
#         env_file = "../.env"

ORDER_SERVICE = os.getenv("ORDER_SERVICE")
PROUDCT_SERVICE = os.getenv("PROUDCT_SERVICE")
CUSTOMER_SERVICE = os.getenv("CUSTOMER_SERVICE")

def host():    
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