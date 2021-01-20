from src.helpers.hachage import HachageHelper
from Crypto.Cipher import AES, DES, DES3, Blowfish, CAST, XOR
import base64

ALGOS = ["AES", "DES", "Triple DES", "Blowfish", "CAST", "XOR"]

padding_character = "#"

class ChiffSymHelper:

    @staticmethod
    def getAvailable():
        return ALGOS

    @staticmethod
    def encrypt(algo, msg, key):
        try:
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
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def decrypt(algo, msg, key):
        try:
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
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    #AES: BLOCK_SIZE(16 bytes) KEY_SIZE(16, 24, or 32 bytes)
    @staticmethod
    def enc_aes(string_to_encrypt,key):
        try:
            # AES key length must be either 16, 24, or 32 bytes long
            # we will use truncated md5 (16 bytes) hash so we don't restrict the user
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
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    @staticmethod
    def dec_aes(string_to_decrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            # use the secret key to create a AES cipher
            cipher = AES.new(hashed_key)
            encrypted_msg = base64.b64decode(string_to_decrypt.encode())
            # use the cipher to decrypt the encrypted message
            decrypted_msg = cipher.decrypt(encrypted_msg)

            return decrypted_msg.decode().rstrip(padding_character)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    #DES: BLOCK_SIZE(8 bytes) KEY_SIZE(7 bytes)
    @staticmethod
    def enc_des(string_to_encrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            cipher = DES.new(hashed_key[:8])
            padded_private_msg = string_to_encrypt + (padding_character * ((8-len(string_to_encrypt)) % 8))
            encrypted_msg = cipher.encrypt(padded_private_msg)
            encoded_encrypted_msg = base64.b64encode(encrypted_msg)

            return encoded_encrypted_msg.decode()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    @staticmethod
    def dec_des(string_to_decrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            cipher = DES.new(hashed_key[:8])
            encrypted_msg = base64.b64decode(string_to_decrypt.encode())
            decrypted_msg = cipher.decrypt(encrypted_msg)

            return decrypted_msg.decode().rstrip(padding_character)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    #Triple DES: BLOCK_SIZE(8 bytes) KEY_SIZE(21 or 14 bytes)
    @staticmethod
    def enc_des3(string_to_encrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            cipher = DES3.new(hashed_key[:24])
            padded_private_msg = string_to_encrypt + (padding_character * ((8-len(string_to_encrypt)) % 8))
            encrypted_msg = cipher.encrypt(padded_private_msg)
            encoded_encrypted_msg = base64.b64encode(encrypted_msg)

            return encoded_encrypted_msg.decode()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    @staticmethod
    def dec_des3(string_to_decrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            cipher = DES3.new(hashed_key[:24])
            encrypted_msg = base64.b64decode(string_to_decrypt.encode())
            decrypted_msg = cipher.decrypt(encrypted_msg)

            return decrypted_msg.decode().rstrip(padding_character)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    #BLOWFISH: BLOCK_SIZE(8 bytes) KEY_SIZE(4 -> 56 bytes)
    @staticmethod
    def enc_blowfish(string_to_encrypt,key):
        try:
            cipher = Blowfish.new(key)
            padded_private_msg = string_to_encrypt + (padding_character * ((8-len(string_to_encrypt)) % 8))
            encrypted_msg = cipher.encrypt(padded_private_msg)
            encoded_encrypted_msg = base64.b64encode(encrypted_msg)

            return encoded_encrypted_msg.decode()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    @staticmethod
    def dec_blowfish(string_to_decrypt,key):
        try:
            cipher = Blowfish.new(key)
            encrypted_msg = base64.b64decode(string_to_decrypt.encode())
            decrypted_msg = cipher.decrypt(encrypted_msg)

            return decrypted_msg.decode().rstrip(padding_character)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    #CAST: BLOCK_SIZE(8 bytes) KEY_SIZE(5 -> 16 bytes)
    @staticmethod
    def enc_cast(string_to_encrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            # CAST key must be at least 5 bytes and no more than 16 bytes long
            cipher = CAST.new(hashed_key[:16])
            padded_private_msg = string_to_encrypt + (padding_character * ((8-len(string_to_encrypt)) % 8))
            encrypted_msg = cipher.encrypt(padded_private_msg)
            encoded_encrypted_msg = base64.b64encode(encrypted_msg)

            return encoded_encrypted_msg.decode()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    @staticmethod
    def dec_cast(string_to_decrypt,key):
        try:
            hashed_key = HachageHelper.hash('md5',key)
            cipher = CAST.new(hashed_key[:16])
            encrypted_msg = base64.b64decode(string_to_decrypt.encode())
            decrypted_msg = cipher.decrypt(encrypted_msg)

            return decrypted_msg.decode().rstrip(padding_character)
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    #XOR
    @staticmethod
    def enc_xor(string_to_encrypt,key):
        try:
            cipher = XOR.new(key)
            encrypted_msg = cipher.encrypt(string_to_encrypt)
            encoded_encrypted_msg = base64.b64encode(encrypted_msg)

            return encoded_encrypted_msg.decode()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            
    @staticmethod
    def dec_xor(string_to_decrypt,key):
        try:
            cipher = XOR.new(key)
            encrypted_msg = base64.b64decode(string_to_decrypt.encode())
            decrypted_msg = cipher.decrypt(encrypted_msg)

            return decrypted_msg.decode()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"
            