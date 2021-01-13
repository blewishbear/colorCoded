from app.models import db, Idea

def seed_ideas():
    """
    Model:
    Idea(user_id=, title="", description="")

    """


    idea1 = Idea(user_id=1, title="CurlyBoyz", description="Draw an anime dude with an afro and a bunch of curly brackets for the hair!")
    idea2 = Idea(user_id=2, title="My Block", description="Up up a block of code with curly brackets and inside, in bold letters put,'My Block!' with brick background")
    idea3 = Idea(user_id=3, title="H1 Voice", description="Have the text 'Use Your h1 voice' with a someone speaking into a megaphone with `'<h1>'` on the side")
    idea4 = Idea(user_id=4, title="Fetch Request", description="Have a dog return a bone that says 'res.json' after fetching it")
    idea5 = Idea(user_id=5, title="King Boolean", description="Text asking 'Are you scared?' King Boo from mario holding True or False sign")
    idea6 = Idea(user_id=6, title="Office Space", description="Text asking 'If you could console.log that, that'd be greeeeaaat")
    idea7 = Idea(user_id=5, title="F vs J", description="Have a folder named JSON, with the Jason mask, being mean mugged my Freddy Cruger")


    ideas = [ idea1, idea2, idea3, idea4, idea5, idea6, idea7 ]
    for idea in ideas:
        db.session.add(idea)

    db.session.commit()

def undo_ideas():
    db.session.execute('TRUNCATE ideas RESTART IDENTITY CASCADE;')
    db.session.commit()
