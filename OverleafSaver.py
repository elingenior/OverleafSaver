# !source activate overleaf, to change the environement

import os

import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import shutil

def get_dic(input,dic):
    i = 0
    i1 = 0
    stop = 0
    while stop == 0:
        i = i+1
        if input[i] == ';':
            if i1 != 0:
                date = input[(i1)+1:i-1]
                place = input[(i):]
                stop = 1
            else :
                name = input[1:(i-1)]
                i1 = i+1
            # print(i)
        if i> 200 or i>(len(input)-1):
            print('Name too long, check')
            stop = 1
    if name != '':
        dic[name] = [date,place]
    return dic
def print_dic(dic,file):
    l = 1
    for line in dic:
        file.writelines("'{0}';'{1}';'{2}'\n".format(line,dic[line][0],l))
        l+=1


def get_name(name):
    i = 0
    for char in name:
        if char == "'":
            return name[i+1 : -1]
            break
        else :
            i = i + 1
def move_file(name):
    name = name.replace(" ","%20")
    name = name.replace("&","%26")
    name+= '.zip'
    source = '/gneven/Downloads/'+name
    destination = '/gneven/Documents/Save_Overleaf' # select desination file
    dest = shutil.move(source, destination)
    # os.remove(source)

profile = webdriver.FirefoxProfile('profile')
profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip"); #list of MIME types to save to disk without asking what to use to open the fil
# profile.set_preference("browser.download.dir", os.getcwd())
try:
    driver = webdriver.Firefox(executable_path='Geckodriver/geckodriver',firefox_profile = profile)
    driver.get("https://www.overleaf.com/login")
except:
    print('No internet connection ?')


email_box = driver.find_element_by_name('email')
email_box.send_keys('email@mail.com') # enter e mail address

password_box = driver.find_element_by_name('password')
password_box.send_keys('pass') # enter password

login_button = driver.find_element_by_class_name("btn-primary")
login_button.click()

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userProfileInformation")))

# all_date = driver.find_elements_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr/td[3]/span[1]")
#name = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[2]/td[1]/div/span/a")
# name = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[2]/td[1]/div/span/a")
# name2 = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[2]/td[1]/div/input")
# # #date = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[3]/td[3]/span[1]")
#date = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[42]/td[2]/span")
#date.getext()
#for date in all_date:
    #print(date.get_attribute("tooltip"))
#test =
#print(date)

logfile = open("log.txt","r",encoding="utf8")

log = logfile.readlines()
dic = {"test" : ["Bite",2]}
for log_l in log :
    dic = get_dic(log_l,dic)

del dic["test"]

# logfile.truncate(0)
logfile.close()
logfile = open("log.txt","w",encoding="utf8")

stop = 1
online =1
if online == 0:
    name_test = ['shit shit shit','PTDO Summary','Transport planning methods summary (Copy)','Avioation I']
    data_test = ['12th Feb 2020, 1:08 pm','12th Feb 2020, 10:46 am','10th Feb 2020, 1:25 pm','5th Feb 2020, 3:57 pm']
i=1

while stop==1 :
    i=i+1
    try:
    # for c in [1,2]:
        if online == 1 :

            date_i = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[%d]/td[3]/span[1]"%(i))
            name_i = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[%d]/td[1]/div/input"%(i))
            name_i = name_i.get_attribute("aria-label")
            date_i = date_i.get_attribute("tooltip")

            name_i = get_name(name_i)
        else:
            name_i = name_test[i-1]
            date_i = data_test[i-1]
        # print(dic)
        # print(dic[name_i][0])
        # print("'{0}' dic _: '{1}'".format(date_i,dic[name_i][0]))
    except :
        print("I have found '{0}' projects".format(i))
        stop = 0
    print(name_i)
    try:
        if name_i in dic.keys():
            if date_i != dic[name_i][0]:
                download_button = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[%d]/td[4]/div/button[2]"%(i))
                # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(download_button))
                download_button.click()
                name = name_i.replace(" ","%20")
                name = name.replace("&","%26")
                name+= '.zip'
                os.remove('/gneven/Documents/Save_Overleaf/'+name)
                dic[name_i] = [date_i,i]
                print('\n \n Project : ',name_i,' changed\n')
                move_file(name_i)
        else:
            download_button = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/div[3]/div/div/ul/table/tbody/tr[%d]/td[4]/div/button[2]"%(i))#
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable(download_button))
            download_button.click()

            print('\n \n New project : ',name_i,'\n')

            dic[name_i] = [date_i,i]
            move_file(name_i)
    except:
        print('Issues with: ',name_i,i)

# print(dic['shit shit shit'])

#print(name.get_attribute("href"))
#print(name2.get_attribute("aria-label"))

print_dic(dic,logfile)


logfile.close()
driver.quit()
