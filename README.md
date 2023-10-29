# Sentiment Analysis FastAPI Project

This is a sentiment analysis API developed with FastAPI

### Prerequisites

- Docker
- Docker Compose
- Google Cloud Platform
- PostgreSQL

### Configuration

#### Environment Variables

Create a file named `.env` in the project root directory and add your configurations, following the example below:

```env
POSTGRES_DB=sentimentanalysis_db
POSTGRES_USER=username
POSTGRES_PASSWORD=password
HOST=localhost | db | IP
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${HOST}:5432/${POSTGRES_DB}
GCP_CREDENTIALS_FILE=gcp.json
```

Google Cloud Credentials

To authenticate with the Google Cloud Platform, you'll need to create a service account, download the JSON key file, and set the GCP_CREDENTIALS_FILE environment variable in your .env file to point to this key file.


```json
{
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": "",
  "universe_domain": ""
}
```
#### Installing

```sh
git clone https://github.com/WilliamSilveiraF/sentiment-analysis.git


cd sentiment-analysis


docker compose up
```

#### Usage

```sh
The server is up and running at http://localhost:8080/
```

#### Flow Diagram

The user invokes the endpoint with an audio file. Subsequently, the Speech-To-Text API from Google Cloud Platform transcribes the content. With the generated text, we will run summarization and sentiment analysis models, and store the resulting data in database for retrieval at a later time.

![all text](https://github.com/WilliamSilveiraF/sentiment-analysis/blob/main/Diagram.png)