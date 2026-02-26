🔐 Password Strength Checker CLI

A simple, modular Password Strength Checker CLI built with Python.

This project demonstrates:

Git & GitHub workflow

Virtual environments

Environment variables

Logging

Unit testing (pytest)

Docker containerization

🚀 Features

Checks:

Minimum length

Uppercase letters

Lowercase letters

Numbers

Special characters

Returns:

Strength score (0–5)

Strength classification (Weak / Medium / Strong)

Improvement suggestions

Logs results to a file

Configurable via .env

Docker-ready

📂 Project Structure
securepass-cli/
│
├── app/
│ ├── **init**.py
│ ├── checker.py
│
├── tests/
│ └── test_checker.py
│
├── main.py
├── requirements.txt
├── .env
├── Dockerfile
├── .gitignore
└── README.md
⚙️ Setup (Local Development)
1️⃣ Clone the repository
git clone https://github.com/ididhalfazan/Password-Strength-Checker---CLI-
cd pwstrength
2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate # Mac/Linux
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Running the Application
Option 1 – Hidden password input
python main.py

You will be prompted securely.

Option 2 – Pass password as argument
python main.py --password "MyPass123!"
📄 Environment Variables

The .env file controls configuration:

MIN_PASSWORD_LENGTH=8
LOG_LEVEL=INFO

You can change minimum password length without modifying code.

📝 Logging

All evaluations are logged in:

app.log

To view logs:

cat app.log

Live view:

tail -f app.log

Note: The actual password is never logged for security reasons.

🧪 Running Tests

Install pytest (if not installed):

pip install pytest

Run tests:

pytest
🐳 Running with Docker
1️⃣ Build the Docker image
docker build -t securepass .
2️⃣ Run interactively
docker run -it securepass
3️⃣ Run with password argument
docker run securepass --password "MyPass123!"
4️⃣ Override environment variables in Docker
docker run -it \
-e MIN_PASSWORD_LENGTH=12 \
-e LOG_LEVEL=DEBUG \
securepass
🎯 Why This Project?

This project demonstrates:

Clean modular architecture

Separation of concerns

Configuration management via environment variables

Logging best practices

Containerization with Docker

Test-driven validation

🔮 Future Improvements

Entropy-based scoring

Common password blacklist

Colorized CLI output

CI/CD with GitHub Actions

Publish Docker image to Docker Hub

👤 Author

Azan Zaman
