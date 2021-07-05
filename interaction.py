from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import time

chrome_driver_path = "/Users/hatimalattas/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


timeout = time.time() + 5  # 5 seconds from now
five_mins = time.time() + 60*5

e = StaleElementReferenceException
e2 = NoSuchElementException


def to_integer(number):
    if len(number) > 3:
        number = number.replace(",", "")
        number = int(number)
    else:
        number = int(number)

    return number


while True:
    if time.time() < five_mins:
        store = driver.find_elements_by_css_selector("#store div")
        cookie = driver.find_element_by_id("cookie")

        if time.time() > timeout:

            money = driver.find_element_by_id("money").text
            money = to_integer(money)

            for product in reversed(store):
                try:
                    price = product.find_element_by_tag_name("b").text.split(" - ")[1]
                    price = to_integer(price)

                    if money >= price:
                        try:
                            product.click()
                            break
                        except e:
                            print("StaleElementReferenceException")

                except IndexError:
                    print("IndexError")

                except e:
                    print("StaleElementReferenceException")

                except e2:
                    print("NoSuchElementException")

            timeout = time.time() + 5

        else:
            cookie.click()

    else:
        cps = driver.find_element_by_id("cps").text
        print(cps)
        break


driver.quit()
