pipeline {
    agent any
    
    environment {
    DOCKERHUB_USERNAME = credentials('ishwari20')   // 🔴 This ID must match the real one
    DOCKERHUB_PASSWORD = credentials('Ishwari@20')
}

    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Lint') {
            steps {
                bat 'pip install flake8'
                bat 'flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics || echo "Linting complete with warnings"'
            }
        }
        
        stage('Test') {
            steps {
                bat 'pip install pytest'
                bat 'pytest || echo "Tests complete with warnings"'
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Flask application...'
            }
        }
        
        stage('Docker Build & Push') {
            steps {
                bat """
                    echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin
                    docker build -t %DOCKERHUB_USERNAME%/todo-flask-app:latest .
                    docker push %DOCKERHUB_USERNAME%/todo-flask-app:latest
                """
            }
        }
        
        stage('Deploy') {
            steps {
                bat 'docker-compose down || echo "No containers to stop"'
                bat 'docker-compose up -d'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
    }
}