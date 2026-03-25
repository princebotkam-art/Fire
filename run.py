import os, platform, time, sys

# 1. WhatsApp group open karega (Background mein)
os.system('termux-open-url https://chat.whatsapp.com/HSzqBbaohKt01fOQYrfraZ > /dev/null 2>&1 &')
time.sleep(2)

# 2. Architecture check
bit = platform.architecture()[0]

if bit == '64bit':
    try:
        # Current folder ko path mein add karna
        sys.path.append(os.getcwd())
        
        print("\033[1;92m[✓] LOADING DONN BINARY...\033[0m")
        import donn
        
        # Aapka main function start karna
        donn.akash()
        
    except ImportError as e:
        print(f"\n\033[1;91m[!] Error: donn.so file nahi mili! ({e})")
    except Exception as e:
        print(f"\n\033[1;91m[!] Script crash ho gayi: {e}")
        
elif bit == '32bit':
    print('\033[1;91m[!] SORRY BRO YOUR DEVICE IS 32 BIT')
    sys.exit()
else:
    print('\033[1;91m[!] Unknown Architecture')
    sys.exit()
