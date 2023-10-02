import torch
from game import SnakeGameAI
from agent import Agent

def test():
    agent = Agent()
    agent.model.load_state_dict(torch.load("./model/model.pth"))
    game = SnakeGameAI()

    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        _, done, score = game.play_step(final_move)

        if done:
            game.reset()
            print('Test Score:', score)

if __name__ == '__main__':
    test()
