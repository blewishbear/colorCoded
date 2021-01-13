from app.models import db, Color

def seed_colors():
    """
    Model:
    Color(name="")

    """

    color1 = Color(name="red")
    color2 = Color(name="blue")
    color3 = Color(name="yellow")
    color4 = Color(name="green")
    color5 = Color(name="white")
    color6 = Color(name="black")

    colors = [ color1, color2, color3, color4, color5, color6 ]

    for color in colors:
        db.session.add(color)

    db.session.commit()

def undo_colors():
    db.session.execute('TRUNCATE colors RESTART IDENTITY CASCADE;')
    db.session.commit()
