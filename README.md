# Nebius AI Examples

This repository contains example notebooks and scripts demonstrating the usage of MLflow with Nebius Cloud.

## Prerequisites

- Python 3.11+
- `uv` (Python package installer)

## Quick Start: Installation & Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mlrepa/monitoring-for-modern-ai-and-mlops.git
    cd monitoring-for-modern-ai-and-mlops
    ```

2. **Create and activate a virtual environment:**

    ```bash
    uv venv .venv --python 3.12

    # Activate the virtual environment
    # On macOS and Linux:
    source .venv/bin/activate
    # On Windows:
    # .\.venv\Scripts\activate
    ```

    > 👉 **Note:** The `uv venv .venv` command creates a virtual environment in a folder named `.venv` within your project directory.

3. **Install Dependencies:**

    With the virtual environment activated, install the required Python packages:

    ```bash
    uv sync
    ```

## Configure Environment Variables

You have two options to set up your environment variables:

**Option 1: Using .env file (Recommended)**

Copy the template file:

```bash
cp .env.template .env
```

Edit the `.env` file with your credentials:
```bash
# Nebius AI Studio credentials
NEBIUS_API_KEY=your_nebius_api_key_here

# MLflow tracking server configuration
MLFLOW_TRACKING_SERVER_CERT_PATH=/path/to/your/ca.pem
MLFLOW_TRACKING_URI=https://your-mlflow-tracking-server-url
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_password
```

**Option 2: Interactive Setup**

Run the environment setup script:

```bash
python env_setup.py
```

This will prompt you to enter each environment variable securely.

**Verify Setup**

You can verify your environment setup by running:

```bash
python env_setup.py
```

## Project Structure

- `mlflow-examples/` - Contains MLflow example notebooks and scripts
- `env_setup.py` - Environment configuration utility
- `.env.template` - Template for environment variables
- `requirements.txt` - Python package dependencies
- `.venv/` - Python virtual environment directory

## Usage

**Running Python Scripts**

```bash
# Make sure your virtual environment is activated
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

# Run your script
python your_script.py
```

**Running Jupyter Notebooks**

```bash
# Make sure your virtual environment is activated
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

# Start Jupyter
jupyter notebook
```

## Troubleshooting

1. If you see "Module not found" errors:
   - Make sure your virtual environment is activated
   - Verify that all dependencies are installed

2. If environment variables are not being loaded:
   - Check that your `.env` file exists and contains the correct values
   - Verify that the environment variables are set: `python env_setup.py`

3. For Jupyter kernel issues:
   - Make sure ipykernel is installed
   - Register your virtual environment as a Jupyter kernel:
  
     ```bash
     python -m ipykernel install --user --name=mlflow-nebius
     ``` 
