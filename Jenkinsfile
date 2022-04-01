String cronTime = "13 23 1 4 *"

pipeline {
    agent any

    triggers { 
        cron(cronTime) 
    }

    stages {
        stage('build') {
            steps {
                sh 'docker build -t scripts .'
            }
        }
        stage('run script1') {
            steps {
                withCredentials([string(credentialsId: 'GitHubAccessToken', variable: 'GITHUB_ACCESS_TOKEN'), string(credentialsId: 'MoodleAccessToken', variable: 'MOODLE_ACCESS_TOKEN') ]){
                    sh '''
                    docker run \
                    -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN \
                    -e MOODLE_ACCESS_TOKEN=$MOODLE_ACCESS_TOKEN \
                    -e COURSE_ID=47 \
                    -e CM_ID=1553 \
                    -e GITHUB_REPO="Dmitriy129/dw-test" \
                    -e GITHUB_PR_ID=2 \
                    --rm \
                    scripts\
                    python main.py\
                    script1 mock 3
                    '''
                }
            }
        }
        stage('run script2') {
            steps {
                withCredentials([string(credentialsId: 'GitHubAccessToken', variable: 'GITHUB_ACCESS_TOKEN'), string(credentialsId: 'MoodleAccessToken', variable: 'MOODLE_ACCESS_TOKEN') ]){
                    sh '''
                    docker run \
                    -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN \
                    -e MOODLE_ACCESS_TOKEN=$MOODLE_ACCESS_TOKEN \
                    -e COURSE_ID=47 \
                    -e CM_ID=1553 \
                    -e GITHUB_REPO="Dmitriy129/dw-test" \
                    -e GITHUB_PR_REGEX="^(\\w*)_(lr1)$" \
                    --rm \
                    scripts\
                    python main.py\
                    script2 mock 5
                    '''
                }
            }
        }
    }
}
