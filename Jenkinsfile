def agentlb(lb) {
    node(lb) {
        try {
            cleanWs()
            checkout scm
            ws('${workspace}/${env.BRANCH_NAME}/${env.BUILD_NAME}') {
            sh '''
                docker login -u $DH_USR -p $DH_PSW
                docker stop cfend || true
                docker stop cbend || true
                docker stop sqliteweb || true
                docker rm -f cfend || true
                docker rm -f cbend || true
                docker rm -f sqliteweb || true
                docker rmi -f fimg || true
                docker rmi -f bimg || true
                docker-compose up --no-cache --build webapp
                docker logout
            '''
            }       
        } catch (Exception e) {
            echo 'Your build and deploy stage are fail on ${lb}: ${e.message}'
            throw e
        }
    }
}

pipeline {
    agent none
    environment {
        DH = credentials('dh-credentials')
    }
    stages {
        stage('build and deploy') {
            steps {
                if (env.BRANCH_NAME == 'dev') {
                    agentlb('dev')
                } else if (env.BRANCH_NAME == 'staging') {
                    agentlb('staging')
                } else if (env.BRANCH_NAME == 'ps') {
                    agentlb('ps')
                } else
                sh 'echo "There is nothing to work ${lb} branch."'
            }
        }
    }
}