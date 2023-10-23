from implements.RL_algo import RLAgent, RLTrainer

class TDAgent(RLAgent):
    def select_action(self, state):
        print('select_action')

    def update(self):
        print('update')

    def show_v_table(self):
        print('show_v_table')

class TDTrainer(RLTrainer):
    def __init__(self, n):
        print(f'TD for {n}')
        
    def train(self):
        TD_agent = TDAgent()
        
        print('train')
        TD_agent.select_action(None)
        TD_agent.update()
        TD_agent.show_v_table()