import time
from selenium import webdriver
from getpass import getpass

loginID  = "plivoiview@gmail.com"
Password = "Plivo@123"
# EndPt_username = input("Enter your username: ")
# EndPt_password = getpass("Enter your password: ")
EndPt_username = "Atul7"
EndPt_password = "Plivo@123"
EndPt_alias    = "Atul7account"
EndPt_username1 = "Atul7"
EndPt_password1 = "Plivo@123"
EndPt_alias1    = "Atul7account"


driver = webdriver.Chrome("E:\\Automation\\chromedriver_win32\\chromedriver.exe")
driver.get("https://manage.plivo.com/")


def login (username, password):
	login = driver.find_element_by_id('id_username').send_keys(username)
	driver.find_element_by_id('id_password').send_keys(password)
	# Password.send_keys(Password)
	loginBut = driver.find_element_by_id('login-sub')
	loginBut.submit()


def CreateEndpoint (username, password, alias): 
	driver.find_element_by_link_text("New Endpoint").click()
	time.sleep(2)
	driver.find_element_by_id('id_username').send_keys(username)
	driver.find_element_by_id('id_password').send_keys(password)
	driver.find_element_by_id('id_alias').send_keys(alias)
	driver.find_element_by_xpath("//select[@name='app']/option[text()='Demo Speak']").click()
	driver.find_element_by_xpath("//*[@id='frm-add-endpoint']/div[3]/ul[2]/li/input").click()
	# driver.find_element_by_xpath("//*[@id='id_sub_account_chosen']/a/span").send_keys('Test_User')
	time.sleep(2)
	return;


login (loginID, Password)

time.sleep(5)
#### Clickin Endpoints
driver.find_element_by_link_text("Endpoints").click()
time.sleep(3)

#Creating the endpoints
CreateEndpoint (EndPt_username, EndPt_password, EndPt_alias )
CreateEndpoint (EndPt_username1, EndPt_password1, EndPt_alias1 )

