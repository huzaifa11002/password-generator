# SecurePass - Password Generator & Strength Checker

## Overview
SecurePass is a Streamlit-based application that not only generates strong and secure passwords but also provides a strength-checking feature. It is a user-friendly tool that offers randomly generated passwords and evaluates their security.

## Features
- **Password Generator**: Option to generate secure passwords.
- **Strength Checker**: Analyzes password security and suggests improvements.
- **Customization**: Allows selection of password length and character types.
- **User-Friendly UI**: Simple and interactive interface.

## Tech Stack
- **Python**
- **Streamlit** (Frontend UI)
- **Custom Modules** (For password generation and strength checking)
- **Unified Virtualenv (UV)** (For project environment)

## Installation
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd securepass
   ```

2. **Set up the environment (using UV)**
   ```bash
   uv venv env
   source env/bin/activate  # (For Windows: env\Scripts\activate)
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## Usage
1. **Password Generator**:
   - Select the "Password Generator" tab.
   - Set password length and additional options (digits, symbols).
   - Click the "Generate Password" button.
   - Your secure password will be generated.

2. **Strength Checker**:
   - Select the "Check Strength" tab.
   - Enter your password.
   - Click the "Check" button to analyze your password strength.

## Live Demo
If you want to try SecurePass without installing it, visit:
[Live App](https://password-generator-huzaifa.streamlit.app/)

## Contribution
If you want to contribute to this project or suggest improvements, feel free to raise a pull request or an issue.

## License
This project is open-source and distributed under the [MIT License](LICENSE).

---
Made with ❤️ using Streamlit

