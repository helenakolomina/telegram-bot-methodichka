# Telegram Bot: Методичка по H. pylori

## 📦 Состав
- `bot.py` — код Telegram-бота с оплатой и выдачей PDF
- `metodichka.pdf` — файл, который отправляется после оплаты
- `requirements.txt` — зависимости
- `Procfile` — для запуска на Railway

## 🚀 Как развернуть на Railway
1. Создай репозиторий на GitHub
2. Загрузи туда все файлы из архива
3. Перейди на https://railway.app → "New Project" → "Deploy from GitHub Repo"
4. Railway сам запустит бота

## 🔧 Команда запуска
Указана в `Procfile`:  
```bash
python bot.py
```

## 🧪 Тестовая оплата
Подключён тестовый токен от Telegram. После «оплаты» бот вышлет PDF.

## 💬 Команда
После запуска просто напиши своему боту:
```
/buy
```
