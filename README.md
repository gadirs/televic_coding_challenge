# Flask Prime Number API
This API computes the N-th prime number.

## Installation and Running
```bash
git clone https://github.com/gadirs/televic_coding_challenge.git
cd televic_coding_challenge
pip3 install -r requirements.txt
python3 run.py
```
After running the application, the API endpoint can be accessed at http://127.0.0.1:5000/prime/n, where n is the number for which you want to find the n-th prime. For example, http://127.0.0.1:5000/prime/10 will return the 10th prime number.

## Design Considerations

### Question #1:

If this Flask API needed extra security headers or cross-origin access from a React frontend, I would consider using **Flask-CORS**. This is important for situations where a React frontend hosted on a different domain needs to make requests to this Flask backend. It would allow us to restrict which domains can access the API, improving the overall security of the application.

In order to use Flask-CORS, the following lines would be needed:
```python
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})
```
Only requests from http://127.0.0.1:5000 (React frontend) would be allowed to access the API.



### Question #2:

For a React UI with a strict Content Security Policy (CSP), Tailwind CSS is a good choice. It's a utility-first CSS framework, meaning it uses small, reusable classes to style elements directly in your HTML. This makes it easier to work with CSP because it doesn't rely on external scripts or stylesheets that might get blocked. On the other hand, Material UI and Chakra UI might need external resources like JavaScript or CSS files. This could be restricted under a strict CSP. Tailwind avoids this issue by letting you define all your styles in your own classes.


