<p align="center">
  <img src="https://img.shields.io/badge/INTERACTIVE_TOOL-PROFILE_ANALYSIS-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Profile Analysis"/>
  <img src="https://img.shields.io/badge/FRONTEND-VANILLA_JS-101010?style=for-the-badge&logo=javascript&logoColor=00FF41" alt="JavaScript"/>
</p>

# Profile Analysis

Cuestionario interactivo de autoexploración que organiza respuestas en cuatro dimensiones de preferencia y genera una descripción tipológica. Todo el procesamiento se realiza en el navegador.

<p align="center">
  <a href="https://tzayadet.github.io/Profile_Analysis/"><strong>LIVE DEMO ↗</strong></a> ·
  <a href="https://github.com/tzayadet/Profile_Analysis"><strong>SOURCE CODE</strong></a>
</p>

[![Quality checks](https://github.com/tzayadet/Profile_Analysis/actions/workflows/quality.yml/badge.svg)](https://github.com/tzayadet/Profile_Analysis/actions/workflows/quality.yml) · [![GitHub Pages](https://github.com/tzayadet/Profile_Analysis/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/tzayadet/Profile_Analysis/actions/workflows/jekyll-gh-pages.yml)

## Features

- 60 afirmaciones con escala de respuesta de cinco niveles.
- Cuatro dimensiones de preferencia: E/I, S/N, T/F y J/P.
- Cálculo local de puntuaciones y generación de un perfil descriptivo.
- Guardado de progreso en `localStorage`.
- Copia y exportación JSON de resultados.
- Eliminación de respuestas y sesión guardadas.

## Use it

Abre la [demo web](https://tzayadet.github.io/Profile_Analysis/) en un navegador moderno. No requiere instalación, cuenta ni backend.

## Privacy

- No requiere nombre, correo ni identificadores personales.
- No envía las respuestas a servicios externos.
- El progreso se guarda localmente mediante `localStorage`.
- La exportación JSON se descarga en el dispositivo del usuario.

## Methodological scope

Es un ejercicio de programación y autoexploración. El cuestionario y sus perfiles no constituyen un instrumento psicométrico validado. No mide inteligencia, capacidad cognitiva, salud mental ni idoneidad profesional. No debe utilizarse para selección de personal, diagnóstico ni decisiones que afecten a otras personas.

## Technology

- HTML5
- CSS3
- JavaScript nativo
- Web Storage API
- Clipboard API

## Validation

Con Python 3.11 y Node.js 20 o superior:

```bash
python scripts/validate_site.py
```

La validación comprueba la estructura del cuestionario, los perfiles y el JavaScript de la aplicación. GitHub Actions ejecuta los controles en push y pull requests.

## Deployment

Sitio estático publicado mediante GitHub Pages. No requiere backend.

## License

See [LICENSE](LICENSE).
