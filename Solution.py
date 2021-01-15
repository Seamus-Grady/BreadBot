import random

import discord
import os

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

bread = ['🍞', '🥖', '🫓', '🥙'
    ,'<:cool_bread:794676418139127858>']
ThreeStooges = ['🍞', '🥖', '🫓', '🥙', '<:sad_croissant:783863839329615923>', '<:cool_bread:783863484122923029>'
    , '<:confusedbread:777763790094729236>', '<:breadF:776593602587394060>']
ZoomU = ['🍞', '🥖', '🫓', '🥙', '<:yeenah:776240505242517545>', '<:thinkin_bread:776301348592418887>'
    ,'<:moaningbread:776233821330604053>','<:meow_bread:776240428248465458>', '<:embarrassed_bread:776247126983442483>'
    ,'<:dyingbread:776240632384454718>','<:breadF:776233740547915776>']
AnimeFans = ['🍞', '🥖', '🫓', '🥙', '<:anime_bread:776302320996057100>']

@client.event
async  def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if 'hello breadbot' in message.content.lower():
        await message.channel.send('Hello ' + message.author.name + '\nI am BreadBot I may not be a big bot, but like my brother SaltBot, I am here to serve you\nIf I see a message I think deserves bread I will react with bread')
    else:
        chance = random.randint(0, 2)
        if chance == 0:
            if message.guild.id == 794676085052801047:
                rand = random.randint(1, len(bread) - 1)
                for i in range(0, rand):
                    reaction = random.randint(0, len(bread) - 1)
                    await message.add_reaction(bread[reaction])
            elif message.guild.id == 776558596884398131:
                rand = random.randint(1, len(ThreeStooges) - 1)
                for i in range(0, rand):
                    reaction = random.randint(0, len(ThreeStooges) - 1)
                    await message.add_reaction(ThreeStooges[reaction])
            elif message.guild.id == 703009739184799804:
                rand = random.randint(1, len(AnimeFans) - 1)
                for i in range(0, rand):
                    reaction = random.randint(0, len(AnimeFans) - 1)
                    await message.add_reaction(AnimeFans[reaction])
            elif message.guild.id == 747510456788189184:
                rand = random.randint(1, len(ZoomU) - 1)
                for i in range(0, rand):
                    reaction = random.randint(0, len(ZoomU) - 1)
                    await message.add_reaction(ZoomU[reaction])



client.run(TOKEN)