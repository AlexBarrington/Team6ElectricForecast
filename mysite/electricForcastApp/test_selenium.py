# from django.test import LiveServerTestCase
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from electricForcastApp.models import MyUser
# from electricForcastApp.models import MyUserManager
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# class AdminTestCase(LiveServerTestCase):
#     def setUp(self):
#         # setUp is where you instantiate the selenium webdriver and loads the browser.
#         MyUser.objects.create_superuser(
#             username='admin',
#             password='admin',
#             email='admin@example.com'
#         )
#
#         self.selenium = webdriver.Chrome()
#         self.selenium.maximize_window()
#         super(AdminTestCase, self).setUp()
#
#     def tearDown(self):
#         # Call tearDown to close the web browser
#         self.selenium.quit()
#         super(AdminTestCase, self).tearDown()
#
#
# driver = webdriver.Firefox()
# driver.get("http://localhost:8000/")
#
# try:
#     element = WebDriverWait(driver, 6).until(
#         EC.presence_of_element_located(By.ID, "sidebar_menu"))
#     )
# finally:
#     print
#     element  # This will either print element object or None
#
# driver.quit()
