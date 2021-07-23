from hashlib import sha256

def senhar_segreda(texto):
    return sha256(texto.encode('ascii')).hexdigest()