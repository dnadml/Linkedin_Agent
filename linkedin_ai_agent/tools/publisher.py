
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def initialize_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/path/to/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def login_to_linkedin(driver, email, password):
    driver.get("https://www.linkedin.com/login")
    driver.find_element(By.ID, "username").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()
    time.sleep(3)

def post_content(content):
    driver = initialize_driver()
    try:
        login_to_linkedin(driver, "your_email", "your_password")
        driver.get("https://www.linkedin.com/feed/")
        post_box = driver.find_element(By.CLASS_NAME, "share-box-feed-entry__trigger")
        post_box.click()
        time.sleep(2)
        editor = driver.find_element(By.CLASS_NAME, "ql-editor")
        editor.send_keys(content)
        post_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Post')]")
        post_button.click()
        print("Content posted successfully!")
    except Exception as e:
        print(f"Error posting content: {e}")
    finally:
        driver.quit()
