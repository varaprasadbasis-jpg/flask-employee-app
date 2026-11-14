pipeline {


    agent any


    stages {


        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                '''
            }
        }


        stage('Install Dependencies') {
            steps {
                sh '''
                    ./venv/bin/python -m pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }


        stage('Run Flask Application') {
            steps {
                sh '''
                    ./venv/bin/python app.py 
                '''
            }
        }


    }


    post {
        success {
            echo 'Flask application started successfully!'
        }


        failure {
            echo 'Pipeline execution failed!'
        }
    }
}
