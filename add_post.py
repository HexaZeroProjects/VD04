from app import app, db
from models import Post

def add_post(title, content):
    with app.app_context():
        # Создание новой записи
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        print(f"Пост '{title}' успешно добавлен в базу данных.")

if __name__ == '__main__':
    # Введите название и содержание нового поста
    title = input("Введите заголовок поста: ")
    content = input("Введите содержание поста: ")

    add_post(title, content)
