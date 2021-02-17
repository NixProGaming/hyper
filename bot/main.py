import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("NzcyMTA0MDY1NTc1ODEzMTMw.X51z8g.2o7hnez2L8yWaSCKW4vNCKS1pWs")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

server.server()
bot.run(TOKEN)
