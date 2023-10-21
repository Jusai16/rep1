import discord
from discord.ext import commands


intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "?", intents=intents)

@bot.event
async def on_ready():
    print("Я готов")


@bot.command()
async def replace(ctx, object):
    if object == "губка":
         await ctx.send("Губку для мытья посуды пожно заменить на мочалку из люфы.")
         with open("m2u2/photo/lufa.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)

    elif object == "пластиковый пакет":
         await ctx.send("Вместо пластикового пакета можно использовать многоразовую сумку из ткани.")
         with open("m2u2/photo/shop.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    elif object == "одноразовая посуда":
         await ctx.send("Лучше использовать многоразовую посуду из стекла, керамики, железа или многоразового пластика.")



@bot.command()
async def rec(ctx, material):
    if material=="пластик":
         await ctx.send("подготовьте и относите пластиковые отходы в специальные центры переработки или выбросите их в специальные контейнеры для пластика.")
    if material == "стекло":
         await ctx.send("помойте тару, целые бутылки можно сдать в специальные пункты приёмы, либо выбросить в специальный контейнер для стекла, как и стеклянные осколки.")
    if material == "металл":
         await ctx.send("металлические предметы можно сдать в пункты металлоприёма.")
         

@bot.command()
async def new(ctx, object):
    if object == "контейнеры яиц":
         await ctx.send("В таких контейнерах можно выращивать зелень на подоконнике.")
         with open("m2u2/photo/kont.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    if object == "молотый кофе":
         await ctx.send("После заварки нерастворимого кофе остаётся осадок, из которого можно сделать скраб для тела.")
         with open("m2u2/photo/cofe.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    if object == "старая одежда":
         await ctx.send("Например, из старых джинс можно сшить шопер.")
         with open("m2u2/photo/jsumka.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)
    if object == "газеты":
         await ctx.send("В интернете можно найти много мастерклассов по изготовлению карзинок из газет.")
         with open("m2u2/photo/korz.jpg", "rb") as file:
            picture = discord.File(file)
            await ctx.send(file=picture)

bot.run("MTE1NTQ0MzU1MzIzMzc5NzE0MA.G_YAPV.BJ9nmDoM154G9wf64y9haMOU4J_nklO4sBk25M")

