from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def register():
	print("---Register---")
	username = input("Username : ")
	password = input("Mot de passe : ")

	database_handler.create_person(username, password)
	menu_connected()

def login():
	print("---Login---")
	username = input("Username : ")
	password = input("Mot de passe : ")

	if database_handler.user_exists_with(username) and password == database_handler.password_for(username):
		menu_connected()
	else:
		print("Nom d'utilisateur/mot de passe incorrect.")

def menu_connected():
	while True:
		print("Vous êtes connecté à votre compte TitouGame")
		print("1. Se deconnecter")

		choix = int(input())
		if choix == 1:
			return

def menu_not_connected():
	while True:
		print("Bienvenue sur TitouGame ! (non connecté)")
		print("Choisissez une option")
		print("1. Login")
		print("2. S'enregistrer")
		choix = int(input())

		if choix == 2:
			register()
		if choix == 1:
			login()

menu_not_connected()