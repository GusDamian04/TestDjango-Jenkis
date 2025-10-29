pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/GusDamian04/TestDjango-Jenkis.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat '''
                echo === Creando entorno virtual ===
                "C:\\Users\\GusDamian\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv

                echo === Activando entorno virtual e instalando dependencias ===
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Migraciones') {
            steps {
                bat '''
                echo === Ejecutando migraciones ===
                cd api_back
                call ..\\venv\\Scripts\\activate
                "C:\\Users\\GusDamian\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" manage.py migrate
                '''
            }
        }

        stage('Pruebas') {
            steps {
                bat '''
                echo === Ejecutando pruebas ===
                cd api_back
                call ..\\venv\\Scripts\\activate
                "C:\\Users\\GusDamian\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" manage.py test
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado correctamente.'
        }
        failure {
            echo 'Error durante el pipeline. Revisa los logs anteriores.'
        }
    }
}
