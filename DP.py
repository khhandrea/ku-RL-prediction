import numpy as np

from implements.RL_algo import RLTrainer
from implements.world import GridWorld
from implements.data_handler import loss_write

class DPTrainer(RLTrainer):
    def __init__(self):
        self.__world = GridWorld()
        self.__policy = np.full((4, 4, 4), 0.25)
        self.__old_policy = np.zeros((4, 4, 4))
        self.__vs = np.zeros((4, 4))
        self.__gamma = 1
        
    def __policy_evaluation(self):
        old_vs = self.__vs.copy()
        
        # Bellman equation
        for y in range(4):
            for x in range(4):
                if (y, x) == (3, 3):
                    continue
                    
                v = 0
                
                for action in range(4):
                    self.__world.x = x
                    self.__world.y = y
                    (next_x, next_y), reward, done = self.__world.step(action)
                    v += self.__policy[y][x][action] * (reward + self.__gamma * old_vs[next_y][next_x])

                self.__vs[y][x] = v

    def __policy_improvement(self):
        for y in range(4):
            for x in range(4):
                if (y, x) == (3, 3):
                    continue
                    
                max_v = -99999

                if x > 0:
                    if self.__vs[y][x - 1] > max_v:
                        argmax = [0]
                        max_v = self.__vs[y][x - 1]
                    elif self.__vs[y][x - 1] == max_v:
                        argmax.append(0)

                if y > 0:
                    if self.__vs[y - 1][x] > max_v:
                        argmax = [1]
                        max_v = self.__vs[y - 1][x]
                    elif self.__vs[y - 1][x] == max_v:
                        argmax.append(1)

                if x < 3:
                    if self.__vs[y][x + 1] > max_v:
                        argmax = [2]
                        max_v = self.__vs[y][x + 1]
                    elif self.__vs[y - 1][x] == max_v:
                        argmax.append(2)

                if y < 3:
                    if self.__vs[y + 1][x] > max_v:
                        argmax = [3]
                        max_v = self.__vs[y + 1][x]
                    elif self.__vs[y - 1][x] == max_v:
                        argmax.append(3)

                self.__policy[y][x][:] = 0
                if len(argmax) == 0:
                    self.__policy[y][x][:] = 0.25
                else:
                    self.__policy[y][x][argmax] = 1 / len(argmax)

    def __is_converged(self):
        result = np.array_equal(self.__policy, self.__old_policy)
        self.__old_policy = self.__policy.copy()
        return result

    def __show_v_table(self):
        for row in self.__vs:
            for v in row:
                print(v, end=' ')
            print()

    def train(self):
        while not self.__is_converged():
            self.__policy_evaluation()
            self.__policy_improvement()
        self.__show_v_table()

        loss_write('DP-0.txt', self.__vs)

if __name__ == '__main__':
    DP_trainer = DPTrainer()
    DP_trainer.train()