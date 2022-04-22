#Deriving the latest base image
FROM python:3.8

RUN adduser -D jobuser
USER jobuser

WORKDIR /home/jobuser

COPY --chown=jobuser:jobuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/jobuser/.local/bin:${PATH}"

COPY --chown=jobuser:jobuser . .
# COPY . ./

# RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "./main.py"]