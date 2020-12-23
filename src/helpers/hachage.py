import hashlib


class HachageHelper:

    @staticmethod
    def getAvailable():
        return list(hashlib.algorithms_available)

    @staticmethod
    def hash(algo, msg):
        h = hashlib.new(algo)
        b = msg.strip().encode('utf-8')
        h.update(b)
        return h.hexdigest()

    @staticmethod
    def crackHash(algo, hash, wordlist):
        h = hashlib.new(algo)
        with open(wordlist) as f:
            for line in f:
                line = line.strip().encode('utf-8')
                h.update(line)
                lineHash = h.hexdigest()
                if lineHash == hash:
                    return line
        return "hash_not_found"