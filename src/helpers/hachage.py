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