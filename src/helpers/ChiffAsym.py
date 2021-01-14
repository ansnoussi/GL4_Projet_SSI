from Crypto.PublicKey import ElGamal
# docs : https://www.dlitz.net/software/pycrypto/api/current/

ALGOS = ["RSA", "DSA", "ElGamal"]

class ChiffSym:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, msg):
        options = {
           "RSA" : ChiffSym.enc_rsa,
           "DSA" : ChiffSym.enc_dsa,
           "ElGamal" : ChiffSym.enc_elgamal,
        }
        if algo in ALGOS :
            return options[algo](msg)
        else :
            return "Something went wrong"

    @staticmethod
    def decrypt(algo, msg, key):
        options = {
           "RSA" : ChiffSym.dec_rsa,
           "DSA" : ChiffSym.dec_dsa,
           "ElGamal" : ChiffSym.dec_elgamal,
        }
        if algo in ALGOS :
            return options[algo](msg, key)
        else :
            return "Something went wrong"

    #RSA
    @staticmethod
    def enc_rsa(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_rsa(string_to_decrypt,key):
        treturn "1"

    #DSA
    @staticmethod
    def enc_dsa(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_dsa(string_to_decrypt,key):
        treturn "1"

    #ElGamal
    @staticmethod
    def enc_elgamal(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_elgamal(string_to_decrypt,key):
        treturn "1"
