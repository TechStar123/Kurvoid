from .avatar import Avatar


def setup(bot):
    bot.add_cog(Avatar())

from .general import General


def setup(bot):
    bot.add_cog(General())

from .penis import Penis


def setup(bot):
    bot.add_cog(Penis())
    
from .hangman import Hangman
from redbot.core import data_manager


def setup(bot):
    n = Hangman(bot)
    data_manager.bundled_data_path(n)
    bot.add_cog(n)

from .race import Race

__red_end_user_data_statement__ = "This cog stores discord IDs as needed for operation."


def setup(bot):
    bot.add_cog(Race())
