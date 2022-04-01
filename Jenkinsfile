pipeline {
    agent any
    // agent { docker { image 'python:3.10.1-alpine' } }

    stages {
        stage('first stage') {
            steps {
                sh 'ls'
            }
        }
        stage('build') {
            steps {
                sh 'docker build -t scripts .'
            }
        }
        stage('run mock script1') {
            steps {
                sh 'docker run --rm scripts python main.py script1 mock 9'
            }
        }
        stage('last stage') {
            steps {
                echo 'last stage'
            }
        }
    }
}
