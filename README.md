# Python Monorepo with Hatch

This repository contains multiple microservices managed using Hatch.

## Services

- **Service A**: A simple Python application.
- **Service B**: A Flask-based web application.

## Setup

1. Install Hatch:
   ```bash
   pip install hatch
   ```

2. Navigate to the root directory and run:
   ```bash
   hatch env create
   ```

3. To run a specific service, navigate to its directory and execute:
   ```bash
   hatch run python app/main.py
   ```
