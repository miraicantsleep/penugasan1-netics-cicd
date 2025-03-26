FROM python:3.11-slim AS build

WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .

FROM python:3.11-slim

WORKDIR /app
COPY --from=build /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=build /app /app

EXPOSE 5000
CMD ["python3", "app.py"]