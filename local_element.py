from selenium import webdriver

from time import sleep

import os
# ChromeOptions options = new ChromeOptions();
#    options.setBinary("C:/Program Files (x86)/Google/Chrome/chrome.exe");



drive = webdriver.Chrome()
drive.get("https://mail.163.com/")
ele = drive.find_element_by_css_selector("html body div#mainBg.main div#loginBlock.login.tab-2 div.loginFunc div#lbNormal.loginFuncNormal")
print(ele.text)
ele.click()

drive.current_window_handle

# drive.find_element_by_name("email")
#drive.minimize_window()
# //*[@id="auto-id-1535805855364"]
# loginFuncNormal
# ele = drive.find_element_by_css_selector("html body div#mainBg.main div#loginBlock.login.tab-2 div.loginFunc div#lbNormal.loginFuncNormal")
# ele.click()
# print("a")
# drive.refresh()
#
# sleep(3)

# ele_count = drive.find_element_by_name("email")
# ele_count.clear()
# ele_count.send_keys("chengli.lily")


# ele.clear()
# ele.send_keys("chengli.lily")
#
# ele_pwd = drive.find_element_by_id("auto-id-1535805855365")
# ele_pwd.clear()
# ele_pwd.send_keys("lclwsf0909")
#
#
# drive.find_element_by_id("dologin").click()
sleep(1)


sleep(5)
# drive.quit()
#
