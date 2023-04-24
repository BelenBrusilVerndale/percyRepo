from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from percy import percy_snapshot

def test_present():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    # Load the  page.
    driver.get("https://www.verndale.com/")


    # Wait until all elements are present
    driver.find_element(By.XPATH, "/html/body/main/div[1]/section/div/div[1]/div[1]/article/div[1]").is_displayed()
    print("Elements Present")

    # Take snapshot
    percy_snapshot(driver, "Test Public 01")