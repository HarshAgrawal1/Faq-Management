# Youtube Link: https://www.youtube.com/watch?v=5A4r0kKvYog

# Multilingual FAQ System

A Django-based FAQ management system with multilingual support, WYSIWYG editor integration, and API capabilities.

## Features

- ✨ Multilingual FAQ Management
- 📝 WYSIWYG Editor Integration (CKEditor)
- 🌐 REST API Support
- 🔄 Automatic Translation (Google Translate)
- 💾 Caching Mechanism
- 👤 Admin Dashboard
- 🔐 Authentication System

## Tech Stack

- Django
- Django REST Framework
- CKEditor
- Redis (for caching)
- Google Translate API
- SQLite/PostgreSQL

## Installation

1. Clone the repository
```bash
git clone https://github.com/HarshAgrawal1/Faq-Management.git)
```


```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run migrations
```bash
python manage.py migrate
```

4. Create superuser
```bash
python manage.py createsuperuser
```

5. Run the development server
```bash
python manage.py runserver
```

## Environment Variables

Create a `.env` file in the root directory and add:

```
SECRET_KEY=your_secret_key
DEBUG=True
```

## API Endpoints

### FAQ Endpoints

- `GET /api/faqs/` - List all FAQs
- `GET /api/faqs/?lang=hi` - List FAQs in Hindi
- `GET /api/faqs/?lang=bn` - List FAQs in Bengali
- `POST /api/faqs/` - Create new FAQ (Admin only)
- `DELETE /api/faqs/<id>/` - Delete FAQ (Admin only)

### Language Parameter

Use the `lang` query parameter to get translated content:
- `en` - English (default)
- `hi` - Hindi
- `bn` - Bengali

## Admin Dashboard

Access the admin dashboard at `/admin` with your superuser credentials to:
- Create and manage FAQs
- Format answers using WYSIWYG editor
- View created FAQs

## Current Status

### Completed Features
- ✅ FAQ Model with WYSIWYG Editor
- ✅ Admin Dashboard
- ✅ User Authentication
- ✅ Basic API Implementation
- ✅ Language Selection Support

### Pending Features
- ⏳ FAQ Deletion by ID
- ⏳ **Fix for Hindi and Bengali translation (Coroutine Object Error)**

### Known Issues
- Translation service returning coroutine object for Hindi and Bengali languages

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

Run tests using:
```bash
python manage.py test
```



## Contact

agawalharsh0522@gmail.com
Project Link: https://github.com/HarshAgrawal1/Faq-Management
