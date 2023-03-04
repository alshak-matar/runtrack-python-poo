class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
        
    def displaypoints(self):
        print(str(self.x)+', '+str(self.y))

    def displayX(self):
        print(self.x)
        
        
        
        
        
    def displayY(self):
        print(self.y)
        
        
        
        
    def replayceX(self, x):
        self.x = x
        print(self.x)
        
        
        
        
        
    def replayceY(self, y):
        self.y = y
        print(self.y)

        
        
note = Point(21, 11)
note.displaypoints()
note.displayX()
note.displayY()
note.replayceX(35)
note.replayceY(34)
