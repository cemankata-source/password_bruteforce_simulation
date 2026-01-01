# Password Bruteforce Simulation (v1)

This project is an educational simulation that demonstrates how password
length and character complexity affect resistance to brute-force attacks.
The program runs locally and does not target any real systems.

## Features
- Simulates brute-force attempts using lowercase letters and digits
- Automatically adjusts brute-force length based on target password
- Displays total attempts and time taken to crack the password
- Educational and ethical use only

## How It Works
1. A target password is defined in the code.
2. The program generates all possible character combinations.
3. Each combination is tested against the target password.
4. The program stops when the correct password is found.
5. Total attempts and time taken are displayed.

## How to Run
1. Make sure Python 3 is installed.
2. Clone this repository or download the file.
3. Open a terminal in the project folder.
4. Run the script:
   ```bash
   python brute_force_v1.py
5.Edit the target_password variable to test different passwords.

example output:
password found!!: aduh12
attempt:  217678234
time 12.314 s

Disclaimer

This project is for educational purposes only.
It demonstrates password security concepts in a controlled environment.
No real accounts or systems are targeted.
