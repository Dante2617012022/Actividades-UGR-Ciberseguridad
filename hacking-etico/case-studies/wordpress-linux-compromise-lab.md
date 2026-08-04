# Caso de estudio - WordPress y escalada de privilegios en Linux

## Resumen

Resolución académica de una máquina vulnerable basada en WordPress y Linux. El ejercicio cubrió reconocimiento, análisis de una vulnerabilidad conocida, reproducción manual del comportamiento, acceso inicial, movimiento entre usuarios, escalada de privilegios y revisión de persistencia.

> Entorno: contenedor y máquina de laboratorio autorizados. Se omiten versiones exactas, credenciales, flags y comandos explotables.

## Objetivo

Comprender cómo una vulnerabilidad en una aplicación puede convertirse en un compromiso del sistema cuando se combina con configuraciones inseguras de usuarios, permisos y tareas administrativas.

## Proceso aplicado

1. Despliegue de la máquina vulnerable.
2. Reconocimiento de servicios y tecnologías.
3. Identificación de WordPress y componentes instalados.
4. Investigación de una vulnerabilidad asociada a un plugin.
5. Lectura y análisis lógico del exploit disponible.
6. Reproducción manual de la condición vulnerable.
7. Acceso administrativo en la aplicación.
8. Ejecución controlada y obtención de shell limitada.
9. Enumeración de usuarios, archivos, SUID y permisos `sudo`.
10. Movimiento a otro usuario mediante información disponible en el laboratorio.
11. Escalada de privilegios por una configuración insegura.
12. Revisión de persistencia y limpieza posterior.

## Cadena de compromiso

```text
Componente WordPress vulnerable
        ↓
Creación o acceso administrativo no autorizado
        ↓
Carga controlada de componente en el CMS
        ↓
Ejecución como usuario del servicio web
        ↓
Enumeración local y movimiento a otro usuario
        ↓
Abuso de permisos SUID o sudo mal configurados
        ↓
Acceso privilegiado en el laboratorio
```

## Aspectos destacados

### Análisis antes de ejecutar

En lugar de depender únicamente de una herramienta automática, el trabajo revisó la lógica del exploit y reprodujo manualmente la condición vulnerable. Esto permitió comprender:

- endpoint afectado;
- parámetros requeridos;
- condición previa;
- acción realizada por la aplicación;
- evidencia de éxito;
- limitaciones del método.

### Separación entre acceso web y acceso al sistema

Obtener privilegios administrativos en WordPress no equivalía automáticamente a controlar el sistema operativo. Fue necesario analizar cómo el CMS podía ejecutar código, qué usuario operaba el servicio y qué permisos tenía.

### Enumeración local

Después del acceso inicial se revisaron:

- usuarios y grupos;
- archivos accesibles;
- variables y configuraciones relevantes;
- binarios SUID;
- permisos `sudo`;
- servicios y procesos;
- posibles rutas de movimiento lateral.

### Escalada por configuración insegura

La escalada final dependió de permisos excesivos y no solamente de la vulnerabilidad inicial.

**Lección:** una aplicación vulnerable aumenta su impacto cuando el sistema operativo no aplica mínimo privilegio, separación de cuentas y controles sobre ejecutables administrativos.

## Recomendaciones

- Mantener WordPress y plugins actualizados.
- Eliminar componentes no utilizados.
- Restringir la instalación de plugins y temas.
- Ejecutar el servicio web con privilegios mínimos.
- Revisar periódicamente SUID, capabilities y reglas `sudo`.
- Evitar credenciales reutilizadas y secretos en archivos legibles.
- Registrar cambios administrativos y alertar sobre nuevas cuentas.
- Aislar la aplicación mediante contenedores o perfiles de seguridad correctamente configurados.
- Comprobar la eliminación de cualquier persistencia introducida durante pruebas autorizadas.

## Competencias demostradas

- Investigación y validación de CVE.
- Comprensión de código de explotación.
- Seguridad de CMS.
- Post-explotación Linux.
- Enumeración y escalada de privilegios.
- Análisis de configuraciones inseguras.
- Documentación de una cadena completa en laboratorio.

## Limitaciones

- La máquina fue diseñada para ser vulnerable.
- Las técnicas se aplicaron con fines académicos.
- No se evaluaron controles de detección de una organización real.
- El ejercicio no constituye experiencia profesional sobre sistemas productivos.
