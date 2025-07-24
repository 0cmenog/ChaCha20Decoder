import subprocess

def run_command(args):
    print(f"Commande : {' '.join(args)}")
    result = subprocess.run(args, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

# Valeurs de base
plaintext  = "HELLO WORLD"
keystream  = "0x1f0a070504010203040506"
ciphertext = "0x574f4b495e21335416515a"
decrypt    = "0x4b4f5451"

# Chemin vers le script
decoder_script = "ChaCha20Decoder.py"

# Test mode 1 : plaintext ⊕ ciphertext -> keystream
run_command([
    "python", decoder_script,
    "--plaintext", plaintext,
    "--ciphertext", ciphertext
])

# Test 2 : decrypt ⊕ keystream -> decrypted
run_command([
    "python", decoder_script,
    "--decrypt", decrypt,
    "--keystream", keystream
])

# Test 3 : plaintext + ciphertext + decrypt -> decrypted
run_command([
    "python", decoder_script,
    "--plaintext", plaintext,
    "--ciphertext", ciphertext,
    "--decrypt", decrypt
])
