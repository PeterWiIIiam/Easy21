from main import *
import numpy as np

def initialize_a_sequence():
    
    state_sequence = []
    award_sequence = []
    action_sequence = []
    state = initializer()
    dealer_first_card = state["dealer_sum"]
    
    while state != None:
        action = 0
        state, reward = step(state, 0)
        state_sequence.append(state["player_sum"])
        award_sequence.append(award)
        action_sequence.append(action)
        
        
    return dealer_first_card, state_sequence, award_sequence

def update(dealer_first_card, state_sequence, award_sequence, N, Q):
    

    # evaluate the policy 
    for t in range(len(state_sequence)):
        G_t = np.sum(award_sequence[t,:])

        N[dealer_first_card, state_sequence[t], 0] += 1
    epislon = 0.1
