import numpy as np
from utils import *
from plots import *


def TD_control():

    # store event sequence for off policy learning
    state_sequence = []
    award_sequence = []
    action_sequence = []

    N = np.zeros([11, 22, 2])
    Q = np.zeros([11, 22, 2])

    for episode_num in range(1000000):

        state = initializer()

        dealer_first_card = state["dealer_sum"]
        epsilon = 100 / (100 + np.sum(N[dealer_first_card, state["player_sum"], :]))
        action = epsilon_greedy(dealer_first_card, state["player_sum"], epsilon, Q)

        while state != None:
            print("state when starting steps", state)

            next_state, award = step(state, action)
            N[dealer_first_card, state["player_sum"], action] += 1

            state_sequence.append(state["player_sum"])
            award_sequence.append(award)
            action_sequence.append(action)

            print(state)

            if next_state == None:
                G_t = award

                Q[dealer_first_card, state["player_sum"], action] += 1 / N[
                    dealer_first_card, state["player_sum"], action] * (G_t - Q[
                    dealer_first_card, state["player_sum"], action])

            else:
                epsilon = 100 / (100 + np.sum(N[dealer_first_card, next_state["player_sum"], :]))
                next_action = epsilon_greedy(dealer_first_card, next_state["player_sum"], epsilon, Q)

                G_t = award + Q[dealer_first_card, next_state["player_sum"], next_action]

                Q[dealer_first_card, state["player_sum"], action] += 1 / N[
                    dealer_first_card, state["player_sum"], action] * (G_t - Q[
                    dealer_first_card, state["player_sum"], action])

                action = next_action

            state = next_state


    print("end")
    print(len(state_sequence), len(award_sequence), len(action_sequence))

if __name__ == '__main__':
    TD_control()