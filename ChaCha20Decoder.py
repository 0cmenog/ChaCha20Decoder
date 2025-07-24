import argparse

def xor_bytes(b1: bytes, b2: bytes) -> bytes:
    # b1i ^ b2i, b1j ^ b2j, ...
    return bytes(a ^ b for a, b in zip(b1, b2))

def hexstr_to_bytes(hex_str: str) -> bytes:
    hex_str = hex_str[2:] if hex_str.startswith("0x") else hex_str
    if len(hex_str) % 2 != 0:
        hex_str = "0" + hex_str
    return bytes.fromhex(hex_str)

def to_hex(b: bytes) -> str:
    return "0x" + b.hex()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--plaintext", help="Message en clair")
    parser.add_argument("--ciphertext", help="Message chiffré dont le message en clair associé est à disposition (hexadécimal)")
    parser.add_argument("--keystream", help="Keystream (hexadécimal)")
    parser.add_argument("--decrypt", help="Message chiffré à déchiffrer (hexadécimal)")

    args = parser.parse_args()

    # Mode 1 : plaintext ⊕ ciphertext = keystream
    if args.plaintext and args.ciphertext and not args.keystream and not args.decrypt:
        plaintext_bytes = args.plaintext.encode('utf-8')
        ciphertext_bytes = hexstr_to_bytes(args.ciphertext)
        keystream = xor_bytes(plaintext_bytes, ciphertext_bytes)
        print("Keystream :", to_hex(keystream))

    # Mode 2 : decrypt ⊕ keystream = decrypted
    elif args.decrypt and args.keystream and not args.plaintext and not args.ciphertext:
        decrypt_bytes = hexstr_to_bytes(args.decrypt)
        keystream_bytes = hexstr_to_bytes(args.keystream)
        decrypted = xor_bytes(decrypt_bytes, keystream_bytes)
        try:
            print("Message déchiffré :", decrypted.decode('utf-8'))
        except UnicodeDecodeError:
            print("Message déchiffré (non UTF-8) :", to_hex(decrypted))

    # Mode 3 : Mode 1 + Mode 2 -> decrypted
    elif args.plaintext and args.ciphertext and args.decrypt:
        plaintext_bytes = args.plaintext.encode('utf-8')
        ciphertext_bytes = hexstr_to_bytes(args.ciphertext)
        decrypt_bytes = hexstr_to_bytes(args.decrypt)

        # La longueur du plaintext et du ciphertext associé restent identiques après chiffrement
        keystream = xor_bytes(plaintext_bytes, ciphertext_bytes)
        # Si le keystream est plus long que le message à déchiffrer, le message sera déchiffré entièrement
        # Si le message est plus long que le keystream, le message sera déchiffré de la longueur du keystream
        decrypted = xor_bytes(decrypt_bytes[:len(keystream)], keystream[:len(decrypt_bytes)])
        try:
            print("Message déchiffré :", decrypted.decode('utf-8'))
        except UnicodeDecodeError:
            print("Message déchiffré (non UTF-8) :", to_hex(decrypted))

    else:
        print("Indiquer : \n1. Plaintext et ciphertext -> keystream\n2. Decrypt et keystream -> decrypted\n3. Plaintext, ciphertext et decrypt -> decrypted\n")
        parser.print_help()

if __name__ == "__main__":
    main()
