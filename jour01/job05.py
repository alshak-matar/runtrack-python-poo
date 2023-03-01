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
        
        
        
        
    def replaycerX(self, x):
        self.x = x
        print(self.x)
        
        
        
        
        
    def replaycerY(self, y):
        self.y = y
        print(self.y)

        
        
note = Point(21, 11)
note.displaypoints()
note.displayX()
note.displayY()
note.replaycerX(35)
note.replaycerY(34)
