pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/youssefahmed8/flask-app-eks-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("$DOCKER_IMAGE")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("$DOCKER_IMAGE").inside {
                        sh 'python3 -m unittest discover tests/'
                    }
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_credentials_id') {
                        docker.image("$DOCKER_IMAGE").push("${env.BUILD_NUMBER}") // Push with build number
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                script {
                    sh 'ansible-playbook -i inventory deploy-app.yml'
                }
            }
        }
    }

    post {
        always {
            mail to: 'Build_status@gmail.com',// edit with your email
            subject: "Job ${env.JOB_NAME} Build #${env.BUILD_NUMBER} Status",
            body: "The build ${env.BUILD_URL} completed with status: ${currentBuild.currentResult}"
        }
    }
}
