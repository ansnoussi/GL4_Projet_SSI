from Cryptodome.PublicKey import RSA, ElGamal
# docs : https://www.dlitz.net/software/pycrypto/api/current/

ALGOS = ["RSA", "ElGamal"]

# modes :  0 (encrypt) , 1 (sign)
# we will use AES to encrypt private key


class ChiffAsymHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, mode, msg, key, pwd):
        sign_options = {
           "RSA" : ChiffSymHelper.sign_rsa,
           "ElGamal" : ChiffSymHelper.sign_elgamal,
        }
        encrypt_options = {
           "RSA" : ChiffSymHelper.enc_rsa,
           "ElGamal" : ChiffSymHelper.enc_elgamal,
        }
        if algo in ALGOS :
            if mode == 1 :
                return sing_options[algo](msg, key, pwd)
            elif mode == 0 :
                return encrypt_options[algo](msg, key, pwd)
            else :
                return "unknown mode"
        else :
            return "Something went wrong"

    @staticmethod
    def decrypt(algo, mode, msg, key, pwd):
        sign_options = {
           "RSA" : ChiffSymHelper.verif_sign_rsa,
           "ElGamal" : ChiffSymHelper.verif_sign_elgamal,
        }
        encrypt_options = {
           "RSA" : ChiffSymHelper.dec_rsa,
           "ElGamal" : ChiffSymHelper.dec_elgamal,
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
    def save_key_pairs(pub, priv):
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

    @staticmethod
    def sign_rsa(string_to_decrypt,key):
        return "1"
    
    @staticmethod
    def verif_sign_rsa(string_to_decrypt,key):
        return "1"

    #ElGamal
    @staticmethod
    def gen_elgamal_key():
        return ["PUB", "PRIV"]

    @staticmethod
    def enc_elgamal(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_elgamal(string_to_decrypt,key):
        return "1"

    @staticmethod
    def sign_elgamal(string_to_decrypt,key):
        return "1"
    
    @staticmethod
    def verif_sign_elgamal(string_to_decrypt,key):
        return "1"