from zipfile import ZipFile

zip_path = "enc.zip"
wordlist_path = "rockyou.txt"

def main():
    with ZipFile(zip_path) as zf:
        with open(wordlist_path, "rb") as f:
            for line in f:
                password = line.strip()

                try:
                    zf.extractall(pwd=password)
                    print(f"[+] Success! Password is: {password.decode(errors='ignore')}")
                    return
                except:
                    continue

    print("[-] Password not found")

if __name__ == "__main__":
    main()
    
    
