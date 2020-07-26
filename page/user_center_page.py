'''用户中心页面类'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base_page import BasePage


class UserCenterPage(BasePage):
    '''用户中心页面类'''

    #定位器
    locator_addr = (By.XPATH,'//div[@class="userMenu"]/a[4]')
    locator_country = (By.NAME,'country')
    locator_province = (By.NAME, 'province')
    locator_city = (By.NAME, 'city')
    locator_district = (By.NAME, 'district')
    locator_consignee = (By.NAME, 'consignee')
    locator_email = (By.NAME, 'email')
    locator_address = (By.NAME, 'address')
    locator_tel = (By.NAME, 'tel')
    locator_submit = (By.NAME, 'submit')

    def get_in_addr(self):
        '''进入收货地址管理'''
        self.driver.find_element(*self.locator_addr).click()

    def select_country(self,country):
        '''选择国家'''
        ele = self.driver.find_element(*self.locator_country)
        select = Select(ele)
        select.select_by_visible_text(country)

    def select_province(self,province):
        '''选择省份'''
        ele = self.driver.find_element(*self.locator_province)
        select = Select(ele)
        select.select_by_visible_text(province)

    def select_city(self,city):
        '''选择城市'''
        ele = self.driver.find_element(*self.locator_city)
        select = Select(ele)
        select.select_by_visible_text(city)

    def select_district(self,district):
        '''选择地区'''
        ele = self.driver.find_element(*self.locator_district)
        select = Select(ele)
        select.select_by_visible_text(district)

    def ele_consignee(self,consignee):
        '''输入收件人'''
        self.driver.find_element(*self.locator_consignee).clear()
        self.driver.find_element(*self.locator_consignee).send_keys(consignee)

    def ele_email(self,email):
        '''输入邮件'''
        self.driver.find_element(*self.locator_email).clear()
        self.driver.find_element(*self.locator_email).send_keys(email)

    def ele_address(self,address):
        '''输入地址'''
        self.driver.find_element(*self.locator_address).clear()
        self.driver.find_element(*self.locator_address).send_keys(address)

    def ele_tel(self,tel):
        '''输入电话'''
        self.driver.find_element(*self.locator_tel).clear()
        self.driver.find_element(*self.locator_tel).send_keys(tel)

    def submit_addr(self):
        '''提交收货信息'''
        self.driver.find_element(*self.locator_submit).click()

    def add_addr(self,country,province,city,district,consignee,email,addr,tel):
        '''新增收货地址'''
        self.font_user_center()
        self.get_in_addr()
        self.select_country(country)
        self.select_province(province)
        self.select_city(city)
        self.select_district(district)
        self.ele_consignee(consignee)
        self.ele_email(email)
        self.ele_address(addr)
        self.ele_tel(tel)
        self.submit_addr()