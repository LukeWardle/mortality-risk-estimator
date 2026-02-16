"""
Vector Visualisation - Part 1: Basic plotting

Demonstrates how to visualise 2D vectors using MatplotLib.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_vector(vector, origin=None, color='b', label='', width=0.006):
  """
  Plot a 2D vector as an arrow

  Args:
    vector (np.ndarray): 2D vector to plit [x, y]
    origin (np.ndarray): Starting point [x, y]. Default to [0, 0]
    color (str): Arrow color
    label (str): Label for legend
    width (float): Arrow shaft width
  
  """

  if origin is None:
    origin = np.array([0, 0])

  plt.quiver(
    origin[0], origin[1], # Starting point
    vector[0], vector[1], # Vector components
    angles='xy',          # Use data coordinates
    scale_units='xy',     # Scale in data units
    scale=1,              # No automatic scaling
    color=color,
    width=width,
    label=label
  )

def setup_plot(xlim=(-5, 5), ylim=(-5, 5), title="Vector Visualisation"):
    """
    Set up a standardised plot environment for vector visualisation.

    Args:
      xlim (tuple): X-axis limits
      ylim (tuple): Y-axis limits
      title (str): Plot title
    
    """

    plt.figure(figsize=(8, 8))

    # Draw coordinate axes
    plt.axhline(0, color='grey', linewidth=0.5, linestyle='-')
    plt.axvline(0, color='grey', linewidth=0.5, linestyle='-')

    # Grid for reference
    plt.grid(True, linestyle='--', alpha=0.6)

    # Set axis limits
    plt.xlim(xlim)
    plt.ylim(ylim)

    # Labels and title
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-label', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')

    # CRITICAL: Equal aspect ratio ensures geometric accuracy
    plt.gca().set_aspect('equal', adjustable='box')

# Example 1: Plot two simple vectors
def example_basic_vectors():
  """Visualise two basic 2D vectors."""
  v1=np.array([2, 3])
  v2=np.array([-1, 4])

  setup_plot(xlim=(-3, 4), ylim=(-1, 5), title="Basic 2D Vectors")

  plot_vector(v1, color='blue', label='v1 = [2, 3]')
  plot_vector(v2, color='red', label='v2 = [-1, 4]')

  plt.legend()
  plt.savefig('basic_vectors.png', dpi=150, bbox_inches='tight')
  plt.show()

def example_vector_addition():
   """Visualise vector addition using the head-to-tail rule."""
   v1 = np.array([2, 3])
   v2 = np.array([-1, 4])
   v_sum = v1 + v2

   print(f"v1 = {v1}")
   print(f"v2 = {v2}")
   print(f"v1 + v2 = {v_sum}")

   setup_plot(xlim=(-2, 4), ylim=(-1, 8), title="Vector Addition: Head-to-Tail Rule")

   # Step 1: Plot v1 from origin
   plot_vector(v1, color='blue', label='v1 = [2, 3]')

   # Step 2: Plot v2 starting from head of v1
   plot_vector(v2, origin=v1, color='red', label='v2 = [-1, 4] (shifted)')

   # Step 3: Plot the sum from origin to final head
   plot_vector(v_sum, color='green', label=f'v_sum = {v_sum}', width=0.008)

   # Draw dotted lines to show the parallelogram
   plt.plot([0, v2[0]], [0, v2[1]], 'r--', alpha=0.3, linewidth=1)
   plt.plot([v1[0], v_sum[0]], [v1[1], v_sum[1]], 'b--', alpha=0.3, linewidth=1)

   plt.legend(loc='upper left')
   plt.savefig('vector_addition.png', dpi=150, bbox_inches='tight')
   plt.show()

if __name__ == "__main__":
    example_basic_vectors()
    example_vector_addition()