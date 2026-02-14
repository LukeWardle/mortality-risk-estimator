"""
Core mathematical operations for vector computations.

This module implements fundamental linear algebra operations
demonstrated through mortality risk calculation.

"""

import numpy as np

def calculate_risk_score(weights: np.ndarray, features: np.ndarray) -> float:
  """
  Calculate mortality risk score using the dot product.

  This implements the fundamental linear model: risk = w^T ∙ x
  where w is the weight vector and x is the feature vector.

  The dot product (also called the inner product or scalar product)
  multiplies corresponding elements and sums the results:
  w∙x = w1x1 + w2x2 + ... + wnxn

  Args:
    weights (np.ndarray) : Model weights, shape (n,)
    features (np.ndarray) : Patient features, shape (n,)

  Returns:
    float: The calculated risk score (scalar value)

  Raises:
    ValueError: If vectors have different lengths

  Example:
    >>> weights = np.array([0.02, 0.5])
    >>> features = np.array([75, 28])
    >>> calculated_risk_score(weights, features)
    15.5

  """
  # Validate dimensions match
  if weights.shape != features.shape:
    raise ValueError(
      f"Dimension mismatch: weights {weights.shape} != features {features.shape}"
    )
  
  # Calculate dot product using @ operator (equivalent to np.dot)
  risk_score = weights @ features

  # Convert from numpy scalar to python float for cleaner output
  return float(risk_score)

def calculate_magnitude(vector: np.ndarray) -> float:
  """
  Calculate the magnitude (length) of a vector.

  The magnitude is calculated using the Euclidean norm (L2 norm):
  ||v|| = √(v₁² + v₂² + ... + vₙ²)

  This is equivalent to taking the square root of the dot product
  of the vector with itself: ||v|| = √(v·v)

  Args:
    vector (np.ndarray): Input vector, shape (n,)

  Returns:
    float: The magnitude (length) of the vector

  Example:
    >>> calculate_magnitude(np.array([3, 4]))
    5.0

  """

  # Use NumPy's linalg.norm for numerical stability
  magnitude = np.linalg.norm(vector)
  return float(magnitude)

def normalize_vector(vector: np.ndarray) -> np.ndarray:
  """
  Normalize a vector to unti length.

  A normalized (unit) vector has magnitude 1 while preserving direction.
  Formula: v̂ = v / ||v||

  Args:
    vector (np.ndarray): Input vector, shape (n,)

  Returns:
    np.ndarray: Unit vector in same direction, shape (n,)

  Raises:
    ValueError: If vector is zero vector (magnitude = 0)

  Example:
    >>> normalize_vector(np.array([3, 4]))
    array([0.6, 0.8])
  """
  magnitude = calculate_magnitude(vector)

  if magnitude == 0:
    raise ValueError("Cannot normalize zero vector")
  return vector / magnitude

