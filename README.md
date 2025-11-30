# Django Authentication API with Email Verification

A robust Django REST API with JWT authentication, email verification for new user registrations, and password reset functionality. This project implements a complete user authentication system with secure email-based workflows.

## Features

- User Registration with Email Verification
- JWT Token-based Authentication
- Login/Logout Functionality
- Password Change
- Password Reset via Email
- Protected User Profile Endpoints
- CORS Support

## Tech Stack

- **Backend**: Django 5.2.8 + Django REST Framework
- **Authentication**: JWT (Simple JWT)
- **Database**: SQLite (default, can be changed)\
- **Email**: Gmail SMTP (configurable)

## Project Structure

```
djangoauthapi/
├── account/                 # Main app for authentication
│   ├── models.py           # Custom user model
│   ├── views.py            # API views
│   ├── serializers.py      # Data serialization
│   ├── urls.py             # URL routing
│   └── utils.py            # Utility functions
├── djangoauthapi/          # Project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py            # WSGI deployment
└── manage.py              # Django CLI tool
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "email verification in djagno"
   cd djangoauthapi
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   cd djangoauthapi
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Configure environment variables**
   
   Create a `.env` file in the `djangoauthapi/` directory:
   ```env
   EMAIL_USER=your_gmail_address@gmail.com
   EMAIL_PASSWORD=your_app_password
   EMAIL_FROM=your_gmail_address@gmail.com
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication

| Method | Endpoint                        | Description              |
|--------|---------------------------------|--------------------------|
| POST   | `/api/user/register/`           | User Registration        |
| POST   | `/api/user/login/`              | User Login               |
| GET    | `/api/user/profile/`            | Get User Profile         |
| POST   | `/api/user/changepassword/`     | Change Password          |
| POST   | `/api/user/sendpasswordresetemail/` | Send Password Reset Email |
| POST   | `/api/user/resetpassword/<uid>/<token>/` | Reset Password         |

### Example Requests

#### User Registration
```bash
curl -X POST http://127.0.0.1:8000/api/user/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "name": "John Doe",
    "tc": true,
    "password": "strongpassword123",
    "password2": "strongpassword123"
  }'
```

#### User Login
```bash
curl -X POST http://127.0.0.1:8000/api/user/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "strongpassword123"
  }'
```

#### Get User Profile (Requires Authentication)
```bash
curl -X GET http://127.0.0.1:8000/api/user/profile/ \
  -H "Authorization: Bearer <your_access_token>"
```

## Email Verification Workflow

When a new user registers, the system:
1. Creates a new user account with `is_active = True` (user can immediately log in)
2. Sends a welcome email to the user's email address

Note: In the current implementation, email verification is not required for login. Users can log in immediately after registration.

## Email Configuration

### Gmail Setup

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account Settings
   - Security → 2-Step Verification → App passwords
   - Generate a new App password for "Mail"
3. Add credentials to `.env` file

### Console Email (Development)

For development, you can use the console email backend which prints emails to the terminal:

In `settings.py`, uncomment:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

The project includes a custom email backend (`PatchedEmailBackend`) that fixes SSL certificate verification issues commonly encountered on macOS with Python 3.13.

## JWT Token Configuration

Tokens are configured with:
- Access Token Lifetime: 5 minutes
- Refresh Token Lifetime: 1 day

## Environment Variables

| Variable        | Description              | Example                     |
|-----------------|--------------------------|-----------------------------|
| EMAIL_USER      | Gmail address            | your_email@gmail.com        |
| EMAIL_PASSWORD  | App Password             | xxxx xxxx xxxx xxxx         |
| EMAIL_FROM      | Sender email             | your_email@gmail.com        |

Note: Default values are provided in settings.py for demonstration purposes. Always use environment variables in production.

## Common Issues & Solutions

### SSL Certificate Errors (macOS)

If you encounter SSL certificate errors:
1. Ensure you're using Python 3.10+
2. Use App Passwords instead of regular passwords
3. Check your system's certificate store

### Email Not Sending

1. Verify Gmail credentials
2. Ensure 2FA is enabled
3. Confirm App Password is correct
4. Check spam/junk folders

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Prabin Khadka

## Acknowledgments

- Django REST Framework
- Simple JWT
- Django CORS Headers
