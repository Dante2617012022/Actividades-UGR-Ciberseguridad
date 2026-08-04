# Tratamiento de Vulnerabilidades - Laboratorios autorizados

Trabajos prácticos realizados por **Dante Gabriel Balbuena Atar** durante la Tecnicatura Universitaria en Ciberseguridad de la Universidad del Gran Rosario.

La materia abordó identificación, validación, explotación controlada, análisis de impacto y remediación sobre aplicaciones intencionalmente vulnerables y CTF educativos.

> Todas las pruebas se realizaron en entornos de laboratorio autorizados. Este material no habilita pruebas sobre sistemas de terceros.

## Metodología aplicada

1. Reconocimiento de la aplicación y superficie expuesta.
2. Enumeración de rutas, parámetros, tecnologías y controles.
3. Identificación de vulnerabilidades.
4. Validación manual con el menor impacto necesario.
5. Encadenamiento de hallazgos cuando correspondía.
6. Registro de evidencias y resultados negativos.
7. Análisis de impacto.
8. Recomendaciones de mitigación.

## Trabajos

### TP1 - DVWA

Laboratorio introductorio de vulnerabilidades web:

- fuerza bruta en entorno controlado;
- command injection;
- CSRF;
- inclusión local de archivos;
- carga insegura de archivos;
- SQL Injection;
- XSS DOM, reflejado y almacenado;
- CSP y redirecciones inseguras.

[Ver informe académico](TP%201%20DVWA.pdf)

### TP2 - Mutillidae II

Evaluación de una aplicación web vulnerable con múltiples técnicas:

- SQL Injection en distintos contextos;
- autenticación y cookies inseguras;
- command injection;
- carga de archivos y ejecución controlada;
- log poisoning combinado con LFI;
- IDOR;
- clickjacking y cabeceras faltantes.

[Ver informe académico](TP%202%20mutillidae.pdf)

### TP3 - Panel Django vulnerable

Resolución de desafíos de seguridad sobre una aplicación Django preparada para laboratorio:

- XSS;
- CSRF;
- IDOR;
- open redirect;
- manipulación de cookies;
- validación de flags y cuestionario técnico.

[Ver informe académico](TP%203%20Django.pdf)

### TP4 - bWAPP

Análisis y encadenamiento de vulnerabilidades:

- bypass de controles de interfaz;
- command injection y ejecución limitada;
- SQL Injection almacenada y por búsqueda;
- log poisoning y LFI;
- HTML injection;
- carga insegura de archivos;
- XSS almacenado;
- exposición de sesión en laboratorio.

[Ver informe académico](TP%204%20BWAPP.pdf)

### TP5 - CTF DDLR

Ejercicio integrador de auditoría web:

- SQL Injection;
- acceso no autorizado a información de laboratorio;
- carga insegura de archivos;
- Local File Inclusion;
- revisión de cookies;
- ejecución controlada y shell limitada;
- recomendaciones de remediación.

[Ver informe académico](TP%205%20ctf%20ddlr.pdf)

## Competencias demostradas

- Pentesting web junior en laboratorios.
- Conocimiento práctico de OWASP Top 10.
- Validación manual de SQLi, XSS, CSRF, LFI, IDOR y command injection.
- Encadenamiento de vulnerabilidades.
- Uso académico de Burp Suite, Nmap, cURL, Netcat, Hydra y Docker.
- Análisis de impacto y riesgo residual.
- Elaboración de documentación técnica con evidencias y mitigaciones.

## Presentación profesional

Los informes completos conservan el formato original de entrega. Para una lectura ejecutiva y sanitizada, consultar los [casos de estudio de Hacking Ético](../hacking-etico/README.md) y la [plantilla de reporte](../metodologia/plantilla-reporte-pentest.md).

## Alcance ético

Consultar [ETHICS_AND_SCOPE.md](../ETHICS_AND_SCOPE.md).
