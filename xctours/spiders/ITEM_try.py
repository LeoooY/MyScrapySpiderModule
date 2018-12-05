from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
Chrome=Options()
# Chrome.add_argument('--headless')
# Chrome.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=Chrome)
# driver.set_window_size(1000,10000)
start=time.time()
print('浏览器打开')
driver.get('http://vacations.ctrip.com/tours/d-leshan-103')
time.sleep(1)
print('下载网页')
for i in range(15) :
    driver.execute_script("window.scrollBy(0,500)")
    time.sleep(0.3)
print('加载完毕，开始解析...')
body=driver.page_source
selector=Selector(text=body)

# a=driver.find_elements_by_xpath('//div[@class="product_main"]')
a=selector.xpath('//div[@class="product_main"]')
i3=0
for each in a:
    print(each.xpath('div/div/div/dl[@class="start_info"]/dd/text()').extract())
    print(each.xpath('div/div/div/p[@class="grade"]/strong/text()').extract())
    print('item%s'%i3)
    i3+=1

end=time.time()
t=start-end
print('用时：%s'%t)
# page = driver.page_source
# with open("car.txt", "w", encoding="utf-8") as f:
#     f.write(page)
#     f.close()