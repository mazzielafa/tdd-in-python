pipeline {
    agent any
    
     environment {
     username = 'admin'
     password = 'Pa55w.rd'
    }

    stages{
        stage('Build'){
            steps{
                git branch: 'main', url: 'https://github.com/mazzielafa/TDD-in-python.git'
                bat 'dir'
            }
        }
        stage('Compile') {
            steps {
                dir ('standalone'){
                    echo 'Building...'
                    bat 'dir'
                }
            }
        }
        stage('Test'){
            steps{
                echo 'Testing...'
            }
        }
        stage ('Package'){
            steps {
                echo 'Packaging...'
                // bat 'c:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe -m build'
                bat 'dir'
            }
        }
        stage('Acceptance test'){
            steps{
                echo 'Acceptance...'
            }
        }
        stage('Deploy'){
             steps {
                echo 'Deploying....'
                echo "u${username} -p${password}"
                bat "twine upload  --repository-url http://localhost:8081/repository/tdd-in-maven-repo/ dist/* -u${username} -p${password}"
            }
        }
    }
}
