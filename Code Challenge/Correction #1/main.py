from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")

def register():
	print("---Register---")
	username = input("Username : ")
	password = input("Mot de passe : ")
	age = input("Age : ")

	database_handler.create_person(username, password, age)


def menu_not_connected():
	while True:
		print("Bienveenue sur TitouaGame ! (non connecté)")
		print("Choisissez une option")
		print("1. Login")
		print("2. S'enregistrer")
		choix = int(input())

		if choix == 2:
			register()

menu_not_connected()