import hashlib


class HachageHelper:

    @staticmethod
    def getAvailable():
        return list(hashlib.algorithms_available)

    @staticmethod
    def hash(algo, msg):
        h = hashlib.new(algo)
        b = msg.encode('utf-8')
        h.update(b)
        return h.hexdigest()

    @staticmethod
    def crackHash(algo, hash, wordlist):
        h = hashlib.new(algo)
        with open(wordlist, "r") as infile:
            for line in infile:
                line = line.strip().encode('utf-8')
                h.update(line)
                lineHash = h.hexdigest()
                if str(lineHash) == str(hash.lower()):
                    print("Word is: %s" % line)