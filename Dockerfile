# Using official Python image
FROM python:3.12-slim

# Prevent installation from getting stuck by disabling interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Python3 and pip
RUN apt-get update && \
    apt-get install -y \
# For Nvidia install
        curl \
        gnupg2 && \
# Removing apt metadata
    rm -rf /var/lib/apt/lists/*

# Add NVIDIA package repositories
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
&& curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# Install Nvidia's container toolkit
RUN apt-get update && \
    apt-get install -y \
        nvidia-container-toolkit && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Install vLLM and Gradio
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose Gradio port
EXPOSE 7860
ENV GRADIO_SERVER_NAME=0.0.0.0

CMD ["python3", "GradioAppFiles/gradio_chatapp.py"]
