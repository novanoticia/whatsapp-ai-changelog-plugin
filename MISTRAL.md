# Instalación en Mistral Work

Mistral Work carga skills con `SKILL.md` y archivos de apoyo. El ZIP del
plugin de Claude contiene manifiestos y dos skills; no se debe importar
ese paquete completo como una única skill de Mistral.

## Qué descargar

En [GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest),
descarga **whatsapp-ai-changelog-mistral-1.5.2.zip** y descomprímelo.
El ZIP se usa para transportar la carpeta, no como formato de importación.

La carpeta resultante tiene esta estructura:

```text
whatsapp-ai-changelog/
  SKILL.md
  references/
    protocolo-bayesian-compose.md
    criterios-30-emision.md
  LICENSE
  NOTICE.md
```

Es una sola skill. El protocolo y los 30 criterios están incluidos como
referencias internas; no hace falta instalar `bayesian-compose` aparte.
No necesita scripts, servidor MCP ni configuración persistente.

## Crear la skill

1. Abre Mistral, activa **Work** y ve a **Context → Skills → New Skill**.
2. Si tu interfaz permite importar una carpeta, selecciona solo
   `whatsapp-ai-changelog/`, la que contiene directamente `SKILL.md`.
3. Si presenta el editor con campos, usa `whatsapp-ai-changelog` como título,
   copia la descripción del frontmatter al campo **Description** y el
   contenido de `SKILL.md` al campo de instrucciones. Añade la carpeta
   `references/` como archivos de apoyo, conservando esos nombres y rutas.
4. Guarda la skill y abre una tarea nueva de Work. Invócala con
   `/whatsapp-ai-changelog [URL-de-GitHub]` o menciona su nombre.

Si no están disponibles los archivos de referencia, el diagnóstico debe
quedar pendiente. Si la navegación no puede leer GitHub, pega o adjunta
el README y las notas de publicación; la skill explicará la limitación.

## Comprobaciones y límites

El paquete se valida para contener una sola skill, referencias internas,
frontmatter estándar y descripción menor de 490 bytes. Se conservan
íntegros los criterios y las escalas originales de Bayesian Compose.
La importación y una conversación real no se han probado en tu cuenta.

Documentación oficial consultada el 9 de octubre de 2026:
[Crear una skill](https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill)
y [Skills en Work](https://docs.mistral.ai/vibe/work/skills).

## Generar la carpeta desde el repositorio

```sh
python3 scripts/package_skills.py --out dist/skills
```

La salida debe estar vacía o no existir: el generador no sobrescribe una
carpeta que contenga archivos.
