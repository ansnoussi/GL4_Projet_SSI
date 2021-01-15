from Cryptodome.PublicKey import RSA, ElGamal
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256, SHA
from os import path
import calendar
import time
import base64


# docs : https://www.dlitz.net/software/pycrypto/api/current/

ALGOS = ["RSA", "ElGamal"]

# modes :  0 (encrypt) , 1 (sign)


class ChiffAsymHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, mode, msg, key, pwd):
        sign_options = {
           "RSA" : ChiffAsymHelper.sign_rsa,
           "ElGamal" : ChiffAsymHelper.sign_elgamal,
        }
        encrypt_options = {
           "RSA" : ChiffAsymHelper.enc_rsa,
           "ElGamal" : ChiffAsymHelper.enc_elgamal,
        }
        if algo in ALGOS :
            if mode == 1 :
                return sign_options[algo](msg, key, pwd)
            elif mode == 0 :
                return encrypt_options[algo](msg, key, pwd)
            else :
                return "unknown mode"
        else :
            return "Something went wrong"

    @staticmethod
    def decrypt(algo, mode, msg, key, pwd):
        sign_options = {
           "RSA" : ChiffAsymHelper.verif_sign_rsa,
           "ElGamal" : ChiffAsymHelper.verif_sign_elgamal,
        }
        encrypt_options = {
           "RSA" : ChiffAsymHelper.dec_rsa,
           "ElGamal" : ChiffAsymHelper.dec_elgamal,
        }
        if algo in ALGOS :
            if mode == 1 :
                return sign_options[algo](msg, key, pwd)
            elif mode == 0 :
                return encrypt_options[algo](msg, key, pwd)
            else :
                return "unknown mode"
        else :
            return "Something went wrong"

    #RSA
    @staticmethod
    def enc_rsa(string_to_encrypt,key,pwd):
        #first we check if key exists:
        key_name = "rsa_" + key + ".key"
        if path.exists(key_name):

            #we import the key
            encoded_key = open(key_name, "rb").read()
            key = RSA.import_key(encoded_key, passphrase=pwd)
        else:
            #we create a new key
            key = RSA.generate(2048)
            encrypted_key = key.export_key(passphrase=pwd, pkcs=8,protection="scryptAndAES128-CBC")
            #then we save the key
            file_out = open(key_name, "wb")
            file_out.write(encrypted_key)
            file_out.close()

        # now we encrypt using the key
        cipher_rsa = PKCS1_OAEP.new(key)
        encrypted_msg = cipher_rsa.encrypt(str.encode(string_to_encrypt))
        # now we save to a file
        cur_timestamp = calendar.timegm(time.gmtime())
        file_out = open(str(str(cur_timestamp) + ".encrypted"), "wb")
        file_out.write(base64.b64encode(encrypted_msg))
        file_out.close()

        return "saved to file : " + str(cur_timestamp) + ".encrypted"

    @staticmethod
    def dec_rsa(file_to_decrypt,key,pwd):
        #first we import the key and init the cipher
        encoded_key = open(key, "rb").read()
        key = RSA.import_key(encoded_key, passphrase=pwd)

        # then we open the encoded msg
        encoded_msg = open(file_to_decrypt, "rb").read()
        msg = base64.b64decode(encoded_msg)
        cipher_rsa = PKCS1_OAEP.new(key)

        #then we decrypt the msg
        decrypted_msg = cipher_rsa.decrypt(msg)

        return decrypted_msg.decode()

    @staticmethod
    def sign_rsa(string_to_sign,key,pwd):
        #first we check if key exists:
        key_name = "rsa_" + key + ".key"
        if path.exists(key_name):

            #we import the key
            encoded_key = open(key_name, "rb").read()
            key = RSA.import_key(encoded_key, passphrase=pwd)
        else:
            #we create a new key
            key = RSA.generate(2048)
            encrypted_key = key.export_key(passphrase=pwd, pkcs=8,protection="scryptAndAES128-CBC")
            #then we save the key
            file_out = open(key_name, "wb")
            file_out.write(encrypted_key)
            file_out.close()

        # we hash the msg to sign
        h = SHA256.new(string_to_sign.encode())

        # and now we sign the hash
        signature = pkcs1_15.new(key).sign(h)

        # now we save to a file
        cur_timestamp = calendar.timegm(time.gmtime())
        # we save the signature
        file_out = open(str(cur_timestamp) + ".signed", "wb")
        file_out.write(base64.b64encode(signature))
        file_out.close()
        # we save the original msg
        hash_out = open(str(str(cur_timestamp) + ".msg"), "wb")
        hash_out.write(base64.b64encode(string_to_sign.encode()))
        hash_out.close()

        return "saved signature to file : " + str(cur_timestamp) + ".signed " +  "and the message to file : " + str(cur_timestamp) + ".msg\n" 
    
    @staticmethod
    def verif_sign_rsa(string_to_verif_sig,key,pwd):
        #first we import the key
        encoded_key = open(key, "rb").read()
        key = RSA.import_key(encoded_key, passphrase=pwd)

        # we get the signature
        encoded_sig = open(string_to_verif_sig, "rb").read()
        sig = base64.b64decode(encoded_sig)

        # we get the msg
        hash_file_name = string_to_verif_sig.split(".")[0] + ".msg"
        hash_file = open(hash_file_name, "rb").read()
        decode_hash = base64.b64decode(hash_file)

        # we create the hash
        h = SHA256.new(decode_hash)


        #then we verify the sig
        try:
            verif = pkcs1_15.new(key).verify(h,sig)
            return  "The signature is valid."
        except (ValueError, TypeError):
            return "The signature is not valid."

    #ElGamal
    @staticmethod
    def enc_elgamal(string_to_encrypt,key,pwd):
        return "0"

    @staticmethod
    def dec_elgamal(string_to_decrypt,key,pwd):
        return "1"

    @staticmethod
    def sign_elgamal(string_to_decrypt,key,pwd):
        return "1"
    
    @staticmethod
    def verif_sign_elgamal(string_to_decrypt,key,pwd):
        return "1"