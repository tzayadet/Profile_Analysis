# Profile Analysis · Exploración de preferencias

[![Quality checks](https://github.com/tzayadet/Profile_Analysis/actions/workflows/quality.yml/badge.svg)](https://github.com/tzayadet/Profile_Analysis/actions/workflows/quality.yml) [![GitHub Pages](https://github.com/tzayadet/Profile_Analysis/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/tzayadet/Profile_Analysis/actions/workflows/jekyll-gh-pages.yml)

Cuestionario interactivo de autoexploración que organiza respuestas en cuatro dimensiones de preferencia y genera una de 16 descripciones tipológicas.

## Demo

https://tzayadet.github.io/Profile_Analysis/

## Funcionamiento

- 60 afirmaciones con una escala de respuesta de cinco niveles.
- Cuatro dimensiones con polos opuestos: E/I, S/N, T/F y J/P.
- Cálculo local de puntuaciones y generación de un perfil descriptivo.
- Guardado de progreso en `localStorage` para poder continuar en el mismo navegador.
- Copia y exportación JSON de los resultados.
- Borrado de la sesión y de las respuestas guardadas.

## Aviso de validez

Este proyecto es un ejercicio de programación y autoexploración. Su cuestionario y sus perfiles **no constituyen un instrumento psicométrico validado**. No mide inteligencia, capacidad cognitiva, salud mental ni idoneidad profesional; tampoco sustituye una evaluación psicológica.

No debe utilizarse para selección de personal, clasificación de candidatos, diagnóstico clínico ni decisiones que afecten a otras personas.

## Privacidad

- No requiere cuenta ni recoge nombre, correo o identificadores personales.
- No utiliza backend ni envía respuestas a servicios externos.
- Las respuestas se guardan localmente en el navegador mediante `localStorage`.
- Usa «Borrar» para eliminar los datos guardados en ese navegador.
- La exportación JSON se descarga localmente y queda bajo control de quien la realiza.

## Tecnologías

- HTML5
- CSS3
- JavaScript nativo
- Web Storage API
- Clipboard API

## Validación

Con Python 3.11 y Node.js 20 o superior:

```bash
python scripts/validate_site.py
```

La validación comprueba el número de preguntas y perfiles, verifica que no haya dependencias JavaScript remotas ni llamadas de red y ejecuta `node --check` sobre el script de la aplicación.

GitHub Actions ejecuta la validación en cada push y pull request.

## Licencia

Consulta [LICENSE](LICENSE).
