# Suggested Development Commands

## Environment Setup
```bash
# Activate direnv environment (if direnv is installed)
direnv allow

# Install dependencies
pip install -r requirements.txt
```

## Running the Application
```bash
# Basic usage
python hsv_viewer.py <image_path>

# Example
python hsv_viewer.py image.jpg

# Show help
python hsv_viewer.py --help

# Show version
python hsv_viewer.py --version
```

## Development Workflow
```bash
# Check Python syntax
python -m py_compile hsv_viewer.py

# Run with test image (if you have one)
python hsv_viewer.py test_image.png
```

## Git Commands
```bash
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# View history
git log --oneline
```

## System Commands (Linux)
```bash
# List files
ls -la

# Navigate directories
cd <directory>

# Find files
find . -name "*.py"

# Search in files
grep -r "pattern" .
```

## Notes
- No specific linting, formatting, or testing commands are configured in this project
- The project uses direnv for environment management
- Application requires X11/display for GUI functionality