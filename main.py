import numpy as np

# Define the state space (list of states)
states = ["A", "B", "C"]

# Define the transition matrix
# Each element (i, j) represents the probability of transitioning from state i to state j
transition_matrix = np.array([
    [0.4, 0.3, 0.3],  # Transition probabilities from state A
    [0.2, 0.5, 0.3],  # Transition probabilities from state B
    [0.1, 0.2, 0.7]   # Transition probabilities from state C
])

# Set the initial state
initial_state = input("enter initial state: ")

# Define the number of steps
num_steps = 50

# Simulate the Markov chain
current_state = initial_state
chain = [current_state]

for _ in range(num_steps):
    next_state = np.random.choice(states, p=transition_matrix[states.index(current_state)])
    chain.append(next_state)
    current_state = next_state

print("Markov Chain States:")
print(chain)
