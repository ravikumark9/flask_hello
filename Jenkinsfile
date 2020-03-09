node {
	checkout scm
	docker.withRegistry('docker.io', 'dockerhub') {
		def customImage = docker.build("ravi/flaskapp")
		customImage.push()
	}
}
