from selenium import webdriver
import time
import unittest

class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://pan.baidu.com/')
        self.assertIn('百度网盘，让美好永远陪伴', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)


# dr = webdriver.Chrome()
# dr.get("https://pan.baidu.com/")
# dr.implicitly_wait(5000)
# loginType = dr.find_element_by_id("TANGRAM__PSP_4__footerULoginBtn")
# loginType.click()
# username = dr.find_element_by_id("TANGRAM__PSP_4__userName")
# username.clear()
# username.send_keys("javanihaoma")
# pwd = dr.find_element_by_id("TANGRAM__PSP_4__password")
# pwd.clear()
# pwd.send_keys("javahenhao")
# isSelect = dr.find_element_by_id("TANGRAM__PSP_4__memberPass")
# isSelect.click()
# submit = dr.find_element_by_id("TANGRAM__PSP_4__submit")
# submit.click()
# time.sleep(5)
# dr.quit()
