FROM python:3.6-slim

COPY ./app /app
COPY ./app /requirements.txt 

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000



CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]


# docker build -t myimage .
# docker run -p 8000:8000 --name mycontainer myimage

