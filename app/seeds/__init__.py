from flask.cli import AppGroup
from .users import seed_users, undo_users
from .ideas import seed_ideas, undo_ideas
from .products import seed_products, undo_products
from .colors import seed_colors, undo_colors
from .sizes import seed_sizes, undo_sizes
from .categories import seed_categories, undo_categories


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_ideas()
    seed_colors()
    seed_sizes()
    seed_categories()
    seed_products()
    # seed_orders()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_ideas()
    undo_products()
    undo_colors()
    undo_sizes()
    undo_categories()
    # undo_orders()
    # Add other undo functions here
