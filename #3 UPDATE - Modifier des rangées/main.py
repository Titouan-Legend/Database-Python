from Data.database_handler import DatabaseHandler

database_handler = DatabaseHandler("database.db")


def register():
    print("---Register---")
    username = input("Username : ")
    password = input("Mot de passe : ")

    database_handler.create_person(username, password)
    menu_connected(username)


def login():
    print("---Login---")
    username = input("Username : ")
    password = input("Mot de passe : ")

    if database_handler.user_exists_with(username) and password == database_handler.password_for(username):
        menu_connected(username)
    else:
        print("Nom d'utilisateur/mot de passe incorrect.")


def change_password(username : str):
    new_password = input("Veuillez entrer le nouveau mot de passe : ")
    new_password_confirmed = input("Veuillez confirmer le mot de passe : ")

    if new_password == new_password_confirmed:
        database_handler.change_password(username, new_password)
        print("Votre mot de passe a bien été modifié.")
    else:
        print("Les mots de passe ne correspondent pas.")

def menu_connected(username : str):
    while True:
        print("Vous êtes connecté à votre compte TitouGame")
        print("1. Se deconnecter")
        print("2. Changer le mot de passe")

        choix = int(input())
        if choix == 1:
            return
        if choix == 2:
            change_password(username)


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
