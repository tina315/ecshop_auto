'''添加商品类'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page.base_page import BasePage

class AddProductPage(BasePage):
    '''添加商品类'''
    #定位器
    locator_menu_frame = 'menu-frame'
    locator_get_add_product = (By.XPATH,'//ul[@id="menu-ul"]/li[1]/ul/li[2]/a')
    locator_main_frame = 'main-frame'
    locator_product_name = (By.NAME,'goods_name')
    locator_product_tag = (By.NAME,'cat_id')
    locator_product_price = (By.NAME,'shop_price')
    locator_product_market_price = (By.XPATH,'//table[@id="general-table"]/tbody/tr[9]/td[2]/input[2]')
    locator_promote_start_date = (By.ID,'promote_start_date')
    locator_promote_end_date = (By.ID,'promote_end_date')
    locator_promote_sale = (By.ID,'promote_1')
    locator_product_picture = (By.NAME,'goods_img')
    locator_product_submit = (By.XPATH,'//div[@id="tabbody-div"]/form/div/input[2]')
    locator_assert = (By.XPATH,'//div[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span')

    def get_add_product(self):
        '''点击添加商品'''
        self.driver.find_element(*self.locator_get_add_product).click()

    def product_name(self,product_name):
        '''输入商品名称'''
        self.driver.find_element(*self.locator_product_name).clear()
        self.driver.find_element(*self.locator_product_name).send_keys(product_name)

    def product_tag(self,value):
        '''选择商品分类'''
        ele = self.driver.find_element(*self.locator_product_tag)
        select = Select(ele)
        select.select_by_value(value)

    def product_price(self,price):
        '''输入商品本店价格'''
        self.driver.find_element(*self.locator_product_price).clear()
        self.driver.find_element(*self.locator_product_price).send_keys(price)

    def product_maret_price(self):
        '''按商店价格取整市场价'''
        self.driver.find_element(*self.locator_product_market_price).click()

    def promote_start_date(self,sdate):
        '''输入开始日期'''
        js = "document.getElementById('%s').removeAttribute('readonly')"%(self.locator_promote_start_date[1])
        self.driver.execute_script(js)
        self.driver.find_element(*self.locator_promote_start_date).clear()
        self.driver.find_element(*self.locator_promote_start_date).send_keys(sdate)

    def promote_end_date(self,edate):
        '''输入开始日期'''
        js = "document.getElementById('%s').removeAttribute('readonly')"%(self.locator_promote_end_date[1])
        self.driver.execute_script(js)
        self.driver.find_element(*self.locator_promote_end_date).clear()
        self.driver.find_element(*self.locator_promote_end_date).send_keys(edate)

    def product_sale_price(self,sale_price):
        '''输入促销价格'''
        js = "document.getElementById('%s').removeAttribute('disabled')"%(self.locator_promote_sale[1])
        self.driver.execute_script(js)
        self.driver.find_element(*self.locator_promote_sale).clear()
        self.driver.find_element(*self.locator_promote_sale).send_keys(sale_price)

    def product_picture(self,path):
        '''上传商品图片'''
        self.driver.find_element(*self.locator_product_picture).send_keys(path)

    def product_submit(self):
        '''提交商品信息'''
        self.driver.find_element(*self.locator_product_submit).click()

    def add_product(self,product_name,value,price,sdate,edate,sale_price,path):
        '''添加商品'''
        self.switch_to_frame(self.locator_menu_frame)
        self.product_management()
        self.get_add_product()
        self.switch_out_frame()
        self.switch_to_frame(self.locator_main_frame)
        self.product_name(product_name)
        self.product_tag(value)
        self.product_price(price)
        self.product_maret_price()
        self.promote_start_date(sdate)
        self.promote_end_date(edate)
        self.product_sale_price(sale_price)
        self.product_picture(path)
        self.product_submit()
        time.sleep(4)
        result = self.assert_result(self.locator_assert)
        self.switch_out_frame()
        return result
