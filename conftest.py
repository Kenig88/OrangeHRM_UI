import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True) #scope-будет открывать драйвер для каждого теста отдельно, autouse-будет использоваться автоматически для каждого теста
def driver(request):
    options = Options()
    options.add_argument("--headless") # для Docker
    options.add_argument("--no-sandbox") # для Docker
    options.add_argument("--disable-dev-shm-usage") # для Docker
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver #создаёт объект driver внутри тестовых классов
    yield driver
    driver.quit()

