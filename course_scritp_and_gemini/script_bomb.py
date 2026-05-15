import os
import time

# Simuliamo un database di dipendenti attivi recuperato dal sistema HR
dipendenti_attivi = ["Mario_Rossi", "Luca_Bianchi", "Giulia_Verdi", "Admin_Cattivo"]


def logic_bomb_check(mio_utente):
    print(f"[SYSTEM] Controllo presenza utente: {mio_utente}...")

    # L'impiegato controlla se è ancora nel sistema
    if mio_utente in dipendenti_attivi:
        print("[SYSTEM] Utente attivo. Nessuna azione intrapresa.")
        return False
    else:
        # SE l'utente non c'è più (è stato licenziato), scatta la bomba
        print(f"[ALLARME] L'utente {mio_utente} è stato rimosso! ATTIVAZIONE PAYLOAD.")
        return True


def esegui_sabotaggio():
    # Simulazione distruzione dati
    # In un caso reale: os.remove("/server/critical_data.db")
    print(">>> CANCELLAZIONE DATABASE IN CORSO...")
    print(">>> DISTRUZIONE BACKUP...")
    print(">>> Danno completato.")


# --- SIMULAZIONE ---
mio_nome = "Admin_Cattivo"

# Giorno 1: Tutto ok
logic_bomb_check(mio_nome)

print("-" * 30)

# Giorno 2: L'azienda licenzia l'admin e lo toglie dalla lista
dipendenti_attivi.remove("Admin_Cattivo")  # Simuliamo il licenziamento

# Lo script gira di nuovo (magari è pianificato ogni notte)
trigger = logic_bomb_check(mio_nome)
if trigger:
    esegui_sabotaggio()