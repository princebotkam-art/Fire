import os, platform, time, sys

# ================= AUTO-INSTALLER =================
def install_requirements():
    packages = ['requests', 'bs4', 'faker', 'fake_email']
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            print(f"\033[1;93m[!] Installing {pkg}...\033[0m")
            os.system(f"pip install {pkg}")

# ================= MAIN RUNNER =================
def main():
    # 1. Requirements Check
    install_requirements()

    # 2. WhatsApp group open karega
    print("\033[1;92m[✓] JOINING WHATSAPP GROUP...\033[0m")
    os.system('termux-open-url https://chat.whatsapp.com/DFj8atKbJZYE1zc68YMnvK?mode=gi_t > /dev/null 2>&1 &')
    time.sleep(3)

    # 3. Architecture check
    bit = platform.architecture()[0]

    if bit == '64bit':
        try:
            # Python ko current folder se import karne ka signal dena
            sys.path.append(os.getcwd())
            
            print("\033[1;92m[✓] LOADING KING BINARY...\033[0m")
            import king
            
            # Script ko start karna (akash function se)
            king.akash()
            
        except ImportError as e:
            print(f"\n\033[1;91m[!] Error: king.so file nahi mili! ({e})")
            print("\033[1;93mCheck karein ki king.so isi folder mein hai.\033[0m")
        except Exception as e:
            print(f"\n\033[1;91m[!] Script crash ho gayi: {e}")
            
    elif bit == '32bit':
        print('\033[1;97m[✓] \033[1;91mSORRY BRO YOUR DEVICE IS 32 BIT')
        print('\033[1;97m[✓] \033[1;91mPLEASE USE 64 BIT DEVICE')
        sys.exit()
    else:
        print('\033[1;97m[!] \033[1;91mUnknown Architecture')
        sys.exit()

if __name__ == "__main__":
    main()
