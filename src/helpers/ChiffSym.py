import base64
import binascii
import urllib.parse

ALGOS = ["AES", "DES", "IDEA",  "Blowfish", "RC4", "RC5", "RC6"]

class ChiffSym:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encode(algo, msg):
        options = {
           "AES" : ChiffSym.enc_aes,
           "DES" : ChiffSym.enc_des,
           "IDEA" : ChiffSym.enc_idea,
           "Blowfish" : ChiffSym.enc_blowfish,
           "RC4" : ChiffSym.enc_rc4,
           "RC5" : ChiffSym.enc_rc5,
           "RC6" : ChiffSym.enc_rc6,
        }
        if algo in ALGOS :
            return options[algo](msg)
        else :
            return "Something went wrong"

    @staticmethod
    def decode(algo, msg):
        options = {
           "AES" : ChiffSym.dec_aes,
           "DES" : ChiffSym.dec_des,
           "IDEA" : ChiffSym.dec_idea,
           "Blowfish" : ChiffSym.dec_blowfish,
           "RC4" : ChiffSym.dec_rc4,
           "RC5" : ChiffSym.dec_rc5,
           "RC6" : ChiffSym.dec_rc6,
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

    #IDEA
    @staticmethod
    def enc_idea(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_idea(string_to_decrypt,key):
        treturn "1"

    #BLOWFISH
    @staticmethod
    def enc_blowfish(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_blowfish(string_to_decrypt,key):
        treturn "1"

    #RC4
    @staticmethod
    def enc_rc4(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_rc4(string_to_decrypt,key):
        treturn "1"

    #RC5
    @staticmethod
    def enc_rc5(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_rc5(string_to_decrypt,key):
        treturn "1"

    #RC6
    @staticmethod
    def enc_rc6(string_to_encrypt,key):
        return "0"

    @staticmethod
    def dec_rc6(string_to_decrypt,key):
        treturn "1"
