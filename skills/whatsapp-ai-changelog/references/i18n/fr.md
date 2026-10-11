<!-- i18n fuente-sha256=640fc9688630 estado=borrador-ia -->

# Équivalences des textes fixes — français

Ce fichier ne traduit que les textes fixes de `SKILL.md`. En cas de divergence,
`SKILL.md` fait foi : sa version espagnole est la référence canonique. Il
n’ajoute aucune règle et ne modifie ni les critères, ni les échelles, ni les
scores. Statut : traduction automatique, `borrador-ia`, non relue par un humain.

## Glossaire

| Español | Français |
| --- | --- |
| mensaje | message |
| borrador | brouillon |
| novedades | nouveautés |
| publicación estable | version stable (release) |
| notas de la publicación | notes de version |
| destinatario / receptor | destinataire |
| entrevista | entretien |
| diagnóstico | diagnostic |
| fortalezas / debilidades | points forts / points faibles |

Forme d’adresse : tutoiement (« tu »), comme dans les équivalences françaises de
Bayesian Compose.

## Ce qui n’est pas traduit

`/whatsapp-ai-changelog`, `idioma=`, `[NOTA]`, `Score`, `REPLY_NEEDED`,
`REVIEW`, `READING_LATER`, `ARCHIVE`, les emojis, les URL, les versions, les noms
d’outils et le contenu cité du README ou des notes de version.

## Entretien — PHASE 2

| Question | Español | Français |
| --- | --- | --- |
| #0 | ¿A quién va dirigido el mensaje? Elige el perfil que mejor describe al receptor: | À qui s’adresse le message ? Choisis le profil qui décrit le mieux le destinataire : |
| #0 a | Usuario general de IA — usa herramientas como ChatGPT, Gemini o Perplexity, sin perfil técnico | Utilisateur grand public de l’IA — utilise des outils comme ChatGPT, Gemini ou Perplexity, sans profil technique |
| #0 b | Profesional que integra IA en su trabajo — médico, abogado, docente, gestor... sin ser dev | Professionnel qui intègre l’IA dans son travail — médecin, avocat, enseignant, gestionnaire... sans être développeur |
| #0 c | Ambos perfiles a la vez — el mensaje debe funcionar para los dos | Les deux profils à la fois — le message doit fonctionner pour les deux |
| #1 (gate) | ¿Qué quieres que el destinatario haga después de leer el mensaje? | Que veux-tu que le destinataire fasse après avoir lu le message ? |
| #2 | ¿Hay una decisión concreta que el destinatario deba tomar? (empezar a usar la herramienta, actualizarla, recomendarla, cambiar cómo la usa...) | Y a-t-il une décision concrète que le destinataire doit prendre ? (commencer à utiliser l’outil, le mettre à jour, le recommander, changer sa manière de l’utiliser...) |
| #3 | ¿Quieres incluir enlace al repositorio, a una demo, a instrucciones de uso, o solo el nombre de la herramienta? | Veux-tu inclure un lien vers le dépôt, une démo, des instructions d’utilisation, ou seulement le nom de l’outil ? |
| #4 | ¿Hay algo que el mensaje debería mencionar pero prefieres no destacar? (limitaciones conocidas, requisitos previos, estado beta, casos en que la herramienta no funciona bien) | Y a-t-il quelque chose que le message devrait mentionner mais que tu préfères ne pas mettre en avant ? (limites connues, prérequis, statut bêta, cas où l’outil fonctionne mal) |
| #5 | ¿Qué pasa si el destinatario lee esto dentro de 3 días en vez de hoy? ¿Hay alguna razón real para que lo lea ahora? | Que se passe-t-il si le destinataire lit ceci dans 3 jours plutôt qu’aujourd’hui ? Y a-t-il une vraie raison de le lire maintenant ? |

Relance du gate quand la réponse à #1 est vague (par exemple « pour qu’il soit au
courant ») : demande si le destinataire doit essayer l’outil, le recommander à
quelqu’un, donner son avis, changer sa façon de travailler, ou simplement
découvrir la nouveauté.

## Sortie et itération — PHASES 4 et 5

| Español | Français |
| --- | --- |
| Tu mensaje (Score: XX · TIER) | Ton message (Score: XX · TIER) |
| Nivel 1 — Mensaje + veredicto | Niveau 1 — Message + verdict |
| Nivel 2 — Fortalezas y debilidades | Niveau 2 — Points forts et points faibles |
| Nivel 3 — Desglose completo | Niveau 3 — Détail complet |
| REPLY_NEEDED 🔴: generaría respuesta activa | REPLY_NEEDED 🔴 : susciterait une réponse active |
| REVIEW 🟡: leído con atención | REVIEW 🟡 : lu avec attention |
| READING_LATER 🔵: leído "cuando pueda" | READING_LATER 🔵 : lu « quand il aura le temps » |
| ARCHIVE ⚪: ignorado o archivado | ARCHIVE ⚪ : ignoré ou archivé |
| Reescribir incorporando las debilidades | Réécrire en intégrant les points faibles |
| Modificar un punto específico | Modifier un point précis |
| Cambiar el perfil del destinatario | Changer le profil du destinataire |
| Entregar el mensaje | Livrer le message |
| Score v1: XX → Score v2: YY | Score v1 : XX → Score v2 : YY |

## Limites et avertissements

| Español | Français |
| --- | --- |
| El repositorio es privado o inaccesible: pega el contenido del README directamente. | Le dépôt est privé ou inaccessible : colle directement le contenu du README. |
| No se ha comprobado cuál es la última publicación. | La dernière version publiée n’a pas été vérifiée. |
| El diagnóstico está pendiente. | Le diagnostic est en attente. |
| Ninguna fuente aporta cambios verificables; el mensaje se limita a funcionalidades documentadas. | Aucune source ne fournit de changements vérifiables ; le message se limite aux fonctionnalités documentées. |
| Idioma no disponible. Idiomas disponibles: `es`, `en`, `fr` y `zh`. | Langue non disponible. Langues disponibles : `es`, `en`, `fr` et `zh`. |

Elaborado con asistencia de IA; requiere revisión humana. (Élaboré avec
l’assistance de l’IA ; relecture humaine requise.)
