import os

def send_sms(number, message):
    os.system(f"termux-sms-send -n {number} {message}")

number = input("Inserisci il numero di telefono: ")
message = input("Inserisci il messaggio: ")

send_sms(number, message)
