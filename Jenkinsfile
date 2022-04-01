pipeline {
    agent any

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
