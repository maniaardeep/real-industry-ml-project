from pathlib import Path
import logging

# ------------------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)

project_name = "mlproject"

# ------------------------------------------------------------------------------
# List of Files to Create
# ------------------------------------------------------------------------------

list_of_files = [

    # =========================
    # Source Package
    # =========================
    f"src/{project_name}/__init__.py",

    # API Layer
    f"src/api/__init__.py",
    f"src/api/prediction_api.py",
    f"src/api/health_api.py",
    f"src/api/training_api.py",
    f"src/api/model_api.py",

    # Components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_monitoring.py",

    # Pipelines
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",

    # Utility Modules
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/utils.py",

    # Main Entry Files
    "main.py",
    "app.py",
    "train.py",

    # Configuration
    "config/config.yaml",
    "config/model.yaml",

    # Project Files
    "README.md",
    ".gitignore",
    "requirements.txt",
    ".env",
    "Dockerfile",
    "pyproject.toml",

    # Tests
    "tests/__init__.py",
    "tests/test_data_ingestion.py",
    "tests/test_model.py",
]

# ------------------------------------------------------------------------------
# Directories to Create
# ------------------------------------------------------------------------------

list_of_directories = [
    "artifacts",        # Saved models, preprocessing pipelines, metrics
    "logs",             # Training, prediction, and application logs

    # Data directories
    "data/raw",         # Original dataset (never modify)

    "data/interim",     # Cleaned and validated data
                         # - Remove duplicates
                         # - Handle missing values
                         # - Convert data types
                         # - Rename columns
                         # - Remove invalid records

    "data/processed",   # Final model-ready dataset
                         # - Feature Engineering
                         # - Encoding
                         # - Scaling
                         # - Train/Test Split
                         # - Feature Selection

    "notebooks",        # Jupyter notebooks for EDA and experiments

    "templates"         # Reusable project templates
                         # - Jinja2/HTML templates for API/UI
                         # - YAML/JSON configs for pipelines
                         # - Markdown/LaTeX templates for reports
                         # - Notebook skeletons for experiments
]


# ------------------------------------------------------------------------------
# Create Directories
# ------------------------------------------------------------------------------

for directory in list_of_directories:
    Path(directory).mkdir(parents=True, exist_ok=True)
    logging.info(f"Directory created: {directory}")

# ------------------------------------------------------------------------------
# Create Files
# ------------------------------------------------------------------------------

for file in list_of_files:

    file_path = Path(file)

    # Create parent directory if needed
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.touch()
        logging.info(f"File created: {file_path}")

    else:
        logging.info(f"File already exists: {file_path}")

logging.info("=" * 60)
logging.info("ML Project Structure Created Successfully.")
logging.info("=" * 60)