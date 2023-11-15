# Flask Search API

## Introduction
Welcome to the Flask Search API repository! This project offers a powerful search API built with Flask, capable of finding the most similar names in a dataset based on input sentences.

## Features
- Search functionality to find similar names.
- Health check endpoint to ensure the service is running.

## Installation

### Prerequisites
Ensure you have Docker installed on your system. If not, follow the installation guides for your platform:
- [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
- [Docker for Linux](https://docs.docker.com/engine/install/)

### Pull the Docker Image
from the link -> [Docker pull web page](https://hub.docker.com/r/nehoraymelamed/searc_layers_service)
```bash
docker pull nehoraymelmed/searc_layers_service:tag_name
```


## API Usage
For detailed API usage and examples, please refer to the [API Documentation](./api_documentation.html) included in this repository.

## Testing the API
Ensure you have all necessary Python requirements installed:

```bash
pip install -r requirements.txt
```

Run the test script [test api](./FlaskSearch/test_api.py)  to test the API endpoints.


