from Base.base import Base
import Page

class PageLogin(Base):
    # 点击登录按钮
    def page_click_btn(self):
        self.base_find_elements(Page.ak_login_btn)

    # 获取登录toast方法封装
    # def page_get_toast(self):
    #     return self.base_get_toast(Page.ak_login_toast_msg)

    def page_click_ty_btn(self):
        self.base_xpath_click("体验")

    def page_click_ljty_btn(self):
        self.base_xpath_click("立即体验")