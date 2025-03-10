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
   
## References

### Videos
- [Fazt Code]. (29, Marzo 2023). Tutorial de Apache en Docker para principiantes (httpd) . YouTube. https://www.youtube.com/watch?v=-563XKoRfZ8&list=LL&index=1
- Schürmann, N. [HolaMundo]. (07 July 2022). Aprende Docker ahora! curso completo gratis desde cero! Youtube https://www.youtube.com/watch?v=4Dko5W96WHg

### Website Template

- Free Css. https://www.free-css.com/free-css-templates/page296/spering

  ### Sites

  - Docker Hub. https://hub.docker.com/_/httpd
  - Aprende HTML y CSS - Curso Desde Cero: https://www.freecodecamp.org/espanol/news/aprende-html-y-css-curso-desde-cero/
  - Usando la API de Kaggle con Google Colab para carga y descarga de datasets: https://platzi.com/tutoriales/1794-pandas/6926-usando-la-api-de-kaggle-con-google-colab-para-carga-y-descarga-de-datasets/#:~:text=Lo%20primero%20que%20debemos%20hacer,a%20la%20api%20de%20Kaggle.
  - 
    


