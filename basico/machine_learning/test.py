import numpy as np

class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.y = y
        self.output = np.zeros(y.shape)
        self.count = 0
        
        self.weights1 = np.random.rand(self.input.shape[1], self.y.shape[0])
        self.weights2 = np.random.rand(self.y.shape[0], 1)

    def feedforward(self):
        self.layer_1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer_1, self.weights2))
        self.count += 1

    def backprop(self):
        d_weights2 = np.dot(self.layer_1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer_1)))
        
        self.weights1 = d_weights1
        self.weights2 = d_weights2

    def predict(self, input):
        self.layer_1 = sigmoid(np.dot(input, self.weights1))
        self.output = sigmoid(np.dot(self.layer_1, self.weights2))
        print(f"After {self.count} testing rounds, the prediction for a well-trained neural network is:")
        print(self.output)

# Define the sigmoid and sigmoid_derivative functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Create an instance of the NeuralNetwork class
x = np.array([[0, 1], [1, 0]])
y = np.array([[1], [0]])
test_input = np.array([[0, 1]])

# Train and test the neural network in an infinite loop
my_neural_network = NeuralNetwork(x, y)
while True:
    my_neural_network.feedforward()
    my_neural_network.backprop()
    my_neural_network.predict(test_input)
    
    # Aquí puedes agregar una condición para detener el bucle, como presionar una tecla o alcanzar un cierto número de iteraciones.
    # Por ejemplo, puedes hacer lo siguiente para detener después de 1000 iteraciones:
    if my_neural_network.count >= 1000:
        break
