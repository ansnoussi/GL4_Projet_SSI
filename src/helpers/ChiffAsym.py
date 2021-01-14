from Crypto.PublicKey import ElGamal
# docs : https://www.dlitz.net/software/pycrypto/api/current/

ALGOS = ["RSA", "ElGamal"]

class ChiffSymHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, msg, key):
        options = {
           "RSA" : ChiffSymHelper.enc_rsa,
           "ElGamal" : ChiffSymHelper.enc_elgamal,
        }
        if algo in ALGOS :
            return options[algo](msg, key)
        else :
            return "Something went wrong"

    @staticmethod
    def decrypt(algo, msg, key):
        options = {
           "RSA" : ChiffSymHelper.dec_rsa,
           "ElGamal" : ChiffSymHelper.dec_elgamal,
        }
        if algo in ALGOS :
            return options[algo](msg, key)
        else :
            return "Something went wrong"

    #GENERAL USE
    @staticmethod
    def enc_key(key_to_enc , key):
        return "0"
    
    @staticmethod
    def dec_key(key_to_dec , key):
        return "1"

    @staticmethod
    def read_priv_key(file_name):
        return "aa"
    
    @staticmethod
    def write_key_pairs():
        return True


    #RSA
    @staticmethod
    def gen_rsa_key():
        return ["PUB", "PRIV"]

    @staticmethod
    def enc_rsa(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_rsa(string_to_decrypt,key):
        return "1"


    #ElGamal
    @staticmethod
    def enc_elgamal(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_elgamal(string_to_decrypt,key):
        return "1"
