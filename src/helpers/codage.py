import base64
import binascii
import urllib.parse

ALGOS = ["Binary", "Base16", "Base32",  "Base64", "Rot13", "URL", "Morse"]

CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "/": "-..-.",
    "@": ".--.-.",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "." : ".-.-.-",
    "," : "--..--",
    ":" : "---...",
    "?" : "..--..",
    "'" : ".----.",
    "-" : "-....-",
    "/" : "-..-.",
    "@" : ".--.-.",
    "=" : "-...-",
    " ": "/"
}

class CodageHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encode(algo, msg):
        try:
            options = {
            "Binary" : CodageHelper.enc_binary,
            "Base16" : CodageHelper.enc_hex,
            "Base32" : CodageHelper.enc_base32,
            "Base64" : CodageHelper.enc_base64,
            "Rot13" : CodageHelper.rot13,
            "URL" : CodageHelper.enc_url,
            "Morse" : CodageHelper.enc_morse,
            }
            if algo in ALGOS :
                return options[algo](msg)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def decode(algo, msg):
        try:
            options = {
            "Binary" : CodageHelper.dec_binary,
            "Base16" : CodageHelper.dec_hex,
            "Base32" : CodageHelper.dec_base32,
            "Base64" : CodageHelper.dec_base64,
            "Rot13" : CodageHelper.rot13,
            "URL" : CodageHelper.dec_url,
            "Morse" : CodageHelper.dec_morse,
            }
            if algo in ALGOS :
                return options[algo](msg)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #BINARY
    @staticmethod
    def enc_binary(string_to_encode):
        try:
            return "0" + bin(int(binascii.hexlify(string_to_encode.encode('utf-8')), 16))[2:]
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def dec_binary(string_to_decode):
        try:
            s = int(string_to_decode, 2)
            return binascii.unhexlify('%x' % s).decode("utf-8")
        except (TypeError, ValueError) :
            return ("Chaîne non binaire fournie")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #HEX
    @staticmethod
    def enc_hex(string_to_encode):
        try:
            return base64.b16encode(string_to_encode.encode('utf-8')).decode("utf-8")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def dec_hex(string_to_decode):
        try:
            if string_to_decode[:2].lower() == '0x':
                string_to_decode = string_to_decode[2:]
            decoded_string = base64.b16decode(string_to_decode).decode("utf-8")
            return decoded_string
        except TypeError:
            print ("Chaîne non hexadécimale fournie")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #BASE32
    @staticmethod
    def enc_base32(string_to_encode):
        try:
            return base64.b32encode(string_to_encode.encode('utf-8')).decode("utf-8")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def dec_base32(string_to_decode):
        try:
            decoded_string = base64.b32decode(string_to_decode).decode("utf-8")
            return decoded_string
        except TypeError:
            print ("Chaîne non-Base32 fournie")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #BASE64
    @staticmethod
    def enc_base64(string_to_encode):
        try:
            return base64.b64encode(string_to_encode).encode("utf-8").decode("utf-8")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def dec_base64(string_to_decode):
        try:
            decoded_string = base64.b64decode(string_to_decode).decode("utf-8")
            return decoded_string
        except TypeError:
            print ("Chaîne non-Base64 fournie")
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #ROT13
    @staticmethod
    def rot13(my_string):
        try:
            normalAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            rot13Alpha = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
            return my_string.translate(str.maketrans(normalAlpha,rot13Alpha))
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #URL
    @staticmethod
    def enc_url(string_to_encode):
        try:
            return urllib.parse.quote(string_to_encode)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def dec_url(string_to_decode):
        try:
            return urllib.parse.unquote(string_to_decode)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #MORSE
    @staticmethod
    def enc_morse(string_to_encode):
        try:
            ret = []
            for t in list(string_to_encode):
                t = t.upper()
                if t in CODE:
                    ret.append(CODE[t])
                    ret.append(' ')
            return ''.join(ret)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"


    @staticmethod
    def dec_morse(string_to_decode):
        try:
            ret = []
            for m in string_to_decode.split(' '):
                for key, val in CODE.items():
                    if val == m:
                        ret.append(key)
            return ''.join(ret)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"