import os

def create_project_structure(base_path):
    # Main project directory
    project_name = "book_recommendation_project"
    project_path = os.path.join(base_path, project_name)
    os.makedirs(project_path, exist_ok=True)

    # Subdirectories for better organization
    subdirs = [
        "raw_data",  # For storing raw downloaded datasets
        "cleaned_data",  # For processed or cleaned data
        "notebooks",  # Jupyter notebooks for exploration
        "scripts",  # Python scripts for data processing
        "models",  # For storing models (if any)
        "outputs"  # For storing results, figures, etc.
    ]

    for subdir in subdirs:
        os.makedirs(os.path.join(project_path, subdir), exist_ok=True)

    print(f"Project structure created under: {project_path}")
    print("Subdirectories:")
    for subdir in subdirs:
        print(f"- {subdir}")

# Specify the base path where you want to create the project (e.g., your home directory)
base_path = os.path.expanduser("/home/mike/Documents/Development_space/Self_Training_with_the_AI/Development_channels/MachineLearningChannels/Traditional_ML_Methods/Book_recommendation_projet/")  # This will set the base path to your home directory
create_project_structure(base_path)
