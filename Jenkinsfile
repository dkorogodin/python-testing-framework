pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "python-testing-framework:latest"
        DB_INFRA = "${params.DB_INFRA ?: 'container'}"
        SELENIUM_GRID = "${params.SELENIUM_GRID ?: 'container'}"
        CONCURRENCY_PARAMS = "${params.CONCURRENCY_PARAMS ?: '-n 4 --dist=loadscope'}"
        ALLURE_DIR = "${params.ALLURE_DIR ?: 'target/reports/allure-results'}"
    }

    stages {
        stage('Show Parameters') {
            steps {
                sh '''
                    echo "DB_INFRA=$DB_INFRA"
                    echo "SELENIUM_GRID=$SELENIUM_GRID"
                    echo "CONCURRENCY_PARAMS=$CONCURRENCY_PARAMS"
                    echo "TEST_MARKERS=$TEST_MARKERS"
                    echo "ALLURE_DIR=$ALLURE_DIR"
                    echo "ADDITIONAL_PARAMS=$ADDITIONAL_PARAMS"
                '''
            }
        }

        stage('Build Test Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Build and Start MySQL Docker Containers') {
            when {
                expression { env.DB_INFRA == 'local' }
            }
            steps {
                echo "Starting MySQL containers because DB_INFRA=$DB_INFRA"
                sh 'docker compose -f data/docker/docker-compose-mysql.yml up -d'
            }
        }

        stage('Build and Start Selenium Grid Docker Container') {
            when {
                expression { env.SELENIUM_GRID == 'local' }
            }
            steps {
                echo "Starting Selenium Grid because SELENIUM_GRID=$SELENIUM_GRID"
                sh 'docker compose -f data/docker/docker-compose-selenium-grid.yml up -d'
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
                    pytest $CONCURRENCY_PARAMS -m $TEST_MARKERS --alluredir=$ALLURE_DIR $ADDITIONAL_PARAMS
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
            echo 'Cleaning up containers...'
            sh 'docker compose -f data/docker/docker-compose-mysql.yml down || true'
            sh 'docker compose -f data/docker/docker-compose-selenium-grid.yml down || true'

            archiveArtifacts artifacts: 'target/reports/allure-results/**', allowEmptyArchive: true
            cleanWs()
        }
    }
}
