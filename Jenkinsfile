pipeline {
    agent any
    environment {
        PYTHONPATH = "${WORKSPACE}/src"
        REGISTRY = "docker.io"
        IMAGE_NAME = "dapy3112/football-flask-project"
        SONARQUBE = 'SonarQube'  // Name of the SonarQube server configured in Jenkins
        SONAR_PROJECT_KEY = 'football-backend'  // The key for your SonarQube project
        SONAR_PROJECT_NAME = 'football-backend'  // The name of your project in SonarQube
        IMAGE_TAG = "latest"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
            bat "pip install --no-cache-dir -r requirements.txt"
            }
        }
        stage('Run Tests') {
            steps {
                bat '.\\scripts\\run_tests.bat'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube analysis
                    withSonarQubeEnv('SonarQube') {
                        bat '''
                        sonar-scanner ^
                            -Dsonar.projectKey=%SONAR_PROJECT_KEY% ^
                            -Dsonar.projectName=%SONAR_PROJECT_NAME% ^
                            -Dsonar.sources=src ^
                            -Dsonar.language=python ^
                            -Dsonar.python.coverage.reportPaths=coverage.xml
                        '''
                    }
                }
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                bat "docker push %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }
        stage('Deploy') {
            steps {
                bat '.\\scripts\\deploy.bat'
            }
        }
    }
    post {
        always {
            echo "Pipeline finished. Ensure sensitive data is handled securely."
        }
    }
}
