# Base OS
FROM python:3.7-stretch

MAINTAINER Tanmay Thakur <tanmaythakurbrn2rule@gmail.com>

# Install Build Utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential

# Check Python Environment
RUN python --version
RUN pip --version

# set the working directory for containers
WORKDIR .

# Copy Files
COPY requirements.txt .

# Install Dependencies
RUN run.sh

# Test Env
RUN test.sh

# Running the server
CMD ["python", "app.py"] 
