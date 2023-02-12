from twilio.rest import Client

# Créez un compte Twilio et obtenez votre numéro de compte SID et votre clé d'authentification
account_sid = "AC10d84daf93f63eab079d7e542214db67"
auth_token = "4454a73f1c055d52c277a6bde5be4c07"

# Initialisez un client Twilio
client = Client(account_sid, auth_token)

# Envoyez le SMS
message = client.messages \
                .create(
                     body="Félicitation, ceci est un message de confirmation pour ta participation voici ton code Paypal d'une valeur de 50€ : GDF8MLVX.",
                     from_="NumberTwilio",
                     to="+33610423765"
                 )

# Affichez le résultat
print(message.sid)