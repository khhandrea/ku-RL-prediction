from abc import ABCMeta, abstractmethod

class RLAgent(metaclass=ABCMeta):
    @abstractmethod
    def select_action(self, state):
        pass