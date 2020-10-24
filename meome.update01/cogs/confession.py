import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import bot
global count
count = 0

class confession(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        global count
        if (str(message.channel.type) == "private"):
            print('Message from {0.author}: {0.content}'.format(message))
            lines = ("Đã nhận được cfs của bạn, mọi cfs có ngôn ngữ, nội dung công không phù hợp( công kích, chửi bậy sẽ bị xóa không báo trước. \nGửi cfs cho mị bằng cú pháp ``cfs:``\n")
            BannedWords = ['địt', 'lồn', 'cặc', 'buồi']
            lowermessage = message.content.lower()
            client = await self.bot.fetch_user(message.author.id)

            if (message.content.startswith('cfs: ') == True):
                count = count + 1
                mess_count = str(count
                # get id of author and send dm if cfs has banned words
                for i in range(0, len(BannedWords)):
                    if BannedWords[i] in lowermessage:
                        await message.author.send('Đụ mẹ không chửi thề nha!!!!!!\nMọi cfs có ngôn ngữ, nội dung công không phù hợp( công kích, chửi bậy, spam ...) sẽ bị xóa không báo trước. \nGửi cfs cho mị bằng cú pháp ``cfs:``\n')
                        return
                # check if bot speak
                if (message.author == self.bot.user):
                    return
                # send dm
                await message.author.send(lines)
                server_channel_confess = self.bot.get_channel(631173678238793729)
                message.content = message.content[5:]
                confession_message = '#' + mess_count + "\n" + message.content
                confession_embed = discord.Embed(description=confession_message, color=0x008080)
                await server_channel_confess.send(embed=confession_embed)

def setup(bot):
    bot.add_cog(confession(bot))
