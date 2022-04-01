pipeline {
    agent any

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
                withCredentials([string(credentialsId: 'GitHubAccessToken', variable: 'GITHUB_ACCESS_TOKEN'), string(credentialsId: 'MoodleAccessToken', variable: 'MOODLE_ACCESS_TOKEN') ]){
                    sh 'docker run -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN -e MOODLE_ACCESS_TOKEN=$MOODLE_ACCESS_TOKEN --rm dw python main.py script1 mock 9'
                }
            }
        }
        stage('last stage') {
            steps {
                echo 'last stage'
            }
        }
    }
}
