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

        stage('Dependency Installation') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                bat 'venv\\Scripts\\activate && pip install flake8 pytest' // Explicitly install flake8 and pytest
            }
        }

        stage('Linting') {
             steps {
                bat 'call venv\\Scripts\\activate && python -m flake8 --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics .'
            }
        }

        stage('Build') {
            steps {
                echo 'Nothing to build for Python, skipping...'
            }
        }

       stage('Test Execution') {
            steps {
                bat 'call venv\\Scripts\\activate && python -m pytest tests/'
            }
        }

        stage('Docker Build & Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', '5bcf4aea-f2d6-4730-98fb-ca1755b8c3ef') {
                        def image = docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                        image.push()
                        image.push("latest")
                    }
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
