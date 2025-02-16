FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN ls -l /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
