import pytest
from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")   #Need to provide fixefox browser path
        driver = webdriver.Firefox(service=service_obj)

    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()