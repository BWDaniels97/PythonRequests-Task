pipeline{
        agent any

	stages{

		stage ('install Docker'){
                        steps{
                                sh "bash install-docker.sh"
                        }
                }
		stage ('Deploy application'){
                        steps{
                                sh "bash deploy.sh"

                        }

        	}
	}
}
