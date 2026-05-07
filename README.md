Here’s a **clean, short, non‑clunky `README.md`** you can drop directly into your repository. It’s developer‑friendly, leadership‑friendly, and avoids unnecessary verbosity.

***

# DevOps AKS CI/CD Use Case

This repository demonstrates an **end‑to‑end DevOps pipeline** for deploying a containerized backend application on **Azure Kubernetes Service (AKS)** using **GitHub Actions**.

***

## What This Project Does

*   Builds a Python FastAPI application into a Docker image
*   Pushes the image to **Azure Container Registry (ACR)**
*   Deploys the application to **Azure Kubernetes Service (AKS)**
*   Automates the entire flow using **GitHub Actions CI/CD**

Every push to `main` triggers a full build → deploy cycle.

***

## Tech Stack

*   **Cloud:** Microsoft Azure
*   **Container Orchestration:** Azure Kubernetes Service (AKS)
*   **Registry:** Azure Container Registry (ACR)
*   **CI/CD:** GitHub Actions
*   **IaC:** Terraform
*   **App Framework:** Python (FastAPI)
*   **Containerization:** Docker



## CI/CD Pipeline Flow

1.  Triggered on push to `main`
2.  GitHub Actions logs into Azure
3.  Docker image is built
4.  Image is pushed to ACR
5.  AKS context is set automatically
6.  Kubernetes manifests are applied

Deployment is fully automated — no manual steps required.

***

## Running Application

Once deployed, the service is exposed via a LoadBalancer.

**Endpoints:**

*   `/health` → Application health status
*   `/info` → Application metadata

Example:

    http://<EXTERNAL-IP>/health

***

## Status

Infrastructure provisioned  
CI/CD pipeline operational  
Application deployed and publicly accessible

***

## Author

**Noel Muppasani**

***

