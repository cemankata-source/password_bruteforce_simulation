import string
import time
import itertools

target_password = "sem12"

def brute_force():
    charset = string.ascii_lowercase + string.digits
    attempt = 0
    start = time.time()
    
    for length in range(1, len(target_password) + 1):
        for guess in itertools.product(charset, repeat = length):
            attempt += 1
            guess_pass = "".join(guess)
            
            if attempt % 500000 == 0:
                   print(f"[INFO] trying {attempt} times...")
            
            if guess_pass == target_password:
                end = time.time()
                print("password found!!: ", guess_pass)
                print("attempt: ", attempt)
                print("time", round(end - start, 3), "s")
                return
 

brute_force()       