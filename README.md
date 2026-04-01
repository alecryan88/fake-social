# fake-social

`fake-social` is a small Python-based event generator for producing synthetic social activity data. The project focuses on creating two streams of events: user signups and user sessions. It is designed to be run locally for development or deployed into AWS using Terraform-managed infrastructure.

## Project overview

The repository contains:

- Application code under `app/`
- Infrastructure definitions at the repository root
- Terraform resources for AWS deployment
- Configuration-driven event generation

The main dependencies and technologies used in the codebase are:

- Python 3.9
- Faker
- boto3
- PyYAML
- Docker
- Docker Compose
- Terraform
- DynamoDB
- AWS

## Architecture overview

The application centers on two generator flows:

- `app/events/create_signups.py` generates synthetic signup events
- `app/events/create_sessions.py` generates synthetic session events

Both flows use `app/config.yml` to control event generation rates and dimensions. The configuration file defines the parameters that influence how much data is produced and how event dimensions are shaped.

At a high level, the project works like this:

1. Load configuration from `app/config.yml`
2. Generate synthetic records for signups and sessions
3. Write events to the target sink, including AWS-backed storage when deployed

## Repository layout

```text
.
├── app/
│   ├── config.yml
│   └── events/
│       ├── create_sessions.py
│       └── create_signups.py
├── docker-compose.yml
├── Dockerfile
├── terraform/
└── README.md
```

## Prerequisites

To work with the project locally, you will need:

- Python 3.9
- Docker
- Docker Compose
- Terraform, if you plan to provision AWS infrastructure
- AWS credentials, if you plan to deploy or write to AWS resources

## Local development setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd fake-social
```

### 2. Create a Python environment

Use your preferred Python 3.9 environment manager. For example:

```bash
python3.9 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install the Python dependencies required by the application. The project uses Faker, boto3, and PyYAML.

```bash
pip install -r requirements.txt
```

If the repository is being run in a containerized workflow, use the Docker instructions below instead.

### 4. Review configuration

Before running the generators, inspect `app/config.yml` and confirm the event rates and dimensions are set appropriately for your environment.

### 5. Run the generators

The repository is organized around the signup and session generators in `app/events/`. Run the appropriate generator entrypoints from your local environment according to the application’s current structure.

## Docker usage

Build the image:

```bash
docker build -t fake-social .
```

Run the application in a container:

```bash
docker run --rm fake-social
```

## Docker Compose usage

If you prefer Compose for local orchestration, use the repository’s `docker-compose.yml` file:

```bash
docker compose up --build
```

## Configuration

The primary application configuration lives in `app/config.yml`.

This file controls:

- Event generation rates
- Event dimensions
- Generator-specific parameters used by the signup and session flows

Update `app/config.yml` when you want to adjust the volume or shape of generated data.

## Terraform and AWS deployment

AWS infrastructure is defined with Terraform in the repository root and related infrastructure files.

Typical deployment workflow:

1. Review the Terraform configuration and any environment-specific variables
2. Authenticate with AWS using credentials that can provision the required resources
3. Initialize Terraform

```bash
terraform init
```

4. Review the planned infrastructure changes

```bash
terraform plan
```

5. Apply the configuration

```bash
terraform apply
```

The project uses DynamoDB and AWS as part of the deployment target, so ensure the necessary AWS resources and permissions are available before running the generators against the cloud environment.

## Event generators

### Signup generator

`app/events/create_signups.py` generates synthetic user signup activity. Use it when you need a stream of new-account events for testing or data seeding.

### Session generator

`app/events/create_sessions.py` generates synthetic user session activity. Use it to produce session-like events associated with the generated users.

Both generators are configuration-driven and should be adjusted through `app/config.yml` rather than hardcoding generation values.
