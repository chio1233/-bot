import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

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



client.run("NzQyMjg3MDY5NjI3NDE2NTg5.XzD6tA.VvmPwPH0eV_QS9C_mkqjtV0Q05I")
