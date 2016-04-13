from io import BytesIO
from urllib import parse

import pycurl

from . import response


class Request():
    proxy_type = {
        'socks5': pycurl.PROXYTYPE_SOCKS5_HOSTNAME,
    }

    def __init__(self, url, proxy=None):
        self.databuffer = BytesIO()
        c = self.curl = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, self.databuffer)
        if proxy is not None:
            self.add_proxy(proxy)

    def __del__(self):
        self.curl.close()

    def get(self):
        self.curl.perform()
        return response.Response(self.curl, self.databuffer)

    def add_proxy(self, proxy_url):
        token = parse.urlparse(proxy_url)
        self.curl.setopt(pycurl.PROXY, token.hostname)
        self.curl.setopt(pycurl.PROXYPORT, token.port or 80)
        self.curl.setopt(pycurl.PROXYTYPE, self.proxy_type[token.scheme])


def get(url, **kwargs):
    request = Request(url, **kwargs)
    return request.get()
