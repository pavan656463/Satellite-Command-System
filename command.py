"""
satellite command system

initial state :
   orientation:North
   solar panels :inactive
   Data collected : 0

"""


class Satellite:
    def __init__(self):
        self.orientation = 'North'
        self.panels = False
        self.DataCollected = 0

    def rotate(self, direction):
        directions = ['North', 'South', 'East', 'West']
        if direction in directions:
            self.orientation = direction

    def activatePanels(self):
        self.panels = True

    def deactivatePanels(self):
        self.panels = False

    def collectData(self):
        if self.panels == True:
            self.DataCollected += 10

    def get_status(self):
        print(f"Orientation : {self.orientation}")
        if self.panels == True :
            print(f"Solar Panels : Active")
        else :
            print(f"Solar Panels : Inactive")
        print(f"Data Collected : {self.DataCollected} ")

if __name__ == '__main__':
    s1 = Satellite()
