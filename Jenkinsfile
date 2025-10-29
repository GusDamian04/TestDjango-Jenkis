pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/GusDamian04/TestDjango-Jenkis.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat '. venv/bin/activate && pip install --upgrade pip'
                bat '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Migrate') {
            steps {
                bat '. venv/bin/activate && python manage.py migrate'
            }
        }

        stage('Test') {
            steps {
                bat '. venv/bin/activate && python manage.py test'
            }
        }
    }
}