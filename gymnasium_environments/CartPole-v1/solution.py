import gymnasium as gym
import numpy as np
import random

# Create environment
env = gym.make("CartPole-v1", render_mode="human")


# Discretize the state space (keep it simple)
def discretize_state(state):
    """Discretize the continuous state space into a smaller grid."""
    # Define state bins
    bins = [np.linspace(-2.4, 2.4, 6),  # cart position
            np.linspace(-3.0, 3.0, 6),  # cart velocity
            np.linspace(-0.5, 0.5, 6),  # pole angle
            np.linspace(-2.0, 2.0, 6)]  # pole velocity

    # Convert the state to indices of the bins
    return tuple(np.digitize(s, bin_edges) - 1 for s, bin_edges in zip(state, bins))


# Initialize Q-table
state_space = (6, 6, 6, 6)  # 6x6x6x6 grid for state space
q_table = np.zeros(state_space + (env.action_space.n,))

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.99  # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 1000  # Number of episodes

# Training loop
for episode in range(episodes):
    state, info = env.reset()
    state = discretize_state(state)  # Discretize the state
    done = False
    total_reward = 0

    while not done:
        # Epsilon-greedy: explore or exploit
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # Random action (exploration)
        else:
            action = np.argmax(q_table[state])  # Best action (exploitation)

        # Take the action and observe the result
        next_state, reward, terminated, truncated, info = env.step(action)
        next_state = discretize_state(next_state)

        # Q-learning update rule
        max_future_q = np.max(q_table[next_state])
        q_table[state][action] += alpha * (reward + gamma * max_future_q - q_table[state][action])

        # Move to the next state
        state = next_state
        total_reward += reward

        done = terminated or truncated

    # Decay epsilon to reduce exploration over time
    epsilon = max(0.01, epsilon * 0.995)

    if episode % 100 == 0:
        print(f"Episode {episode}/{episodes}, Total Reward: {total_reward}")

# Test the trained agent (no exploration)
epsilon = 0  # No exploration during testing
total_reward = 0
state, info = env.reset()
state = discretize_state(state)
done = False

while not done:
    action = np.argmax(q_table[state])  # Choose the best action
    state, reward, terminated, truncated, info = env.step(action)
    state = discretize_state(state)
    total_reward += reward
    done = terminated or truncated

print(f"Test completed. Total reward: {total_reward}")

# Close the environment
env.close()
