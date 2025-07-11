🌐 SaniYadav-Portfolio
A professional and dynamic portfolio website built with Django, designed to showcase your projects, skills, and contact information — all easily managed through a modern Django admin panel.

🚀 Features
🎯 Project Showcase: Display your projects with images, descriptions, and live/demo links.

💼 Skills Section: Highlight your technical stack and expertise.

📬 Contact Form: Allow visitors to send messages directly from the site.

🛠️ Admin Dashboard: Manage projects, skills, resume, and profile content through Django Admin.

📱 Responsive Design: Fully optimized for mobile, tablet, and desktop screens.

🖼️ Media Support: Upload images for your profile and projects using Django's media handling.

🔧 Easy Customization: Update your content anytime without touching code.

🛠️ Tech Stack
Backend: Django (Python)

Database: SQLite (easily upgradable to PostgreSQL/MySQL)

Frontend: HTML5, CSS3, Bootstrap 5, JavaScript

Media Handling: Pillow

Deployment Ready: Gunicorn + Nginx compatible

⚙️ Getting Started
Follow these steps to set up the project locally:

bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/Sani-Yadav/SaniYadav-Portfolio.git
cd SaniYadav-Portfolio/portfolio

# 2. Create and activate virtual environment
python -m venv env

# For Windows:
env\Scripts\activate

# For Linux/macOS:
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create admin user
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
🖥️ Access the site:

Portfolio: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

📁 Project Structure
php
Copy
Edit
portfolio/
├── manage.py
├── portfolio/        # Project settings and URLs
├── webapp/           # App logic: models, views, admin, forms
├── static/           # CSS, JavaScript, images
├── media/            # Uploaded media files
├── templates/        # HTML templates
├── requirements.txt  # Python dependencies
└── db.sqlite3        # SQLite database
📫 Contact
🔗 GitHub: Sani-Yadav

📧 Email: sani228142@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/sani-yadav-986778292

