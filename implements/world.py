class GridWorld:
    def __init__(self):
        self.w = 3
        self.h = 3
        self.x = 0
        self.y = 0

    def step(self, a):
        if a == 0:
            self.__move_left()
        elif a == 1:
            self.__move_up()
        elif a == 2:
            self.__move_right()
        elif a == 3:
            self.__move_down()

        reward = -1
        done = self.__is_done()
        return (self.x, self.y), reward, done

    def reset(self):
        self.x = 0
        self.y = 0
        return (self.x, self.y)

    def get_state(self):
        return (self.x, self.y)
    
    def __move_left(self): 
        if self.x > 0:
            self.x -=1

    def __move_right(self):
        if self.x < self.w:
            self.x += 1
    
    def __move_up(self): 
        if self.y > 0:
            self.y -= 1

    def __move_down(self): 
        if self.y < self.h:
            self.y += 1

    def __is_done(self):
        return (self.x, self.y) == (self.w, self.h)