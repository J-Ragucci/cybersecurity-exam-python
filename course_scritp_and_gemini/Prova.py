import hashlib

def chech_hash_file(percorso_file):
    with open (percorso_file, "rb") as f:
        h1 = hashlib.sha256()
        for (labda x : f.read(4096))
