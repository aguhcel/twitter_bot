#############################################################
#   Bot para hacer comentarios random sobre las tendencias  #
#############################################################
import tweepy
from time import sleep
from random import randrange
# Acceso a Twitter
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")

auth.set_access_token("access_token", "access_token_secret")
# Creando el objeto API
api = tweepy.API(auth)

# Iniciamos una lista con comentarios graciosos que se te ocurran
comentarios = ['Viva AMLO ', "Mi abuelita decia que ", "Todos soñamos con ", "Me prende que digan ",
               "Ya no tengo miedo de ", "De eso se murio mi tio ", "Se tenia que decir y se dijo ",
               "Come tierra y ", "Yo lo habia pensado desde antes "]

# Obtenemos las tendencias de nuestro pais, nuestra API consume la API WOEID (a Yahoo! Where On Earth ID)
# Lo puedes hacer con api.trends_aviable() y preparate para buscar un rato, en mi caso uso la de Ciudad de México
# que es el ID: 23424900

try:
    while True:
        mexico = api.trends_place(id = 23424900)[0]['trends']
        # Pasamos las tendencias de México a una lista
        trends = [dato['name'] for dato in mexico]
        rand_com = randrange(len(comentarios))
        rand_ten = randrange(len(trends))
        api.update_status(comentarios[rand_com] + trends[rand_ten])
        print(comentarios[rand_com] + trends[rand_ten])
        sleep(60*30)
except KeyboardInterrupt:
    print("Me matas...!!!!\nCtrl-C")
    pass
