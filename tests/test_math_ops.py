"""
Unit tests for mathematical operations.


Tests verify correctness of core functions with known inputs/outputs.
"""
import numpy as np
import pytest
from src.math_ops import calculate_risk_score, calculate_magnitude, normalize_vector


def test_calculate_risk_score_basic():
    """Test risk score calculation with simple inputs."""
    weights = np.array([0.02, 0.5])
    features = np.array([50, 30])
    expected = (0.02 * 50) + (0.5 * 30)  # 1.0 + 15.0 = 16.0
    
    result = calculate_risk_score(weights, features)
    
    assert abs(result - expected) < 1e-9, f"Expected {expected}, got {result}"


def test_calculate_risk_score_realistic():
    """Test with realistic patient data."""
    weights = np.array([0.02, 0.5, 0.1, 5.0])
    features = np.array([75, 120, 80, 1])
    expected = 74.5  # Manually verified
    
    result = calculate_risk_score(weights, features)
    
    assert abs(result - expected) < 1e-9


def test_calculate_risk_score_dimension_mismatch():
    """Test that dimension mismatch raises ValueError."""
    weights = np.array([0.02, 0.5, 0.1])
    features = np.array([75, 120])
    
    with pytest.raises(ValueError, match="Dimension mismatch"):
        calculate_risk_score(weights, features)


def test_calculate_magnitude_classic():
    """Test magnitude with the classic 3-4-5 triangle."""
    vector = np.array([3, 4])
    expected = 5.0
    
    result = calculate_magnitude(vector)
    
    assert abs(result - expected) < 1e-9


def test_calculate_magnitude_zero_vector():
    """Test that zero vector has magnitude 0."""
    vector = np.array([0, 0, 0])
    
    result = calculate_magnitude(vector)
    
    assert result == 0.0


def test_normalize_vector_basic():
    """Test that normalized vector has magnitude 1."""
    vector = np.array([3, 4])
    
    normalized = normalize_vector(vector)
    magnitude = calculate_magnitude(normalized)
    
    assert abs(magnitude - 1.0) < 1e-9
    # Verify direction is preserved (scaled version)
    assert np.allclose(normalized, np.array([0.6, 0.8]))


def test_normalize_vector_zero_raises_error():
    """Test that normalizing zero vector raises ValueError."""
    vector = np.array([0, 0])
    
    with pytest.raises(ValueError, match="Cannot normalize zero vector"):
        normalize_vector(vector)
