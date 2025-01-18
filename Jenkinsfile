pipeline {
    agent any
    environment {
        PYTHONPATH = "${WORKSPACE}/src"
        REGISTRY = "docker.io"  // Docker Hub registry URL (default)
        IMAGE_NAME = "dapy3112/football-flask-project"  // Replace with your Docker Hub username and image name
        IMAGE_TAG = "latest"  // Define the tag for the image
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '.\\scripts\\run_tests.bat'  // Run your test script
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub using credentials from Jenkins
                    docker.withRegistry('https://docker.io', 'dockerhub-credentials') {
                        // Authentication done here
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                bat "docker build -t dapy3112/football-flask-project:latest ."  // Use Windows environment variable syntax
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                 script {
                        bat 'docker logout'  // Clear any existing credentials
                        docker.withRegistry('https://docker.io', 'dockerhub-credentials') {
                        def image = docker.image("dapy3112/football-flask-project:latest") // Create the Docker image reference
                        image.push()  // Push the image to Docker Hub
                    }
                }
             }
         }
        stage('Deploy') {
            steps {
                bat '.\\scripts\\deploy.bat'  // Run your deployment script
            }
        }
    }
    post {
        always {
            // Clean up resources or perform any necessary security post-actions
            echo "Pipeline finished. Make sure to clean up and rotate sensitive credentials if needed."
        }
    }
}

