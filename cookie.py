from selenium import webdriver # type: ignore
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.facebook.com")

    driver.add_cookie({'name': 'c_user', 'value': '100062865436377'})  
    driver.add_cookie({'name': 'xs', 'value': '39%3AGFNMj83Z0opW2w%3A2%3A1735817118%3A-1%3A6297%3A%3AAcXKx3ZJIXCo6ZzgxutgfSVa8iy8aGIZvRFVa8bOvIg'})  

    driver.refresh()

    time.sleep(500)

except Exception as e:
    print(f"Lỗi xảy ra: {e}")

finally:
    driver.quit()
