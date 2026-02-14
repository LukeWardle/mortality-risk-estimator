"""
Input/Output parsing utilities for command-line interface.

This module handles conversion of string inputs to NumPy arrays.
"""
import numpy as np

def parse_vector_input(input_str: str) -> np.ndarray:
  """
  Converts a comma-seperated string into a Numpy array of floats.

  This function performs three critical steps:
  1. Split the string by commas into individual string elements
  2. Convert each string element to a float.
  3. Convert the list of floats into NumPy array

  Args:
    input_str (str): Comma-separated numbers, e.g., "75,120,80,1"

  Returns:
    np.ndarray: A 1D NumPy array of floating-point numbers

  Raises:
    ValueError: If input contains non-numeric values

  Example:
    >>> parse_vector_input("1,2,3")
    array([1., 2., 3.])

  """
  try:
    # Step 1 & 2: Split string and convert each part to float
    # .strip() removes leading/trailing whitespace from each element 
    list_of_floats = [float(part.strip()) for part in input_str.split(',')]
    # Step 3: Convert list to NumPy array 
    return np.array(list_of_floats)
  except ValueError as e:
    raise ValueError(
      f"Invalid input: '{input_str}'."
      f"Expected comma-seperated numbers. Error: {e}"
    )