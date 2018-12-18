import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utils.constants import *


def send_mail(sender_email, sender_passwd, recv_email, subject_txt, body_txt, browser):
    # Compose Email Button
    composeElem = browser.find_element_by_class_name('z0')  # this only works half of the time
    composeElem.click()

    time.sleep(2)

    # To Button
    toElem = browser.find_element_by_name("to")
    toElem.send_keys(recv_email)

    time.sleep(2)

    subjElem = browser.find_element_by_name("subjectbox")
    subjElem.send_keys(subject_txt)

    time.sleep(2)

    bodyElem = browser.find_element_by_class_name(
        'editable')  # _css_selector('#\:nw') #this is where I get stuck and not sure what to do here
    bodyElem.send_keys(body_txt)

    time.sleep(2)

    sendElem = browser.find_element_by_xpath('//*[@id=":8t"]')  # not sure if this is correct too
    time.sleep(2)
    sendElem.click()

    time.sleep(5)

    return True;


def login_send_mail(sender_email, sender_passwd, recv_email, subject_txt, body_txt, browser):
    try:
        browser.get(GMAIL_WEBSITE)

        time.sleep(4)

        emailElem = browser.find_element_by_id('identifierId')
        emailElem.send_keys(sender_email)

        next = browser.find_element_by_id('identifierNext')
        if next:
            next.click()

        time.sleep(2)

        passwordElem = browser.find_element_by_name("password")
        passwordElem.send_keys(sender_passwd)
        passwordElem.submit()

        time.sleep(2)

        # Passwd Next Button
        composeElem = browser.find_element_by_class_name("CwaK9")  # this only works half of the time
        composeElem.click()

        time.sleep(7)
        # Now I am logged in

        return send_mail(sender_email, sender_passwd, recv_email, subject_txt, body_txt, browser)

    except Exception as ex:
        print(str(ex))
    finally:
        return True


if __name__ == '__main__':
    browser = webdriver.Chrome()


    login_send_mail(CLIENT_MAIL, CLIENT_MAIL_PASSWD, CONTROLLER_EMAIL, "WHATEVER", "GOTOHELL", browser);

    print("Main called")
