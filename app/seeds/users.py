from werkzeug.security import generate_password_hash
from app.models import db, User

# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(username='Demo', email='demo@aa.io',
                password='password')
    steph = User(username='steph', email='steph@aa.io',
                password='password')
    kodi = User(username='kodi', email='kodi@aa.io',
                password='password')
    dan = User(username='dan', email='dan@aa.io',
                password='password')
    james = User(username='james', email='james@aa.io',
                password='password')
    resa = User(username='resa', email='resa@aa.io',
                password='password')
    rome = User(username='rome', email='rome@aa.io',
                password='password')

    users = [ demo, steph, kodi, dan, james, resa, rome ]

    for user in users:
        db.session.add(user)
    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
