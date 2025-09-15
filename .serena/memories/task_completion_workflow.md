# Task Completion Workflow

## What to Do When a Task is Completed

Since this project doesn't have configured linting, formatting, or testing tools, the completion workflow is minimal:

### 1. Code Validation
```bash
# Check Python syntax
python -m py_compile hsv_viewer.py
```

### 2. Functional Testing
```bash
# Test the application with a sample image
python hsv_viewer.py <test_image_path>
```

### 3. Version Control
```bash
# Check what changed
git status
git diff

# Add and commit changes
git add .
git commit -m "Descriptive commit message"
```

### 4. Manual Testing Checklist
When making changes to the HSVViewer application:
- [ ] Application starts without errors
- [ ] Image loads correctly
- [ ] Mouse clicks display HSV values
- [ ] Statistics window updates properly
- [ ] Keyboard shortcuts work (q, r, c, s)
- [ ] Application exits cleanly
- [ ] Error handling works for invalid image paths

### 5. Code Review Points
- Follow the established naming conventions (snake_case, descriptive names)
- Add docstrings for new methods
- Maintain the single-file structure
- Ensure error messages are user-friendly
- Keep UI elements consistent with existing design

### Notes
- No automated testing framework is currently set up
- No linting tools (flake8, pylint, black) are configured
- No CI/CD pipeline exists
- Manual testing is the primary quality assurance method