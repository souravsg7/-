import json
from User_Interface import BoxFrame
SettingsName = 'Settings.json'

class PrinterSettings:
    def __init__(self):
        with open(SettingsName, 'r') as file:
            data = json.load(file)
        
        laser_frame = [tuple(l) for l in data['laser_frame']]
        image_frame = [tuple(l) for l in data['image_frame']]

        self.laser_frame = BoxFrame.BoxFrame(laser_frame)
        self.image_frame =  BoxFrame.BoxFrame(image_frame)
        self.xOffset = data['xOffset']
        self.yOffset = data['yOffset']
    
    def saveSettings(self):
        jsonDict = {
            "laser_frame": self.laser_frame.corners,
            "image_frame": self.image_frame.corners,
            "xOffset": self.xOffset,
            "yOffset": self.yOffset
        }
        with open(SettingsName, 'w') as file:
            json.dump(jsonDict, file)
