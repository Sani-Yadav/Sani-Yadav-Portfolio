# SaniYadav-Portfolio
A dynamic portfolio website powered by Django and SQLite, showcasing projects, skills, and contact — fully managed via Django Admin.

## Deployment on Render

This portfolio is configured for easy deployment on Render.com. Follow these steps to deploy:

1. Fork or clone this repository to your GitHub account
2. Sign up for a Render account at https://render.com
3. Connect your GitHub account to Render
4. Click on "New Web Service" and select your repository
5. Render will automatically detect the configuration from render.yaml
6. Set the following environment variables in Render dashboard:
   - SECRET_KEY: (Render will generate this automatically)
   - PYTHON_VERSION: 3.10.0
7. Click "Create Web Service"

The deployment will start automatically. Once completed, your portfolio will be live at the URL provided by Render.
