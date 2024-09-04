# Cricket Commentary Application

This project is a Dockerized FastAPI application designed for managing live cricket commentary. It consists of two separate FastAPI services:
- **Publish Service**: Publishes cricket commentary to a Kafka topic.
- **Consume Service**: Consumes and processes cricket commentary from the Kafka topic.

Both services are containerized using Docker and are configured to communicate with a Kafka broker running in a separate container. Zookeeper is also included as Kafka's dependency.


## Prerequisites

- Docker
- Docker Compose

## Setup and Running the Application

### 1. Clone the Repository

```bash
git clone [https://github.com/your-repo/cricket-commentary-app.git](https://github.com/rahuladream/cricket-commentary-kafka)
cd cricket-commentary-app

## Build and Start the Docker Containers
Build the Docker images and start all the services using Docker Compose:

```bash
docker-compose build
docker-compose up
```

## Access the Services

- Publish Service: Available at http://localhost:8001. Use this service to publish cricket commentary to Kafka.
- Consume Service: Available at http://localhost:8002. This service consumes commentary from Kafka

## Testing the Services

```bash
curl -X POST "http://localhost:8001/v1/publish_commentary/" -H "Content-Type: application/json" -d "{\"commentary\": \"Player X hits a six!\"}"
```

Make sure to have websocket connection this
[WebSocket-Chrome](https://chrome.google.com/webstore/detail/mdmlhchldhfnfnkfmljgeinlffmdgkjo)
```bash
curl "http://localhost:8002/ws/commentary/"
```
