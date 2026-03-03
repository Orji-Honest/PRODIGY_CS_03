 ## Password Complexity Checker
 
A Python-based command-line tool that evaluates password strength using multiple security criteria — built with cybersecurity best practices in mind.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Usage](#-usage)
- [Scoring System](#-scoring-system)
- [Cybersecurity Relevance](#-cybersecurity-relevance)
- [Project Structure](#-project-structure)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)

---

## 🧠 Overview

Weak passwords remain one of the top attack vectors in cybersecurity. This tool was built to help everyday users and developers understand what makes a password strong — and why it matters. It performs real-time static analysis of a password's structure and provides actionable feedback without ever storing or transmitting the password.

---

## ✨ Features

- **Multi-criteria strength analysis** — length, character variety, patterns
- **Scoring system** with a 9-point scale and four strength levels: `WEAK`, `MODERATE`, `STRONG`, `VERY STRONG`
- **Common pattern detection** — flags passwords containing `123`, `abc`, `qwerty`, `password`, `admin`, etc.
- **Sequential character detection** — identifies patterns like `abc`, `xyz`, `123`, `456`
- **Repeated character detection** — catches patterns like `aaa`, `111`
- **Visual feedback** with emoji indicators (🔴 🟡 🟢)
- **Password creation tips** built into the tool
- **No data storage** — the password never leaves your machine

---

## ⚙️ How It Works

The tool evaluates a password against seven core criteria:

| Criterion | Points |
|---|---|
| Length ≥ 8 characters | +1 |
| Length ≥ 12 characters | +1 |
| Length ≥ 16 characters | +1 |
| Contains lowercase letters | +1 |
| Contains uppercase letters | +1 |
| Contains numbers | +1 |
| Contains special characters | +2 |
| Common/predictable patterns detected | -1 |
| Sequential characters detected | -1 |

**Max possible score: 9**

Strength levels:
- 🔴 **WEAK** → Score 0–2
- 🟡 **MODERATE** → Score 3–5
- 🟢 **STRONG** → Score 6–7
- 🟢🟢 **VERY STRONG** → Score 8+

---

## 🛠 Installation

**Requirements:** Python 3.6 or higher. No third-party libraries needed — uses only the Python standard library.

```bash
# Clone the repository
git clone https://github.com/Orji-Honest/password-complexity-checker.git

# Navigate into the project folder
cd PRODIGY_CS_03

# Run the tool
python task03_password_checker.py
```

---

## 🚀 Usage

```bash
python task03_password_checker.py
```

You'll be presented with an interactive menu:

```
============================================================
PASSWORD COMPLEXITY CHECKER
============================================================

Options:
1. Check password strength
2. View password tips
3. Exit
```

**Example output for a weak password (`password123`):**
```
Strength: 🔴 WEAK
Score: 2/9

--- Detailed Analysis ---
  ✗ Too short (11 chars). Minimum 8 characters recommended
  ✓ Contains lowercase letters
  ✗ Missing uppercase letters
  ✓ Contains numbers
  ✗ Missing special characters
  ⚠ Contains common/predictable pattern
```

**Example output for a strong password (`C0ffee!Morning@2024`):**
```
Strength: 🟢🟢 VERY STRONG
Score: 9/9

--- Detailed Analysis ---
  ✓ Excellent length (16+ characters)
  ✓ Contains lowercase letters
  ✓ Contains uppercase letters
  ✓ Contains numbers
  ✓ Contains special characters (!@#$%^&* etc.)
```

---

## 🔒 Cybersecurity Relevance

This tool directly addresses real-world security concerns relevant to both defenders and ethical hackers:

**For Defenders (Blue Team):**
- Helps enforce password policy awareness during security training
- Can be integrated into onboarding or security awareness programs
- Educates users about why certain passwords fail in dictionary or brute-force attacks

**For Ethical Hackers & Penetration Testers (Red Team):**
- Understanding how password checkers score inputs helps testers evaluate how strong a target's password policy is
- Pattern detection logic mirrors what tools like `Hashcat` and `John the Ripper` exploit — sequential characters, common words, low entropy
- Useful for generating test cases to audit password validation implementations in applications

**Attack Vectors This Tool Helps Defend Against:**
| Attack Type | How This Tool Helps |
|---|---|
| **Brute Force** | Encourages longer passwords (exponentially harder to crack) |
| **Dictionary Attacks** | Flags common words and patterns (`password`, `admin`, `qwerty`) |
| **Credential Stuffing** | Tips section warns against password reuse |
| **Pattern-Based Cracking** | Detects and penalises sequential/repeated character patterns |

---

## 📁 Project Structure

```
password-complexity-checker/
│
├── task03_password_checker.py   # Main script
└── README.md                    # Project documentation
```

---

## 📚 What I Learned

Building this project deepened my understanding of several key areas:

- **Regex (Regular Expressions):** Used `re` module to detect character classes and common attack patterns
- **Password entropy concepts:** Why length and character variety increase the time-to-crack exponentially
- **Scoring system design:** Balancing rewarding good behaviour vs. penalising bad patterns
- **Security UX:** Making security feedback understandable and actionable for non-technical users
- **Cybersecurity mindset:** Thinking like an attacker to decide *what* patterns to flag

---

## 🔮 Future Improvements

- [ ] Add entropy calculation (bits of entropy per password)
- [ ] Integrate with [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) to check if password appears in known breach databases
- [ ] Add a passphrase generator
- [ ] Build a web-based GUI version (Flask/Django)
- [ ] Add support for custom organisation password policy rule
> **⚠️ Disclaimer:** This tool is built for educational purposes and personal security awareness. It performs static analysis only and does not guarantee protection against all attack vectors. Always use a reputable password manager for generating and storing passwords securely.

---

*Built with ❤️ and a passion for cybersecurity.*
