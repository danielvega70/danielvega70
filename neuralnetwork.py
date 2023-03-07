import numpy as np
import matplotlib.pyplot as plt

# Define the activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def linear(x):
    return x

# Define the neural network architecture
input_size = 2
hidden_size = 3
output_size = 1

# Initialize the weights and biases
np.random.seed(0)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros(hidden_size)
W2 = np.random.randn(hidden_size, hidden_size)
b2 = np.zeros(hidden_size)
W3 = np.random.randn(hidden_size, output_size)
b3 = np.zeros(output_size)

# Define the training data
X = np.array([[0, 0], [0, 1], [1, 0]])
y = np.array([[0], [1], [1]])

# Define the training parameters
learning_rate = 0.1
num_epochs = 100
num_examples = X.shape[0]

# Train the neural network
errors = []
for epoch in range(num_epochs):
    epoch_error = 0
    for i in range(num_examples):
        # Forward pass
        a1 = sigmoid(np.dot(X[i], W1) + b1)
        a2 = sigmoid(np.dot(a1, W2) + b2)
        y_hat = linear(np.dot(a2, W3) + b3)

        # Compute the error
        error = y_hat - y[i]
        epoch_error += np.sum(error**2)

        # Backward pass
        d_y_hat = error
        d_a2 = np.dot(d_y_hat, W3.T) * (a2 * (1 - a2))
        d_a1 = np.dot(d_a2, W2.T) * (a1 * (1 - a1))

        # Update the weights and biases
        d_W3 = np.dot(a2.T, d_y_hat)
        d_b3 = np.sum(d_y_hat, axis=0)
        d_W2 = np.dot(a1.T, d_a2)
        d_b2 = np.sum(d_a2, axis=0)
        d_W1 = np.dot(X[i].reshape(input_size, 1), d_a1.reshape(1, hidden_size))
        d_b1 = np.sum(d_a1, axis=0)

        W3 -= learning_rate * d_W3
        b3 -= learning_rate * d_b3
        W2 -= learning_rate * d_W2
        b2 -= learning_rate * d_b2
        W1 -= learning_rate * d_W1
        b1 -= learning_rate * d_b1

    errors.append(epoch_error)

# Plot the error after each training example
plt.plot(errors)
plt.title("Error per Training Example")
plt.xlabel("Training Example")
plt.ylabel("Error")
plt.show()

# Plot the error after each training epoch
epoch_errors = [np.sum(errors[i*num_examples:(i+1)*num_examples]) for i in range(num_epochs)]
plt.plot(epoch_errors)
plt.title("Error per Training Epoch")
plt.xlabel("Training Epoch")
plt.ylabel("Error")
plt.show()

# Plot the error after each training iteration
iteration_errors = [errors[i*num_examples:(i+1)*num_examples] for i in range(num_epochs)]
for i in range(num_epochs):
    plt.plot(iteration_errors[i])
plt.title("Error per Training Iteration")
plt.xlabel("Training Iteration")
plt.ylabel("Error")
plt.show()
