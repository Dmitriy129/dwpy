pipeline {
    agent { docker { image 'python:3.10.1-alpine' } }
    
    stages {
        stage('first stage') {
            steps {
                echo 'first stage'
            }
        }
        stage('run script') {
            steps {
                sh 'python jt.py'
            }
        }
        stage('last stage') {
            steps {
                echo 'last stage'
            }
        }
    }
}
