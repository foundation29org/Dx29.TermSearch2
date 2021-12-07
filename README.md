<div style="margin-bottom: 1%; padding-bottom: 2%;">
	<img align="right" width="100px" src="https://dx29.ai/assets/img/logo-Dx29.png">
</div>

Dx29 TermSearch
==============================================================================================================================================
### Overview

This project allows the symptoms and disease searches to be carried out, in different languages (EN and ES).

It is used in the [Dx29 application](https://dx29.ai/) and therefore how to integrate it is described in the [Dx29 architecture guide](https://dx29-v2.readthedocs.io/en/latest/index.html).


It is programmed in Python, and the structure of the project is as follows:

>- src folder: This is made up of two folders: Sample, which contains an example project of how to use the project and Dx29.TermSearch2, which contains the source code of the project. The latter contains: 
>>- app.py file: Is the main file, that access the aforementioned methods.
>>- WebAPI folder: With the files to expose the method funcionality.
>>- Lib folfer: with the files to tah contains the logic to perform the relevant operations.
>>- Deployment folder: with example files to perform the deployment tasks.
>>- requirements.txt and setup.py for perform the build tasks.
>- .gitignore file
>- README.md file

<p>&nbsp;</p>

### Getting Started

####  1. Configuration: Pre-requisites

This is a Python project, therefore it will be necessary to have a valid [programming environment](https://packaging.python.org/en/latest/tutorials/installing-packages/#) installed to work with this project.

In the code file "requirements.txt" are defined all the libraries that we must have [pre-installed](https://packaging.python.org/en/latest/tutorials/installing-packages/#requirements-files) for the execution of this project.

This project doesn't use external services, so it is not neccessary to configure any secret key for running it.

<p>&nbsp;</p>

####  2. Download and installation

Download the repository code with `git clone` or use download button.

Having a Python](https://www.python.org/downloads/) environment installed, installs the requirements.txt packages with [pip](https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line):
``` pip install -r requirements.txt ```

<p>&nbsp;</p>

####  3. Latest releases

The latest release of the project deployed in the [Dx29 application](https://dx29.ai/) is: v0.15.00.

<p>&nbsp;</p>

#### 4. API references

**Search symptoms**:
>- GET request
>- Query paramenters: 
>>- q or text for the search
>>- lang: Select language for the results from the list of available languages: en or es
>>- rows: Number of results
>- URL: http://127.0.0.1:8080/api/v1/search/symptoms?q={query}&lang={lang}&rows={rows}
>- Result request: List of Terms (objects) with: identifier, name and description strings, and a list of strings with the identifiers of the synonyms.

**Search diseases**:
>- GET request
>- Query paramenters: 
>>- q or text for the search
>>- lang: Select language for the results from the list of available languages: en or es
>>- rows: Number of results
>- URL: http://127.0.0.1:8080/api/v1/search/diseases?q={query}&lang={lang}&rows={rows}
>- Result request: List of Terms (objects) with: identifier, name and description strings, and a list of strings with the identifiers of the synonyms.

<p>&nbsp;</p>

### Build and Test

#### 1. Build

On the one hand, the setup.py file is the local build script for this project: ``` python setup.py ```

On the other hand, we could use Docker. 
Docker builds images automatically by reading the instructions from a Dockerfile – a text file that contains all commands, in order, needed to build a given image.

>- A Dockerfile adheres to a specific format and set of instructions.
>- A Docker image consists of read-only layers each of which represents a Dockerfile instruction. The layers are stacked and each one is a delta of the changes from the previous layer.

Consult the following links to work with Docker:

>- [Docker Documentation](https://docs.docker.com/reference/)
>- [Docker get-started guide](https://docs.docker.com/get-started/overview/)
>- [Docker Desktop](https://www.docker.com/products/docker-desktop)

The first step is to run docker image build. We pass in . as the only argument to specify that it should build using the current directory. This command looks for a Dockerfile in the current directory and attempts to build a docker image as described in the Dockerfile. 
```docker image build . ```

[Here](https://docs.docker.com/engine/reference/commandline/docker/) you can consult the Docker commands guide.

<p>&nbsp;</p>

#### 2. Deployment

To work locally, it is only necessary to install the project and build it. 

The deployment of this project in an environment is described in [Dx29 architecture guide](https://dx29-v2.readthedocs.io/en/latest/index.html), in the deployment section. In particular, it describes the steps to execute to work with this project as a microservice (Docker image) available in a kubernetes cluster:

1. Create an Azure container Registry (ACR). A container registry allows you to store and manage container images across all types of Azure deployments. You deploy Docker images from a registry. Firstly, we need access to a registry that is accessible to the Azure Kubernetes Service (AKS) cluster we are creating. For this purpose, we will create an Azure Container Registry (ACR), where we will push images for deployment.
2. Create an Azure Kubernetes cluster (AKS) and configure it for using the prevouos ACR
3. Import image into Azure Container Registry
4. Publish the application with the YAML files that defines the deployment and the service configurations. 

This project includes, in the Deployments folder, YAML examples to perform the deployment tasks as a microservice in an AKS. 
Note that this service is configured as "ClusterIP" since it is not exposed externally in the [Dx29 application](https://dx29.ai/), but is internal for the application to use. If it is required to be visible there are two options:
>- The first, as realised in the Dx29 project an API is exposed that communicates to third parties with the microservice functionality.
>- The second option is to directly expose this microservice as a LoadBalancer and configure a public IP address and DNS.

>>- **Interesting link**: [Deploy a Docker container app to Azure Kubernetes Service](https://docs.microsoft.com/en-GB/azure/devops/pipelines/apps/cd/deploy-aks?view=azure-devops&tabs=java)

<p>&nbsp;</p>

####  3. Testing

The Sample folder contains an example of a C# project that uses the symptom search project.
In it, you can see how the project is used and the tests that have been carried out on it.

<p>&nbsp;</p>

### Contribute

Please refer to each project's style and contribution guidelines for submitting patches and additions. The project uses [gitflow workflow](https://nvie.com/posts/a-successful-git-branching-model/). 
According to this it has implemented a branch-based system to work with three different environments. Thus, there are two permanent branches in the project:
>- The develop branch to work on the development environment.
>- The master branch to work on the test and production environments.

In general, we follow the "fork-and-pull" Git workflow.

>1. Fork the repo on GitHub
>2. Clone the project to your own machine
>3. Commit changes to your own branch
>4. Push your work back up to your fork
>5. Submit a Pull request so that we can review your changes

The project is licenced under the **(TODO: LICENCE & LINK & Brief explanation)**

<p>&nbsp;</p>
<p>&nbsp;</p>

<div style="border-top: 1px solid !important;
	padding-top: 1% !important;
    padding-right: 1% !important;
    padding-bottom: 0.1% !important;">
	<div align="right">
		<img width="150px" src="https://dx29.ai/assets/img/logo-foundation-twentynine-footer.png">
	</div>
	<div align="right" style="padding-top: 0.5% !important">
		<p align="right">	
			Copyright © 2020
			<a style="color:#009DA0" href="https://www.foundation29.org/" target="_blank"> Foundation29</a>
		</p>
	</div>
<div>