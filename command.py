class Satellite:
    def __init__(self):
        self.orientation = 'North'
        self.panels_status = False
        self.panels = 'Unactive'
        self.DataCollected = 0

    def rotate(self, direction):
        self.orientation = direction

    def activatePanels(self):
        self.panels_status = True
        self.panels ='Active'

    def deactivatePanels(self):
        self.panels_status = False
        self.panels = 'Unactive'
    def collectData(self):
        if self.panels_status == True:
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
        command = input(str()).strip()
        if command == '0' :
            break
        left  = command.find('(')
        right = command.find(')')

        if left != -1 and right != -1:
            function = command[:left]
            direction= command[left + 1:right]

        commands = ['rotate' , 'activatePanels','deactivatePanels' , 'collectData' , 'help']

        if function not in commands:
            if function == 'rotate':
                directions = ['North', 'South', 'East', 'West']
                if direction in directions:
                    s.rotate(direction)
                    print(f'Orientation: "{s.orientation}"')
                else:
                    print('Invalid direction given (North , South , East , West)')

            if function == 'activatePanels':
                s.activatePanels()
                print(f'Solar Panels: "Active"')

            if function == 'deactivatePanels':
                s.activatePanels()
                print(f'Solar Panels: "Unactive"')

            if function == 'collectData':
                try:
                    s.collectData()
                    print(f'Data Collected: {s.DataCollected}')
                except:
                    print('Unable to collect Data')

            if function == 'getStatus' or command == '':
                status = s.get_status()

                print(f'Orientation : "{status[0]}"\n'
                      f'Solar Panels: "{status[1]}"\n'
                      f'Data Collected:{status[2]}')

            if function == 'help':
                print(f'---satellite commands---\n'
                      f'*---------------------------------------------------------*\n'
                      f'| Functions      | commands                               |\n'
                      f'|---------------------------------------------------------|\n'
                      f'| Rotation       | rotate(Direction)                      |\n'
                      f'| Solar panels   | activatePanels() or deactivatePanels() |\n'
                      f'| To collect Data| collectData()                          |\n'
                      f'*---------------------------------------------------------*\n')
        else :
            print('Please check the input given')
