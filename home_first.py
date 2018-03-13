'''
Created on 20.02.2018

@author: sven
'''


class home(object):
    place = ""
    uuid = 0
    devices = []
    def __init__(self, uuid = 0, place = ""):
        self.uuid = uuid
        self.place = place

    def addDevice(self, device):
        self.devices.append(device)
        
    def getDevices(self):
        return self.devices
        

class device():
    def __init__(self, uuid = 0, place = ""):
        self.uuid = uuid
        self.place = place
        
    
     
class schalter(device):
    def __init__(self, uuid = 0, place = ""):
        super(self, uuid, place)



class leuchte(device):
    def __init__(self, uuid = 0, place = "", name = ""):
        device.__init__(self, uuid, place)
        self.name = name
        
    def __str__(self):
        return self.name
    
def main():
    myHome = home(3, "Bornstr")
    wohnzimmer1 = leuchte(4, "Wohnzimmer", "Decke")
    wohnzimmer2 = leuchte(5, "Wohnzimmer", "Stehleuchte")
    myHome.addDevice(wohnzimmer1)
    myHome.addDevice(wohnzimmer2)

    
    print(myHome.getDevices())


if __name__ == '__main__':
    main()
