pipeline {
    agent any

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
            }
        }
        stage('Acceptance test'){
            steps{
                echo 'Acceptance...'
            }
        }
        stage('Deploy'){
            steps {
                echo'Deploying...'
            }
        }
    }
}