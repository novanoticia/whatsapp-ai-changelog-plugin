<!-- i18n fuente-sha256=7685d7af6b68 estado=borrador-ia -->

# WhatsApp AI Changelog v1.6.0

> Traduction française de [README.md](README.md) (`borrador-ia` : traduction
> automatique, non relue par un humain). En cas de divergence, le
> [README.md](README.md) espagnol fait foi.

Plugin basé sur la version 1.5 de la skill `whatsapp-ai-changelog` du fichier
joint. Il transforme le README et les nouveautés vérifiables d’un dépôt d’IA en
un message WhatsApp destiné à des utilisateurs grand public ou à des
professionnels sans profil de développeur.

Il inclut **Bayesian Compose v1.3.0**, avec ses 30 critères, sa configuration et
ses références. Inutile d’installer cette dépendance séparément.

## Langue

**L’espagnol (`es`)** est la langue par défaut du plugin et de la documentation.
L’entretien, le message et le diagnostic sont présentés en espagnol. Tu peux
demander une autre langue pour la conversation ou pour le destinataire.

Pour mener l’entretien et le diagnostic dans une autre langue, écris `idioma=en`,
`idioma=fr` ou `idioma=zh` (chinois simplifié) comme mot isolé sur la première
ligne de ton message, par exemple
`/whatsapp-ai-changelog idioma=fr https://github.com/utilisateur/depot`. Sans
marqueur, rien ne change. Langues disponibles : `es` (référence), `en`, `fr` et
`zh` (brouillons de traduction automatique, non relus par un humain ; le chinois
traditionnel n’est pas disponible). Chaque réponse dans ces langues commence par
un avis de traduction dans cette langue ; le message final que tu copies dans
WhatsApp ne le contient jamais. Documentation traduite :
[README.en.md](README.en.md), [README.fr.md](README.fr.md) et
[README.zh.md](README.zh.md), chacune avec ses `CHANGELOG.<code>.md` et
`PRIVACY.<code>.md`.

Le message lui-même est rédigé dans la langue que tu choisis pour le destinataire ;
sinon, dans la langue de la conversation. Le texte de l’interface, les marqueurs
`[NOTA]`, les codes de niveau, les commandes, les URL et le contenu cité du README
ne sont pas traduits. Les manifestes (`plugin.json`, marketplace), `VALIDATION.md`,
`MISTRAL.md`, `PERPLEXITY.md` et `THIRD_PARTY_NOTICES.md` restent en espagnol.

Pour ajouter une langue, crée `skills/whatsapp-ai-changelog/references/i18n/<code>.md`
en suivant la structure de `en.md`, ajoute le code au bloc de langue de
`skills/whatsapp-ai-changelog/SKILL.md`, déclare le fichier dans
`scripts/package_skills.py` et la nouvelle langue dans `tests/test_i18n.py`, puis
ajoute ses fichiers de documentation.

## Utilisation

```text
/whatsapp-ai-changelog https://github.com/usuario/repositorio
```

Tu peux aussi demander : « Message WhatsApp sur cet outil d’IA : [lien vers le
dépôt] ».

1. Il lit le README et vérifie toujours la dernière version stable publiée sur
   GitHub quand il doit décrire les dernières nouveautés, même si le README
   mentionne déjà une version.
2. Il demande le profil du destinataire, puis pose une par une les cinq questions
   adaptées de l’entretien.
3. Il génère un brouillon de 200 à 350 mots, au format WhatsApp.
4. Il évalue les 30 critères et présente un score, les points forts, les points
   faibles et un tableau.
5. Il permet d’itérer et te remet le texte propre à copier-coller.

Le score estime la qualité du message du point de vue du destinataire ; ce n’est
pas une probabilité calibrée de réponse. Les notes de version GitHub vérifiées
sont utilisées même si le README n’a pas de section sur les versions. Ce n’est que
si aucune des deux sources ne fournit de changements vérifiables qu’il se limite
aux fonctionnalités documentées, en indiquant la limite. S’il ne peut pas vérifier
la dernière version publiée, il ne présente pas une version du README comme la
plus récente. Le plugin rédige des messages ; il ne les envoie pas.

## Installation dans Claude Code

Une fois ce dépôt publié :

```text
/plugin marketplace add novanoticia/whatsapp-ai-changelog-plugin
/plugin install whatsapp-ai-changelog@whatsapp-ai-changelog-plugin
```

Dans les clients qui utilisent des noms de commande avec espace de noms, la
commande peut être `/whatsapp-ai-changelog:whatsapp-ai-changelog [URL]`.

Pour essayer le dossier local avec Claude Code :

```sh
claude --plugin-dir /ruta/whatsapp-ai-changelog-plugin
```

## Installation dans Mistral Work

Utilise l’asset **whatsapp-ai-changelog-mistral-1.6.0.zip** de
[GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest).
Décompresse-le et crée une skill avec le dossier `whatsapp-ai-changelog/`. Le
protocole d’évaluation est inclus comme références internes ; une seule skill
suffit. Le ZIP du plugin Claude a un autre format. Consulte [MISTRAL.md](MISTRAL.md)
(en espagnol) pour importer le dossier ou utiliser l’éditeur.

## Installation dans Perplexity Computer

Utilise **whatsapp-ai-changelog-perplexity-1.6.0.zip** de
[GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest)
et téléverse-le directement via **Skills → Create skill → Upload a skill**.
Enregistre uniquement `whatsapp-ai-changelog` : la méthode Bayesian Compose est
incluse dans les références et évite une seconde skill du même nom. Consulte
[PERPLEXITY.md](PERPLEXITY.md) (en espagnol) pour les détails.

## Autres clients

La racine contient `plugin.json` pour les clients compatibles avec Agent Plugins
1.0.0, et `skills/` contient les deux skills au format SKILL.md. La possibilité
d’installer depuis GitHub dépend du client. La prise en charge de ChatGPT/Codex
doit être vérifiée dans son propre installateur ; ce paquet ne crée ni
n’enregistre à lui seul un plugin dans son catalogue.

Pour les autres clients qui importent les skills du plugin une par une, importe
**les deux** dossiers : `skills/whatsapp-ai-changelog/` et
`skills/bayesian-compose/`.

## Prérequis

Un assistant compatible avec les skills et un accès en lecture à GitHub par
navigation ou via un connecteur autorisé. S’il ne peut pas lire le dépôt, tu peux
coller ou joindre le README et les notes de version. Il ne nécessite ni serveur
MCP, ni identifiants WhatsApp, ni code exécutable.

## Structure

```text
.claude-plugin/
  plugin.json
  marketplace.json
plugin.json
commands/whatsapp-ai-changelog.md
skills/
  whatsapp-ai-changelog/SKILL.md
  bayesian-compose/
    SKILL.md
    config.yaml
    references/
README.md
CHANGELOG.md
PRIVACY.md
THIRD_PARTY_NOTICES.md
LICENSE
```

## Provenance et licence

La skill principale provient de `whatsapp-ai-changelog.zip`, de Pablo. Bayesian
Compose provient de
[novanoticia/bayesian-compose-plugin](https://github.com/novanoticia/bayesian-compose-plugin)
et conserve ses échelles et son protocole. Consulte
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) pour les fichiers et les
empreintes. Licence Apache-2.0 ; voir [LICENSE](LICENSE).

Élaboré avec l’assistance de l’IA ; relecture humaine requise.
