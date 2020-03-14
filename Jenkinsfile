node {
	checkout scm
	docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
		def customImage = docker.build("ravikumark9/flaskrepo")
		customImage.push()
	        def customImage1 = docker.image('flaskrepo')
		customImage1.withRun('-p 8080:80')
	}
}
