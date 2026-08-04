# Caso de estudio - Pivoting en laboratorio multihost

## Resumen

Ejercicio académico de compromiso encadenado sobre dos entornos vulnerables conectados por una red interna. El trabajo comenzó con una aplicación expuesta, continuó con acceso al primer host y finalizó con descubrimiento y validación controlada de un segundo servicio interno.

> Entorno: laboratorio aislado y autorizado. Se omiten direcciones, credenciales, flags, versiones exactas y procedimientos operativos completos.

## Objetivo

Analizar cómo la exposición de secretos y la falta de segmentación pueden permitir que un compromiso inicial se extienda hacia otros activos que no eran accesibles directamente desde la red atacante.

## Cadena de ataque

```text
Aplicación expuesta con lectura indebida de archivos
        ↓
Acceso a configuración y credenciales del laboratorio
        ↓
Ingreso a paneles o servicios del primer entorno
        ↓
Ejecución controlada y acceso al contenedor inicial
        ↓
Descubrimiento de una red y servicio interno
        ↓
Pivoting a través del primer entorno
        ↓
Explotación de un segundo servicio vulnerable
        ↓
Acceso al segundo host y evaluación de impacto
```

## Riesgos demostrados

### Exposición de configuración

La lectura de archivos permitió acceder a información que no debía quedar disponible para el proceso web.

**Impacto:** descubrimiento de usuarios, servicios, rutas internas y credenciales reutilizables.

**Remediación:** separar secretos del código, restringir permisos, utilizar gestores de secretos y evitar que la aplicación pueda resolver rutas arbitrarias.

### Reutilización de credenciales

Credenciales obtenidas en un componente permitieron probar acceso a otros servicios del mismo entorno.

**Impacto:** ampliación rápida del compromiso y pérdida de aislamiento entre capas.

**Remediación:** credenciales únicas por servicio, rotación, MFA donde sea aplicable y monitoreo de autenticaciones anómalas.

### Segmentación insuficiente

El primer host tenía visibilidad y conectividad hacia servicios internos que luego pudieron evaluarse desde la posición comprometida.

**Impacto:** movimiento lateral hacia activos no expuestos públicamente.

**Remediación:** segmentación, reglas explícitas de entrada y salida, autenticación entre servicios y política de denegación predeterminada.

### Servicio interno vulnerable

El segundo activo ejecutaba un componente desactualizado o configurado de forma insegura.

**Impacto:** compromiso de un segundo host y aumento del alcance de la intrusión.

**Remediación:** inventario de activos, gestión de parches, reducción de servicios, hardening y análisis continuo de vulnerabilidades.

## Decisiones metodológicas

- Se registraron tanto intentos exitosos como fallidos.
- El movimiento se limitó a los activos incluidos en el laboratorio.
- No se mantuvo persistencia fuera del ejercicio.
- La evidencia pública describe la cadena sin publicar detalles reutilizables.
- Las conclusiones separan vulnerabilidad inicial, controles compensatorios y riesgo residual.

## Competencias demostradas

- Reconocimiento desde una posición externa e interna.
- Enumeración de redes y servicios.
- Análisis de secretos y configuraciones.
- Pivoting y movimiento lateral en laboratorio.
- Encadenamiento de vulnerabilidades entre activos.
- Evaluación de segmentación y mínimo privilegio.
- Documentación técnica de una intrusión multietapa.

## Mapeo conceptual a MITRE ATT&CK

El ejercicio puede relacionarse, a nivel formativo, con categorías como:

- Initial Access.
- Credential Access.
- Discovery.
- Lateral Movement.
- Command and Control.
- Privilege Escalation.
- Persistence.

Este mapeo es conceptual. Para presentarlo como una emulación formal de adversario sería necesario documentar técnicas y sub-técnicas exactas, reglas de enfrentamiento, telemetría defensiva y objetivos de detección.

## Limitaciones

- La infraestructura fue creada deliberadamente con fallas.
- No se midió la respuesta de un SOC o Blue Team.
- No existió una campaña asociada a un actor real.
- No se realizaron acciones sobre terceros ni fuera del alcance académico.
