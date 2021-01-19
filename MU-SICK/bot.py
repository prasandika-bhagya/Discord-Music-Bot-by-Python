
#importing
import discord
import os
from discord.ext import commands

# files
TokenFile = open("./data/Token.txt", "r") # Make sure to paste the token in the txt file
TOKEN = TokenFile.read() 

OWNERID = 800816866980921364

#bot prefix command
bot = commands.Bot(command_prefix = "bp!", case_insensitive=True)

# showing online status
@bot.event
async def on_ready():
    print("ONLINE")

# permission
@bot.event 
async def on_command_error(ctx,error):
    embed = discord.Embed(
    title='',
    color=discord.Color.orange())
    #error handle
    if isinstance(error, commands.CommandNotFound):
        pass
    if isinstance(error, commands.MissingPermissions):
        embed.add_field(name=f'Invalid Permissions', value=f'You dont have {error.missing_perms} permissions.')
        await ctx.send(embed=embed)
    else:
        #error showing
        embed.add_field(name = f':x: Terminal Error', value = f"```{error}```")
        await ctx.send(embed = embed)
        raise error

# Loading
@bot.command()
async def load(ctx, extension):
    # Checking the permission
    if ctx.author.id == OWNERID:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"Ohhh! You have no permission")

@bot.command()
async def unload(ctx, extension):
    # Checking the permission
    if ctx.author.id == OWNERID:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"Ohhh! You have no permission")


@bot.command(name = "reload")
async def reload_(ctx, extension):
    # Checking the permission
    if ctx.author.id == OWNERID:
        bot.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloading") 
    else:
        await ctx.send(f"Ohhh! You have no permission")

    # Checking the permission
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'Cogs.{filename[:-3]}')
        except Exception:
            raise Exception
        
#token
bot.run(str("ODAwODE2ODY2OTgwOTIxMzY0.YAXo0w.bWajrbcj9E1RkZ2ok-VCSg0-EyI")) # Make sure you paste the CORRECT token in the "./data/Token.txt" file
#This bot is designed by B.B.Prasandika by learning from an open source Youtube tutorial. All rights reserved to the owner