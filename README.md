# ChaCha20Decoder
ChaCha20Decoder permet de déchiffrer un message chiffré à partir des mêmes constantes qu'un autre message (plus long), dont on connaît la forme chiffrée et déchiffrée. Cette attaque est connue sous le nom two-time pad.
Un article expliquant le procédé plus en détail est disponible à l'adresse suivante : https://0cmenog.github.io/posts/ChaCha20/.

ChaCha20Decoder dispose de 3 modes : 
1. Mode 1 : Retrouver le keystream à partir du message en clair et son message chiffré associé
```python
python ChaCha20Decoder.py --plaintext "HELLO WORLD" --ciphertext 0x574f4b495e21335416515a
> Keystream : 0x1f0a07051101641b441d1e
```

2. Mode 2 : Retrouver le message en clair à partir de son message chiffré associé et son keystream
```python
python ChaCha20Decoder.py --decrypt 0x4b4f5451 --keystream 0x1f0a070504010203040506
> Message déchiffré : TEST
```

3. Mode 3 : Retrouver le message en clair à partir de son message chiffré associé, un message en clair et son message chiffré associé, généré à partir des mêmes constantes
```python
python ChaCha20Decoder.py --plaintext "HELLO WORLD" --ciphertext 0x574f4b495e21335416515a --decrypt 0x4b4f5451
> Message déchiffré : TEST
```