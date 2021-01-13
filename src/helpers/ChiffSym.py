

ALGOS = ["AES", "DES", "DES3", "Blowfish", "ARC2", "ARC4", "CAST", "XOR"]

class ChiffSym:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, msg):
        options = {
           "AES" : ChiffSym.enc_aes,
           "DES" : ChiffSym.enc_des,
           "DES3" : ChiffSym.enc_des3,
           "Blowfish" : ChiffSym.enc_blowfish,
           "ARC2" : ChiffSym.enc_arc2,
           "ARC4" : ChiffSym.enc_arc4,
           "CAST" : ChiffSym.enc_cast,
           "XOR" : ChiffSym.enc_xor,
        }
        if algo in ALGOS :
            return options[algo](msg)
        else :
            return "Something went wrong"

    @staticmethod
    def decrypt(algo, msg):
        options = {
           "AES" : ChiffSym.dec_aes,
           "DES" : ChiffSym.dec_des,
           "DES3" : ChiffSym.dec_des3,
           "Blowfish" : ChiffSym.dec_blowfish,
           "ARC2" : ChiffSym.dec_arc2,
           "ARC4" : ChiffSym.dec_arc4,
           "CAST" : ChiffSym.dec_cast,
           "XOR" : ChiffSym.dec_xor,
        }
        if algo in ALGOS :
            return options[algo](msg)
        else :
            return "Something went wrong"

    #AES
    @staticmethod
    def enc_aes(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_aes(string_to_decrypt,key):
        treturn "1"

    #DES
    @staticmethod
    def enc_des(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_des(string_to_decrypt,key):
        treturn "1"

    #DES3
    @staticmethod
    def enc_des3(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_des3(string_to_decrypt,key):
        treturn "1"

    #BLOWFISH
    @staticmethod
    def enc_blowfish(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_blowfish(string_to_decrypt,key):
        treturn "1"

    #ARC2
    @staticmethod
    def enc_arc2(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_arc2(string_to_decrypt,key):
        treturn "1"

    #ARC4
    @staticmethod
    def enc_arc4(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_arc4(string_to_decrypt,key):
        treturn "1"

    #CAST
    @staticmethod
    def enc_cast(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_cast(string_to_decrypt,key):
        treturn "1"

    #XOR
    @staticmethod
    def enc_xor(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_xor(string_to_decrypt,key):
        treturn "1"
