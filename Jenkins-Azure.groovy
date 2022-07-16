pipeline {
    agent any
    
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'docker',url: 'https://github.com/mazzielafa/TDD-in-python.git'
	        }
        }        
        stage('Requirements') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Unit/Integration tests') {
            steps {
                echo 'Unit/Integration...'
                sh 'python3 -m unittest discover -s tests/unit -v'
            }
        }        
        stage('Acceptance tests') {
            steps {
                echo 'Acceptance...'
                sh 'python3 -m unittest discover -s tests/acceptance -v'
            }
        }     
        stage('Create image') {
            steps {
                echo 'creating image...'
                sh 'docker build -t mazziebootcampregistry.azurecr.io/TDD-Python-Test:latest -f Dockerfile .'
            }
        } 
        stage('Publish image') {
            steps {
                echo 'pushing image...'
                withDockerRegistry([ credentialsId: "azure-credentials", url: "https://mazziebootcampregistry.azurecr.io" ]) {
                    sh 'docker push mazziebootcampregistry.azurecr.io/TDD-Python-Test:latest'
                }
            }
        } 
    }
    post {
        always {
            echo 'post do this always...'
        }
        success{
            echo 'post do this when success...'
        }
        failure {
            echo 'post do this when failure...'
        }
        cleanup{
            echo 'post do this when cleanup...'
            deleteDir()
        }
    }
}