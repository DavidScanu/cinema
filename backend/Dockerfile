FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app/backend
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD fastapi dev main.py --host 0.0.0.0 --port $PORT --reload