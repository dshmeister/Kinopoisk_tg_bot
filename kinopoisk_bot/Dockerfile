FROM python:3.9

RUN mkdir -p /usr/src/ap1/
WORKDIR /usr/src/app1/

COPY . /usr/src/app1/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/main.py"]