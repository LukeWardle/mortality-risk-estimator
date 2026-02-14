"""
Command-line interface for Mortality Risk Estimator.


This module orchestrates input parsing, mathematical computation,
and output formatting for the mortality risk calculator.
"""
import argparse
import sys
from src.io_parser import parse_vector_input
from src.math_ops import calculate_risk_score, calculate_magnitude


def main():
    """
    Main entry point for the Mortality Risk Estimator CLI.
    
    Parses command-line arguments, performs risk calculation,
    and displays results in a formatted manner.
    """
    # 1. Define argument parser
    parser = argparse.ArgumentParser(
        description="Mortality Risk Estimator - Week 1 Code Session",
        epilog="Example: python src/cli.py --vector '75,120,80,1' --weights '0.02,0.5,0.1,5'"
    )
    # 2. Define arguments
    parser.add_argument(
        '--vector',
        required=True,
        type=str,
        help='Patient feature vector: age,systolic_bp,diastolic_bp,smoker (e.g., "75,120,80,1")'
    )
    parser.add_argument(
        '--weights',
        required=True,
        type=str,
        help='Model weight vector (same length as feature vector, e.g., "0.02,0.5,0.1,5")'
    )
    # 3. Parse arguments
    args = parser.parse_args()
    try:
        # 4. Parse string inputs to NumPy arrays
        feature_vector = parse_vector_input(args.vector)
        weight_vector = parse_vector_input(args.weights)
        # 5. Calculate risk score
        risk_score = calculate_risk_score(weight_vector, feature_vector)
        # 6. Calculate magnitudes (for additional insight)
        feature_magnitude = calculate_magnitude(feature_vector)
        weight_magnitude = calculate_magnitude(weight_vector)
        # 7. Display results
        print("="*60)
        print("MORTALITY RISK ESTIMATOR - CALCULATION RESULTS")
        print("="*60)
        print(f"\nInput Patient Features: {feature_vector}")
        print(f"Feature Vector Magnitude: {feature_magnitude:.4f}")
        print(f"\nModel Weights: {weight_vector}")
        print(f"Weight Vector Magnitude: {weight_magnitude:.4f}")
        print(f"\n{'─'*60}")
        print(f"CALCULATED RISK SCORE: {risk_score:.4f}")
        print(f"{'─'*60}")
        print("\nCalculation: risk_score = weights · features (dot product)")
        print("="*60)
    except ValueError as e:
        # Handle input parsing or dimension mismatch errors
        print(f"\nERROR: {e}", file=sys.stderr)
        print("\nPlease check your input format and try again.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"\nUNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()



