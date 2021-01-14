from src.helpers.hachage import HachageHelper
from Crypto.Cipher import AES, DES, DES3, Blowfish
import base64

ALGOS = ["AES", "DES", "Triple DES", "Blowfish", "CAST", "XOR"]

padding_character = "#"

class ChiffSymHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, msg, key):
        options = {
           "AES" : ChiffSymHelper.enc_aes,
           "DES" : ChiffSymHelper.enc_des,
           "Triple DES" : ChiffSymHelper.enc_des3,
           "Blowfish" : ChiffSymHelper.enc_blowfish,
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
           "Triple DES" : ChiffSymHelper.dec_des3,
           "Blowfish" : ChiffSymHelper.dec_blowfish,
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
        # AES key length must be either 16, 24, or 32 bytes long
        # we will use truncated md5 hash so we don't restrict the user
        hashed_key = HachageHelper.hash('md5',key)
        # use the secret key to create a AES cipher
        cipher = AES.new(hashed_key)
        # pad the private_msg
        # because AES encryption requires the length of the msg to be a multiple of 16
        padded_private_msg = string_to_encrypt + (padding_character * ((16-len(string_to_encrypt)) % 16))
        # use the cipher to encrypt the padded message
        encrypted_msg = cipher.encrypt(padded_private_msg)
        # encode the encrypted msg
        encoded_encrypted_msg = base64.b64encode(encrypted_msg)

        return encoded_encrypted_msg.decode()

    @staticmethod
    def dec_aes(string_to_decrypt,key):
        hashed_key = HachageHelper.hash('md5',key)
        # use the secret key to create a AES cipher
        cipher = AES.new(hashed_key)
        encrypted_msg = base64.b64decode(string_to_decrypt.encode())
        # use the cipher to decrypt the encrypted message
        decrypted_msg = cipher.decrypt(encrypted_msg)

        return decrypted_msg.decode().rstrip(padding_character)

    #DES
    @staticmethod
    def enc_des(string_to_encrypt,key):
        hashed_key = HachageHelper.hash('md5',key)
        cipher = DES.new(hashed_key[:8])
        padded_private_msg = string_to_encrypt + (padding_character * ((16-len(string_to_encrypt)) % 16))
        encrypted_msg = cipher.encrypt(padded_private_msg)
        encoded_encrypted_msg = base64.b64encode(encrypted_msg)

        return encoded_encrypted_msg.decode()

    @staticmethod
    def dec_des(string_to_decrypt,key):
        hashed_key = HachageHelper.hash('md5',key)
        cipher = DES.new(hashed_key[:8])
        encrypted_msg = base64.b64decode(string_to_decrypt.encode())
        decrypted_msg = cipher.decrypt(encrypted_msg)

        return decrypted_msg.decode().rstrip(padding_character)

    #Triple DES
    @staticmethod
    def enc_des3(string_to_encrypt,key):
        hashed_key = HachageHelper.hash('md5',key)
        cipher = DES3.new(hashed_key[:16])
        padded_private_msg = string_to_encrypt + (padding_character * ((16-len(string_to_encrypt)) % 16))
        encrypted_msg = cipher.encrypt(padded_private_msg)
        encoded_encrypted_msg = base64.b64encode(encrypted_msg)

        return encoded_encrypted_msg.decode()

    @staticmethod
    def dec_des3(string_to_decrypt,key):
        hashed_key = HachageHelper.hash('md5',key)
        cipher = DES3.new(hashed_key[:16])
        encrypted_msg = base64.b64decode(string_to_decrypt.encode())
        decrypted_msg = cipher.decrypt(encrypted_msg)

        return decrypted_msg.decode().rstrip(padding_character)


    #BLOWFISH
    @staticmethod
    def enc_blowfish(string_to_encrypt,key):
        cipher = Blowfish.new(key)
        padded_private_msg = string_to_encrypt + (padding_character * ((16-len(string_to_encrypt)) % 16))
        encrypted_msg = cipher.encrypt(padded_private_msg)
        encoded_encrypted_msg = base64.b64encode(encrypted_msg)

        return encoded_encrypted_msg.decode()

    @staticmethod
    def dec_blowfish(string_to_decrypt,key):
        cipher = Blowfish.new(key)
        encrypted_msg = base64.b64decode(string_to_decrypt.encode())
        decrypted_msg = cipher.decrypt(encrypted_msg)

        return decrypted_msg.decode().rstrip(padding_character)

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
