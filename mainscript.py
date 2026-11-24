#External Imports
import discord
from discord.ext import commands
from dotenv import load_dotenv
#Internal Imports
import os
import asyncio
import time
from collections import defaultdict, deque

#Defines the intents (the ability to message, detect joins, etc.)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Creates the bot so bot. prefix works
bot = commands.Bot(command_prefix="!", intents=intents)

#Loads the .env file where the token is stored and then stores it in its own variable
load_dotenv("bottoken.env")
TOKEN = os.getenv("DISCORD_TOKEN")

#if the token somehow doesnt exist
if not TOKEN:
    raise RuntimeError("Whoops! No Token!")

@bot.event
#If this script works, loads the command modules.
async def online():
    #Prints this in the code script 
    print(f"This code works! John is active!")

    #Loads all the outer commands scripts
    await bot.load_extension("Commands.Logs.py") 
    await bot.load_extension("Commands.Permission systems.py")
    await bot.load_extension("Commands.Suggestions.py")
    await bot.load_extension("Commands.Other Dev Tools.py")
    await bot.load_extension("Commands.Gameplay Appraisal.py")
    await bot.laod_extension("Silly Other Things.py")
    
#Starts the bot
bot.run(TOKEN)
