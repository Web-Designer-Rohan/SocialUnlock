import time
import random
import sys
import os
import json

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def instagram_password_cracker():
    clear_screen()

    # Use a triple-quoted raw string to preserve all backslashes
    ascii_art = r"""
 _____ _____ _____ _____ _____
|  __ \  _  |  _  |  _  |  _  |
| |  \/ | | | | | | | | | | | |
| | __| | | | | | | | | | | | |
| |_\ \ \_/ | \_/ | \_/ | \_/ |
 \____/\___/ \___/ \___/ \___/ 
"""

    # Print the ASCII art in magenta, then reset color, and flush immediately
    print("\033[95m" + ascii_art + "\033[0m", flush=True)

    print("\033[94mSelect Cracking Tool:\033[0m", flush=True)
    print("1. Brute-force attack", flush=True)
    print("2. Dictionary attack (Simulated)", flush=True)
    print("3. Rainbow table lookup (Simulated)", flush=True)
    choice = input("Enter tool number: ")

    if choice == "1":
        username = input("Enter username: ")
        account_name = input("Enter account name: ")
        account_url = input("Enter account URL: ")
        password_list_path = input("Enter path to password list (Simulated): ")

        clear_screen()

        # Reprint ASCII art (with correct escaping) for consistency
        print("\033[95m" + ascii_art + "\033[0m", flush=True)
        print(f"\033[94mInitiating Brute-force attack on {username}...\033[0m", flush=True)
        time.sleep(1)

        start_time = time.time()
        while time.time() - start_time < 5:  # shortened for demo
            print("\033[91m[ERROR] Firewall detected. Attempting bypass...\033[0m", flush=True)
            time.sleep(1)

        sql_php_permission = input("Allow SQL and PHP injection? (y/n): ")
        if sql_php_permission.lower() != "y":
            print("\033[91mCracking stopped.\033[0m", flush=True)
            return

        start_time = time.time()
        while time.time() - start_time < 5:  # shortened for demo
            print("\033[93mTrying to pass the firewall...\033[0m", flush=True)
            time.sleep(1)

        print("\033[92mFirewall passed! Decrypting password...\033[0m", flush=True)

        # Fake password generation
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password_length = random.randint(8, 16)
        fake_password = "".join(random.choice(characters) for _ in range(password_length))

        # Simulate a progress bar
        for i in range(100):
            progress = i + 1
            bar_length = 40
            filled_length = int(bar_length * progress / 100)
            bar = '\033[92m' + '█' * filled_length + '-' * (bar_length - filled_length) + '\033[0m'
            percent = (progress / 100) * 100
            print(f"[{bar}] {percent:.1f}%", end="\r", flush=True)
            time.sleep(0.02)  # faster for demo
        print("\n", flush=True)

        # Fake hash
        fake_hash = "".join(random.choice(characters) for _ in range(64))
        print(f"\033[92mPassword hash: {fake_hash}\033[0m", flush=True)

        data = {
            "username": username,
            "account_name": account_name,
            "account_url": account_url,
            "password": fake_password,
            "hash": fake_hash
        }

        with open("cracked_credentials.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Credentials saved to cracked_credentials.json", flush=True)

        hash_crack_choice = input("Would you like to hash crack the password? (y/n): ")
        if hash_crack_choice.lower() == "y":
            print("Hash cracking not implemented in this example.", flush=True)

    else:
        print("Simulated cracking methods not implemented in this example.", flush=True)

if __name__ == "__main__":
    instagram_password_cracker()
