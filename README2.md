# Integración con JSONPlaceholder usando FastAPI

## Descripción del Proyecto

Este proyecto es desarrollado como parte de una prueba técnica, el cual se basa en FastAPI para lograr el consumo de la API de [JSONPlaceholder](https://jsonplaceholder.typicode.com/) para obtener datos de usuarios y sus publicaciones asociadas.

---

## Alcance del proyecto

- Endpoint que permite la consulta de un usuario por ID desde JSONPlaceholder.
- Endpoint para consultar publicaciones de un usuario específico o del último usuario obtenido.
- Registro solicitudes y errores mediante un sistema de log en archivos y consola.
- Manejo de excepciones HTTP para aclarar el motivo de los errores.

---

## Requisitos Previos

- **Python 3.X+**
- **pip3** (administrador de paquetes de Python)

Cuando esté seguro de cumplir con estos requisitos, clone el repositorio usando:

   ```bash
    git clone <url-del-repositorio>
   ```

Una vez clonado, asegurese de usar un entorno virtual para evitar la instalación global de paquetes que aquí fueron usados. Puede crear un entorno virtual y activarlo usando los siguientes comandos:

   ```bash
    python3 -m venv ./venv
    source env/bin/activate
   ```

En el repositorio se encuentra un archivo "requirements.txt", el cual le será de utilidad para la instalción de los paquetes necesarios para la ejecución del proyecto, para esto, ejecute el siguiente comando:

   ```bash
    pip3 install -r requirements.txt 
   ```

Una vez cumplido esto, es posible proceder con la ejecución del proyecto

---

## Ejecución

Dentro del repositorio, será posible encontrar dos puntos de partida para la ejecución del proyecto, los cuales corresponden a la ejecución de las pruebas unitarias predefinidas para los endpoints, y la ejecución regular del proyecto, a continuación las instrucciones para la ejecución de ambos puntos de partida:

1. **Ejecución de pruebas**:

    Las pruebas unitarias definidas, se desarrollaron usando pytest, por lo que, para la ejecución de las mismas puede usar los siguientes comandos:

   ```bash
   
   pytest #Para una ejecución de todas las pruebas
   pytest tests/test_endpoints.py::<NombreDelTest> -v #Para la ejecución de un test determinado
   ```
2. **Ejecución de la aplicación**:

    Para una ejecución regular de la aplicación, es posible usar el siguiente comando:

   ```bash
   
   fastapi dev app/main.py #Para una ejecución usando fastapi en un servidor de desarrollo
   ```