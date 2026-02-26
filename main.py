"""
main.py

Entry point for the Password Strength Checker CLI application.

This module:
- Loads environment variables for configuration.
- Configures application logging.
- Parses command-line arguments.
- Accepts password input securely if not provided via CLI.
- Evaluates password strength using the evaluate_password function.
- Displays a formatted strength report.
- Logs evaluation results (without logging the actual password).

Environment Variables:
    MIN_PASSWORD_LENGTH (int): Minimum required password length.
                               Default is 8 if not provided.
    LOG_LEVEL (str): Logging level (e.g., DEBUG, INFO, WARNING).
                     Default is INFO.

Security Note:
    The application never logs the actual password.
"""

import argparse
import logging
import os
from getpass import getpass
from dotenv import load_dotenv

from app.checker import evaluate_password

# Load environment variables
load_dotenv()
MIN_LENGTH = int(os.getenv("MIN_PASSWORD_LENGTH", 8))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


# Configure logging
logging.basicConfig(
    level=LOG_LEVEL,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    """
    Main entry point for the Password Strength Checker CLI.

    This function:
    1. Parses optional command-line arguments.
    2. Accepts password input either via:
        - --password argument
        - Secure interactive prompt (hidden input)
    3. Evaluates password strength using configured minimum length.
    4. Prints a structured strength report.
    5. Logs evaluation metadata (excluding the actual password).

    Command-Line Arguments:
        --password (str, optional):
            Password to evaluate. If not provided,
            the user will be prompted securely.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Password Strength Checker CLI")
    parser.add_argument("--password", type=str, help="Password to evaluate")

    args = parser.parse_args()

    # If password not provided as argument, ask securely
    if args.password:
        password = args.password
    else:
        password = getpass("Enter password: ")

    result = evaluate_password(password, MIN_LENGTH)

    print("\n--- Password Strength Report ---")
    print(f"Score: {result['score']}/5")
    print(f"Strength: {result['strength']}")

    if result["suggestions"]:
        print("\nSuggestions:")
        for suggestion in result["suggestions"]:
            print(f"- {suggestion}")

    # Log evaluation (never log actual password)
    logging.info(
        f"Password evaluated | Score: {result['score']} | Strength: {result['strength']}"
    )


if __name__ == "__main__":
    main()
