from app.models import db, Idea, User

def seed_ideas():
    """
    Model:
    Idea(user_id=, title="", description="")

    """


    idea1 = Idea(user_id=1 title="CurlyBoyz", description="Draw an anime dude with an afro and a bunch of curly brackets for the hair!")
    idea2 = Idea(user_id= title="My Block", description="Up up a block of code with curly brackets and inside, in bold letters put,'My Block!' with brick background")
    idea3 = Idea(user_id= title="H1 Voice", description="Have the text 'Use Your h1 voice' with a someone speaking into a megaphone with <h1> tbe side")
    idea4 = Idea(user_id= title="Fetch Request", description="Have a dog return a bone that says 'res.json' after fetching it")
    idea5 = Idea(user_id= title="King Boolean", description="Text asking 'Are you scared?' King Boo from mario holding True or False sign")
    idea6 = Idea(user_id= title="Office Space", description="Text asking 'If you could console.log that, that'd be greeeeaaat")


    ideas = [ idea1, idea2, idea3, idea4, idea5, idea6 ]
    for idea in ideas:
        db.session.add(idea)

    db.session.commit()

def undo_ideas():
    db.session.execute('TRUNCATE ideas RESTART IDENTITY;')
    db.session.commit()
