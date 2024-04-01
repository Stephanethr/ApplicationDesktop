<div align="center">

# PassGuardian V2

![alt text](./assets/logo_passguardian.png)

Un gestionnaire de mots de passe simple et sécurisé.

</div>


## Fonctionnalités

- Stockage de mots de passe.
- Génération de mots de passe.
- Affichage des mots de passe.

## Algorithme de chiffrement utilisé

AES-GCM, soit Galois/Counter Mode (GCM) est un mode d'opération de chiffrement par bloc en chiffrement symétrique. Il est relativement répandu en raison de son efficacité et de ses performances. 

    Chiffrement : 
        Pour chiffrer des données, AES-GCM divise le texte en clair en blocs de taille fixe et chiffre 
        chaque bloc en utilisant AES avec la clé secrète. 
        Contrairement à d'autres modes d'opération, GCM ne nécessite pas de rembourrage pour les blocs, 
        car il est conçu pour fonctionner avec des blocs de taille fixe.

    Authentification : 
        En plus du chiffrement, GCM génère également un tag d'authentification pour chaque bloc de données chiffrées.
        Ce tag est calculé en utilisant une fonction de hachage spécialisée appelée le mode Galois Counter (GC). 
        Le tag d'authentification est ajouté à la sortie chiffrée et est utilisé pour vérifier l'intégrité des données 
        lors du déchiffrement.

    Utilisation d'un nonce (numéro utilisé une seule fois) :
        Pour garantir la sécurité, chaque message chiffré nécessite un nonce unique. 
        Le nonce est combiné avec un compteur pour produire un "nonce couplé" qui est utilisé dans le processus de chiffrement. 
        Cela garantit que même si les mêmes données sont chiffrées plusieurs fois avec la même clé,
        elles produiront des sorties différentes en raison de l'utilisation du nonce.

    Sécurité : 
        AES-GCM est considéré comme sécurisé et efficace. Il est utilisé dans de nombreux protocoles 
        de sécurité tels que TLS (Transport Layer Security) pour sécuriser les communications sur Internet,
        ainsi que dans d'autres applications nécessitant à la fois le chiffrement et l'authentification des données.

## Comment utiliser

1. Exécutez le fichier main.py.
2. L'application s'ouvre.

## Auteurs

- Thiry Stéphane
- Mirande Clémentine
- Michelozzi Matthieu
