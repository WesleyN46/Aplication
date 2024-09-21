from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
users_file = 'users.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    if not email or not password:
        return "Email e senha são obrigatórios", 400
    
    with open(users_file, 'a') as f:
        f.write(f"{email},{password}\n")
    return "Registro bem-sucedido", 200

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    if not os.path.exists(users_file):
        return "Usuário não encontrado", 400

    with open(users_file, 'r') as f:
        for line in f:
            user_email, user_password = line.strip().split(',')
            if user_email == email and user_password == password:
                return "Login bem-sucedido", 200
    return "Email ou senha inválidos", 400

if __name__ == '__main__':
    app.run(debug=True)
