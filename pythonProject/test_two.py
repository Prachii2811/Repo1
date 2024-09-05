import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(autouse=True)
def setup_and_teardown():
    global driver
    driver = WebDriver()
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield
    driver.quit()


def test_login_with_valid_credentials():

    driver.find_element("xpath","//a[.='Log in']").click()
    driver.find_element("id","Email").send_keys("prachi2811singh@gmail.com")
    driver.find_element("id","Password").send_keys("Shriganesh@1")
    driver.find_element("xpath","//input[@value='Log in']").click()
    assert driver.find_element("xpath","//a[.='prachi2811singh@gmail.com']").is_displayed()
#      we use assert keyword to forcefully fail or pass a test case


def test_login_with_invalid_credentials():
    driver.find_element("xpath","//a[.='Log in']").click()
    driver.find_element("id","Email").send_keys("prachi1128singh@gmail.com")
    driver.find_element("id","Password").send_keys("selenium")
    driver.find_element("xpath","//input[@value='Log in']").click()

