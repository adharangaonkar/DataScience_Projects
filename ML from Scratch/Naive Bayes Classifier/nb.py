import numpy as np

class NaiveBayes:

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_clesses = leb(self._classes)

        # intitialize mean, var, priors
        self._mean = np.zeros((n_classes, n_features), dtype= np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes ), dtype=np.float64)

        for c in self._classes:



    def predict(self, X):
        pass