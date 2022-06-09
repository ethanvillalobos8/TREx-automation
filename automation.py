from selenium import webdriver
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
import os
import os.path
import datetime
import time
import csv
import sys

# Gets absolute path to resource
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

# CSV FILE CREATION
date = datetime.datetime.now()
date = date.strftime("%m-%d-%y_%H-%M-%S")
save_path = r'C:\Users\ethan\ideapublicschools.org\Student Information Systems - TREx Audit'
fileName = save_path + '\TREx Audit_' + date + '.csv'
csvfile = open(fileName,'w', newline = '\n')                                                                                                              
filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['Campus', 'Inbound Requests', 'Inbound Records & Transfers', 'Rejected Outbound Requests', 'Rejected Outbound Records & Transfers'])

# Establish Chrome webdriver
driver = webdriver.Chrome()
driver.get('https://tealprod.tea.state.tx.us/TSP/TEASecurePortal/Access/LogonServlet')

load_dotenv()
USERNAME = os.getenv('UNAME')
PASSWORD = os.getenv('PASSWORD')

print(USERNAME, PASSWORD)

# Enter username and password
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys(USERNAME)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(PASSWORD)

# Log-in
loginButton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/form/div[2]/span[2]/input')
loginButton.click()

# Stalls GET request below to prevent overriding initial client-server communication
time.sleep(2)

# Send GET request to district registrar route
driver.get('https://tealprod.tea.state.tx.us/TSP/TEASecurePortal/Access/ApplicationServlet?idx=TREx0distreg')

ddContents = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[1]/div/div/select')
ddContents = Select(ddContents)

# Iterate over dropdown contents and print results
count = 1
for contents in ddContents.options:
    campus = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[1]/div/div/select/option[' + str(count) + ']')
    campus.click()

    campus = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[1]/div/div/select/option[' + str(count) + ']')
    campusName = campus.get_attribute('innerHTML')

    inboundReq = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]')
    count1 = inboundReq.find_element_by_class_name('count').get_attribute('innerHTML')

    inboundRecTran = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[3]/div/div[2]/div[1]/table/tbody/tr[2]')
    count2 = inboundRecTran.find_element_by_class_name('count').get_attribute('innerHTML')

    rejectedOut = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[3]/div/div[2]/div[1]/table/tbody/tr[3]')
    count3 = rejectedOut.find_element_by_class_name('count').get_attribute('innerHTML')

    rejectedOutRecTran = driver.find_element_by_xpath('//*[@id="ie_width_hack"]/div[3]/div/div[2]/div[1]/table/tbody/tr[4]')
    count4 = rejectedOutRecTran.find_element_by_class_name('count').get_attribute('innerHTML')

    arr = [count1, count2, count3, count4]

    # Prints to console for testing purposes
    # print(campusName)
    # print(arr)
    # print('\n')

    filewriter.writerow([campusName, count1, count2, count3, count4])
    
    count = count + 1

csvfile.close()
driver.close()