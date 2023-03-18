# Projet 9 - Developpez une application Web en utilisant django

Etapes à suivre pour la mise en place du projet et son utilisation.

1 - Mise en place de l'environnement virtuel :
    - une fois le projet récupéré, aller sous le répertoire principal du projet "LR" sous l'invit de commande windows .
    - Créer l'environnement virtuel en tapant la commande "python -m venv env"
    - Activer l'environnement virtuel en tapant la commande "env\scripts\activate" 

2 - Une fois l'environnement virtuel activé, installer tous les packages du projet : 
    - toujours sous le répertoire "LR", taper la commande "pip install -r requirements.txt"

3 - Aller sous le répertoire LitReview (cd LitReview)

4 - Exécution du serveur django :
    Afin de lancer le serveur, taper la commande "python manage.py runserver"

5 - En tapant "http://127.0.0.1:8000/" dans le navigateur, 
    la page d'inscription s'affiche, permettant de créer un utilisateur ou de se connecter via un utilisateur existant, 
    l'application est fonctionnelle.

6 - Une fois l'utilisateur connecté, la page flux de l'application s'affiche, l'application est utilisable 
    par l'utilisateur connecté.

- La page Flux dans laquelle les critiques et les tickets sont affichés chronologiquement dans l'ordre de leur création,
  permet à l'utilisateur connecté de :
      - demander une critique en créant un ticket via le bouton "Demander une critique".
      - créer une critique en créant à la fois le ticket et la critique via le bouton "Demander une critique".
      - répondre à une demande de critique via le bouton "créer une critique" suite à une demande de critique (ticket)
        suite à une demande de critique.
      - répondre à une critique d'un utilisateur qui a créé une critique de son propre ticket via le bouton 
        "créer une critique" suite à une review. (Une fois la réponse effectuée, le bouton de création ne doit plus être 
        accessible).
      
- La page Post, dans laquelle les critiques et les tickets de l'utilisateur connecté et des utilisateurs suivis sont 
  affichés chronologiquement dans l'ordre de leurs créations, permet à l'utilisateur :
    - De modifier ces posts ou de les supprimer.

- La page Abonnement permet de sélectionner un utilisateur pour le suivre et de supprimer le suivi d'un utilisateur, 
  cela permet de voir ensuite les posts de cet utilisateur dans la page de flux.

- Une démonstration du fonctionnement de l'application sera effectuée lors de la spoutenance. Lors de 
  cette démonstration, des utilisateurs, des suivis d'utilisateurs, des tickets, des reviews, 
  des réponses aux tickets et reviews seront créés.
