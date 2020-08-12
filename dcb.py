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
    if message.content.startswith('경고 부여') :
        author = message.guild.get_member(int(message.content[9:27]))
        file = openpyxl.load_workbook('경고.xlsx')
        sheet = file.active
        why = str(message.content[28:])
        i = 1
        while True :
            if sheet["A" + str(i)].value == str(author) :
                sheet['B' + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 2:
                    await message.guild.ban(author)
                    await message.channel.send(str(author) + "님은 경고 2회누적으로 서버에서 추방되었습니다.")
                else:
                    await message.channel.send(str(author) + "님은 경고를 1회 받았습니다")
                    sheet["c" + str(i)].value = why
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author)
                sheet["B" + str(i)].value = 1
                sheet["c" + str(i)].value = why
                file.save("경고.xlsx")
                await message.channel.send(str(author) + "님은 경고를 1회 받았습니다.")
                break
            i += 1
            


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
