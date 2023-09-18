class Satellite:
    def __init__(self):
        self.orientation = 'North'
        self.panels = False
        self.DataCollected = 0

    def rotate(self, direction):
        self.orientation = direction

    def activatePanels(self):
        self.panels = True

    def deactivatePanels(self):
        self.panels = False

    def collectData(self):
        if self.panels == True:
            self.DataCollected += 10

    def get_status(self):
        return [self.orientation , self.panels , self.DataCollected]


if __name__ == '__main__':
    s = Satellite()
    while True:
        function = None
        direction = None
        """
        getting input from user 
        ex : rotate(North) or rotate(South) 
        """
        command = input(str())
        if command == '0' :
            break
        left  = command.find('(')
        right = command.find(')')


        if left != -1 and right != -1:
            function = command[:left]
            direction= command[left + 1:right]

        if function == 'rotate':
            directions = ['North', 'South', 'East', 'West']
            if direction in directions:
                s.rotate(direction)
            print(f'Orientation: "{s.orientation}"')

        if function == 'activatePanels':
            s.activatePanels()
            print(f'Solar Panels: "Active"')

        if function == 'deactivatePanels':
            s.activatePanels()
            print(f'Solar Panels: "Unactive"')

        if function == 'collectData':
            s.collectData()
            print(f'Data Collected: {s.DataCollected}')

        if function == 'getStatus' or command =='':
            print(f'{s.get_status()}')
