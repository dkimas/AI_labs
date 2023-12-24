import numpy as np


class NeuralNetwork:
    def __init__(self, layers, activations):
        self.num_layers = len(layers)
        self.layers = layers
        self.activations = activations
        self.weights = [np.random.randn(y, x) / np.sqrt(x) for x, y in zip(layers[:-1], layers[1:])]
        self.biases = [np.zeros((y, 1)) for y in layers[1:]]

    def forward(self, x):
        for i in range(self.num_layers - 1):
            x = self.activations[i](np.dot(self.weights[i], x) + self.biases[i])
        return x

    def train(self, X_train, y_train, epochs, batch_size, optimizer):
        for i in range(epochs):
            X_train, y_train = shuffle(X_train, y_train)
            for j in range(0, len(X_train), batch_size):
                X_batch = X_train[j:j + batch_size]
                y_batch = y_train[j:j + batch_size]
                gradients = self.backprop(X_batch.T, y_batch.T)
                self.weights, self.biases = optimizer.update_weights(self.weights, self.biases, gradients)

    def backprop(self, X, y):
        gradients_w = [np.zeros(w.shape) for w in self.weights]
        gradients_b = [np.zeros(b.shape) for b in self.biases]
        n = X.shape[1]

        # forward pass
        activations = [X]
        zs = []
        a = X
        for i in range(self.num_layers - 1):
            z = np.dot(self.weights[i], a) + self.biases[i]
            a = self.activations[i](z)
            zs.append(z)
            activations.append(a)

        # backward pass
        delta = (activations[-1] - y) * self.activations[-1](zs[-1])
        gradients_b[-1] = np.sum(delta, axis=1, keepdims=True) / n
        gradients_w[-1] = np.dot(delta, activations[-2].T) / n

        for l in range(2, self.num_layers):
            delta = np.dot(self.weights[-l + 1].T, delta) * self.activations[-l](zs[-l])
            gradients_b[-l] = np.sum(delta, axis=1, keepdims=True) / n
            gradients_w[-l] = np.dot(delta, activations[-l - 1].T) / n

        return (gradients_w, gradients_b)

    def predict(self, X):
        y_pred = self.forward(X.T)
        return np.argmax(y_pred, axis=0)



def shuffle(X, y):
    """Перемешивает данные X и соответствующие им метки y."""
    indices = np.random.permutation(len(X))
    return X[indices], y[indices]

def minibatches(X, y, batch_size):
    """Генерирует мини-батчи данных размером batch_size."""
    for i in range(0, len(X), batch_size):
        X_batch = X[i:i+batch_size]
        y_batch = y[i:i+batch_size]
        yield X_batch, y_batch

def map_features(X, degree):
    """Добавляет входным данным X дополнительные полиномиальные признаки до заданной степени degree."""
    X_poly = X
    for i in range(2, degree+1):
        X_poly = np.column_stack((X_poly, np.power(X, i)))
    return X_poly

def normalize(X):
    """Нормализует входные данные X."""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

class SGD:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def update_weights(self, weights, biases, gradients):
        updated_weights = [w - self.learning_rate * dw for w, dw in zip(weights, gradients[0])]
        updated_biases = [b - self.learning_rate * db for b, db in zip(biases, gradients[1])]
        return updated_weights, updated_biases


class MomentumSGD:
    def __init__(self, learning_rate, momentum=0.9):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.velocities_w = None
        self.velocities_b = None

    def update_weights(self, weights, biases, gradients):
        if self.velocities_w is None:
            self.velocities_w = [np.zeros_like(w) for w in weights]
            self.velocities_b = [np.zeros_like(b) for b in biases]

        velocities_w_updated = []
        velocities_b_updated = []

        for i in range(len(weights)):
            velocity_w = self.momentum * self.velocities_w[i] - self.learning_rate * gradients[0][i]
            velocity_b = self.momentum * self.velocities_b[i] - self.learning_rate * gradients[1][i]

            weights[i] += velocity_w
            biases[i] += velocity_b

            velocities_w_updated.append(velocity_w)
            velocities_b_updated.append(velocity_b)

        self.velocities_w = velocities_w_updated
        self.velocities_b = velocities_b_updated

        return weights, biases



class Adagrad:
    def __init__(self, learning_rate=0.01, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.cache_w = None
        self.cache_b = None

    def update_weights(self, weights, biases, gradients):
        if self.cache_w is None:
            self.cache_w = [np.zeros_like(w) for w in weights]
            self.cache_b = [np.zeros_like(b) for b in biases]

        gradients_w, gradients_b = gradients
        updated_weights = []
        updated_biases = []
        for i in range(len(weights)):
            self.cache_w[i] += np.square(gradients_w[i])
            self.cache_b[i] += np.square(gradients_b[i])

            updated_weights.append(
                weights[i] - self.learning_rate * gradients_w[i] / (np.sqrt(self.cache_w[i]) + self.epsilon))
            updated_biases.append(
                biases[i] - self.learning_rate * gradients_b[i] / (np.sqrt(self.cache_b[i]) + self.epsilon))

        return updated_weights, updated_biases


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def softmax(x):
    exp_scores = np.exp(x)
    return exp_scores / np.sum(exp_scores, axis=0)


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def binary_cross_entropy(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def categorical_cross_entropy(y_true, y_pred):
    return -np.mean(y_true * np.log(y_pred))

def softmax_cross_entropy(y_true, y_pred):
    return -np.mean(np.sum(y_true * np.log(y_pred), axis=1))



from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Загрузка данных
iris = load_iris()
X = iris.data
y = iris.target

# Нормализация данных
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создание экземпляра нейронной сети
nn = NeuralNetwork([4, 50, 3], [sigmoid, relu])
# Обучение нейронной сети
nn.train(X_train, y_train, epochs=25, batch_size=8, optimizer=Adagrad(learning_rate=0.1))

# Оценка точности нейронной сети на тестовых данных
y_pred = nn.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print('Accuracy: ', accuracy)



