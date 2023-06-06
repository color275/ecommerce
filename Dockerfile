FROM python:3.10

WORKDIR /app

COPY . .

# 해당 명령어를 실행해라
RUN pip install -r requirements.txt

# opne port 문서화
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# cmd

# docker build -t color275/ecommerce-linux --platform .
# docker build -t color275/ecommerce-linux --platform linux/amd64 .
# docker push color275/ecommerce-linux
# docker pull color275/ecommerce-linux

# docker exec -it ecommerce bash

# docker logs -f ecommerce

# docker run --name ecommerce --add-host=host.docker.internal:host-gateway --env-file=.env -p 8000:8000 -d color275/ecommerce-mac

# .env

# HOST_IP=$(hostname -I | awk '{print $1}')
# HOST_NAME=$(hostname)
# cat <<EOF> .env
# DBUSER=appuser
# PASSWORD=Appuser12#$
# HOST=host.docker.internal
# PORT=3306
# DBNAME=ecommerce
# EOF
# echo "HOST_IP=${HOST_IP}" >> .env
# echo "HOST_NAME=${HOST_NAME}" >> .env

# LOCAL DOCKER
# export DBUSER="appuser"
# export PASSWORD="Appuser12#$"
# export HOST="host.docker.internal"
# export PORT="3306"
# export DBNAME="ecommerce"
# export HOST_NAME=$(hostname)
# export HOST_IP=$(hostname -I | awk '{print $1}')

# LOCAL 
# export DBUSER="appuser"
# export PASSWORD="Appuser12#$"
# export HOST="localhost"
# export PORT="3306"
# export DBNAME="ecommerce"
# export HOST_NAME=$(hostname)
# export HOST_IP=$(hostname -I | awk '{print $1}')
# export ORDER_SERVICE="localhost"
# export CUSTOMER_SERVICE="localhost"
# export PRODUCT_SERVICE="localhost"

# # 삭제
# docker stop $(docker ps -a -q)
# docker container prune