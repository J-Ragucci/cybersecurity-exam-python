import hashlib

def calcola_hash(percorso):
    sha256 = hashlib.sha256()
    try:
        with open(percorso, "rb") as f:
            for blocco in iter(lambda: f.read(4096), b""):
                sha256.update(blocco)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

# Simulazione
iso_originale = calcola_hash("ubuntu.iso")
iso_modificata = calcola_hash("ubutu_modificato.iso")
if iso_originale == iso_modificata:
    print("Il file non è stato modificato, l'integrity è stata mantenuta")
else:
    print("il file è stato modificato, rimuovere il file con os.remove(ubuntu_modificato.iso")