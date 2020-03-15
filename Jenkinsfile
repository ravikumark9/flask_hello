pipeline
{
    options
    {
        buildDiscarder(logRotator(numToKeepStr: '3'))
    }
    agent any
    environment 
    {
        VERSION = 'latest'
        PROJECT = 'flask_hello'
        IMAGE = 'flask_hello:latest'
        ECRURL = '514433652690.dkr.ecr.us-east-1.amazonaws.com'
        ECRCRED = 'ecr:us-east-1:awscred'
    }
    stages
    {
      stage('S3copy') 
        {      
            steps {
                withAWS(region:'us-east-1',credentials:'awscred')\
                {
                    s3Download(file:'tests3.txt', bucket:'testjenkinsdocker', path:'', force:true)
                }
                   sh 'mv /var/lib/jenkins/workspace/flask_hello/tests3.txt/tests3.txt /var/lib/jenkins/workspace/rr/'
            }
        }
    
      stage('Build preparations')
        {
            steps
            {
                script 
                {
                    // calculate GIT lastest commit short-hash
                    gitCommitHash = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                    shortCommitHash = gitCommitHash.take(7)
                    // calculate a sample version tag
                    VERSION = shortCommitHash
                    // set the build display name
                    currentBuild.displayName = "#${BUILD_ID}-${VERSION}"
                    IMAGE = "$PROJECT:$VERSION"
                }
            }
        }
        stage('Docker build')
        {
            steps
            {
                script
                {
                    // Build the docker image using a Dockerfile
                    docker.build("$IMAGE")
                }
            }
        }
        stage('Docker push')
        {
            steps
            {
                script
                {
                    // login to ECR - for now it seems that that the ECR Jenkins plugin is not performing the login as expected. I hope it will in the future.
                    //sh("eval \$(aws ecr get-login --no-include-email | sed 's|https://console.aws.amazon.com/ecr/repositories?region=us-east-1||')")
                    sh("eval \$(aws ecr get-login --registry-ids 514433652690 --region us-east-1)")
                    // Push the Docker image to ECR
                    //docker.withRegistry(ECRURL, ECRCRED)
                    docker.withRegistry([url: "ECRURL",credentialsId: "$ECRCRED"]
                    {
                        docker.image(IMAGE).push()
                    }
                }
            }
        }
    }
    
    post
    {
        always
        {
            // make sure that the Docker image is removed
            sh "docker rmi $IMAGE | true"
        }
    }
} 
