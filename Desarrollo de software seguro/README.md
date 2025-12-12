🧩 Desarrollo de Software Seguro

Trabajos prácticos orientados al análisis, diseño e implementación de software seguro, con foco en APIs REST, autenticación, control de accesos y buenas prácticas alineadas con OWASP y estándares modernos.

🔍 TP Individual – Análisis y Endurecimiento de una API en Flask

Objetivo:
Analizar una API desarrollada en Flask + MySQL, identificar vulnerabilidades de seguridad y aplicar técnicas de hardening siguiendo las recomendaciones de OWASP API Security Top 10.

Principales riesgos identificados:

Autenticación básica (BasicAuth) con credenciales fijas.

Credenciales de base de datos hardcodeadas.

Falta de validación de entradas (riesgo de inyección).

Manejo inseguro de errores (fuga de información).

Exposición del servicio sin TLS.

Manejo incorrecto de fechas y conexiones.

Medidas de endurecimiento aplicadas:

Reemplazo de BasicAuth por tokens Bearer.

Propuesta de uso de OAuth 2.0 + JWT para entornos productivos.

Gestión de secretos mediante variables de entorno.

Validación de entradas con expresiones regulares (whitelisting).

Manejo seguro de errores y logging interno.

Uso de HTTPS/TLS.

Registro de eventos en UTC.

Cierre seguro de conexiones (try/finally).

Tecnologías y conceptos utilizados:

Python

Flask

MySQL

OWASP API Security Top 10

OAuth 2.0

JWT

📄 Documentación completa:

Análisis y Endurecimiento de una API en Flask: Identificación de Riesgos y Aplicación de Buenas Prácticas OWASP.pdf 

🔐 TP Grupal – Autenticación Segura en APIs con Flask y FastAPI + OpenAPI

Objetivo:
Implementar y comparar distintos mecanismos de autenticación en APIs, utilizando Flask y FastAPI, y documentar los endpoints con el estándar OpenAPI.

Análisis teórico:

Métodos de autenticación:

Basic Auth

Autenticación por IP

API Key

OAuth 2.0

JWT (JSON Web Token)

Comparativa entre Flask y FastAPI:

Arquitectura (WSGI vs ASGI)

Rendimiento y concurrencia

Validación de datos

Seguridad

Documentación automática

Implementación práctica:

API en Flask con autenticación HTTP Basic.

API equivalente en FastAPI usando fastapi.security.

Entorno virtual en Debian GNU/Linux 12.

Pruebas de acceso autenticado y no autenticado.

Documentación automática con Swagger UI (/docs).

Resultados destacados:

FastAPI genera documentación OpenAPI automáticamente.

Mejor validación y seguridad nativa en FastAPI.

Flask ofrece mayor control manual, ideal para aprendizaje.

OpenAPI mejora trazabilidad, auditoría y mantenimiento.

Repositorio del proyecto:

👉 https://github.com/Dante2617012022/api_segura_tp

Tecnologías utilizadas:

Python

Flask

FastAPI

OpenAPI / Swagger UI

HTTPie

Debian GNU/Linux

📄 Documentación completa:

Implementación y Comparativa de Autenticación Segura en APIs con Flask y FastAPI: Análisis Práctico y Documentación OpenAPI.pdf 

🧠 Competencias adquiridas

Secure Software Development (SSDLC)

OWASP API Security Top 10

Diseño de APIs seguras

Autenticación y autorización

OAuth 2.0 y JWT

Documentación OpenAPI

Flask vs FastAPI (comparativa técnica)

Hardening de aplicaciones backend
