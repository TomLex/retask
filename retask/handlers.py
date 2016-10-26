import ujson


class BytesEncoding(object):
    @staticmethod
    def loads(data):
        return ujson.loads(data.decode())

    @staticmethod
    def dumps(data):
        return ujson.dumps(data).encode()