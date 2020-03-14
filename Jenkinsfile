node {
	checkout scm
	docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
		def customImage = docker.build("ravikumark9/flaskrepo:1")
		customImage.push()
	docker.image('flaskrepo').withRun('-p 8080:80')
	}
}
