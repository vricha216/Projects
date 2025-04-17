import json
import os
import matplotlib.pyplot as plt
from logger_config import get_logger

logger = get_logger(__name__)


# Load configuration from JSON file
def load_config(path='config/resume_config.json'):
    try:
        with open(path, 'r') as f:
            logger.info(f"Loading configuration from {path}")
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Configuration file not found at {path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in config file: {e}")
        raise

# Generate resume image using matplotlib
def create_resume(config):
    try:
        # Extract fields from config
        name = config['name']
        email = config['email']
        contact = config['contact']
        address = config['address']
        skills = '\n. '.join(config['skills'])
        languages = '\n'.join(config['languages'])
        objective = config['objective']

        # Labels and section headers from config
        header = config.get('header', '')
        title = config.get('title', '')
        skills_header = config.get('skills_header', 'SKILLS')
        languages_header = config.get('languages_header', 'LANGUAGES')
        objective_header = config.get('objective_header', 'OBJECTIVE')

        # Set up the canvas (A4 size approx)
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.set_facecolor('white')
        plt.axis('off')

        # Decorative blue vertical bar (hidden with alpha=0.0)
        ax.axvline(x=0.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)

        # Sidebar background
        plt.axvline(x=0.1, color='#000000', alpha=0.5, linewidth=300)

        # Header and personal info
        plt.annotate(header, (0.45, 0.98), weight='regular', fontsize=8, alpha=0.75)
        plt.annotate(name, (0.04, 0.96), weight='bold', fontsize=22)
        plt.annotate(title, (0.06, 0.93), weight='regular', color='blue', fontsize=10)
        plt.annotate(contact, (0.12, 0.91), weight='regular', fontsize=10, color='#ffffff')
        plt.annotate(address, (0.1, 0.89), weight='regular', fontsize=10, color='#ffffff')
        plt.annotate(email, (0.1, 0.87), weight='regular', fontsize=10, color='#ffffff')

        # Skills section
        plt.axhline(y=0.85, xmin=0, xmax=0.396, color='black', linewidth=20)
        plt.annotate(skills_header, (0.02, 0.84), weight='bold', color='white', fontsize=14)
        plt.annotate(skills, (0.02, 0.66), weight='bold', color='white', fontsize=10)

        # Languages section
        plt.axhline(y=0.60, xmin=0, xmax=0.396, color='black', linewidth=20)
        plt.annotate(languages_header, (0.02, 0.59), weight='bold', color='white', fontsize=14)
        plt.annotate(languages, (0.02, 0.51), weight='bold', color='white', fontsize=10)

        # Objective section
        plt.annotate(objective_header, (0.44, 0.95), weight='bold', color='black', fontsize=14)
        plt.annotate(objective, (0.44, 0.87), weight='regular', color='black', fontsize=10)

        # Ensure output directory exists
        os.makedirs('output', exist_ok=True)

        # Save resume image
        filename = f"output/{name.lower().replace(' ', '_')}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        logger.info(f"Resume saved at {filename}")

    except Exception as e:
        logger.exception("An error occurred while creating the resume.")
        raise



# Entry point
if __name__ == '__main__':
    try:
        config = load_config()
        create_resume(config)
    except Exception as e:
        logger.error("Resume generation failed.")
