import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='$')

@bot.command(pass_context=True)
async def hel(ctx,): 
    await bot.send_message(ctx.message.author,  '`Commands:\n $hel = Bot sends a pm of a list of commands to the user.\n $test = Test to see if bot is responsive.`')
    
@bot.command(pass_context=True)
async def spam(ctx):
  spammsg = 'LOLOLOLOLOLOLOLOL '
  await bot.say(spammsg *100)
  await bot.delete_message(msg.message)


@bot.command(pass_context=True)
async def test(ctx, msg):
  await bot.say('Test works! Message Deleted. Bot is responsive.')
  await bot.delete_message(msg.message)

@bot.event
async def  on_ready():
    print("I'm in")
    print(bot.user.name)

token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
