import discord

from discord.ext import commands

#指揮機器人
bot= commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    
@bot.event
async def on_member_join(member):
    channel= bot.get_channel(882615406148337713) #抓取頻道
    await channel.send(f"{member} join welcome!") #用f字串因成員名字為變數

@bot.event
async def on_member_remove(member):
    channel= bot.get_channel(882615406148337713) #抓取頻道
    await channel.send(member + " leave so sad") 
 
@bot.command()
async def ping(ctx): #ctx=context 上下文
    await ctx.send(f'{round(bot.latency*1000)} ms')
    
bot.run("OTM4MDExNDE5NTMyNzM4NTYw.YfkFNQ.253aYUt90kEOYHmxzrRrpI_oIbE")
#新的token:O刪除TM4MDExNDE5NTMyNzM4NTYw.YfkFNQ.yxYtZPtG60g4G8f74KSCx_q3pd0
