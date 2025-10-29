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
                bat 'py -m venv venv'
                bat '. venv/Scripts/activate && pip install --upgrade pip'
                bat '. venv/Scripts/activate && pip install -r requirements.txt'
            }
        }

        stage('Migrate') {
            steps {
                bat '. venv/Scripts/activate && py manage.py migrate'
            }
        }

        stage('Test') {
            steps {
                bat '. venv/Scripts/activate && py manage.py test'
            }
        }
    }
}