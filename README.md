## 📁 Data Analysis Projects

### 📊 Mean-Variance-Standard Deviation Calculator  
Created a function named `calculate()` in `mean_var_std.py` that uses NumPy to compute the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3x3 matrix.

**Tasks Completed:**
- Input is a list of 9 digits which is converted into a 3x3 NumPy array.
- Computed the following statistics across:
  - Axis 0 (columns)
  - Axis 1 (rows)
  - Flattened matrix
- Returned the results in a dictionary format:
  ```python
  {
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
  }
