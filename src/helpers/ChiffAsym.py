from Cryptodome.PublicKey import RSA
from Crypto.PublicKey import ElGamal
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256, SHA
from Cryptodome.Random import get_random_bytes, random
from Cryptodome.Util.number import GCD
from os import path
import calendar
import time
import base64
from src.helpers.ChiffSym import ChiffSymHelper
from src.helpers.codage import CodageHelper

ALGOS = ["RSA", "ElGamal"]

# specific to ElGamal algo
comps = ('p', 'g', 'y', 'x')

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
        #first we check if key exists:
        key_name = "elgamal_" + key + ".key"
        if path.exists(key_name):
            #we import the key
            b64encoded_encrypted_key = open(key_name, "rb").read()
            #we decrypt it using the password provided
            _key = ChiffSymHelper.decrypt("AES" , b64encoded_encrypted_key.decode() , pwd)
            
            # we extract the components of the key (p,g,y,x)
            clean_key_comps = []
            key_comps = _key.split("\n")
            for c in key_comps:
                clean_key_comps.append(int(c.split('=')[1].strip()))

            #we construct a new key using these components
            key = ElGamal.construct(tuple(clean_key_comps))
        else:
            # we create a new key
            # we could use 2048 but it takes a LONG time
            key = ElGamal.generate(256, get_random_bytes)
            # "out" is a string containing the components of the key like follows: p = 23 \n g = 4 ...
            out = "\n".join(["{} = {}".format(comp, getattr(key, comp)) for comp in comps])
            # we encrypt that string using AES
            encrypted_key = ChiffSymHelper.encrypt("AES" , out , pwd)
            #then we it to a file
            file_out = open(key_name, "wb")
            file_out.write(encrypted_key.encode())
            file_out.close()


        # we choose a k
        while 1:
            k = random.StrongRandom().randint(1,int(key.p)-1)
            if GCD(k,int(key.p)-1)==1: break
        
        # we encrypt our data
        # returns a tuple : u v
        encrypted_msg = key.encrypt(string_to_encrypt.encode(), k)

        # we seperate u and v by "\n" so we can save them in the same file
        out_msg = str(encrypted_msg[0]) + "\n" + str(encrypted_msg[1])

        # now we save the encrypted msg to a file
        cur_timestamp = calendar.timegm(time.gmtime())
        file_out = open(str(cur_timestamp) + ".encrypted", "wb")
        file_out.write(base64.b64encode(out_msg.encode()))
        file_out.close()

        return "saved to file : " + str(cur_timestamp) + ".encrypted"



    @staticmethod
    def dec_elgamal(file_to_decrypt,key,pwd):
        #first we get the key
        b64encoded_encrypted_key = open(key, "rb").read()
        _key = ChiffSymHelper.decrypt("AES" , b64encoded_encrypted_key.decode() , pwd)
        
        clean_key_comps = []
        key_comps = _key.split("\n")
        for c in key_comps:
            clean_key_comps.append(int(c.split('=')[1].strip()))

        key = ElGamal.construct(tuple(clean_key_comps))

        #now we get the encrypted msg
        encoded_msg = open(file_to_decrypt, "rb").read()
        msg = base64.b64decode(encoded_msg)
        uv_strings = msg.decode().split("\n")

        uv= []
        for c in uv_strings:
            uv.append(c.encode())

        # and now we decrypt it

        d = key.decrypt(tuple(uv))

        return d


    @staticmethod
    def sign_elgamal(string_to_sign,key,pwd):
        #first we check if key exists:
        key_name = "elgamal_" + key + ".key"
        if path.exists(key_name):
            # we import the key
            b64encoded_encrypted_key = open(key_name, "rb").read()
            # we decrypt it using the password we have
            _key = ChiffSymHelper.decrypt("AES" , b64encoded_encrypted_key.decode() , pwd)
            
            # we extract the components of the key, and save them in a tuple
            clean_key_comps = []
            key_comps = _key.split("\n")
            for c in key_comps:
                clean_key_comps.append(int(c.split('=')[1].strip()))

            # we construct a new key using the components we got from the file
            key = ElGamal.construct(tuple(clean_key_comps))
        else:
            # we create a new key
            # we could use 2048 but it takes a LONG time
            key = ElGamal.generate(256, get_random_bytes)
            # "out" is a string containing the components of the key like follows: p = 23 \n g = 4 ...
            out = "\n".join(["{} = {}".format(comp, getattr(key, comp)) for comp in comps])
            # we encrypt the string "out"
            encrypted_key = ChiffSymHelper.encrypt("AES" , out , pwd)
            #then we save it
            file_out = open(key_name, "wb")
            file_out.write(encrypted_key.encode())
            file_out.close()

        # we hash the msg to sign
        h = SHA256.new(string_to_sign.encode())

        # we generate k
        while 1:
            k = random.StrongRandom().randint(1,int(key.p)-1)
            if GCD(k,int(key.p)-1)==1: break

        # and now we sign the hash
        signature = key.sign(h,k)

        # we get the output as a tuple, so we seperate them to be able to save them to the same file
        out_sig = str(signature[0]) + "\n" + str(signature[1])

        # now we save to a file
        cur_timestamp = calendar.timegm(time.gmtime())
        # we save the signature
        file_out = open(str(cur_timestamp) + ".signed", "wb")
        file_out.write(base64.b64encode(out_sig))
        file_out.close()
        # we save the original msg
        hash_out = open(str(str(cur_timestamp) + ".msg"), "wb")
        hash_out.write(base64.b64encode(string_to_sign.encode()))
        hash_out.close()

        return "saved signature to file : " + str(cur_timestamp) + ".signed " +  "and the message to file : " + str(cur_timestamp) + ".msg\n" 
    
    @staticmethod
    def verif_sign_elgamal(string_to_verif_sig,key,pwd):
        #first we get the key
        b64encoded_encrypted_key = open(key, "rb").read()
        # we decrypt the key
        _key = ChiffSymHelper.decrypt("AES" , b64encoded_encrypted_key.decode() , pwd)
        
        # we extract the components of the key
        clean_key_comps = []
        key_comps = _key.split("\n")
        for c in key_comps:
            clean_key_comps.append(int(c.split('=')[1].strip()))

        #we construct a new key with the components we extracted
        key = ElGamal.construct(tuple(clean_key_comps))

        # we get the signature
        encoded_sig = open(string_to_verif_sig, "rb").read()
        # we decode it
        sig = base64.b64decode(encoded_sig)

        # we get the msg file
        hash_file_name = string_to_verif_sig.split(".")[0] + ".msg"
        hash_file = open(hash_file_name, "rb").read()
        # we decode it
        decode_hash = base64.b64decode(hash_file)

        # we create the hash again
        h = SHA256.new(decode_hash).hexdigest()

        #then we verify the sig
        if key.verify(h,sig):
            return  "The signature is valid."
        else:
            return "The signature is not valid."
            
