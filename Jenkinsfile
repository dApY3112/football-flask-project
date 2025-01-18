pipeline {
    agent any
    environment {
        PYTHONPATH = "${WORKSPACE}/src"
        REGISTRY = "docker.io"  // Docker Hub registry URL (default)
        IMAGE_NAME = "dapy3112/football-backend"  // Replace with your Docker Hub username and image name
        IMAGE_TAG = "latest"  // Define the tag for the image
        DOCKER_CLI_EXPERIMENTAL = "enabled"  // Enable experimental features for Docker (e.g., scan)
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
                bat '.\\scripts\\run_tests.bat'  // Run your test script
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."  // Use Windows environment variable syntax
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
    // Add Docker image scanning for vulnerabilities (using Docker Scan or Trivy)
          stage('Scan Docker Image for Vulnerabilities') {
            steps {
                script {
                    // Check if Docker Scan is available
                    bat 'docker scan --help'
                    
                    // If Docker Scan is available
                    bat 'docker scan --accept-license %IMAGE_NAME%:%IMAGE_TAG%'  // For Docker's native scanning

                    // If you are using Trivy, replace the command with Trivy scan
                    // Ensure Trivy is installed and available in the environment
                    // bat 'trivy image %IMAGE_NAME%:%IMAGE_TAG%'  // If using Trivy for scanning
                }
            }
        }
        
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    docker.withRegistry('https://docker.io', 'dockerhub-credentials') {
                        def image = docker.image("${IMAGE_NAME}:${IMAGE_TAG}") // Create the Docker image reference
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

