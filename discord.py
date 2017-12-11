# An amazing Discord bot by @TheRealBen#6753 & @Cringy Adam#4611
# Please do not copy this and make it your own because it's hard work making a Discord bot.

import discord
from discord.ext import commands
import config
import asyncio # Just in case ;) Py has issues sometimes

description = "Description here..."
bot = commands.Bot(command_prefix=config.prefix, description=description) ## constructing a bot object--> a fancy sentence for "declaring a bot" ecks dee

@bot.event
async def on_ready():
    print('Logged in as')
    print(str(bot.user))
    print(bot.user.id)
    print('------')

@bot.command()
hidden=True
async def test(ctx, *, args: str): # ctx is the context of the command. server (guild in dpy), author etc... always make sure its defined
    """ | Test"""
    await ctx.send(f"Args were *{args}*")

@bot.command()
async def ping(ctx):
    """ | Calculates CookieCoin's latency"""
    await ctx.send(f"Pong! {round(bot.latency*1000)}ms")
    await ctx.message.add_reaction("\n{COOKIE}")

# This is some complex shit I copied from Adam's bot because its complex
hidden=True
@bot.command(name="eval")
async def on_eval(ctx, code: str): # In that case I cant use the worn "eval" in a command as python recognises that word and acts wonky
    """ | Evaluates python code"""
    if ctx.author.id != config.benID: return # Means that only Ben can eval code. As this command is VERY VERY powerful
    env = {
        'ctx': ctx,
        'message': ctx.message,
        'guild': ctx.guild,
        'channel': ctx.channel,
        'author': ctx.message.author,
    }

    try:
        result = eval(code, env)
        if inspect.isawaitable(result):
            result = await result
    except Exception as e:
        try:
            await ctx.message.add_reaction('\N{HEAVY MULTIPLICATION X}')
        except:
            pass
    try:
        await ctx.message.add_reaction("\n{COOKIE}")
    except:
        pass
    await ctx.send(result)

bot.run(config.token)

# AND HERE WE GO! THIS IS A DISCORD BOT!
