import requests as req
import xml.etree.ElementTree as ET

ZWSID="X1-ZWz1h1qivh5edn_5jgqp"

class Property:
    def __init__(self,streetAddr='',city='',state=''):
        self.info={'Street Addr':streetAddr,
                    'City':city,
                    'State':state,
                    'zipcode':'',
                    'Zestimate':0,
                    'latitude':0,
                    'longitude':0
                    }

    def findValues(self):
        url="http://www.zillow.com/webservice/GetSearchResults.htm?zws-id="+ZWSID+"&address="+self.info['Street Addr']+"&citystatezip="+self.info['City']+"%2C+"+self.info['State']
        resp = req.get(url)
        root = ET.fromstring(resp.content)
        
        for key in self.info:
            for child in root.iter(key):
                self.info[key]=child.text

        for child in root.iter('amount'):
            self.info['Zestimate']=child.text







