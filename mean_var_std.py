import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 NumPy array
    a = np.array(list).reshape(3, 3)

    # Compute statistics
    calculations = {
        'mean': [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean().item()],
        'variance': [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var().item()],
        'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std().item()],
        'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max().item()],
        'min': [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min().item()],
        'sum': [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum().item()]
    }

    return calculations