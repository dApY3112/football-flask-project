pipeline {
    agent {
        docker { image 'docker:19.03.12' }
    }
    environment {
        PYTHONPATH = "${WORKSPACE}/src"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '.\\scripts\\run_tests.bat'  // Change to batch script for Windows
            }
        }

        stage('Package') {
            steps {
                bat 'docker build -t football-backend .'  // Same docker command, ensure Docker is installed on Windows
            }
        }
        stage('Deploy') {
            steps {
                bat '.\\scripts\\deploy.bat'  // Change to batch script for Windows
            }
        }
    }
}
