#!/usr/bin/python

from scapy.layers.inet import ICMP, IP
import gmail_send
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
from utils.crypt import get_encrypted_content


def main(argv):
    print("asdsad")

    if len(argv) != 5:
        print('usage: ./<name>.py <OD2 IP Address> <OD1 IP Address> <TimeoutInSeconds> <src_port> Your Len ' + str(
            len(argv)))
        exit(1)

    OD2_IP = argv[1]
    OD1_IP = argv[2]
    TIMEOUT = argv[3]
    SRC_PORT = argv[4]

    payload = MAGIC_WORD + SEP + OD2_IP + SEP + OD1_IP + SEP + TIMEOUT + SEP + SRC_PORT + SEP

    print("Payload : " + PING_A_SUBJECT + " : " + payload)
    cipher_text = get_encrypted_content(payload)

    sender_email = CLIENT_MAIL
    sender_passwd = CLIENT_MAIL_PASSWD
    recv_email = CONTROLLER_EMAIL
    subject_txt = PING_A_SUBJECT
    body_txt = cipher_text
    browser = webdriver.Chrome()

    gmail_send.login_send_mail(sender_email, sender_passwd, recv_email, subject_txt, body_txt, browser);

    print("Email Sent to Controller")
    print("Waiting for Ack.....")


if __name__ == '__main__':
    main(sys.argv)
