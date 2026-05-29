# Password Analyzer — Secure Vault

I built this project to practice Python and web development while doing something actually useful — a tool that tells you whether your password is strong or not, and *why*.

There are two versions: a simple command-line script you can run in the terminal, and a proper web app with a UI built using Flask.

---

## What it does

You type in a password, and the tool will:

- Tell you if it passes the basic security requirements
- Give it a score out of 5
- Calculate the entropy (how unpredictable it actually is)
- Warn you if it's a commonly used password
- Tell you exactly what's missing if it doesn't pass

---

## Files

```
├── app.py              # The Flask web app
├── checker_cli.py      # The terminal version
├── templates/
│   └── index.html      # The web UI
└── 10-million-password-list-top-1000.txt  # Common passwords list
```

---

## What makes a password valid?

The tool checks for five things:

- At least one uppercase letter (A–Z)
- At least one lowercase letter (a–z)
- At least one number (0–9)
- At least one special character like `!`, `@`, `#`, `$`, etc.
- Length between 6 and 60 characters

All five need to pass for the password to be considered valid.

---

## How the score works

Each requirement above is worth 1 point, so the max score is 5.

- **1 or below** → Weak
- **2 to 4** → Fair
- **5** → Strong

---

## What's entropy and why does it matter?

Entropy measures how hard your password is to guess or brute-force. The longer your password and the more variety of characters it uses, the higher the entropy.

The formula used here is:

```
Entropy = length × log₂(charset size)
```

| Entropy | What it means |
|---|---|
| Under 28 bits | Very Weak |
| 28–35 bits | Weak |
| 36–59 bits | Reasonable |
| 60–127 bits | Strong |
| 128+ bits | Very Strong |

---

## How to run it

### You'll need

- Python 3
- Flask → install it with `pip install flask`
- The common passwords file saved at `10-million-password-list-top-1000.txt`
  (or update the path in the code to wherever you saved it)

---

### Terminal version

```bash
python3 checker_cli.py
```

It'll ask for your name and password, then print the result straight away.

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

---

### Web app version

```bash
python3 app.py
```

Then open your browser and go to `http://127.0.0.1:5000`

> Make sure `index.html` is inside a folder called `templates/` next to `app.py` — Flask won't find it otherwise.

---

## The web UI

The frontend has a cyberpunk-style design and gives you real-time results after you click Analyze. You'll see:

- A strength meter that fills up based on your score
- A checklist showing which requirements passed or failed
- Your entropy score and password length
- A warning if your password is on the common passwords list

You can also press **Enter** instead of clicking the button.

---

## A couple of things to note

- The common password check in `checker_cli.py` uses a loose match (`in`), which can sometimes flag a password incorrectly if its text appears anywhere inside the file. The web app uses an exact match, which is more accurate. Worth fixing if you continue developing this.
- The passwords list path is hardcoded in both files — just update the path if yours is saved somewhere different.

---

## Built with

- Python 3 + Flask
- HTML, CSS, JavaScript
- Shannon entropy formula from the `math` module
- Tabler Icons for the web UI

---

