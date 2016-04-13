import pycurl


class Response():
    def __init__(self, curl, databuffer):
        self.status_code = curl.getinfo(pycurl.HTTP_CODE)
        self.content = databuffer.getvalue()
        self.encoding = 'iso-8859-1'

    @property
    def text(self):
        return self.content.decode(self.encoding)
