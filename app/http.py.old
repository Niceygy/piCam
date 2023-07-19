import json
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qsl, urlparse

class WebRequestHandler(BaseHTTPRequestHandler):
    #url format: /{LED, POWER}/
    #                           000-000-000 (R:G:B) or
    #                           {REBOOT, OFF}


    def get_response(self):
        url = self.url.path # type: ignore
        return json.dumps(
            {
                "path": self.url.path, # type: ignore
                "query_data": self.query_data, # type: ignore
                "post_data": self.post_data.decode("utf-8"), # type: ignore
                "form_data": self.form_data, # type: ignore
                "cookies": {
                    name: cookie.value
                    for name, cookie in self.cookies.items() # type: ignore
                },
            }
        )
    def handler(url):
                url = str(url)
                if("LED" in url):
                       #assuming LED request
                       RGB = url.split("-")
                       red = RGB[0]
                       green = RGB[1]
                       blue = RGB[2]