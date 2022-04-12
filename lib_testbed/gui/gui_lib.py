import time
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from lib.logger import log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class GuiLib:
    def __init__(self, browser):
        self.browser = browser
        self.type = {'xpath': By.XPATH, 'id': By.ID, "link text": By.LINK_TEXT,
                     "partial link text": By.PARTIAL_LINK_TEXT, "name": By.NAME, "tag name": By.TAG_NAME,
                     "class name": By.CLASS_NAME, "css selector": By.CSS_SELECTOR}

    def open(self, url):
        try:
            self.browser.get(url)
        except NoAlertPresentException:
            raise

    def action_element(self, element):
        new_element = element.split('=', 1)
        self.check_action(new_element[0])
        return self.type[new_element[0]], new_element[1]

    def check_action(self, act):
        if act not in self.type.keys():
            raise Exception('your action is not correct, only support id xpath')

    def upload_file(self, element):
        action, element = self.action_element(element)
        upload = self.browser.find_element(action, element)
        upload.send_keys('/Users/hitron-app/Downloads/basic.cfg')
        print(upload.get_attribute('value'))
        # 上传按钮属于input框，可直接使用send_keys，如果是非input类型，需要通过js、flash等实现。

    def print(self, element):
        action, element = self.action_element(element)
        a = self.browser.find_element(action, element)
        print(a.text)
        a.click()
        # 打印元素的text

    def alert(self):
        dig_confirm = self.browser.switch_to.alert
        # 切换弹窗
        time.sleep(1)
        print(dig_confirm.text)
        time.sleep(1)
        dig_confirm.accept()
        # dig_confirm.dismiss()

    def Find_element(self, text):
        try:
            a = self.browser.find_element_by_partial_link_text(text).click()
        except NoSuchElementException:
            print("No element found")

    def clear(self, element):
        action, element = self.action_element(element)
        self.browser.find_element(action, element).clear()

    def input(self, element, text):
        action, element = self.action_element(element)
        self.browser.find_element(action, element).send_keys(text)

    def keyboard(self, element):
        action, element = self.action_element(element)
        self.browser.find_element(action, element).send_keys(Keys.COMMAND, 'a')
        # 快捷键command+a全选，因为用clear清除数据有的清除后click不成功

    def key_Enter(self, element):
        action, element = self.action_element(element)
        self.browser.find_element(action, element).send_keys(Keys.ENTER)

    def click(self, element):
        action, element = self.action_element(element)
        a = self.browser.find_element(action, element)
        a.click()

    def click2(self, element):
        action, element = self.action_element(element)
        a = self.browser.find_element(action, element)
        webdriver.ActionChains(self.browser).move_to_element(a).click(a).perform()

    def select(self, element, text):
        action, element = self.action_element(element)
        self.browser.find_element(action, element).select(text)

    def wait_until(self, element):
        action, element = self.action_element(element)
        # WebDriverWait(self.browser, 30, 1).until(EC.presence_of_element_located((action, element)))
        # 在30s内，每隔1s检查一次所需要的元素是否被加载出来，加载出来了就执行下一步，没有加载出来就继续等待
        WebDriverWait(self.browser, 30, 1).until(EC.visibility_of_all_elements_located((action, element)))
        # EC.visibility_of_all_elements_located可见元素

    def get_status_text(self, element):
        action, element = self.action_element(element)
        try:
            print(self.browser.find_element(action, element).text)
        except (ImportError, AttributeError) as e:
            log.logger.warning(e)

    def refresh(self):
        try:
            self.browser.refresh()  # 刷新方法 refresh
            print('test pass: refresh successful')
            self.browser.quit()
        except (ImportError, AttributeError) as e:
            log.logger.warning(e)

    def get_title(self):
        self.browser.find_element(By.ID, 'kw').send_keys('456')
        self.browser.find_element(By.ID, 'su').click()
        self.browser.find_element(By.XPATH, '//*[@id="1"]/h3/a').click()
