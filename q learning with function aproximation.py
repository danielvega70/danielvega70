import numpy as np

class QLearningFA:
    def __init__(self, env, alpha=0.01, gamma=0.99, epsilon=0.1, num_episodes=1000):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.num_episodes = num_episodes
        
        # Initialize weights for linear function approximation
        self.weights = np.zeros((env.observation_space.shape[0], env.action_space.n))
        
    def train(self):
        for i in range(self.num_episodes):
            state = self.env.reset()
            done = False
            
            while not done:
                # Choose action using epsilon-greedy policy
                if np.random.rand() < self.epsilon:
                    action = self.env.action_space.sample()
                else:
                    q_values = np.dot(self.weights.T, state)
                    action = np.argmax(q_values)
                
                # Take action and observe next state and reward
                next_state, reward, done, _ = self.env.step(action)
                
                # Update weights using TD error and eligibility trace
                q_values_next = np.dot(self.weights.T, next_state)
                td_error = reward + self.gamma * np.max(q_values_next) - np.dot(self.weights.T, state)[action]
                eligibility_trace = state
                self.weights[:, action] += self.alpha * td_error * eligibility_trace
                
                # Update state
                state = next_state
                
    def predict(self, state):
        q_values = np.dot(self.weights.T, state)
        return q_values
