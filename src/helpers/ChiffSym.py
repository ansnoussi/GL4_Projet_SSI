

ALGOS = ["AES", "DES", "DES3", "Blowfish", "ARC2", "ARC4", "CAST", "XOR"]

class ChiffSymHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, msg, key):
        options = {
           "AES" : ChiffSymHelper.enc_aes,
           "DES" : ChiffSymHelper.enc_des,
           "DES3" : ChiffSymHelper.enc_des3,
           "Blowfish" : ChiffSymHelper.enc_blowfish,
           "ARC2" : ChiffSymHelper.enc_arc2,
           "ARC4" : ChiffSymHelper.enc_arc4,
           "CAST" : ChiffSymHelper.enc_cast,
           "XOR" : ChiffSymHelper.enc_xor,
        }
        if algo in ALGOS :
            return options[algo](msg, key)
        else :
            return "Something went wrong"

    @staticmethod
    def decrypt(algo, msg, key):
        options = {
           "AES" : ChiffSymHelper.dec_aes,
           "DES" : ChiffSymHelper.dec_des,
           "DES3" : ChiffSymHelper.dec_des3,
           "Blowfish" : ChiffSymHelper.dec_blowfish,
           "ARC2" : ChiffSymHelper.dec_arc2,
           "ARC4" : ChiffSymHelper.dec_arc4,
           "CAST" : ChiffSymHelper.dec_cast,
           "XOR" : ChiffSymHelper.dec_xor,
        }
        if algo in ALGOS :
            return options[algo](msg, key)
        else :
            return "Something went wrong"

    #AES
    @staticmethod
    def enc_aes(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_aes(string_to_decrypt,key):
        return "1"

    #DES
    @staticmethod
    def enc_des(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_des(string_to_decrypt,key):
        return "1"

    #DES3
    @staticmethod
    def enc_des3(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_des3(string_to_decrypt,key):
        return "1"

    #BLOWFISH
    @staticmethod
    def enc_blowfish(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_blowfish(string_to_decrypt,key):
        return "1"

    #ARC2
    @staticmethod
    def enc_arc2(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_arc2(string_to_decrypt,key):
        return "1"

    #ARC4
    @staticmethod
    def enc_arc4(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_arc4(string_to_decrypt,key):
        return "1"

    #CAST
    @staticmethod
    def enc_cast(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_cast(string_to_decrypt,key):
        return "1"

    #XOR
    @staticmethod
    def enc_xor(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_xor(string_to_decrypt,key):
        return "1"
