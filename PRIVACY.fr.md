<!-- i18n fuente-sha256=f14a6950c1cf estado=borrador-ia -->

# Confidentialité

> Traduction française de [PRIVACY.md](PRIVACY.md) (`borrador-ia` : traduction
> automatique, non relue par un humain). En cas de divergence, le fichier espagnol
> fait foi.

WhatsApp AI Changelog rédige du texte à l’intérieur de la conversation de
l’assistant. Le paquet ne contient ni serveur, ni scripts, ni outils d’envoi, ni
services de stockage propres.

Pour extraire l’information, l’assistant interroge GitHub par la navigation ou le
connecteur dont dispose l’utilisateur. Le traitement de ces données dépend de
l’assistant, du connecteur et de GitHub.

Bayesian Compose admet une configuration personnelle en dehors du paquet et une
télémétrie locale facultative. Aucune session ni aucun motif n’est enregistré sans
demande expresse de l’utilisateur, même s’il existe un dossier de configuration.
La télémétrie n’autorise que des métadonnées : jamais le texte du message ni des
données d’identification. Voir l’ÉTAPE 7 de son SKILL.md.

Le message final est copié manuellement dans WhatsApp. Le plugin n’envoie pas de
messages et ne se connecte pas au compte WhatsApp.

Élaboré avec l’assistance de l’IA ; relecture humaine requise.
