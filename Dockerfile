FROM python:latest

# Установка Chrome и Chrome WebDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -y \
    && apt-get install -y google-chrome-stable \
    && CHROME_VERSION=$(google-chrome --version | grep -oP "[0-9]+") \
    && CHROME_DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") \
    && wget -q --continue -P /chromedriver "https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip /chromedriver/chromedriver* -d /chromedriver \
    && rm /chromedriver/chromedriver_linux64.zip \
    && chmod +x /chromedriver/chromedriver \
    && mv -f /chromedriver/chromedriver /usr/local/bin/chromedriver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Копирование проекта в Docker-образ
COPY . .

# Установка зависимостей Python
RUN pip install -r requirements.txt

# Команда для запуска тестов
CMD ["pytest"]