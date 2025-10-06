# 🧠 Project: 0. Basics of HTTP/HTTPS

## 1. Differences Between HTTP and HTTPS

| Aspect | HTTP | HTTPS |
|--------|------|--------|
| Port used | 80 | 443 |
| Security | Non sécurisé – les données sont envoyées en clair | Sécurisé grâce à un chiffrement SSL/TLS |
| Encryption | Aucune, les données peuvent être interceptées | Les données sont chiffrées entre le client et le serveur |
| Certificate | Aucun certificat requis | Nécessite un certificat SSL/TLS valide |
| Typical use case | Sites simples ou internes sans données sensibles | Sites de e-commerce, banques, services en ligne |

### 📝 Summary

HTTP (HyperText Transfer Protocol) est le protocole standard de communication entre un client (comme un navigateur) et un serveur web.  
HTTPS (HyperText Transfer Protocol Secure) est une version sécurisée d’HTTP qui ajoute une couche de chiffrement via SSL/TLS.  
Cette couche empêche les attaques d’interception (“man-in-the-middle”) et garantit que les données ne peuvent pas être lues ni modifiées pendant leur transfert.  
En pratique, tout site manipulant des informations sensibles (connexion, paiement, données personnelles) doit utiliser HTTPS.

---

## 2. Structure of an HTTP Request and Response

### 📤 Example of an HTTP Request

GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive


- **Method:** `GET` — indique l’action à effectuer (ici, récupérer une ressource)
- **Path:** `/index.html` — la ressource demandée sur le serveur
- **Version:** `HTTP/1.1` — version du protocole utilisée
- **Headers:** métadonnées fournissant des informations supplémentaires (navigateur, format accepté, connexion)
- **Body:** souvent vide pour GET, mais présent pour POST/PUT (contient des données à envoyer)

---

### 📥 Example of an HTTP Response

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
Date: Mon, 06 Oct 2025 09:15:00 GMT

<html> <body> <h1>Welcome!</h1> </body> </html> ```

Status line: HTTP/1.1 200 OK → version + code de statut + message

Headers: précisent le type et la longueur du contenu

Body: le contenu réel renvoyé (souvent HTML, JSON, ou autre)

🧩 Explanation

Une communication HTTP est composée de deux éléments :

La requête (Request) envoyée par le client pour demander une ressource ou une action.

La réponse (Response) envoyée par le serveur avec le résultat ou le contenu demandé.

Cette interaction suit un modèle client-serveur et se répète à chaque échange, car HTTP est un protocole sans état (stateless).

3. Common HTTP Methods
Method	Description	Typical Use Case
GET	Récupère une ressource sans la modifier	Charger une page web, ou lire des données depuis une API
POST	Envoie des données au serveur pour créer une ressource	Soumettre un formulaire ou créer un utilisateur
PUT	Remplace une ressource existante par une nouvelle version	Mettre à jour le profil d’un utilisateur
DELETE	Supprime une ressource sur le serveur	Supprimer un élément dans une base de données via une API
PATCH (optionnel)	Met à jour partiellement une ressource	Modifier seulement un champ d’un utilisateur
4. Common HTTP Status Codes
Code	Meaning	Typical Scenario
200 OK	Requête réussie, le serveur a renvoyé le contenu demandé	Chargement normal d’une page ou d’une ressource API
201 Created	Une nouvelle ressource a été créée avec succès	Lors d’un POST pour ajouter un nouvel élément
301 Moved Permanently	La ressource a été déplacée vers une nouvelle URL	Redirection permanente d’un ancien site
404 Not Found	La ressource demandée est introuvable sur le serveur	Mauvais lien ou URL inexistante
500 Internal Server Error	Erreur interne du serveur	Bug côté serveur ou panne d’un service
🔢 Category Overview

1xx – Information: Le serveur a reçu la requête et continue à la traiter.

2xx – Success: La requête a été reçue, comprise et exécutée correctement.

3xx – Redirection: Le client doit effectuer une action supplémentaire pour obtenir la ressource.

4xx – Client Error: La requête comporte une erreur (souvent du côté du client).

5xx – Server Error: Le serveur a échoué à exécuter une requête valide.

🧾 Summary of Learning

HTTP est la base de la communication web, mais n’offre aucune sécurité.

HTTPS ajoute un chiffrement grâce à SSL/TLS, protégeant les données en transit.

Une requête HTTP contient une méthode, un chemin, des en-têtes et parfois un corps.

Les réponses HTTP utilisent des codes de statut pour indiquer le résultat de la requête.

Les méthodes comme GET, POST, PUT, DELETE permettent de manipuler des ressources côté serveur.