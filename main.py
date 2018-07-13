import numpy as np



def draw_randomly(initialize=False):
        random_color = np.random.choice(['red', 'black'], p=[0.33333333333333333333333333, 0.6666666666666666666666666666])
        random_number = np.random.randint(1, 11)

        if initialize:
                print(initialize)
                return random_number
        if random_color == 'red':
                return  -random_number
        return random_number


def initializer():
        player_card = draw_randomly(True)
        dealer_card = draw_randomly(True)
        
        state = {"dealer_sum" : dealer_card, 
                 "player_sum" : player_card}

        return state



def step(state, action):
	
        if action == 1:
                player_card = draw_randomly()
                state["player_sum"] += player_card
                print(player_card)
                if state["player_sum"] > 21:
                        return None, -1
                if state["player_sum"] < 1:
                        return None, -1
                else:
                        return state, 0

        if action == 0:
                print("action step", action)

                if state['dealer_sum'] > 21 or state['dealer_sum'] < 1:
                        return None, 1

                if state["dealer_sum"] < 17:
                        dealer_card = draw_randomly()
                        print(dealer_card)
                        state["dealer_sum"] += dealer_card
                        print("state when recur for dealer", state)
                        step(state, 0)

                if state["player_sum"] < 1:
                        return None, -1
                        
                if state["dealer_sum"] > state["player_sum"]:
                        return None, -1
                
                if state["dealer_sum"] < state["player_sum"]:
                        return None, 1
                
                if state["dealer_sum"] == state["player_sum"]:
                        return None, 0


