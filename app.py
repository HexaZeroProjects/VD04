from flask import Flask, render_template
from datetime import datetime
from database import db
from models import Post

app = Flask(__name__)

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db.init_app(app)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница блога
@app.route('/blog')
def blog():
    posts = Post.query.all()
    return render_template('blog.html', posts=posts)

# Страница контактов
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Страница с текущим временем
@app.route('/time')
def time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', current_time=current_time)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
