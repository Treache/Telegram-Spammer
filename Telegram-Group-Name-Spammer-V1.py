## Erfan and Aref ##
## Telegram Group Name Spammer V1.0 ##

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

strings = ['triskaidekaphobia','spooky','creepy','horrifying','unnerving','carry','Death is only the beginning','Demacia, Now and forever','mojalleqin Organization','ogre','evil','elf','eerie']
phoneNumber = raw_input('shomare khod ra vared konid : ')
browser = webdriver.Firefox()
browser.get('https://web.telegram.org/')
time.sleep(10)
a = browser.find_element_by_name("phone_number")
a.send_keys(phoneNumber)
a.send_keys(Keys.ENTER)
print ('aknoon ok dar alert ra click konid ;)\n')
flagOk = False
while not flagOk:
    flag = raw_input('harvaght ok ra click kardid harf y ra befrestid : ')
    if flag == 'y':
        flagOk = True
phoneCode = raw_input('code tayid shode dar telegram ra inja vared konid : ')
a = browser.find_element_by_name("phone_code")
a.send_keys(phoneCode)
a.send_keys(Keys.ENTER)
print ('aknoon gp morede nazar khod ra vared konid ; masalan CE ;)')
flagOk = False
while not flagOk:
    flag = raw_input('harvaght gp ra click kardid harf y ra befrestid : ')
    if flag == 'y':
        flagOk = True
counter = 0
while True:
    if(counter == 12):
        counter = 0
    counter += 1
    time.sleep(5)
    browser.find_element_by_class_name("tg_head_peer_title").click()
    browser.find_element_by_css_selector("a.md_modal_action.ng-scope").click()
    changeTxt = browser.find_element_by_class_name("md-input")
    changeTxt.clear()
    changeTxt.send_keys(strings[counter])
    changeTxt.send_keys(Keys.ENTER)
