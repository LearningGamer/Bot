import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def test(ctx):
  msg = 'Hi!'
  await bot.say(msg)


@bot.event
async def  on_ready():
    print("I'm in")
    print(bot.user.name)

bot.run(os.environ["token"])
