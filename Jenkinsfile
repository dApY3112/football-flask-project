pipeline {
    agent any
    environment {
        PYTHONPATH = "${WORKSPACE}/src"
        REGISTRY = "docker.io"
        IMAGE_NAME = "dapy3112/football-flask-project"
        SONARQUBE = 'SonarQube'  
        SONAR_PROJECT_KEY = 'football-backend'  
        SONAR_PROJECT_NAME = 'football-backend'  
        VERCEL_TOKEN = credentials('VERCEL_TOKEN')
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
        stage('Deploy to Vercel') {
            steps {
                script {
                    bat """
                    REM Authenticate Vercel CLI
                    vercel login --token %VERCEL_TOKEN%
                    
                    REM Deploy the project
                    vercel --prod --token %VERCEL_TOKEN%
                    """
                }
            }
        }
    }
    post {
            success {
                echo "Deployment to Vercel successful!"
            }
            failure {
                echo "Deployment failed. Check logs for details."
            }
        }
    }
