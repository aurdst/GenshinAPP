from twilio.rest import Client

# Créez un compte Twilio et obtenez votre numéro de compte SID et votre clé d'authentification
account_sid = ""
auth_token = ""

# Initialisez un client Twilio
client = Client(account_sid, auth_token)

# Envoyez le SMS
message = client.messages \
                .create(
                     body="Félicitation, ceci est un message de confirmation pour ta participation voici ton code Paypal d'une valeur de 50€ : GDF8MLVX.",
                     from_="NumberTwilio",
                     to="+"
                 )

# Affichez le résultat
print(message.sid)
