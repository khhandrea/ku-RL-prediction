from abc import ABCMeta, abstractmethod

class RLAgent(metaclass=ABCMeta):
    @abstractmethod
    def select_action(self, state):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def show_v_table(self):
        pass

class RLTrainer(metaclass=ABCMeta):
    @abstractmethod
    def train(self):
        pass