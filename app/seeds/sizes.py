from app.models import db, Size

def seed_sizes():
    """
    Model:
    Size(name="")

    """

    size1 = Size(name="XS")
    size2 = Size(name="S")
    size3 = Size(name="M")
    size4 = Size(name="L")
    size5 = Size(name="XL")
    size6 = Size(name="XXL")

    sizes = [ size1, size2, size3, size4, size5 ]
    for size in sizes:
        db.session.add(size)

    db.session.commit()

def undo_sizes():
    db.session.execute('TRUNCATE sizes RESTART IDENTITY CASCADE;')
    db.session.commit()
