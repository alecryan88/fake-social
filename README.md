# fake-social

A small infrastructure-backed sample project that generates mock social-app events and ingests them as part of a near-real-time data pipeline.

## Overview

`fake-social` appears to be a demo project for producing synthetic social activity data using the Python `faker` library and packaging it for local or cloud execution.

The repository includes:

- `app/` - the Python application and Docker assets
- Terraform configuration (`main.tf`, `aws.tf`, `providers.tf`, `variables.tf`) for AWS infrastructure
- Docker files for building and running the app container

## Repository layout

```text
.
├── app/
│   ├── config.yml
│   ├── docker-compose.yml
│   ├── events/
│   ├── requirements.txt
│   └── Dockerfile
├── Dockerfile
├── README.md
├── TODO
└── Terraform files
```

## Prerequisites

- Python 3.x
- Docker and Docker Compose
- Terraform, if you plan to work with the infrastructure code
- AWS credentials/configuration, if deploying the Terraform stack

## Local setup

### 1. Install Python dependencies

From the `app/` directory:

```bash
pip install -r requirements.txt
```

### 2. Run with Docker Compose

If you want to use the containerized workflow, build and start the app from `app/`:

```bash
docker-compose up --build
```

### 3. Run the application directly

If the app entrypoint is configured in the container or compose setup, you can also run it from the `app/` directory after installing dependencies:

```bash
python <entrypoint>.py
```

> Note: this repository does not yet document a single canonical Python entrypoint, so check `app/docker-compose.yml` and the app source for the exact command used to start the generator.

## Infrastructure

The root-level Terraform files define the cloud infrastructure needed to support the app. Typical Terraform workflows would be:

```bash
terraform init
terraform plan
terraform apply
```

Use caution when applying infrastructure changes, especially in AWS.

## Usage

The project is intended to generate fake social interaction/event data for testing or demonstration purposes. Based on the existing repo structure, the likely flow is:

1. Generate synthetic social data in the Python app.
2. Package and run it in Docker.
3. Optionally deploy supporting infrastructure with Terraform.

## Notes

- `TODO` likely contains additional implementation tasks or future enhancements.
- If you update the app behavior or add a clearer entrypoint, please also update this README with the exact run command.
