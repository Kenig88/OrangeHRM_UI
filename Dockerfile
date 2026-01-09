# ❗ Используем СТАБИЛЬНЫЙ Python, не alpha
FROM python:3.11-alpine

# --------------------------------------
# System dependencies
# --------------------------------------
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    tzdata \
    openjdk11-jre \
    curl \
    tar \
    wget \
    bash

# --------------------------------------
# Allure
# --------------------------------------
RUN curl -Ls -o allure.tgz \
    https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure.tgz -C /opt && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure.tgz

# --------------------------------------
# Environment variables for Chromium
# --------------------------------------
ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROMEDRIVER_BIN=/usr/bin/chromedriver

# --------------------------------------
# Working directory
# --------------------------------------
WORKDIR /usr/workspace

# --------------------------------------
# Python dependencies
# --------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------
# Copy project
# --------------------------------------
COPY . .

# --------------------------------------
# Default command
# --------------------------------------
CMD ["pytest"]
