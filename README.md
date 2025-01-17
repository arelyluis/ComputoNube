# Dockerized Web Service

##  Contact
* Arely Hilda Luis Tiburcio | arelyhildalt@gmail.com

## License
GNU General Public License v3.0
## Affilation
Extraodinary Distributed Computing (Cloud Computing) class January 2025, designed and developed at the Universidad Nacional Autonoma de México(UNAM), at the Escuela Nacional de Estudios Superiores (ENES Morelia). 

## Introduction

The following project is part of the extraodinary exam for the distributed computing (cloud computing) class.  
As indicated, a personal web page is created and served through a web server that is dockerized.


## How to execute the project

### Prerequirements
- **Python 3.x** install.
- **Git** install
- **Docker** install

### Steps
1. Clone this repository:
   ```bash
   git clone <https://github.com/arelyluis/ComputoNube.git>
   ```
2. Go to folder ComputoNube:
   ```bash
   cd <ComputoNube>
   ```
3. Go To folder spering_prueba:
   ```bash
   cd <spering_prueba>
   ```
4. Build image:
   ```bash
    docker build -t --final-docker .
   ```

5. Run Docker:
   ```bash
    docker run -p 4000:80 --name final-apache -d final-docker
   ```
6. Visit http://localhost:4000⁠ and you will see It works!:
   ```bash
    docker run -p 4000:80 --name final-apache -d final-docker
   ```
## References
- Apellido, Iniciales. [Fazt Code]. (29, Marzo 2023). Tutorial de Apache en Docker para principiantes (httpd) . YouTube. https://www.youtube.com/watch?v=-563XKoRfZ8&list=LL&index=1


