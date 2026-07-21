# Bitácora IA

Registro de interacciones, decisiones aceptadas y revisiones del subagente crítico.

Formato sugerido:
- Fecha: YYYY-MM-DD
- Actor: `Coordinador` / `Especialista` / `Crítico` / `Datos` / `Programación`
- Decisión / Comentario:
- Referencia (archivo, línea, commit):

Ejemplo inicial:

- Fecha: 2026-07-20
- Actor: Coordinador
- Decisión / Comentario: Crear estructura inicial de carpetas y archivos.
- Referencia: Estructura del proyecto

- Fecha: 2026-07-20
- Actor: Coordinador / Especialista / Programación / Datos / Crítico
- Decisión / Comentario: Iniciar fase formal de simulación y desarrollo metodológico del BDH en Ecuador. Se redactó borrador académico de PSM, se implementó flujo inicial en Python para estimar puntajes de propensión, soporte común, emparejamiento y balance de covariables.
- Referencia: `src/analysis/psm_bdh_report.md`, `src/analysis/did_analysis.py`

- Fecha: 2026-07-20
- Actor: Coordinador / Programación / Datos / Especialista
- Decisión / Comentario: Generar README raíz completo con referencias oficiales de ENEMDU y Registro Social/MIES; crear dashboard interactivo en `src/dashboard/index.html` con Tailwind y Chart.js para la visualización de soporte común y comparación de ingresos pre/post emparejamiento.
- Referencia: `README.md`, `src/dashboard/index.html`

- Fecha: 2026-07-20
- Actor: Programación / Datos / Especialista / Crítico
- Decisión / Comentario: Crear exportador `src/dashboard/export_data_json.ps1` para convertir `data/datos_reales_psm.xlsx` en `src/dashboard/datos_reales_psm.json`; actualizar el dashboard para estimar el Propensity Score con un modelo logit y emparejar por nearest neighbor con datos reales.
- Referencia: `src/dashboard/export_data_json.ps1`, `src/dashboard/index.html`, `src/analysis/psm_bdh_report.md`

- Fecha: 2026-07-20
- Actor: Coordinador / Programación / Datos / Especialista
- Decisión / Comentario: Finalizar la documentación del proyecto con README raíz completo, actualizar la interfaz del dashboard interactivo en `src/dashboard/index.html`, y generar bitácora con referencias metodológicas y fuentes oficiales de ENEMDU e INEC.
- Referencia: `README.md`, `src/dashboard/index.html`, `bitacora_ia.md`
