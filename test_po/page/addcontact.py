from selenium.webdriver.common.by import By

from test_po.page.base import Base
from test_po.page.conttact import Contact


class AddContact(Base):

    def addcon(self,name,account,phonenum):
        self.find(By.ID,'username').send_keys(name)
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        self.find(By.ID,'memberAdd_phone').send_keys(phonenum)
        self.find(By.CSS_SELECTOR,'.qui_btn ww_btn js_btn_save').click()
        return Contact(self.driver)