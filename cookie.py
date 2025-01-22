from selenium import webdriver # type: ignore
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.facebook.com")

    driver.add_cookie({'name': 'c_user', 'value': ''})  
    driver.add_cookie({'name': 'xs', 'value': ''})  

    driver.refresh()

    time.sleep(500)

except Exception as e:
    print(f": {e}")

finally:
    driver.quit()
