import random, time, pickle, base64
from hashlib import md5, sha512, sha1


def encrypt_password(salt, raw_password):
    hsh = sha512(salt + raw_password).hexdigest()
    return hsh

def check_password(raw_password, enc_password):
    try:
        salt, hsh = enc_password.split('$')
    except:
        return False
    return hsh == encrypt_password(salt, raw_password)

def get_enc_password(password):
    salt = md5(str(random.random())).hexdigest()[:12]
    hsh = encrypt_password(salt, password)
    return "%s$%s" % (salt, hsh)
