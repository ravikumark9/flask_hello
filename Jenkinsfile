node {
	checkout scm
	docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
		def customImage = docker.build("ravikumark9/flaskrepo")
		customImage.push()
	docker.image('ravikumark9/flaskrepo').withRun('-p 8080:80')
	}
}
