# 🚀 Portafolio Web 

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Proyecto de **portafolio profesional** desarrollado con **Django 5 y PostgreSQL**, completamente orquestado con **Docker**.

El objetivo del proyecto es demostrar **buenas prácticas de ingeniería de software**, incluyendo:

- Arquitectura desacoplada
- Persistencia segura de datos
- Gestión profesional de variables de entorno
- Infraestructura reproducible mediante contenedores

---

# 📌 Tabla de Contenidos

- [Resumen Ejecutivo](#-resumen-ejecutivo)
- [Stack Tecnológico](#-stack-tecnológico)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Gestión de Seguridad](#-gestión-de-seguridad)
- [Quality Assurance](#-quality-assurance)
- [Autor](#-autor)

---

# 📖 Resumen Ejecutivo

Este sistema representa un **ecosistema web moderno y profesional** construido utilizando **Django como framework principal** y **PostgreSQL como motor de base de datos**.

Toda la infraestructura del proyecto se ejecuta dentro de **contenedores Docker**, lo que garantiza:

- Entornos de desarrollo reproducibles
- Aislamiento completo de dependencias
- Despliegue simplificado
- Persistencia segura de datos

El proyecto aplica principios de **ingeniería de software orientados a robustez, escalabilidad y mantenibilidad**.

---

### Componentes principales

**Contenedor Web**

- Aplicación Django
- Manejo del ORM
- Renderizado de plantillas

**Contenedor DB**

- PostgreSQL
- Persistencia en volumen Docker

**Volumen Docker**

- Garantiza persistencia de datos incluso si el contenedor se elimina
---

# 🧰 Stack Tecnológico

## Backend
- **Python 3.12**
- **Django 5.x**

## Base de Datos
- **PostgreSQL 16**
- Ejecutado en contenedor independiente

## Infraestructura
- **Docker**
- **Docker Compose**

## Seguridad
- **django-environ**
- Variables de entorno mediante `.env`

## Persistencia
- **Docker Volumes** para almacenamiento seguro de datos

## Frontend
- **Bootstrap 5.3**
- Arquitectura de plantillas **DRY**

---

# 🏗 Arquitectura del Sistema

El sistema utiliza una **arquitectura basada en contenedores**, donde cada componente tiene responsabilidades separadas.

```mermaid
graph TD
    User((Usuario)) -->|Navega| Web[Contenedor Django]

    subgraph Docker Network
        Web -->|Lee| Env[Variables .env]
        Web -->|ORM Query| DB[(PostgreSQL 16)]
        DB -->|Persistencia| Volume[(Docker Volume)]
    end

    subgraph Assets
        Web --> Static[Static Files]
        Web --> Media[Media Files]
    end
    

