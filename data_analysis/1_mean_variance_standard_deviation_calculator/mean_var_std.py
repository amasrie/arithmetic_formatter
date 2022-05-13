import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  matrix = np.reshape(list, (3, 3))
  calculations = {
    'mean': [[np.mean(matrix[:, i]) for i in range(3)], [np.mean(matrix[i, :]) for i in range(3)], np.mean(matrix)],
    'variance': [[np.var(matrix[:, i]) for i in range(3)], [np.var(matrix[i, :]) for i in range(3)], np.var(matrix)],
    'standard deviation': [[np.std(matrix[:, i]) for i in range(3)], [np.std(matrix[i, :]) for i in range(3)], np.std(matrix)],
    'max': [[np.max(matrix[:, i]) for i in range(3)], [np.max(matrix[i, :]) for i in range(3)], np.max(matrix)],
    'min': [[np.min(matrix[:, i]) for i in range(3)], [np.min(matrix[i, :]) for i in range(3)], np.min(matrix)],
    'sum': [[np.sum(matrix[:, i]) for i in range(3)], [np.sum(matrix[i, :]) for i in range(3)], np.sum(matrix)],
  }
  return calculations
  