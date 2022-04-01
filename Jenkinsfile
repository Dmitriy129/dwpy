String cronTime = '10 * * * *'
// String cronTime = '27 23 1 4 *'

pipeline {
    agent any

     parameters {
      string(name: 'COURSE_ID')
      string(name: 'CM_ID')
      string(name: 'GITHUB_REPO')
      string(name: 'GITHUB_PR_REGEX')
    }
    triggers {
        parameterizedCron('''
            41 21 1 4 * %COURSE_ID=47;CM_ID=1553;GITHUB_REPO=Dmitriy129/dw-test;GITHUB_PR_REGEX=^(\\w*)_(lr1)$
            */5 * * * * %COURSE_ID=47;CM_ID=1553;GITHUB_REPO=Dmitriy129/dw-test;GITHUB_PR_REGEX=^(\\w*)_(lr1)$
        ''')
    }

    // triggers { 
    //     cron(cronTime) 
    // }

    stages {
        stage('build') {
            steps {
                sh 'docker build -t scripts .'
            }
        }
        // stage('run script1') {
        //     steps {
        //         withCredentials([string(credentialsId: 'GitHubAccessToken', variable: 'GITHUB_ACCESS_TOKEN'), string(credentialsId: 'MoodleAccessToken', variable: 'MOODLE_ACCESS_TOKEN') ]){
        //             sh '''
        //             docker run \
        //             -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN \
        //             -e MOODLE_ACCESS_TOKEN=$MOODLE_ACCESS_TOKEN \
        //             -e COURSE_ID=47 \
        //             -e CM_ID=1553 \
        //             -e GITHUB_REPO="Dmitriy129/dw-test" \
        //             -e GITHUB_PR_ID=2 \
        //             --rm \
        //             scripts\
        //             python main.py\
        //             script1 mock 3
        //             '''
        //         }
        //     }
        // }
        stage('run script2') {
             when {
                triggeredBy 'ParameterizedTimerTriggerCause'
            }
            steps {
                withCredentials([string(credentialsId: 'GitHubAccessToken', variable: 'GITHUB_ACCESS_TOKEN'), string(credentialsId: 'MoodleAccessToken', variable: 'MOODLE_ACCESS_TOKEN') ]){
                    sh '''
                    docker run \
                    -e GITHUB_ACCESS_TOKEN=$GITHUB_ACCESS_TOKEN \
                    -e MOODLE_ACCESS_TOKEN=$MOODLE_ACCESS_TOKEN \
                    -e COURSE_ID="$COURSE_ID" \
                    -e CM_ID="$CM_ID" \
                    -e GITHUB_REPO="$GITHUB_REPO" \
                    -e GITHUB_PR_REGEX="$GITHUB_PR_REGEX" \
                    --rm \
                    scripts\
                    python main.py\
                    script2 mock 8
                    '''
                }
            }
        }
    }
}
