import hashlib


def calcola_hash_file(percorso_file):
    # Usiamo SHA256 come raccomandato dalle slide (MD5 è insicuro)
    lo_sha256 = hashlib.sha256()

    try:
        with open(percorso_file, "rb") as f:
            # Leggiamo a blocchi di 4096 byte per non intasare la RAM [cite: 1282]
            for blocco in iter(lambda: f.read(4096), b""):
                lo_sha256.update(blocco)
        return lo_sha256.hexdigest()
    except FileNotFoundError:
        return None


# --- SIMULAZIONE SCENARIO ---
# Immagina di aver scaricato due file: "ubuntu_originale.iso" e "ubuntu_hackerato.iso"
# Creiamo due file finti per l'esempio
with open("doc_legittimo.txt", "w") as f: f.write("Contratto v1.0")
with open("doc_fake.txt", "w") as f: f.write("Contratto v1.0 con Backdoor")  # Basta un carattere diverso

# 1. Calcoliamo gli hash (le impronte digitali)
hash_legittimo = calcola_hash_file("doc_legittimo.txt")
hash_fake = calcola_hash_file("doc_fake.txt")

print(f"Hash File 1: {hash_legittimo}")
print(f"Hash File 2: {hash_fake}")

# 2. Controllo Integrità
if hash_legittimo == hash_fake:
    print("ESITO: I file sono identici. Integrità confermata.")
else:
    print("ESITO: ALLARME! I file sono diversi. Integrità compromessa!")