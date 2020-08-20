pipeline{
        agent any

	stages{

		stage ('Deploy application'){
                        steps{
                                sh "sudo -t docker-compose up"

                        }

        	}
	}
}
