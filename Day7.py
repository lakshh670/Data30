import numpy as np

matrix = np.arange(9).reshape(3, 3)
print("Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Size:", matrix.size)
print("Dimension:", matrix.ndim)

data = np.random.normal(loc=0, scale=1, size=100)
print("\nMean of data:", np.mean(data))
print("Standard Deviation of data:", np.std(data))
