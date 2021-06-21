from selenium import webdriver
import time

url ='https://mops.twse.com.tw/mops/web/stapap1_all'

options = webdriver.ChromeOptions()
options.add_argument('--disable-site-isolation-trials')
driver = webdriver.Chrome(chrome_options = options, executable_path = '/usr/local/bin/chromedriver')
driver.get(url)
print('url:', url)
#html = driver.page_source
#print(html)

skind_select = driver.find_element_by_xpath('//*[@id="search"]/table/tbody/tr/td[6]/select')
skind_select.click()
skind = driver.find_element_by_xpath('//*[@id="search"]/table/tbody/tr/td[6]/select/option[16]')
skind.click()
co_id = driver.find_element_by_name('YM')
co_id.send_keys('10801')
search_co = driver.find_element_by_xpath('//*[@id="search_bar1"]/div/input')
search_co.click()
time.sleep(3)
select_co = driver.find_element_by_xpath('//*[@id="table01"]/form/table/tbody/tr[5]/td[3]/input')
select_co.click()

now_handle = driver.current_window_handle
all_handles = driver.window_handles
print('Found', len(all_handles), 'windows')
print(now_handle)

for handle in all_handles:
    if handle != now_handle:
        driver.switch_to.window(handle)
        time.sleep(3)
        print(driver.current_window_handle)
        print('ok')
        print('test')
        #hangs here
        print(driver.page_source)
        value = driver.find_element_by_xpath('//*[@id="table01"]/center/table[4]/tbody/tr[7]/td[8]')
print(value.text)

print('OK!')
