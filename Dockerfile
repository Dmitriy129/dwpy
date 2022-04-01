#Deriving the latest base image
FROM python:3.8

WORKDIR /usr/app/src

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "./main.py"]