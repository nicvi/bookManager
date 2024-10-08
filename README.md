# bookManager
This project is a book management system built with FastAPI. It allows users to manage authors and books using a JSON file as a data source.

## Installation
To install the necessary dependencies, run:
```bash
make install
```

# Usage
You can use the following commands to manage the project:

### Running Tests
To run tests and linting, use:
```bash
make run-test
```

### Running the Application
To run the application, use:

```bash
make run-app
```
The application will be available at http://127.0.0.1:7000.

# CI/CD Configuration
This project utilizes a Continuous Integration and Continuous Deployment (CI/CD) pipeline configured with GitHub Actions. The pipeline automates the process of building, testing, and deploying the application using Docker and Kubernetes with Minikube.

### Workflow Overview
The CI/CD workflow is triggered on pull requests to the main branch. Below is a high-level breakdown of the key steps in the pipeline:

1. **Code Checkout:** The workflow checks out the latest code from the repository.

2. **Python Setup:** It sets up the specified version of Python (currently 3.10) for the build environment.

3. **Install Dependencies:** The required dependencies are installed using the make install command.

4. **Run Tests:** The pipeline runs tests using pytest to ensure code quality and functionality.

5. **Build Docker Image:** A Docker image is built for the application and tagged as nicvi/nicvi-repository:latest.

6. **Push Docker Image:** The built Docker image is pushed to the Docker registry. The Docker login credentials are securely stored in GitHub Secrets.

7. **Install Minikube and Dependencies:**

   - Installs necessary dependencies, including conntrack and crictl.
   - Downloads and installs Minikube and kubectl.
8. **Start Minikube:** The pipeline starts a local Minikube cluster using the --driver=none option.

9. **Verify Minikube Status:** The status of the Minikube cluster is verified to ensure it is running correctly.

10. **Deploy to Kubernetes:** The deployment and service configurations are applied using kubectl apply, which deploys the application to the Minikube cluster.

11. **Verify Deployment:** Finally, the workflow verifies the deployment by checking the status of the pods and services in the cluster.

### Requirements
Ensure that you have a valid Docker Hub account and store your Docker username and password as secrets in your GitHub repository (DOCKER_USERNAME and DOCKER_PASSWORD).
This pipeline assumes that you are using a GitHub Actions runner with the appropriate permissions to install and run Docker and Minikube.

### Note
Running Minikube in GitHub Actions may have limitations due to the ephemeral nature of the runners. For production deployments, consider using a managed Kubernetes service for better reliability and scalability.
