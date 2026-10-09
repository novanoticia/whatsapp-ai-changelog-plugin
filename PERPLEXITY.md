# Instalación en Perplexity Computer

Si ya tienes `bayesian-compose`, importar el plugin completo puede intentar
registrar otra skill con ese mismo nombre. Usa la distribución autónoma,
que registra solo `whatsapp-ai-changelog` e incluye el método de evaluación
como archivos de referencia internos.

1. Descarga **whatsapp-ai-changelog-perplexity-1.5.2.zip** de
   [GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest).
2. En Perplexity Computer, abre **Skills → Create skill → Upload a skill**.
3. Sube ese ZIP directamente. Contiene `SKILL.md` en la raíz y sus referencias.
4. Activa la skill y abre una tarea nueva. Pide un mensaje de WhatsApp sobre
   el repositorio que quieras compartir.

La skill `bayesian-compose` que ya tienes puede seguir instalada. No se
registra una segunda copia al importar esta distribución. Si ya existe
también `whatsapp-ai-changelog`, usa la opción de actualizar esa skill.

```text
SKILL.md
references/
  protocolo-bayesian-compose.md
  criterios-30-emision.md
LICENSE
NOTICE.md
```

El ZIP completo del plugin de Claude y el ZIP de transporte de Mistral
tienen estructuras distintas. Usa el asset que lleva **perplexity** en el nombre.
No subas únicamente `SKILL.md`, porque faltarían los criterios de evaluación.

Se comprueba que el archivo tenga una sola skill y esté por debajo de 10 MB.
No se ha probado su importación en tu cuenta de Perplexity.

Fuente oficial consultada el 9 de octubre de 2026:
[Skills en Perplexity Computer](https://www.perplexity.ai/en-GB/hub/workshops/perplexity-computer-for-buyside-professionals).
