import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def hel(ctx,): 
    await bot.send_message(ctx.message.author,  '`You must create a role called Bot Owner for this bot to work properly. \n Commands:\n $hel = Bot sends a pm of a list of commands to the user.\n $test = Test to see if bot is responsive. \n $spam = Spams chat, must have Bot Owner role to use the command. \n $game = Sets the game the bot is to display, must have Bot Owner role. \n $watching = Sets the thing the bot is to display as Watching, must have Bot Owner role. \n $listening Sets the thing the bot is to display as listening to, must have the Bot Owner role.`')
    await bot.say('Sent a DM containing a list of commands')
    await bot.delete_message(ctx.message)
    
@bot.command(pass_context=True)
@commands.has_role('Bot Owner')
async def watching(ctx,*,status):
    await bot.change_presence(game=discord.Game(name=status,type=3))
    await bot.send_message(ctx.message.channel,"Bot status changed to {}".format(status))
    
@bot.command(pass_context=True)
@commands.has_role('Bot Owner')
async def listening(ctx,*,status):
    await bot.change_presence(game=discord.Game(name=status,type=2))
    await bot.send_message(ctx.message.channel,"Bot status changed to {}".format(status))

@bot.command(pass_context=True)
@commands.has_role('Bot Owner')
async def game(ctx,*,status):
    await bot.change_presence(game=discord.Game(name=status))
    await bot.send_message(ctx.message.channel,"Bot status changed to {}".format(status))

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
