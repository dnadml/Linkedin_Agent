
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def initialize_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/path/to/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_profile(profile_url):
    driver = initialize_driver()
    try:
        driver.get(profile_url)
        profile_name = driver.find_element(By.CLASS_NAME, "text-heading-xlarge").text
        about_section = driver.find_element(By.CLASS_NAME, "pv-about-section").text
        return {"name": profile_name, "about": about_section}
    except Exception as e:
        print(f"Error scraping profile: {e}")
    finally:
        driver.quit()

def scrape_posts(profile_url):
    driver = initialize_driver()
    try:
        driver.get(profile_url + "/detail/recent-activity/posts/")
        posts = driver.find_elements(By.CLASS_NAME, "feed-shared-text")
        return [post.text for post in posts]
    except Exception as e:
        print(f"Error scraping posts: {e}")
    finally:
        driver.quit()
