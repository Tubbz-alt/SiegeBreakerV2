from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


import os
import base64




def get_key_path(path):
    try:
        return open(path)
    except Exception as e:
        return open('../' + path)



def get_encrypted_content(plain_text):
    cwd = os.getcwd()
    print(cwd)
    public_key = RSA.importKey(get_key_path('../keys/public.pem').read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    cipher_text= cipher_rsa.encrypt(plain_text)
    return base64.encodestring(cipher_text)


def get_decrypted_content(encrypted_content):
    encrypted_content = base64.decodestring( encrypted_content )
    private_key = RSA.importKey(get_key_path('../keys/private.pem').read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    plain_text = cipher_rsa.decrypt(encrypted_content)
    return plain_text


if __name__ == '__main__':

    a = get_encrypted_content("abc")
    print(get_decrypted_content(a))