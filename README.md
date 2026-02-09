# MediaVault
A lightweight web application built using **Python Flask** that allows users to register, log in, upload media (images/videos), browse a gallery, search content, and provides an administrative interface for management and moderation.

This project demonstrates a classic **server-rendered Flask architecture** using HTML templates, static assets (CSS & JS), and backend route handling.

---

## Features

### User System
- User registration
- Login authentication
- Session-based login persistence
- Error feedback pages for invalid login/registration
- Success redirection after authentication

### Media Handling
- Upload images and videos
- View uploaded media in gallery pages
- Dedicated image and video viewing pages
- Client-side upload handling (JavaScript)

### Search
- Search for uploaded media
- Content discovery through filtered results

### Admin Dashboard
- Dedicated admin interface
- View and manage uploaded media
- Moderation functionality (delete/inspect items)

### UI/UX
- Landing page
- Styled pages using CSS
- JavaScript enhanced interactions
- Loading and feedback pages
  Here is a comprehensive `README.md` file based on the architectural analysis of your repository.

***



























































































---

## 📂 Project Structure

```text
├── app.py              # Main Flask application logic and routing
├── requirements.txt    # Python dependencies
├── static/             # Frontend assets
│   ├── css/            # Page-specific styles (landing, admin, styles, etc.)
│   ├── js/             # Client-side logic (upload handling, interactivity)
│   └── 6.image         # Static placeholders/assets
└── templates/          # Jinja2 HTML templates
    ├── index.html      # Home/Landing page
    ├── log.html        # Login page
    ├── reg.html        # Registration page
    ├── images.html     # Image gallery
    ├── video.html      # Video player/view
    ├── search.html     # Search results page
    ├── adminpage.html  # Admin dashboard
    └── ...             # Error and helper templates (success.html, login_error.html)
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Create a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Application

### Development Mode
Run the Flask development server:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000`.

### Production
For production environments, it is recommended to use a WSGI server like **Gunicorn**:
```bash
gunicorn app:app
```

---

## 🛣️ Key Routes

| Endpoint | Description |
| :--- | :--- |
| `/` | Landing page / Introduction |
| `/login` | User login interface |
| `/register` | User registration interface |
| `/upload` | Media upload handler (handled via `upload.js`) |
| `/images` | Image gallery view |
| `/video` | Video playback view |
| `/search` | Search and discovery interface |
| `/admin` | Administrative dashboard |

---

## 🔒 Security & Best Practices

To ensure the application is production-ready, consider the following:

1.  **Environment Variables:** Store `SECRET_KEY` and database URIs in a `.env` file rather than hardcoding them in `app.py`.
2.  **File Validation:** The application performs server-side validation on uploads to prevent path traversal and restrict file types to images/videos.
3.  **Password Hashing:** Ensure passwords are encrypted using libraries like `Werkzeug` or `Passlib` (standard in the registration flow).
4.  **Static Files:** For high-traffic use, serve the `static/` directory via Nginx or a dedicated CDN.

---

## 🛠️ Future Improvements

- [ ] Implement **Database Migration** (e.g., Flask-Migrate) for easier schema updates.
- [ ] Add **Unit Testing** using `pytest` for authentication and upload routes.
- [ ] Integrate **Cloud Storage** (AWS S3 or Google Cloud Storage) for uploaded media.
- [ ] Add **Pagination** to the image gallery and search results.
- [ ] Implement **Rate Limiting** on login and upload endpoints to prevent abuse.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## Project Structure

