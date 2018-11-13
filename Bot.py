import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def hel(ctx,): 
    await bot.send_message(ctx.message.author,  '`You must create a role called Bot Owner for this bot to work properly. \n Commands:\n $hel = Bot sends a pm of a list of commands to the user.\n $test = Test to see if bot is responsive. \n $spam = Spams chat, must have Bot Owner role to use the command.`')
    await bot.say('Sent a DM containing a list of commands')
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
@commands.has_role('Bot Owner')
async def spam(ctx):
  spammsg = 'LOLOLOLOLOLOLOLOL '
  await bot.say(spammsg *100)


@bot.command(pass_context=True)
async def test(ctx):
  await bot.say('Test works! Command message deleted. Bot is responsive.')
  await bot.delete_message(ctx.message)


@bot.event
async def  on_ready():
    print("I'm in")
    print(bot.user.name)
    
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
