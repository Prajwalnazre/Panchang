'''
Class :
>> PanchangObject
- Used in panchanWidget.py
'''

class PanchangObject :
    thithi = ''
    maasa = ''
    dayOfMonth = 0
    paksha = ''

    def __init__(self, thithi, maasa, dayOfMonth, paksha) :
        self.thithi = thithi
        self.maasa = maasa
        self.dayOfMonth = dayOfMonth
        self.paksha = paksha

    def printPanchangInfo(self) :
        print("Thithi : " + self.thithi)
        print("Maasa : " + self.maasa)
        print("Day of the Month : " + str(self.dayOfMonth))
        print("Paksha : " + self.paksha)