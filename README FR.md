
# CHATGPTFORWINDOWS
**ChatGPT for Windows bypass** pour permettre aux utilisateurs réguliers (non premium) d'accéder aux nouvelles fonctionnalités vocales et de créer des ChatGPT personnalisés.

## Étapes d'installation

### 1. Télécharger ChatGPT (version précoce)

- [Lien vers l'application ChatGPT sur le Microsoft Store](https://apps.microsoft.com/detail/9nt1r1c2hh7j?hl)

### 2. Installer mitmproxy

- Téléchargez mitmproxy depuis leur site officiel : [mitmproxy.org](https://www.mitmproxy.org/)
- Installez le certificat :
  - [Télécharger le certificat](https://github.com/guilatoffi/CHATGPTFORWINDOWS/blob/main/mitmproxy-ca-cert.p12)
  - Lancez le fichier, puis cliquez sur "Suivant" et laissez toutes les options par défaut.

### 3. Configurer le proxy avec kill2.py

#### Option 1 : Configuration automatique (fichier batch)

1. Téléchargez tous les fichiers nécessaires sur votre bureau.
2. Exécutez `LaunchProxy.bat` pour configurer et démarrer le proxy automatiquement.

#### Option 2 : Configuration manuelle

1. Dans un terminal avec privilèges administrateur, allez dans le répertoire où se trouve le fichier `kill2.py`.
2. Exécutez la commande suivante :
   ```bash
   mitmproxy -s kill2.py
   ```
3. Dans les paramètres de Windows, configurez le proxy à `127.0.0.1:8080`.
4. Lancez ChatGPT normalement.

### 4. Désactiver le proxy

- Une fois terminé, exécutez `DISABLE PROXY.bat` pour remettre les paramètres de proxy à leur état par défaut.
