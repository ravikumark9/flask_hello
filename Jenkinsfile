node {
	checkout scm
	docker.withRegistry('https://hub.docker.com', 'dockerhub') {
		def customImage = docker.build("ravi/flaskapp")
		customImage.push()
	}
}
