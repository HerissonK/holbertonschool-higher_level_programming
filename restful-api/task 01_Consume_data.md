# 🌐 Project: 1. Consume Data from an API using Command Line Tools (curl)

## 1. Introduction

`curl` (Client URL) est un outil en ligne de commande qui permet de transférer des données depuis ou vers un serveur à l’aide de différents protocoles (HTTP, HTTPS, FTP, etc.).  
Il est souvent utilisé pour **tester des API REST**, **vérifier des connexions réseau**, ou **inspecter des réponses HTTP**.  
Savoir utiliser `curl` est une compétence essentielle pour comprendre et manipuler des APIs, avant même d’écrire une seule ligne de code.

---

## 2. Installation and Verification

### 🧰 Installation

- **Linux / macOS** → déjà installé sur la plupart des systèmes. Sinon :
  ```bash
  sudo apt install curl        # Debian/Ubuntu
  brew install curl            # macOS (Homebrew)

Windows → via PowerShell ou le Windows Subsystem for Linux (WSL).

✅ Verification

Pour vérifier l’installation :

curl --version

curl 8.4.0 (x86_64-pc-linux-gnu) libcurl/8.4.0 OpenSSL/3.0.10 zlib/1.3 brotli/1.1.0
Release-Date: 2024-09-20
Protocols: dict file ftp ftps http https imap imaps pop3 pop3s smtp smtps
Features: AsynchDNS, IPv6, SSL, libz, NTLM, TLS-SRP, UnixSockets

Fetching a Web Page with curl

To retrieve a simple web page:

curl http://example.com


📄 Expected Output:
Tu verras le code HTML brut de la page :

<!doctype html>
<html>
<head><title>Example Domain</title></head>
<body><h1>Example Domain</h1></body>
</html>


💡 Note : Par défaut, curl affiche uniquement le contenu de la réponse, pas les en-têtes HTTP.

4. Fetching Data from an API (GET Request)
🔗 Example API: JSONPlaceholder

C est une API publique de test gratuite, très utile pour s exercer :

curl https://jsonplaceholder.typicode.com/posts


📄 Expected Output (abridged):

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae..."
  }
]


💡 Astuce : si la sortie est trop longue, tu peux la formater avec jq :

curl https://jsonplaceholder.typicode.com/posts | jq .

5. Viewing Only the Headers (-I Option)

Pour voir uniquement les en-têtes HTTP, utilise l’option -I :

curl -I https://jsonplaceholder.typicode.com/posts


📄 Expected Output:

HTTP/2 200
date: Mon, 06 Oct 2025 10:05:00 GMT
content-type: application/json; charset=utf-8
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
via: 1.1 vegur


💡 Interprétation :

HTTP/2 200 → requête réussie

content-type → indique le type de contenu (ici JSON)

Les autres headers donnent des infos de serveur, limite de requêtes, etc.

6. Sending Data with a POST Request

Pour envoyer des données à l’API (simuler une création) :

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts


📄 Expected Output:

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}


💬 Explication :

-X POST → définit la méthode HTTP utilisée.

-d → envoie des données dans le corps de la requête (ici en x-www-form-urlencoded).

L’API JSONPlaceholder simule la création d’un nouvel objet, mais ne l’enregistre pas réellement.

Elle renvoie un id fictif (101) pour signifier que la création a été "réussie".

7. Additional Useful curl Options
Option	Description	Example
-v	Mode verbeux : affiche les détails de la requête/réponse	curl -v https://example.com
-s	Mode silencieux : n’affiche pas la barre de progression	curl -s https://example.com
-H	Ajoute un header personnalisé	curl -H "Content-Type: application/json"
-o file.txt	Sauvegarde la sortie dans un fichier	curl https://example.com -o page.html
8. Summary of Learning

curl est un outil puissant pour tester des requêtes HTTP et interagir avec des APIs.

La commande curl --version vérifie ton installation et les protocoles pris en charge.

Une requête simple curl http://example.com affiche le contenu d’une page.

L’option -I permet de visualiser uniquement les en-têtes.

Les options -X et -d permettent de faire des requêtes POST, PUT, ou DELETE avec des données.

Tu peux combiner curl avec jq pour formater le JSON et rendre les résultats lisibles.

🧩 Example Summary Commands
Action	Command
Check version	curl --version
Fetch a web page	curl http://example.com
Get API data	curl https://jsonplaceholder.typicode.com/posts
Show only headers	curl -I https://jsonplaceholder.typicode.com/posts
Make a POST request	curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts