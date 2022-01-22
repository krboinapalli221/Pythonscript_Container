FROM python:latest

COPY welcome.py ./root
WORKDIR /root

CMD [ "python3","welcome.py"] 
