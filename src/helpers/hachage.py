import hashlib

# we used hashlib instead of pycrypto because it offers more options for hashing

class HachageHelper:

    @staticmethod
    def getAvailable():
        try:
            return list(hashlib.algorithms_available)
        except:
            return "Une erreur s'est produite"

    @staticmethod
    def hash(algo, msg):
        try:
            h = hashlib.new(algo)
            b = msg.strip().encode('utf-8')
            h.update(b)
            return h.hexdigest()
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"

    @staticmethod
    def crackHash(algo, hash, wordlist):
        try:
            with open(wordlist) as f:
                for line in f:
                    h = hashlib.new(algo)
                    line = line.strip().encode()
                    h.update(line)
                    lineHash = h.hexdigest()
                    if lineHash == hash:
                        return line.decode()
            return 'not_found'
        except:
            return "Une erreur s'est produite, veuillez vérifier vos entrées"