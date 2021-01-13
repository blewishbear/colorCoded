from app.models import db, Category

def seed_categories():
    """
    Model:
    Category(name="")

    """

    category = Category(name="T-shirt")
    db.session.add(category)

    db.session.commit()

def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
