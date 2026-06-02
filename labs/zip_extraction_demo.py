from zipfile import ZipFile

zip_path = "enc.zip"
output_dir = "output"

def main():
    print("[+] ZIP extraction demo")

    password = b"example_password"

    try:
        with ZipFile(zip_path) as zf:
            zf.extractall(path=output_dir, pwd=password)

        print("[+] Extraction successful")
    except:
        print("[-] Extraction failed")

if __name__ == "__main__":
    main()