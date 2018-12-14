#!/usr/bin/python

from scapy.layers.inet import ICMP, IP
import gmail_recv
from selenium import webdriver

from scapy.all import *
import sys
import binascii
from random import randint
from Crypto.PublicKey import RSA
from datetime import datetime
import seccure
import time

import sys
from utils.constants import *
from utils.crypt import get_decrypted_content


def main():

    print("Initializing....")

    browser = webdriver.Chrome()

    payloads_list = gmail_recv.login_recv_all_mail(CONTROLLER_EMAIL, CONTROLLER_EMAIL_PASSWD, CLIENT_MAIL, PING_A_SUBJECT , browser);


    for iPayload in payloads_list:
        argv =  get_decrypted_content( iPayload ).split(SEP)

        magic_wrd = argv[0]

        if(magic_wrd == MAGIC_WORD):
            OD2_IP = argv[1]
            OD1_IP = argv[2]
            TIMEOUT = argv[3]
            SRC_PORT = argv[4]

            print("Add rule to Controller :  Send self ping ...")

            #send_ack()




if __name__ == '__main__':
    main(sys.argv)
