pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('5bcf4aea-f2d6-4730-98fb-ca1755b8c3ef') // Jenkins credentials ID
        DOCKER_IMAGE = "ishwari20/devopstodo"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Linting') {
            steps {
                bat 'docker run --rm -v %cd%:/app -w /app ishwari20/devopstodo:latest flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
            }
        }

        stage('Build') {
            steps {
                echo 'Nothing to build for Python, skipping...'
            }
        }

        stage('Test Execution') {
            steps {
                bat 'docker run --rm -v %cd%:/app -w /app ishwari20/devopstodo:latest pytest tests/'
            }
        }

        stage('Docker Build & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: '5bcf4aea-f2d6-4730-98fb-ca1755b8c3ef', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%"
                    bat "docker build -t ishwari20/devopstodo:${BUILD_NUMBER} ."
                    bat "docker tag ishwari20/devopstodo:${BUILD_NUMBER} ishwari20/devopstodo:latest"
                    bat "docker push ishwari20/devopstodo:${BUILD_NUMBER}"
                    bat "docker push ishwari20/devopstodo:latest"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
