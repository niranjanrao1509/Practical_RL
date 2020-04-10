
def get_action_value(mdp, state_values, state, action, gamma):
    """ Computes Q(s,a) as in formula above """
    Q=0
    next_states = mdp.get_next_states(state, action)
    for next_state in next_states:
      probability = next_states[next_state]
      reward = mdp.get_reward(state,action,next_state)
      Q += probability*(reward + gamma*state_values[next_state])
    

    # YOUR CODE HERE

    return Q
