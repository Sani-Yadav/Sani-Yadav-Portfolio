# 🌐 SaniYadav-Portfolio

A professional and dynamic portfolio website built with Django, designed to showcase your projects, skills, and contact information — all easily managed through a modern Django admin panel.

---

## 🚀 Features

- **🎯 Project Showcase:** Display your projects with images, descriptions, and live/demo links.
- **💼 Skills Section:** Highlight your technical stack and expertise.
- **📬 Contact Form:** Allow visitors to send messages directly from the site.
- **🛠️ Admin Dashboard:** Manage projects, skills, resume, and profile content through Django Admin.
- **📱 Responsive Design:** Fully optimized for mobile, tablet, and desktop screens.
- **🖼️ Media Support:** Upload images for your profile and projects using Django's media handling.
- **🔧 Easy Customization:** Update your content anytime without touching code.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (easily upgradable to PostgreSQL/MySQL)
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Media Handling:** Pillow
- **Deployment Ready:** Gunicorn + Nginx compatible

---

## ⚙️ Getting Started

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sani-Yadav/SaniYadav-Portfolio.git
   cd SaniYadav-Portfolio/portfolio
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   # For Windows:
   env\Scripts\activate
   # For Linux/macOS:
   source env/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

### 🖥️ Access the site:
- **Portfolio:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Project Structure

```
portfolio/
├── manage.py
├── portfolio/        # Project settings and URLs
├── webapp/           # App logic: models, views, admin, forms
├── static/           # CSS, JavaScript, images
├── media/            # Uploaded media files
├── templates/        # HTML templates
├── requirements.txt  # Python dependencies
└── db.sqlite3        # SQLite database
```

---

## 📫 Contact

- **🔗 GitHub:** [Sani-Yadav](https://github.com/Sani-Yadav/SaniYadav-Portfolio)
- **📧 Email:** sani228142@gmail.com
- **💼 LinkedIn:** [https://www.linkedin.com/in/sani-yadav-986778292](https://www.linkedin.com/in/sani-yadav-986778292)

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

> **Tip:**
> - Customize your profile, projects, and skills from the Django Admin panel.
> - For deployment, configure static/media settings and use Gunicorn + Nginx for production.