
import random
import os
import discord 
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "?", intents=intents)


@bot.event
async def on_ready():
    print("I am ready")


@bot.command()
async def mem(ctx):
   files = os.listdir("m2u1/images")
   rand_mem = random.choice(files)
   with open(f"m2u1/images/{rand_mem}", "rb") as file:
       picture = discord.File(file)
       await ctx.send(file=picture)
@bot.command()
async def math(ctx):
    mfiles = os.listdir("m2u1/math")
    rand_mathmem = random.choice(mfiles)
    with open(f"m2u1/math/{rand_mathmem}", "rb") as file:
        mpicture = discord.File(file)
        await ctx.send(file = mpicture)




    
bot.run("MTE1NTQ0MzU1MzIzMzc5NzE0MA.Gm8ZOk.e2xN51bETNI5uHujfDe5EiTOsaqbR364CyHBDk")

