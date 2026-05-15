blacklisted_password = ["admin", "qwerty", "1234"]
def check_password_policy(password):
    if len(password) < 8:
        return False, "Errore, la password è troppo corta!"
    if password.lower() in blacklisted_password:
        return False, "Errore, la password è nella blacklist!"
    return True, "Password accettata"

password = input("Inserisci la tua passwor, per verificare la sua validità: " )
esito, messaggio = check_password_policy(password)
print(f"Esito: {esito}, Messaggio: {messaggio}")