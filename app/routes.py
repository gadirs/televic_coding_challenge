from flask import Blueprint, jsonify
from app.services import nth_prime

prime_bp = Blueprint('prime', __name__)

@prime_bp.route('/prime/<string:n>', methods=['GET'])
def get_nth_prime(n):
    try:
        #this part needed to handle negative numbers
        n = int(n)
    except ValueError:
        return jsonify({"error": "n must be a valid integer"}), 400
    if n < 1:
        return jsonify({"error": "n must be greater than 0"}), 400
    
    return jsonify({"n": n, "nth_prime": nth_prime(n)})