'''结算页面类'''
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class PayPage(BasePage):
    '''结算页面类'''

    #定位器
    locator_submit = (By.XPATH,'//form[@id="theForm"]/div[11]/div[2]/input[1]')
    locator_send_way = (By.NAME,'shipping')
    locator_pay_way = (By.NAME,'payment')

    def select_send_way(self,index):
        '''选择配送方式'''
        self.driver.find_elements(*self.locator_send_way)[index].click()

    def select_pay_way(self,index):
        '''选择支付方式'''
        self.driver.find_elements(*self.locator_pay_way)[index].click()

    def submit_order(self):
        '''提交订单'''
        xy = self.driver.find_element_by_tag_name('html').size
        print(xy)  #打标记
        self.driver.execute_script("window.scrollTo(0,"+str(xy["height"])+")")
        self.driver.find_element(*self.locator_submit).click()
        result = self.driver.current_url
        return result

    def pay_order(self,send_index,pay_index):
        '''订单支付'''
        self.select_send_way(send_index)
        self.select_pay_way(pay_index)
        result = self.submit_order()
        return result