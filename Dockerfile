FROM python:3.11.4-alpine

WORKDIR /opt/

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]