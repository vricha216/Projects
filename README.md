A visually appealing, customizable resume generator built with Python and matplotlib. This tool creates a polished resume image using your personal data and design preferences defined in a configuration file.

📁 Project Structure
resume-project/
├── assets/              # Profile pictures or other visual assets
├── config/              # JSON configuration for resume content
├── output/              # Generated resume image saved here
├── src/
│   ├── resume_generator.py   # Main script to generate resume
│   └── logger_config.py      # Logger setup for better debugging
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
✨ Features
⚙️ Fully configurable resume content via JSON

🎨 Custom layout with sections like Skills, Languages, and Objective

🖼️ Generates a high-resolution resume image

🧩 Modular codebase with logging for easier debugging and maintenance

📦 Requirements
Python 3.x
matplotlib library

Install dependencies with:
pip install -r requirements.txt


🚀 Usage
Update your information
Edit config/resume_config.json to include your name, contact info, skills, languages, and more.

Run the resume generator
From the root directory, run:

python src/resume_generator.py

View your resume
The generated image (resume.png) will be saved in the output/ directory.

🛠 Customization
Change labels (e.g., section headers) directly in the config file.

Update fonts, colors, or layout in resume_generator.py for more visual control.

Enable logging for debugging or verbose outputs (configured in logger_config.py).