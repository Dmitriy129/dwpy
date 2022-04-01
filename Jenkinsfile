pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'docker build -t scripts .'
            }
        }
        stage('run script') {
            steps {
                withCredentials([string(credentialsId: 'GitHubAccessToken', variable: 'GITHUB_ACCESS_TOKEN'), string(credentialsId: 'MoodleAccessToken', variable: 'MOODLE_ACCESS_TOKEN') ]){
                    sh '''
                    docker run \
                    -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN \
                    -e MOODLE_ACCESS_TOKEN=$MOODLE_ACCESS_TOKEN \
                    --rm \
                    scripts\
                    python main.py\
                    script1 mock 9
                    '''
                }
            }
        }
    }
}
