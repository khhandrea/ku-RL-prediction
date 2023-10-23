from implements.RL_algo import RLAgent, RLTrainer

class MCAgent(RLAgent):
    def select_action(self, state):
        print('select_action')

    def update(self):
        print('update')

    def show_v_table(self):
        print('show_v_table')

class MCTrainer(RLTrainer):
    def train(self):
        MC_agent = MCAgent()
        
        print('train')
        MC_agent.select_action(None)
        MC_agent.update()
        MC_agent.show_v_table()