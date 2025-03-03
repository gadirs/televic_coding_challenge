# Flask Prime Number API
This API computes the N-th prime number.

## Installation and Running
```bash
git clone https://github.com/your-username/televic_coding_challenge.git
cd flask_prime_api
pip3 install -r requirements.txt
python3 run.py
```

## Design Considerations

### Question #1: Extra Security Headers or CORS for React Frontend

If this Flask API needed extra security headers or cross-origin access from a React frontend, I would consider using **Flask-CORS**. Flask-CORS is a simple and widely used library that provides Cross-Origin Resource Sharing (CORS) support for Flask applications. This is important for situations where a React frontend hosted on a different domain needs to make requests to this Flask backend.

**Why Flask-CORS?**
- **Security**: It allows you to restrict which domains can access your API, improving the overall security of the application.
- **Ease of Use**: It’s simple to integrate and configure in a Flask app, offering customizable CORS options such as allowing specific HTTP methods and headers from trusted origins only.

To use Flask-CORS, you would add it to your app like so:
```python
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
