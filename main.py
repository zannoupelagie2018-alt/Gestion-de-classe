# Version 2 : amélioration du programme de gestion des élèves
def demander_nom():
    while True:
        nom = input("Nom : ").strip()

        nom_verifie = nom.replace(" ", "").replace("-", "").replace("'", "")

        if nom_verifie.isalpha() and nom_verifie:
            return nom
        else:
            print("Erreur : entre un nom composé uniquement de lettres.")


def demander_note():
    while True:
        try:
            note = int(input("Note : "))

            if 0 <= note <= 20:
                return note
            else:
                print("Erreur : la note doit être entre 0 et 20.")

        except ValueError:
            print("Erreur : veuillez entrer un nombre entier.")


def demander_nombre():
    while True:
        try:
            nombre = int(input("Combien d'élèves : "))

            if nombre >= 0:
                return nombre
            else:
                print("Erreur : le nombre doit être positif.")

        except ValueError:
            print("Erreur : entre un nombre entier.")


def calculer_moyenne(eleves):
    if len(eleves) == 0:
        return 0

    somme = 0

    for eleve in eleves:
        somme += eleve["note"]

    return somme / len(eleves)


def trouver_meilleur_eleve(eleves):
    if len(eleves) == 0:
        return None, None

    meilleur = eleves[0]

    for eleve in eleves:
        if eleve["note"] > meilleur["note"]:
            meilleur = eleve

    return meilleur["note"], meilleur["nom"]


def afficher_resultats(eleves):
    for eleve in eleves:
        if eleve["note"] >= 10:
            print(eleve["nom"], ":", "Admis")
        else:
            print(eleve["nom"], ":", "Ajourné")


def calculer_taux_de_reussite(eleves):
    if len(eleves) == 0:
        return 0

    admis = 0

    for eleve in eleves:
        if eleve["note"] >= 10:
            admis += 1

    return admis / len(eleves) * 100


def ajouter_eleve(eleves):
    nom = demander_nom()
    note = demander_note()

    eleves.append({"nom": nom, "note": note})

    print("Élève ajouté avec succès !")


def rechercher_eleve(eleves):
    nom_recherche = input("Nom de l'élève à rechercher : ").strip()

    trouve = False

    for eleve in eleves:
        if eleve["nom"].lower() == nom_recherche.lower():
            trouve = True
            print("Élève trouvé :", eleve["nom"])
            print("Note :", eleve["note"])

    if not trouve:
        print("Élève introuvable.")


def modifier_note(eleves):
    nom_recherche = input("Nom de l'élève : ").strip()

    for eleve in eleves:
        if eleve["nom"].lower() == nom_recherche.lower():
            print("Ancienne note :", eleve["note"])
            nouvelle_note = demander_note()

            eleve["note"] = nouvelle_note

            print("Note modifiée avec succès !")
            return

    print("Élève introuvable.")


def modifier_nom(eleves):
    nom_recherche = input("Nom de l'élève à modifier : ").strip()

    for eleve in eleves:
        if eleve["nom"].lower() == nom_recherche.lower():
            nouveau_nom = demander_nom()

            eleve["nom"] = nouveau_nom

            print("Nom modifié avec succès !")
            return

    print("Élève introuvable.")


def supprimer_eleve(eleves):
    nom_recherche = input("Nom de l'élève à supprimer : ").strip()

    for eleve in eleves:
        if eleve["nom"].lower() == nom_recherche.lower():
            eleves.remove(eleve)

            print("Élève supprimé avec succès !")
            return

    print("Élève introuvable.")


def afficher_liste(eleves):
    if len(eleves) == 0:
        print("Aucun élève dans la classe.")
    else:
        print("\n===== LISTE DES ÉLÈVES =====")

        for i, eleve in enumerate(eleves, start=1):
            print(f"{i}. {eleve['nom']:<15} | {eleve['note']:>2}/20")


def afficher_message():
    print("\nBienvenue dans la gestion de classe !")


def main():
    eleves = []

    nombre = demander_nombre()

    for i in range(nombre):
        print("\nÉlève", i + 1)

        nom = demander_nom()
        note = demander_note()

        eleves.append({"nom": nom, "note": note})

    choix = 0

    while choix != 11:
        afficher_message()

        print("\n===== GESTION DE CLASSE =====")
        print("1. Voir la moyenne")
        print("2. Voir le meilleur élève")
        print("3. Voir les résultats")
        print("4. Voir le taux de réussite")
        print("5. Ajouter un élève")
        print("6. Rechercher un élève")
        print("7. Modifier la note d'un élève")
        print("8. Supprimer un élève")
        print("9. Afficher la liste des élèves")
        print("10. Modifier un nom")
        print("11. Quitter")

        try:
            choix = int(input("Choisis une option : "))

            if not 1 <= choix <= 11:
                print("Erreur : choisis une option entre 1 et 11.")
                continue

        except ValueError:
            print("Erreur : entre un nombre entier.")
            continue

        if choix == 1:
            moyenne = calculer_moyenne(eleves)
            print(f"Moyenne de la classe : {moyenne:.2f}/20")

        elif choix == 2:
            meilleure_note, meilleur_eleve = trouver_meilleur_eleve(eleves)

            if meilleur_eleve is None:
                print("Aucun élève dans la classe.")
            else:
                print("Meilleur élève :", meilleur_eleve)
                print("Sa note :", meilleure_note)

        elif choix == 3:
            if len(eleves) == 0:
                print("Aucun élève dans la classe.")
            else:
                afficher_resultats(eleves)

        elif choix == 4:
            taux = calculer_taux_de_reussite(eleves)
            print(f"Taux de réussite : {taux:.2f}%")

        elif choix == 5:
            ajouter_eleve(eleves)

        elif choix == 6:
            rechercher_eleve(eleves)

        elif choix == 7:
            modifier_note(eleves)

        elif choix == 8:
            supprimer_eleve(eleves)

        elif choix == 9:
            afficher_liste(eleves)

        elif choix == 10:
            modifier_nom(eleves)

        elif choix == 11:
            print("Au revoir !")


if __name__ == "__main__":
    main()
