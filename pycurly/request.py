from io import BytesIO

import pycurl

from . import response


class Request():
    def __init__(self, url):
        self.databuffer = BytesIO()
        c = self.curl = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, self.databuffer)

    def __del__(self):
        self.curl.close()

    def get(self):
        self.curl.perform()
        return response.Response(self.curl, self.databuffer)


def get(url):
    request = Request(url)
    return request.get()
