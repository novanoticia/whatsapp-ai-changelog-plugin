<!-- i18n fuente-sha256=99bcfec1477f estado=borrador-ia -->

# Changelog

> Traduction française de [CHANGELOG.md](CHANGELOG.md) (`borrador-ia` :
> traduction automatique, non relue par un humain). En cas de divergence, le
> fichier espagnol fait foi. Les notes de version publiées sur GitHub proviennent
> du fichier espagnol.

## [Non publié]

- Modification de la `description` de la skill principale et des paquets à skill
  unique : elle inclut désormais aussi des phrases de déclenchement en français et
  en chinois (« message WhatsApp sur cet outil d’IA », « 关于这个AI工具的WhatsApp消息 »),
  afin que la skill puisse s’activer sur des demandes dans ces langues. Cela change
  le moment où la skill s’active ; pour le retirer, annuler ce changement. Pour
  respecter la limite de 500 caractères de la skill elle-même, le reste du texte a
  été raccourci : « novedades de herramientas de IA » (avant « … o proyectos de
  IA »), « desde el README de un repo GitHub », « Adapta el tono al receptor » et
  « Trigger: » (avant « Trigger obligatorio: »). L’activation dépend toujours de la
  plateforme.

Élaboré avec l’assistance de l’IA ; relecture humaine requise.

## [1.7.0] — 2026-10-11

- Ajout du français (`fr`) et du chinois simplifié (`zh`) comme langues de
  l’interface, avec `idioma=fr` et `idioma=zh` et des équivalences de textes fixes
  dans `skills/whatsapp-ai-changelog/references/i18n/fr.md` et `zh.md`. Le chinois
  traditionnel (`zh-Hant`, `zh-TW`, `zh-HK`) n’est pas disponible et n’est pas
  remplacé par le simplifié. Sans marqueur, le comportement ne change pas.
- Ajout de la documentation en français et en chinois : `README`, `CHANGELOG` et
  `PRIVACY` (`.fr.md` et `.zh.md`). Ce sont des brouillons d’IA non relus par un
  humain.
- Modification de l’avis de traduction : chaque langue l’affiche dans cette
  langue, et avec le mode de repli (fichier d’équivalences absent) la réponse
  repasse en espagnol avec la ligne d’avis de la langue demandée (auparavant elle
  restait dans la langue demandée ; corrige le constat S6 de l’évaluation par
  scénarios).
- Les paquets Mistral et Perplexity incluent `fr.md` et `zh.md`.
- La `description` n’est pas modifiée : en français et en chinois, l’activation en
  langage naturel dépend de la plateforme ; la commande `/whatsapp-ai-changelog`
  fonctionne toujours.
- Évaluation par scénarios exécutée le 2026-10-11 (simulée, un essai par
  scénario) : 7 sur 7 réussis lors de cette série ; la reprise de S6 corrige
  l’échec précédent. En attente : relecture humaine des traductions (le chinois
  avec davantage d’incertitude).

Élaboré avec l’assistance de l’IA ; relecture humaine requise.

## [1.6.0] — 2026-10-11

Ajouts :

- Interface en anglais sélectionnable avec `idioma=en` sur la première ligne du
  message (`es` et `en` disponibles), avec des équivalences de textes fixes dans
  `skills/whatsapp-ai-changelog/references/i18n/en.md`. Sans marqueur, le
  comportement ne change pas.
- Documentation en anglais : `README.en.md`, `CHANGELOG.en.md` et `PRIVACY.en.md`.
- Tests dans `tests/test_i18n.py` ; les paquets Mistral et Perplexity incluent
  désormais `references/i18n/en.md`.
- Ajout du workflow `Pruebas`, qui exécute `tests/` à chaque pull request.

Modifications (exceptions approuvées à la sortie par défaut, à retirer en
annulant ce changement) :

- La `description` de la skill principale et celle des paquets à skill unique
  mentionnent aussi la phrase de déclenchement en anglais, afin que la skill
  puisse s’activer sur des demandes en anglais. Cela change le moment où la skill
  s’active.
- Chaque réponse en anglais commence par l’avis « Translation machine-generated,
  not human-reviewed. ». Il n’apparaît jamais en espagnol ni dans le message final
  à copier.

Limites :

- Les fichiers anglais sont des traductions automatiques (`borrador-ia`), non
  relues par un humain.
- Les manifestes, `VALIDATION.md`, `MISTRAL.md`, `PERPLEXITY.md` et
  `THIRD_PARTY_NOTICES.md` restent uniquement en espagnol. Le schéma des manifestes
  n’a pas de champ de description multilingue vérifié.
- L’évaluation par scénarios du nouveau bloc de langue n’a pas été exécutée (en
  attente).

## [1.5.2] — 2026-10-09

- Ajout de distributions à skill unique pour Mistral Work et Perplexity, avec le
  protocole Bayesian Compose et ses 30 critères comme références internes.
- Suppression, dans cette distribution, de la dépendance à une autre skill et aux
  chemins entre dossiers. Conservation des échelles et des corrections de
  publication.
- Évitement de l’enregistrement en double de `bayesian-compose` dans Perplexity.
- Ajout d’un générateur, d’instructions par client et de ZIP séparés : un dossier
  pour Mistral et `SKILL.md` à la racine du ZIP pour Perplexity.
- Installation : dans Perplexity, téléverser directement
  `whatsapp-ai-changelog-perplexity-1.5.2.zip` ; dans Mistral, décompresser
  `whatsapp-ai-changelog-mistral-1.5.2.zip` et utiliser le dossier obtenu.

## [1.5.1] — 2026-10-09

- Vérification de la dernière version stable publiée même lorsque le README
  mentionne des versions.
- Conservation des notes de version vérifiées lorsque le README ne documente aucune
  version ; le repli sur les seules fonctionnalités exige qu’aucune des deux
  sources ne fournisse de changements vérifiables.
- Déclaration de l’espagnol comme langue par défaut du flux et traduction des
  descriptions des manifestes et du marketplace.
- Publication des versions et des ZIP du plugin via GitHub Actions.

## [1.5.0] — 2026-10-09

- Empaquetage de la skill WhatsApp AI Changelog v1.5 sous forme de plugin.
- Ajout de manifestes pour Claude et Agent Plugins 1.0.0, d’un marketplace et d’une
  commande.
- Inclusion de Bayesian Compose v1.3.0 avec sa configuration et ses références
  d’origine.
- Clarification de l’intégration pour éviter les entretiens en double et préserver
  les échelles.
- Documentation de l’installation, de la confidentialité et de la provenance.

Élaboré avec l’assistance de l’IA ; relecture humaine requise.
