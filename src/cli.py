"""
Command-line interface for Mortality Risk Estimator.
"""
import argparse
import sys
def main():
    """Main entry point for the CLI tool."""
    # Define the argument parser
    parser = argparse.ArgumentParser(
        description="Mortality Risk Estimator CLI - Week 1 Code Session"
    )
    # Define command-line arguments
    parser.add_argument(
        '--vector',
        required=True,
        type=str,
        help='Patient feature vector, e.g., "75,120,80,1"'
    )
    # Parse the arguments
    args = parser.parse_args()
    # Placeholder: confirm setup works
    print(f"CLI received input vector: {args.vector}")
if __name__ == "__main__":
    main()
