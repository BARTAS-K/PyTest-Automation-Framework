import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    browserName = request.config.getoption("browserName")
    if browserName == "chrome":
        serviceObject = Service("D:/Downloads/chromedriver.exe")
        driver = webdriver.Chrome(service=serviceObject)
    elif browserName == "firefox":
        serviceObject = Service("D:/Downloads/geckodriver.exe")
        driver = webdriver.Firefox(service=serviceObject)

    driver.get("https://academybugs.com/")
    driver.implicitly_wait(5)
    request.cls.driver = driver

def pytest_addoption(parser):
    parser.addoption("--browserName", action="store", default="chrome")
