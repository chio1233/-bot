import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='',type=1))

@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕 만나서 반가웡")
    if message.content.startswith("!이름"):
        await message.channel.send("난 귀여운 무기양 이무기!")
    if message.content.startswith("!개발자"):
        await message.channel.send("치오")
    if message.content.startswith("!치오"):
        await message.channel.send("멋지공 귀엽고 참 완벽한 치오!")
    if message.content.startswith("!용용"):
        await message.channel.send("나 용용친구 무기!")
    if message.content.startswith("!레드"):
        await message.channel.send("레드 왕자님~~")        
    if message.content.startswith("!블루"):
        await message.channel.send("레드친구 블루예여!")
    
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        emmbed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)    
            


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
