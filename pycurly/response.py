import pycurl


class Response():
    def __init__(self, curl, databuffer):
        self.status_code = curl.getinfo(pycurl.HTTP_CODE)
        self.data = databuffer.getvalue().decode('iso-8859-1')
