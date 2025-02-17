FROM python:3.10

WORKDIR /bot

RUN apt update && apt upgrade -y && apt install -y git

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
