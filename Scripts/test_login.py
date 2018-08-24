import os,sys
sys.path.append(os.getcwd())
import allure

from Page.page_login import PageLogin
from Base.get_driver import get_driver

class TestLogin():
    def setup_class(self):
        self.driver = get_driver("com.vcooline.aike",".umanager.LoginActivity")
        self.login = PageLogin(self.driver)
    def teardown_class(self):
        self.driver.quit()
    # def test_login(self):
    #     self.login.page_click_btn()
    #     print("获取的toast信息为:",self.login.base_get_toast("输入手机"))
    #     # 断言
    #     try:
    #         assert "输入手机号" in self.login.base_get_toast("输入手机")
    #     except:
    #         print("出错啦!")
    #         raise

    # 立即体验
    @allure.step("开始测试体验")
    def test_ty(self):
        # 点击体验
        allure.attach("描述", "点击体验按钮")
        self.login.page_click_ty_btn()
        # 点击立即体验
        allure.attach("描述", "点击立即体验按钮")
        self.login.page_click_ljty_btn()
        print("获取的toast值为:",self.login.base_get_toast("输入手机"))
        try:
            # 断言
            assert "请1输入" in self.login.base_get_toast("请输入手机")
            allure.attach("描述", "获取toast成功！")
        except:
            allure.attach("描述", "获取toast失败！")
            print("出错啦!")
            # 截图
            self.login.base_get_screen_image()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("描述：失败原因", f.read(), allure.attach_type.PNG)
                raise
