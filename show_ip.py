#!python
import rumps
import re
import json
from urllib.request import urlopen
class ShowIP(rumps.App):
    @rumps.clicked("refresh")
    def refresh(self, _):
        self.__init__(self.get_ip())

    def get_ip(self):
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)

        IP=data['ip']
        org=data['org']
        city = data['city']
        country=data['country']
        region=data['region']

        return f"{IP} {city} {region}"

if __name__ == '__main__':
    app = ShowIP("ShowIP")
    app.refresh(None)
    app.run()
