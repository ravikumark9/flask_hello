node {
	checkout scm
	docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
		def customimage = docker.build("ravi/flaskapp")
		customImage.push()
	}
}
