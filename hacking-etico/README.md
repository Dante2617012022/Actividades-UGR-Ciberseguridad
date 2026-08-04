# Hacking Ético - Laboratorios autorizados

Selección curada de trabajos realizados en la materia **Hacking Ético** de la Tecnicatura Universitaria en Ciberseguridad.

Los ejercicios fueron desarrollados sobre máquinas vulnerables, CTF y laboratorios aislados. La documentación pública resume metodología, hallazgos, impacto y remediación sin publicar credenciales, flags ni payloads reutilizables.

## Competencias trabajadas

- Reconocimiento pasivo y activo.
- Enumeración de hosts, puertos, servicios y aplicaciones.
- Identificación y análisis de vulnerabilidades conocidas.
- Explotación manual y controlada.
- Obtención y estabilización de shells.
- Enumeración local y escalada de privilegios en Linux.
- Reutilización controlada de credenciales y movimiento lateral.
- Pivoting entre entornos de laboratorio.
- Persistencia y limpieza posterior, únicamente como práctica académica.
- Elaboración de informes técnicos y ejecutivos.
- Recomendaciones de hardening y remediación.

## Casos de estudio recomendados

### 1. Auditoría de aplicación web en CTF

Cadena de compromiso documentada desde reconocimiento y enumeración hasta explotación controlada y post-explotación limitada.

[Leer caso de estudio](case-studies/authorized-web-assessment.md)

### 2. WordPress y escalada de privilegios en Linux

Análisis manual de una vulnerabilidad en WordPress, acceso administrativo, ejecución controlada, movimiento entre usuarios y escalada por configuraciones inseguras.

[Leer caso de estudio](case-studies/wordpress-linux-compromise-lab.md)

### 3. Pivoting en laboratorio multihost

Ejercicio de compromiso encadenado con descubrimiento de red interna, acceso a un segundo servicio y análisis de exposición entre contenedores.

[Leer caso de estudio](case-studies/pivoting-multihost-lab.md)

## Matriz resumida de prácticas

| Práctica | Foco principal | Técnicas trabajadas |
|---|---|---|
| Reconocimiento inicial | Superficie de ataque | DNS, cabeceras, Nmap, enumeración web y revisión de tecnologías |
| El Blog de M2 | WordPress y Linux | CVE, creación de usuario, plugin, shell, SUID, sudo y escalada |
| Mi primera chamba | Aplicación y sistema | Enumeración, acceso inicial, post-explotación y revisión local |
| DDLR Pwneable 3 | Explotación Linux | Servicios vulnerables, credenciales, escalada y documentación |
| DDLR Pwneable 4 | Entorno multihost | Traversal, credenciales, pivoting, segundo host y persistencia controlada |
| Auditoría TP9 | Reporte profesional | Alcance, metodología, evidencias, criticidad, impacto y remediación |

## Diferencia entre pentesting y red teaming

El material demuestra una base práctica de **pentesting junior** y fundamentos de técnicas utilizadas en red teaming, como post-explotación, movimiento lateral, persistencia y pivoting.

No se presenta como experiencia profesional de Red Team porque los ejercicios no constituyen una campaña completa contra una organización productiva, con reglas de enfrentamiento, emulación de adversario, coordinación defensiva y medición formal de detección.

## Herramientas utilizadas en los laboratorios

- Debian y Kali Linux.
- VirtualBox y Docker.
- Nmap, Gobuster, cURL y herramientas DNS.
- Burp Suite y DevTools.
- Netcat y shells de laboratorio.
- WordPress y phpMyAdmin vulnerables.
- Scripts de enumeración y análisis local.
- GTFOBins y referencias de CVE para validación académica.

## Alcance ético

Consultar [ETHICS_AND_SCOPE.md](../ETHICS_AND_SCOPE.md). Ninguna técnica documentada debe utilizarse fuera de un entorno propio o expresamente autorizado.
