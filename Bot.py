import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot




bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def test(msg):
  await bot.say('Hi.')
  await bot.delete_message(msg.message)

@bot.event
async def  on_ready():
    print("I'm in")
    print(bot.user.name)

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
