

import base64
import crypt

'''
Some constants, used for email communication between client and controller.
'''

SEP = "@@"
MAGIC_WORD = "Siege"

GMAIL_WEBSITE = "https://www.gmail.com"


CLIENT_MAIL = "nsl-test1@iiitd.ac.in"
CONTROLLER_EMAIL = "nsl-test2@iiitd.ac.in"

CLIENT_MAIL_PASSWD = 'XXXXXXXX-Enter-Password'
CONTROLLER_EMAIL_PASSWD = "XXXXXXXX-Enter-Password"

CLIENT_A_SUBJECT = "SiegeBreaker_CLIENT_A_SUBJECT"
CLIENT_B_SUBJECT = "SiegeBreaker_CLIENT_B_SUBJECT"


CLIENT_A_ACK_SUB = "SiegeBreaker_PING_A_ACK_SUBJECT"
CLIENT_A_ACK_BODY = "SiegeBreaker_PING_A_ACK_BODY"


LIMIT_UNREADMAIL = 10



