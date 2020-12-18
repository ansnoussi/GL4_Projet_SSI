import hashlib


class HachageHelper:

    @staticmethod
    def getAvailable():
        return list(hashlib.algorithms_available)

    @staticmethod
    def hash(alog, msg):
        h = hashlib.new(alog)
        b = msg.encode('utf-8')
        h.update(b)
        return h.hexdigest()