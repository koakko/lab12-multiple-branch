pipeline {
    agent none
    environment {
        wkd = '~/'
        DH = credentials('dh-credentials')
    }
    stages {
        stage('build and deploy webapp') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'dev') {
                        node('dev') {
                            cleanWs()
                            ws('${wkd}') {
                                checkout GitSCM
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
                            }
                        }
                    } else if (env.BRANCH_NAME == 'staging') {
                        node('staging') {
                            cleanWs()
                            ws('${wkd}') {
                                checkout GitSCM
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
                            }
                        }
                    } else if (env.BRANCH_NAME == 'ps') {
                        node('ps') {
                            cleanWs()
                            ws('${wkd}') {
                                checkout GitSCM
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
                            }
                        }
                    }
                }
            }
        }
    }
}