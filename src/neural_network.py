import numpy as np

class MLP:
    """Red neuronal multicapa implementada desde cero con NumPy."""
    def __init__(self, layers, activations=None):
        self.layers = layers
        self.activations = activations or ["relu"] * (len(layers) - 2) + ["sigmoid"]
        self.weights = []
        self.biases = []
        for i in range(len(layers) - 1):
            self.weights.append(np.random.randn(layers[i], layers[i + 1]) * np.sqrt(2 / layers[i]))
            self.biases.append(np.zeros((1, layers[i + 1])))

    @staticmethod
    def _relu(x): return np.maximum(0, x)
    @staticmethod
    def _sigmoid(x): return 1 / (1 + np.exp(-np.clip(x, -50, 50)))
    @staticmethod
    def _relu_deriv(x): return (x > 0).astype(float)

    def _activar(self, z, nombre):
        return self._sigmoid(z) if nombre == "sigmoid" else self._relu(z)

    def forward(self, x):
        a = x
        for w, b, act in zip(self.weights, self.biases, self.activations):
            a = self._activar(a @ w + b, act)
        return a

    def predict_proba(self, x):
        return self.forward(x)

    def predict(self, x, threshold=0.5):
        return (self.predict_proba(x) >= threshold).astype(int)

    def guardar(self, ruta):
        datos = {f"W{i}": w for i, w in enumerate(self.weights)}
        datos.update({f"b{i}": b for i, b in enumerate(self.biases)})
        np.savez(ruta, **datos)

    @classmethod
    def cargar(cls, ruta):
        datos = np.load(ruta)
        n = len([k for k in datos.files if k.startswith("W")])
        pesos = [datos[f"W{i}"] for i in range(n)]
        sesgos = [datos[f"b{i}"] for i in range(n)]
        obj = cls([pesos[0].shape[0]] + [w.shape[1] for w in pesos])
        obj.weights, obj.biases = pesos, sesgos
        return obj
