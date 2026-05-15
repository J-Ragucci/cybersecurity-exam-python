def calcola_risk_score(threat_level, vulnerability_level, asset_value):
    # Mappiamo i livelli testuali in numeri (1-10)
    punteggi = {
        "basso": 2,
        "medio": 5,
        "alto": 10,
        "critico": 50  # Un asset critico pesa tantissimo
    }

    # Recuperiamo i valori numerici (default a 1 se non trovato)
    t = punteggi.get(threat_level.lower(), 1)
    v = punteggi.get(vulnerability_level.lower(), 1)
    a = punteggi.get(asset_value.lower(), 1)

    risk_score = t * v * a
    return risk_score


# Scenario 1: Server Pubblico (Alto rischio attacco) con vulnerabilità media, dati poco importanti
score_1 = calcola_risk_score("alto", "medio", "basso")
# Calcolo: 10 * 5 * 2 = 100

# Scenario 2: Server Interno (Bassa minaccia) con vulnerabilità alta, ma contiene i brevetti (Critico)
score_2 = calcola_risk_score("basso", "alto", "critico")
# Calcolo: 2 * 10 * 50 = 1000

print(f"Rischio Scenario 1: {score_1}")
print(f"Rischio Scenario 2: {score_2}")

if score_2 > score_1:
    print("PRIORITÀ: Bisogna patchare subito il Server Interno (Scenario 2)!")