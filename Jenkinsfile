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
        // Define credentials IDs
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
        SNYK_CREDENTIALS_ID = 'snyk-token'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh "pip install --no-cache-dir -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                sh './scripts/run_tests.sh'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh """
                    sonar-scanner \
                      -Dsonar.projectKey=${env.SONAR_PROJECT_KEY} \
                      -Dsonar.projectName=${env.SONAR_PROJECT_NAME} \
                      -Dsonar.sources=src \
                      -Dsonar.host.url=http://your-sonar-server \
                      -Dsonar.login=${env.SONAR_LOGIN}
                    """
                }
            }
        }

        stage('Security Scan - DAST') {
            steps {
                script {
                    def zapHome = tool('OWASP ZAP');
                    def zaproxy = new org.zaproxy.clientapi.core.ClientApi('localhost', 8090, null);
                    zaproxy.accessUrl('http://your-application-url');
                }
            }
        }

        stage('Dependency Scan with Snyk') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${env.SNYK_CREDENTIALS_ID}", passwordVariable: 'SNYK_TOKEN', usernameVariable: 'SNYK_USERNAME')]) {
                    sh "snyk auth ${SNYK_TOKEN}"
                    sh "snyk test --all-projects"
                    sh "snyk monitor --all-projects"
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${env.DOCKERHUB_CREDENTIALS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${env.IMAGE_NAME}:${env.IMAGE_TAG} ."
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                sh "docker push ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
            }
        }

        stage('Deploy to Vercel') {
            steps {
                script {
                    sh """
                    # Authenticate Vercel CLI
                    vercel login --token ${env.VERCEL_TOKEN}
                    
                    # Deploy the project
                    vercel --prod --token ${env.VERCEL_TOKEN}
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
