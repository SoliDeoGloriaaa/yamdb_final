# FROM python:3.7-slim 
 
# WORKDIR /app 
 
# COPY requirements.txt . 
 
# RUN pip3 install -r requirements.txt --no-cache-dir 
 
# COPY api_yamdb/ /app
 
# CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]

FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r ./requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]