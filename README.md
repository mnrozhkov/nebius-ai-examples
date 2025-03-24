# Nebius AI Examples

This repository contains example notebooks and scripts demonstrating the usage of MLflow with Nebius Cloud.

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- venv (Python's built-in virtual environment module)

## Environment Setup

### 1. Create and Activate Virtual Environment

```bash
# Create a new virtual environment
python -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 3. Configure Environment Variables

You have two options to set up your environment variables:

#### Option 1: Using .env file (Recommended)

1. Copy the template file:
```bash
cp .env.template .env
```

2. Edit the `.env` file with your credentials:
```bash
# Nebius AI Studio credentials
NEBIUS_API_KEY=your_nebius_api_key_here

# MLflow tracking server configuration
MLFLOW_TRACKING_SERVER_CERT_PATH=/path/to/your/ca.pem
MLFLOW_TRACKING_URI=https://your-mlflow-tracking-server-url
MLFLOW_TRACKING_USERNAME=your_username
MLFLOW_TRACKING_PASSWORD=your_password
```

#### Option 2: Interactive Setup

Run the environment setup script:
```bash
python env_setup.py
```

This will prompt you to enter each environment variable securely.

### 4. Verify Setup

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

### Running Python Scripts

```bash
# Make sure your virtual environment is activated
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows

# Run your script
python your_script.py
```

### Running Jupyter Notebooks

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
   - Verify that all dependencies are installed: `pip install -r requirements.txt`

2. If environment variables are not being loaded:
   - Check that your `.env` file exists and contains the correct values
   - Verify that the environment variables are set: `python env_setup.py`

3. For Jupyter kernel issues:
   - Make sure ipykernel is installed
   - Register your virtual environment as a Jupyter kernel:
     ```bash
     python -m ipykernel install --user --name=mlflow-nebius
     ``` 
