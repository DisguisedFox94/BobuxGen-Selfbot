from discord.ext.commands.core import check
import requests
import discord
from discord.ext import commands
from discord.utils import get
import json
from datetime import date
import io
import asyncio,time
import threading
import os
from colorama import Fore
bot_config = json.loads(open("config.json", "r").read())
token = bot_config["token"]
prefix = bot_config["prefix"]

bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_ready():
	print("""
    
    ██████╗░░█████╗░██████╗░██╗░░░██╗██╗░░██╗░░█████╗░██████╗░██╗
    ██╔══██╗██╔══██╗██╔══██╗██║░░░██║╚██╗██╔╝░░██╔══██╗██╔══██╗██║
    ██████╦╝██║░░██║██████╦╝██║░░░██║░╚███╔╝░░░███████║██████╔╝██║
    ██╔══██╗██║░░██║██╔══██╗██║░░░██║░██╔██╗░░░██╔══██║██╔═══╝░██║
    ██████╦╝╚█████╔╝██████╦╝╚██████╔╝██╔╝╚██╗░░██║░░██║██║░░░░░██║
    ╚═════╝░░╚════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░░╚═╝░░╚═╝╚═╝░░░░░╚═╝
    Lucifer gave me permission to use this, Don't dm me hate ig.
    """)
@bot.command()
async def buy(ctx, id=None): # buys the gamepass 1 time, Manually solve the Captcha
    channel = bot.get_channel(893744951916101642) #bot cmds channel
    if id == "": #check if no id
        await ctx.reply('Please provide a id.') #reply
        return #break command
    await channel.send(f'>buy {id}')
    await ctx.reply(f'<@{ctx.author.id}>, Check your DMs with: AltGen/BobuxGen')
@bot.command()
async def cooldown(ctx): # sends >cooldown in bot-commands
    channel = bot.get_channel(893744951916101642) #bot cmds channel
    await channel.send('>cooldown')
    cooldownmsg = await bot.wait_for("message",timeout=60.0,check=check)
    await ctx.reply(f'<@{ctx.author.id}>, Check: <#893744951916101642>')
@bot.command() 
async def auto(ctx, id=None): # sends >buy <id> every time ur cooldown is over, manually solve the captcha
    await ctx.reply('Auto API has been enabled, (solve the captcha in your DMs)')
    while True:
        channel = bot.get_channel(893744951916101642)
        await channel.send(f'>buy {id}')
        print(f'Go solve the captcha in your DMs with: AltGen/Bobux Gen\n\nYour on a 31m second cooldown, Please wait.')
        time.sleep(1860)
        print(f'{bot.user}, Your cooldown is over!')
bot.run(token, bot=False)
