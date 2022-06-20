from selenium import webdriver
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
import os
import os.path
import datetime
import time
import csv
import numpy as np

# CSV FILE CREATION
date = datetime.datetime.now()
date = date.strftime("%m-%d-%y_%H-%M-%S")
save_path = r'C:\Users\ethan\ideapublicschools.org\Student Information Systems - TREx Audit'
filePath = save_path + '\TREx Audit_' + date + '.csv'
fileName = '\TREx Audit_' + date + '.csv'
csvfile = open(filePath,'w', newline = '\n')                                                                                                              
filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
filewriter.writerow(['Region', 'Campus', 'Inbound Requests', 'Inbound Records & Transfers', 'Rejected Outbound Requests', 'Rejected Outbound Records & Transfers'])

# Establish Chrome webdriver
driver = webdriver.Chrome()
driver.get('https://tealprod.tea.state.tx.us/TSP/TEASecurePortal/Access/LogonServlet')

load_dotenv()
USERNAME = os.getenv('UNAME')
PASSWORD = os.getenv('PASSWORD')

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

# Texas Regions
regions = [
    'AUSTIN', 
    'EL PASO', 
    'GREATER HOUSTON', 
    'PERMIAN BASIN', 
    'RGV-LOWER', 
    'RGV-UPPER', 
    'SAN ANTONIO', 
    'TARRANT COUNTY'
]

# Region Campuses
austin = [
    'IDEA BLUFF SPRINGS ACADEMY',
    'IDEA BLUFF SPRINGS COLLEGE PREPARATORY', 
    'IDEA HEALTH PROFESSIONS ACADEMY', 
    'IDEA HEALTH PROFESSIONS COLLEGE PREPARATORY',
    'IDEA KYLE ACADEMY',
    'IDEA KYLE COLLEGE PREPARATORY',
    'IDEA MONTOPOLIS ACADEMY',
    'IDEA MONTOPOLIS COLLEGE PREPARATORY',
    'IDEA PARMER PARK ACADEMY',
    'IDEA PARMER PARK COLLEGE PREPARATORY',
    'IDEA PFLUGERVILLE ACADEMY',
    'IDEA PFLUGERVILLE COLLEGE PREPARATORY',
    'IDEA ROUND ROCK TECH ACADEMY',
    'IDEA ROUND ROCK TECH COLLEGE PREPARATORY',
    'IDEA RUNDBERG ACADEMY',
    'IDEA RUNDBERG COLLEGE PREPARATORY'
]
el_paso = [
    'IDEA EDGEMERE ACADEMY',
    'IDEA EDGEMERE COLLEGE PREPARATORY',
    'IDEA HORIZON VISTA ACADEMY',
    'IDEA HORIZON VISTA COLLEGE PREPARATORY',
    'IDEA MESA HILLS ACADEMY',
    'IDEA MESA HILLS COLLEGE PREPARATORY',
    'IDEA MESQUITE HILLS ACADEMY',
    'IDEA MESQUITE HILLS COLLEGE PREPARATORY',
    'IDEA RIO VISTA ACADEMY',
    'IDEA RIO VISTA COLLEGE PREPARATORY'
]
greater_houston = [
    'IDEA HARDY ACADEMY',
    'IDEA HARDY COLLEGE PREPARATORY',
    'IDEA LAKE HOUSTON ACADEMY',
    'IDEA LAKE HOUSTON COLLEGE PREPARATORY',
    'IDEA SPEARS ACADEMY',
    'IDEA SPEARS COLLEGE PREPARATORY'
]
permian_basin = [
    'IDEA YUKON ACADEMY',
    'IDEA YUKON COLLEGE PREPARATORY'
]
rgv_lower = [
    'IDEA ACADEMY ALAMO',
    'IDEA COLLEGE PREPARATORY ALAMO',
    'IDEA BROWNSVILLE ACADEMY',
    'IDEA BROWNSVILLE COLLEGE PREPARATORY',
    'IDEA ELSA ACADEMY',
    'IDEA ELSA COLLEGE PREPARATORY',
    'IDEA FRONTIER ACADEMY',
    'IDEA FRONTIER COLLEGE PREPARATORY',
    'IDEA HARLINGEN ACADEMY',
    'IDEA HARLINGEN COLLEGE PREPARATORY',
    'IDEA RIVERVIEW ACADEMY',
    'IDEA RIVERVIEW COLLEGE PREPARATORY',
    'IDEA ROBINDALE ACADEMY',
    'IDEA ROBINDALE COLLEGE PREPARATORY',
    'IDEA ACADEMY SAN BENITO',
    'IDEA COLLEGE PREPARATORY SAN BENITO',
    'IDEA SPORTS PARK ACADEMY',   
    'IDEA SPORTS PARK COLLEGE PREPARATORY',
    'IDEA ACADEMY WESLACO',
    'IDEA COLLEGE PREP WESLACO',
    'IDEA WESLACO PIKE ACADEMY',
    'IDEA WESLACO PIKE COLLEGE PREPARATORY'
]
rgv_upper = [
    'IDEA ACADEMY',
    'IDEA COLLEGE PREP',
    'IDEA EDINBURG ACADEMY',
    'IDEA EDINBURG COLLEGE PREPARATORY',
    'IDEA LA JOYA ACADEMY',
    'IDEA LA JOYA COLLEGE PREPARATORY',
    'IDEA LOS ENCINOS ACADEMY',
    'IDEA LOS ENCINOS COLLEGE PREPARATORY',
    'IDEA MCALLEN ACADEMY',
    'IDEA MCALLEN COLLEGE PREPARATORY',
    'IDEA ACADEMY MISSION',
    'IDEA COLLEGE PREPARATORY MISSION',
    'IDEA NORTH MISSION ACADEMY',
    'IDEA NORTH MISSION COLLEGE PREPARATORY',
    'IDEA OWASSA ACADEMY',
    'IDEA OWASSA COLLEGE PREPARATORY',
    'IDEA PALMVIEW ACADEMY',
    'IDEA PALMVIEW COLLEGE PREPARATORY',
    'IDEA ACADEMY PHARR',
    'IDEA COLLEGE PREPARATORY PHARR',
    'IDEA QUEST ACADEMY',
    'IDEA QUEST COLLEGE PREPARATORY',
    'IDEA RIO GRANDE CITY ACADEMY',
    'IDEA RIO GRANDE CITY COLLEGE PREPARATORY',
    'IDEA ACADEMY SAN JUAN',
    'IDEA COLLEGE PREPARATORY SAN JUAN',
    'IDEA TOROS COLLEGE PREPARATORY',
    'IDEA TRES LAGOS ACADEMY',
    'IDEA TRES LAGOS COLLEGE PREPARATORY'
]
san_antonio = [
    'IDEA AMBER CREEK ACADEMY',
    'IDEA AMBER CREEK COLLEGE PREPARATORY',
    'IDEA BRACKENRIDGE ACADEMY',
    'IDEA BRACKENRIDGE COLLEGE PREPARATORY',
    'IDEA BURKE ACADEMY',
    'IDEA BURKE COLLEGE PREPARATORY',
    'IDEA CARVER ACADEMY',
    'IDEA CARVER COLLEGE PREPARATORY',
    'IDEA CONVERSE ACADEMY',
    'IDEA CONVERSE COLLEGE PREPARATORY',
    'IDEA EASTSIDE ACADEMY',
    'IDEA EASTSIDE COLLEGE PREPARATORY',
    'IDEA EWING HALSELL ACADEMY',
    'IDEA EWING HALSELL COLLEGE PREPARATORY',
    'IDEA HIDDEN MEADOW ACADEMY',
    'IDEA HIDDEN MEADOW COLLEGE PREPARATORY',
    'IDEA INGRAM HILLS ACADEMY',
    'IDEA INGRAM HILLS COLLEGE PREPARATORY',
    'IDEA JUDSON ACADEMY',
    'IDEA JUDSON COLLEGE PREPARATORY',
    'IDEA MAYS ACADEMY',
    'IDEA MAYS COLLEGE PREPARATORY',
    'IDEA MONTERREY PARK ACADEMY',
    'IDEA MONTERREY PARK COLLEGE PREPARATORY',
    'IDEA NAJIM ACADEMY',
    'IDEA NAJIM COLLEGE PREPARATORY',
    'IDEA SOUTH FLORES ACADEMY',
    'IDEA SOUTH FLORES COLLEGE PREPARATORY',
    'IDEA WALZEM ACADEMY',
    'IDEA WALZEM COLLEGE PREPARATORY'
]
tarrant_county = [
    'IDEA ACHIEVE ACADEMY',
    'IDEA ACHIEVE COLLEGE PREPARATORY',
    'IDEA EDGECLIFF ACADEMY',
    'IDEA EDGECLIFF COLLEGE PREPARATORY',
    'IDEA RISE ACADEMY',
    'IDEA RISE COLLEGE PREPARATORY',
    'IDEA SOUTHEAST ACADEMY',
    'IDEA SOUTHEAST COLLEGE PREPARATORY'
]

# Array of regions
region_campus = np.array([
    austin, 
    el_paso, 
    greater_houston, 
    permian_basin, 
    rgv_lower, rgv_upper, 
    san_antonio, 
    tarrant_county
])

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

    # Prints to console for testing purposes
    # arr = [count1, count2, count3, count4]
    # print(campusName)
    # print(arr)
    # print('\n')

    for region in range(8):
        if campusName in region_campus[region]:
            filewriter.writerow([regions[region], campusName, count1, count2, count3, count4])
            break
        elif campusName not in region_campus[0] and campusName not in region_campus[1] and campusName not in region_campus[2] and campusName not in region_campus[3] and campusName not in region_campus[4] and campusName not in region_campus[5] and campusName not in region_campus[6] and campusName not in region_campus[7]:
            filewriter.writerow(['NA', campusName, count1, count2, count3, count4])
            break
    
    count = count + 1

csvfile.close()
driver.close() 