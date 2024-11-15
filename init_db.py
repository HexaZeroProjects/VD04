from app import app, db
from models import Post

with app.app_context():
    db.create_all()

    # Пример добавления записи
    post1 = Post(title='Первый пост', content='Добро пожаловать в наш блог!')
    db.session.add(post1)
    db.session.commit()

    print("База данных инициализирована.")
