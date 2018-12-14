import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.constants import *


def find_all_mail(from_who_email, subject_txt , limit):
    mails = browser.find_elements_by_class_name('zE')
    # mails.click()

    emails_list = []

    index_limit = 0;
    for item in mails:
        # item.click()

        time.sleep(2)
        iTR = item

        itd = iTR.find_elements(By.TAG_NAME, 'td')

        subject = itd[5].find_element_by_class_name('bqe').text

        time.sleep(2)

        if (subject_txt in subject):
            index_limit = index_limit + 1

            if index_limit > limit:
                return emails_list

            iTR.click()
            time.sleep(2)

            body2 = browser.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]')

            print(body2.text)

            print("###################")

            time.sleep(2)

            emails_list.append( body2.text )

            browser.back()

    return emails_list



def find_single_mail( from_who_email, subject_txt):
    mails = browser.find_elements_by_class_name('zE')
    # mails.click()

    for item in mails:
        # item.click()

        time.sleep(2)
        iTR = item

        itd = iTR.find_elements(By.TAG_NAME, 'td')

        subject = itd[5].find_element_by_class_name('bqe').text

        time.sleep(2)

        if (subject_txt in subject):
            iTR.click()
            time.sleep(2)

            body2 = browser.find_element_by_xpath(
                '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]')

            print(body2.text)

            print("###################")

            time.sleep(2)

            return body2.text

            browser.back()


def login_recv_all_mail(recv_email, recv_passwd,  from_who_email , subject_txt, browser):
    try:
        browser.get(GMAIL_WEBSITE)

        time.sleep(4)

        emailElem = browser.find_element_by_id('identifierId')
        emailElem.send_keys(recv_email)

        next = browser.find_element_by_id('identifierNext')
        if next:
            next.click()

        time.sleep(2)

        passwordElem = browser.find_element_by_name("password")
        passwordElem.send_keys(recv_passwd)
        passwordElem.submit()

        time.sleep(2)

        # Passwd Next Button
        composeElem = browser.find_element_by_class_name("CwaK9")  # this only works half of the time
        composeElem.click()

        time.sleep(7)
        # Now I am logged in

        return find_all_mail( from_who_email, subject_txt)

    except Exception as ex:
        print(str(ex))
    finally:
        return None


def login_recv_single_mail(recv_email, recv_passwd,  from_who_email , subject_txt, browser):
    try:
        browser.get(GMAIL_WEBSITE)

        time.sleep(4)

        emailElem = browser.find_element_by_id('identifierId')
        emailElem.send_keys(recv_email)

        next = browser.find_element_by_id('identifierNext')
        if next:
            next.click()

        time.sleep(2)

        passwordElem = browser.find_element_by_name("password")
        passwordElem.send_keys(recv_passwd)
        passwordElem.submit()

        time.sleep(2)

        # Passwd Next Button
        composeElem = browser.find_element_by_class_name("CwaK9")  # this only works half of the time
        composeElem.click()

        time.sleep(7)
        # Now I am logged in

        return find_single_mail( from_who_email, subject_txt)

    except Exception as ex:
        print(str(ex))
    finally:
        return None


if __name__ == '__main__':

   browser = webdriver.Chrome()
   print("Main called")


'''

SIEGEBREAKER_SUB = "SiegeBreaker"

browser = webdriver.Chrome()
browser.get('https://www.gmail.com')

time.sleep(4)

emailElem = browser.find_element_by_id('identifierId')

EMAIL = ""
PASSWD = ""

emailElem.send_keys(EMAIL)


next = browser.find_element_by_id('identifierNext')
if next:
    next.click()

# emailElem.submit()

time.sleep(2)

passwordElem = browser.find_element_by_name("password")  # .sendKeys("Password");#browser.find_element_by_id('pstMsg')
passwordElem.send_keys(PASSWD)

passwordElem.submit()

# time.sleep(4)

# next = browser.find_element_by_id('identifierNext')
# if next:
#        next.click()

composeElem = browser.find_element_by_class_name("CwaK9")  # this only works half of the time
composeElem.click()

time.sleep(7)

# browser.get("https://mail.google.com/mail/u/0/#all")

mails = browser.find_elements_by_class_name('zE')
# mails.click()

for item in mails:
    #item.click()

    time.sleep(2)
    iTR = item

    itd = iTR.find_elements(By.TAG_NAME, 'td')

    subject = itd[5].find_element_by_class_name('bqe').text

    time.sleep(2)

    print("Subject Processed" + subject)
    if( SIEGEBREAKER_SUB in subject ):

        iTR.click()
        time.sleep(2)

        body2 = browser.find_element_by_xpath(
            '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]')

        print(body2.text)

        print("###################")


        time.sleep(2)
        browser.back()
        
        
'''
