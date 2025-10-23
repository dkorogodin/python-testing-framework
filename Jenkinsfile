pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "python-testing-framework:latest"
        ALLURE_DIR = "target/reports/allure-results"
    }

    stages {
        stage('Build Test Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh '''
                docker run --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    --privileged \
                    -v $(pwd):/app -w /app \
                    -e DOCKER_HOST_INTERNAL=1 \
                    $DOCKER_IMAGE \
                    pytest -n 4 --dist=loadscope -m api --mock_service=local --alluredir=$ALLURE_DIR
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: "$ALLURE_DIR"]]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'target/reports/allure-results/**', allowEmptyArchive: true
            cleanWs()
        }
    }
}
