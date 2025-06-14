FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо лише requirements.txt для кешування залежностей
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код проєкту
COPY src/ .

# Виставляємо порт, який буде використовуватися
EXPOSE 8000

# Запускаємо Django сервер на всіх інтерфейсах
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
