from selenium import webdriver

chrome_driver_path = "/Users/hatimalattas/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

ul_elements = driver.find_elements_by_xpath('/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')[0]
li_elements = ul_elements.find_elements_by_tag_name("li")


dic = {}
count = 0

for element in li_elements:
    name = element.find_element_by_tag_name("a").text
    time = element.find_element_by_tag_name("time").text
    dic[count] = {
        "time": time,
        "name": name
    }
    count += 1

print(dic)

driver.quit()
