from flask import Flask, jsonify, abort, request, render_template, make_response
from .models import create_db
from .auth import sign_up, sign_in, AuthError, get_by_token

app = Flask(__name__, static_folder='assets')
db = create_db(app)

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    req = request.get_json()
    if req is None: abort(400)
    name = req.get('name', None)
    email = req.get('email', None)
    password = req.get('password', None)
    if not (name and email and password): abort(400)
    sign_up(name, email, password)
    return jsonify({
        'success': True
    })


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    req = request.get_json()
    if req is None: abort(400)
    email = req.get('email', None)
    password = req.get('password', None)
    if email is None or password is None: abort(400)
    token = sign_in(email, password)
    if token is None: abort(401)
    return jsonify({
        'success': True,
        'token': token
    })


@app.route('/user', methods=['GET'])
def get_user():
    return render_template('user.html')

@app.route('/user-data', methods=['GET'])
def get_user_data():
    header = request.headers.get('Authorization', None)
    if header is None: abort(400)
    parts = header.split()
    if parts[0].lower() != 'bearer': abort(400)
    if len(parts) != 2: abort(400)
    token = parts[1]
    if token is None: abort(400)
    user = get_by_token(token)
    return jsonify({
        'success': True,
        'name': user.name,
        'email': user.email
    })


@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        'success': False,
        'error': 400,
        'message': 'bad request'
    }), 400

@app.errorhandler(401)
def unauthorized(e):
    return jsonify({
        'success': False,
        'error': 401,
        'message': 'unauthorized'
    }), 401

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'error': 404,
        'message': 'not found'
    }), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        'success': False,
        'error': 405,
        'message': 'method not allowed'
    }), 405

@app.errorhandler(AuthError)
def autherror(e):
    return jsonify({
        'success': False,
        'error': 401,
        'message': e.message
    }), 401

if __name__ == '__main__':
    app.run()
