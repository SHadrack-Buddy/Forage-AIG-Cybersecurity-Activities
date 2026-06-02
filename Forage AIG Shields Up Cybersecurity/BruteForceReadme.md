# ZIP Password Brute Force Tool (Educational Use)

## Overview

This Python script demonstrates how a dictionary-based password attack can be performed against a password-protected ZIP file using a wordlist (such as `rockyou.txt`).

It is intended strictly for **educational and cybersecurity training purposes**, such as understanding password strength, encryption limitations, and brute-force attack concepts.

---

## ⚙️ How It Works

The script performs the following steps:

1. Opens an encrypted ZIP file (`enc.zip`)
2. Loads a password list (`rockyou.txt`)
3. Reads each password candidate line-by-line
4. Attempts to extract the ZIP file using each password
5. Stops when the correct password is found

---

## 🧠 Key Components

### `attempt_extract(zf_handle, password)`
- Tries to extract all files from the ZIP using the provided password
- Returns:
  - `True` → if extraction succeeds (correct password)
  - `False` → if extraction fails

---

### `main()`
- Loads the ZIP file and password list
- Iterates through each password in `rockyou.txt`
- Strips newline characters from each password
- Tests each password using `attempt_extract()`
- Prints whether each password is correct or incorrect
- Stops execution once the correct password is found

---

## 📂 Requirements

- Python 3.x
- Built-in module: `zipfile`
- Files required:
  - `enc.zip` (password-protected ZIP file)
  - `rockyou.txt` (password wordlist)

---

## ▶️ How to Run

```bash
python bruteforce.py