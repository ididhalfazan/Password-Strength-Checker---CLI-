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
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    parser = argparse.ArgumentParser(description="Password Strength Checker CLI")
    parser.add_argument(
        "--password",
        type=str,
        help="Password to evaluate"
    )

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
    logging.info(f"Password evaluated | Score: {result['score']} | Strength: {result['strength']}")


if __name__ == "__main__":
    main()