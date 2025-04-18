pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('5bcf4aea-f2d6-4730-98fb-ca1755b8c3ef') // Jenkins credentials ID
        DOCKER_IMAGE = "ishwari20/devopstodo" // <-- replace with your actual Docker Hub repo name
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Dependency Installation') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Linting') {
            steps {
                sh '. venv/bin/activate && flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics'
            }
        }

        stage('Build') {
            steps {
                echo 'Nothing to build for Python, skipping...' // optional
            }
        }

        stage('Test Execution') {
            steps {
                sh '. venv/bin/activate && pytest tests/'
            }
        }

        stage('Docker Build & Push') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                        def image = docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                        image.push()
                        image.push('latest')
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
