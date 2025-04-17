# gradio-distill-r1
 A simple chat app using Gradio and vLLM.
 
## Table of contents
* [Overview](#overview)
* [Requirements](#requirements)
* [Functionalities](#functionalities)
* [Setting up (Python environment)](#setting-up-python-environment)
* [Setting up (Docker)](#setting-up-docker)
* [TO DO](#to-do)

# Overview

This project implements a chatbot using the vLLM library for inference, combined with the Gradio framework for the web interface. The app uses the DeepSeek-R1-Distill-Qwen-1.5B model to generate conversational responses.

## Requirements

- Python 3.12
- Linux
- Nvidia GPU: compute capability 7.0 or higher (e.g., V100, T4, RTX20xx, A100, L4, H100, etc.)

## Functionalities

- Interactive UI: Easy interaction with the chatbot via a simple web interface using Gradio.
- Thinking Process Visualization: A checkbox to for displaying the model's thinking process, which shows how the model arrives to its response.

## Setting up (Python environment)
To ensure a clean and isolated development environment for this project, it is recommended to set it up within a Python virtual environment. Follow the steps below to create and activate a virtual environment for the project:

### Create a Virtual Environment
Create a new virtual environment for the project by executing the following command:
```bash
python3 -m venv projectdir
```

### Activate the Virtual Environment
Activate the virtual environment by running the following command:

```bash
source projectdir/bin/activate
```
Once activated, your command prompt should indicate the name of the virtual environment.

### Install Project Dependencies
With the virtual environment active, you can now install the project dependencies. Assuming you have a requirements.txt file in your project directory, open a terminal in the folder and run the following command:
```bash
pip install -r requirements.txt
```
This command will install all the necessary dependencies for the project.

### Run the Application
You are now ready to run the web application within the virtual environment. Execute the following command to start the application:
```bash
python3 GradioAppFiles/gradio_chatapp.py
```
You can exit the application by using Ctrl+C

Remember to always activate the virtual environment before working on the project. If you need to deactivate the virtual environment, simply run the command:
```bash
deactivate
```
By following these steps, you can easily set up and work on the project in an isolated Python virtual environment, ensuring a clean development environment and avoiding conflicts with other Python projects on your system.

## Setting up (Docker)
To containerize the project and run it using Docker, follow the steps below:

### Build the Docker Image
Open a terminal or command prompt and navigate to the root directory of the project, where the Dockerfile is located. Run the following command:

```bash
docker build -t gradio_app .
```
This command builds a Docker image using the Dockerfile in the current directory. The -t flag allows you to specify a name for the image, such as gradio_app.

### Run the Docker Container: After successfully building the Docker image, you can run a container based on that image. Execute the following command:

```bash
docker run --gpus all -p 7860:7860 testapp_gradio
```
This command starts a Docker container using the testapp_gradio image and maps port 7860 (Gradio's default) from the container to port 7860 on your local machine. Adjust the port mapping if you wish to use a different port.

### Access the Gradio Application
With the Docker container running, you can access the application in a web browser by visiting http://localhost:7860. You should see it running inside the Docker container.

# TO DO

Implement RAG to address AI Hallucinations.