import string
import secrets
import time
import datetime

RED = "\033[31m"
RESET = "\033[0m"

def display_header():
    header = r"""
███╗   ███╗██████╗ ██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
████╗ ████║██╔══██╗██╔══██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██╔████╔██║██║  ██║██████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██║╚██╔╝██║██║  ██║██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚═╝ ██║██████╔╝██║         ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝╚═════╝ ╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
by discord : 6azd
"""
    print(RED + header + RESET)

def generate_password(length=16, use_symbols=True):
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

def save_password(label, pwd):
    try:
        with open("passwords.txt", "a", encoding="utf-8") as f:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{current_date}] {label}: {pwd}\n")
        print(f"\n{RED}[+] Password saved to 'passwords.txt'{RESET}")
    except Exception as e:
        print(f"\n[!] Error: {e}")

def main():
    display_header()
    print(f"{RED}Password Generator - Save System Active{RESET}\n")
    
    while True:
        try:
            length = int(input(f"{RED}Password length? : {RESET}"))
            if length < 4:
                print("Minimum 4 characters required.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    symbol_choice = input(f"{RED}Include symbols? (y/n) : {RESET}").lower()
    use_symbols = symbol_choice in ['y', 'yes']
    
    generated_pwd = generate_password(length, use_symbols)
    
    print("\n" + RED + "="*50)
    print(f"PASSWORD: {generated_pwd}")
    print("="*50 + RESET + "\n")
    
    should_save = input(f"{RED}Save password? (y/n) : {RESET}").lower()
    if should_save in ['y', 'yes']:
        service_name = input(f"{RED}Service name: {RESET}")
        if not service_name:
            service_name = "Unnamed Service"
        save_password(service_name, generated_pwd)
    
    print(f"\n{RED}Goodbye!{RESET}")

if __name__ == "__main__":
    main()
