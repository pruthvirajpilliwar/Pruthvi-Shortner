FROM python:3.12.5-slim

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt-get update -y
 
COPY .requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
