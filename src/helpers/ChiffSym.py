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
           "AES" : ChiffSym.enc_binary,
           "DES" : ChiffSym.enc_hex,
           "IDEA" : ChiffSym.enc_base32,
           "Blowfish" : ChiffSym.enc_base64,
           "RC4" : ChiffSym.rot13,
           "RC5" : ChiffSym.enc_url,
           "RC6" : ChiffSym.enc_morse,
        }
        if algo in ALGOS :
            return options[algo](msg)
        else :
            return "Something went wrong"

    @staticmethod
    def decode(algo, msg):
        options = {
           "AES" : ChiffSym.dec_binary,
           "DES" : ChiffSym.dec_hex,
           "IDEA" : ChiffSym.dec_base32,
           "Blowfish" : ChiffSym.dec_base64,
           "RC4" : ChiffSym.rot13,
           "RC5" : ChiffSym.dec_url,
           "RC6" : ChiffSym.dec_morse,
        }
        if algo in ALGOS :
            return options[algo](msg)
        else :
            return "Something went wrong"

    #AES
    @staticmethod
    def enc_aes(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_aes(string_to_decrypt):
        treturn "1"

    #DES
    @staticmethod
    def enc_des(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_des(string_to_decrypt):
        treturn "1"

    #IDEA
    @staticmethod
    def enc_idea(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_idea(string_to_decrypt):
        treturn "1"

    #BLOWFISH
    @staticmethod
    def enc_blowfish(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_blowfish(string_to_decrypt):
        treturn "1"

    #RC4
    @staticmethod
    def enc_rc4(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_rc4(string_to_decrypt):
        treturn "1"

    #RC5
    @staticmethod
    def enc_rc5(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_rc5(string_to_decrypt):
        treturn "1"

    #RC6
    @staticmethod
    def enc_rc6(string_to_encrypt):
        return "0"

    @staticmethod
    def dec_rc6(string_to_decrypt):
        treturn "1"
