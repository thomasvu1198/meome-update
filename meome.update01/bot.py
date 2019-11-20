import discord
import time
import asyncio
from discord.utils import get
import random
import os
from discord.ext import commands
from discord.ext.commands import bot
bot = commands.Bot(command_prefix = ';')

@bot.event
async def on_ready():
    print('Logged on as {0}!'.format(bot.user))

@bot.command()
async def set(ctx,status) :
    if ctx.message.author.id == 376047361765670912:
        await bot.wait_until_ready()
        await bot.change_presence(activity=discord.Game(
                    name= status))
    else:
        return

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("NjI5MTc1NTQxMzg3MjMxMjMy.XaRAfg.BRDEYwhGSCO30_O4WX1CKce2Eqw")
