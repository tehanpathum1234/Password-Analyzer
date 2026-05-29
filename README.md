# 🔐 Password Analyzer — Secure Vault

A password strength checker that tells you whether your password is secure or not, and exactly why. There are two versions — a terminal script and a Flask web app.

---

## 📁 Project files

```
├── app.py                                      # Flask web app (backend)
├── checker_cli.py                              # Terminal version
├── templates/
│   └── index.html                              # Web UI frontend
└── 10-million-password-list-top-1000.txt       # Common passwords list
```

---

## What it does

- Checks if your password meets all the security requirements
- Scores it out of 5 based on what it contains
- Calculates entropy to measure how hard it would be to brute-force
- Warns you if your password appears in a common passwords list
- Tells you exactly what's missing if it doesn't pass

---

## What counts as a valid password?

Your password needs to meet all five of these:

| # | Requirement |
|---|---|
| 1 | At least one uppercase letter (A–Z) |
| 2 | At least one lowercase letter (a–z) |
| 3 | At least one digit (0–9) |
| 4 | At least one special character — `!`, `@`, `#`, `$`, etc. |
| 5 | Length between 6 and 60 characters |

If any of these are missing, the tool prints exactly which ones you need to fix.

---

## Scoring

Each requirement above is worth 1 point:

| Score | Rating |
|---|---|
| 0 – 1 | 🔴 Weak |
| 2 – 4 | 🟡 Fair |
| 5 / 5 | 🟢 Strong |

---

## Entropy

Entropy is calculated using:

```
Entropy = password length × log₂(charset size)
```

Charset size is built up based on which character types are present:

| Character type | Added to charset |
|---|---|
| Uppercase (A–Z) | +26 |
| Lowercase (a–z) | +26 |
| Digits (0–9) | +10 |
| Special characters | +32 |

| Entropy (bits) | Strength |
|---|---|
| Under 28 | Very Weak |
| 28 – 35 | Weak |
| 36 – 59 | Reasonable |
| 60 – 127 | Strong |
| 128 and above | Very Strong |

---

## 🚀 How to run it

### What you need

- Python 3
- Flask — `pip install flask`
- The common passwords file at:
  `/home/kali/Downloads/10-million-password-list-top-1000.txt`

  > If your file is saved somewhere else, update the path at the top of `app.py` and `checker_cli.py`.

---

### Terminal version

```bash
python3 checker_cli.py
```

It will ask for your name and password, then print the result.

**Example output:**
```
Enter your name : Pathum

Enter your Password : MyPass@99

Password is valid  :)

Score : 5
Password is Strong (Based on Score)

Entropy Calculation :
Password length: 9 characters
Entropy : 57.00 bits
Strength : Reasonable
```

If the password doesn't pass, it prints what's missing:
```
Your password is easy to break :(

- at least one uppercase letter (A-Z)
- at least one digit (0-9)
```

---

### Web app version

```bash
python3 app.py
```

Open your browser and go to `http://127.0.0.1:5000`

> The `index.html` file must be inside a folder called `templates/` in the same directory as `app.py`, otherwise Flask won't find it.

---

## Web UI

The frontend has a dark cyberpunk theme. After you enter your name and password and click **Analyze**, you get:

- A strength meter bar based on your score
- A checklist showing which requirements passed or failed
- Your entropy score and password length
- A warning if your password is found in the common list
- You can also press **Enter** instead of clicking the button

---

## ⚠️ Things to note

- The common password check in `checker_cli.py` uses a loose `in` match, so it might flag a password incorrectly if it appears as part of a longer string in the file. The web app uses an exact match. Worth fixing.
- The passwords file path is hardcoded in both scripts — update it if you're running this on a different machine.

---

## Built with

- Python 3 + Flask
- `math.log2()` for entropy calculation
- HTML
- Tabler Icons

---
