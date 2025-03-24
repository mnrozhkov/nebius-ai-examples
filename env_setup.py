import os
import getpass
from typing import List, Optional
from pathlib import Path
from dotenv import load_dotenv

def get_required_env_vars() -> List[str]:
    """Return list of required environment variables."""
    return [
        'NEBIUS_API_KEY',
        'MLFLOW_TRACKING_SERVER_CERT_PATH',
        'MLFLOW_TRACKING_URI',
        'MLFLOW_TRACKING_USERNAME',
        'MLFLOW_TRACKING_PASSWORD'
    ]

def setup_env_interactive() -> None:
    """Set up environment variables interactively using getpass."""
    env_vars = get_required_env_vars()
    
    for var_name in env_vars:
        prompt = f'Please enter the value for {var_name}: '
        os.environ[var_name] = getpass.getpass(prompt=prompt)

def setup_env_from_file(env_file: Optional[str] = '.env') -> None:
    """Set up environment variables from a .env file.
    
    Args:
        env_file: Path to the .env file. Defaults to '.env' in the current directory.
    """
    env_path = Path(env_file)
    print("Load ENV variables from file:", env_path)
    if not env_path.exists():
        raise FileNotFoundError(f"Environment file not found: {env_file}")
    
    load_dotenv(env_path, override=True)
    
    # Verify all required variables are set
    missing_vars = [var for var in get_required_env_vars() if var not in os.environ]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

def verify_env_setup() -> bool:
    """Verify that all required environment variables are set.
    
    Returns:
        bool: True if all required variables are set, False otherwise.
    """
    missing_vars = [var for var in get_required_env_vars() if var not in os.environ]
    if missing_vars:
        print(f"Missing required environment variables: {', '.join(missing_vars)}")
        return False
    else:
        print("All required environment variables are set.")
        return True

if __name__ == "__main__":
    # Example usage
    try:
        # Try to load from .env file first
        env_file = Path.cwd() / '.env'
        setup_env_from_file(env_file)
    except FileNotFoundError:
        # If .env file doesn't exist, use interactive setup
        print("No .env file found. Using interactive setup...")
        setup_env_interactive()
    
    # Verify the setup
    if verify_env_setup():
        print("Environment setup completed successfully!")
    else:
        print("Environment setup failed. Please check the missing variables.") 
