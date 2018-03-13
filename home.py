'''
Created on 20.02.2018

@author: sven
'''

class homeid(object):
    uuid = 1
    devices = []
    def __init__(self, name="", place=""):
        homeid.uuid += 1
        self.uuid = homeid.uuid
        self.name = name
        self.place = place
        
    def __str__(self):
        return str(self.uuid) + " - " + self.name + " - " +  self.place

class homeAutomation(homeid):
    def __init__(self, name="", place=""):
        super(homeAutomation, self).__init__( name, place)
        self.devices = []
    
    def addDevice(self, device):
        self.devices.append(device)
        
    def __str__(self):
        return '\n'.join(map(str, self.devices))
            

class device(homeid):
    pass

    

myHome = homeAutomation("Zentrale", "Bornstr")
myHome2 = homeAutomation("Niederlassung", "Obernstr")

schalter1 = device("Schalter 1", "Wohnzimmer")
schalter2 = device("Schalter 2", "Esszimmer")

myHome.addDevice(schalter1)
myHome.addDevice(schalter2)


print(myHome.uuid, myHome.name)
print(myHome2.uuid, myHome2.name)

print(schalter1.uuid, schalter1.name)
print(myHome)

