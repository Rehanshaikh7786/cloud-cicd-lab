
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub repository connected'
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Cloud CI/CD Lab'
                sh 'echo Build completed successfully'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application'
                sh 'echo All tests passed'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage'
                sh 'echo Deployment completed successfully'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: CI/CD PIPELINE COMPLETED'
        }
        failure {
            echo 'ERROR: PIPELINE FAILED'
        }
    }
}
