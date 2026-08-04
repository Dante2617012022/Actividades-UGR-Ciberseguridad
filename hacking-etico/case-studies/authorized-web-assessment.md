# Caso de estudio - Auditoría web autorizada en CTF

## Resumen

Evaluación académica de una aplicación web intencionalmente vulnerable. El trabajo se organizó como una auditoría técnica: alcance, reconocimiento, enumeración, validación de hallazgos, explotación controlada, análisis posterior, criticidad y recomendaciones.

> Entorno: CTF autorizado. Los nombres, credenciales, direcciones, flags y payloads se omiten deliberadamente.

## Objetivo

Determinar si vulnerabilidades de la aplicación podían encadenarse hasta comprometer la confidencialidad, integridad o ejecución del servicio, sin exceder el entorno asignado.

## Metodología

1. Definición del alcance y límites del ejercicio.
2. Reconocimiento de DNS, cabeceras y tecnologías visibles.
3. Enumeración de puertos, rutas y parámetros.
4. Validación manual de vulnerabilidades.
5. Explotación mínima necesaria para demostrar impacto.
6. Post-explotación limitada y revisión del contexto alcanzado.
7. Clasificación de hallazgos y propuesta de remediación.
8. Registro de evidencias y bitácora de comandos.

## Cadena de ataque observada

```text
Parámetro vulnerable a SQL Injection
        ↓
Acceso a información de usuarios de laboratorio
        ↓
Ingreso al panel administrativo
        ↓
Carga de archivo con validación insuficiente
        ↓
Inclusión local de archivo
        ↓
Ejecución controlada en el servidor
        ↓
Shell limitada para comprobar impacto
```

La cadena muestra que vulnerabilidades aparentemente separadas pueden aumentar significativamente el impacto cuando se combinan.

## Hallazgos principales

### Inyección SQL

La aplicación construía consultas sin separar correctamente datos y código. Se demostró que un atacante dentro del laboratorio podía alterar la consulta y acceder a información no prevista.

**Impacto:** exposición de registros, acceso no autorizado y facilitación de ataques posteriores.

**Remediación:** consultas parametrizadas, validación de tipos, privilegios mínimos en la base y manejo uniforme de errores.

### Control de acceso insuficiente

El panel administrativo dependía de credenciales que pudieron obtenerse a través de otra vulnerabilidad y no incorporaba controles adicionales de contexto o segundo factor.

**Impacto:** acceso a funciones sensibles y aumento de la superficie de explotación.

**Remediación:** MFA para roles privilegiados, sesiones seguras, limitación por función, auditoría y protección contra intentos repetidos.

### Carga insegura de archivos

El formulario validaba insuficientemente el tipo y comportamiento del archivo recibido.

**Impacto:** almacenamiento de contenido activo y posibilidad de encadenamiento con otras fallas.

**Remediación:** allowlist de extensiones y MIME, validación por contenido, nombres aleatorios, almacenamiento fuera del webroot y bloqueo de ejecución.

### Inclusión local de archivos

Un parámetro permitía seleccionar recursos del servidor sin una lista cerrada de valores válidos.

**Impacto:** lectura de archivos y ejecución indirecta al combinarse con la carga insegura.

**Remediación:** eliminar rutas aportadas por el usuario, utilizar identificadores internos, normalizar rutas y aplicar una allowlist estricta.

### Configuración de sesión mejorable

Las evidencias permitieron revisar atributos y alcance de cookies.

**Impacto:** mayor exposición ante robo o abuso de sesión si las cookies no se restringen correctamente.

**Remediación:** `HttpOnly`, `Secure`, `SameSite`, expiración razonable, rotación de sesión y HTTPS.

## Post-explotación controlada

Luego de obtener ejecución limitada, se verificaron únicamente:

- usuario y contexto del proceso;
- versión general del sistema;
- interfaces y servicios visibles desde el contenedor;
- archivos de configuración relevantes para determinar impacto;
- posibilidades de escalada y movimiento lateral, incluyendo intentos no exitosos.

No se realizaron acciones destructivas ni se mantuvo acceso fuera del ejercicio.

## Evidencia generada

El paquete académico original incluye:

- reporte ejecutivo y técnico;
- capturas clasificadas por fase;
- salidas de reconocimiento y enumeración;
- bitácora de comandos;
- registro de hallazgos;
- intentos exitosos y no exitosos;
- recomendaciones de remediación.

La versión pública no incluye material sensible ni instrucciones operativas completas.

## Competencias demostradas

- Pentesting web con metodología.
- Encadenamiento de vulnerabilidades.
- Análisis de impacto técnico y de negocio.
- Diferenciación entre evidencia y suposición.
- Registro de pruebas negativas.
- Elaboración de recomendaciones priorizadas.
- Comunicación ejecutiva y técnica.

## Limitaciones

- El activo era deliberadamente vulnerable.
- No existió una organización productiva ni usuarios reales.
- No se realizó retesteo posterior a una corrección.
- El ejercicio no equivale por sí solo a una operación profesional de red team.
