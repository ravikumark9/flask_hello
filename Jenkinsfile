node {
	checkout scm
	docker.withRegistry('https://registry.dockerhub.com', 'dockerhub') {
		def customImage = docker.build("ravi/flaskapp")
		customImage.push()
	}
}
