import discord
import time
import asyncio
from discord.utils import get
import random
from discord.ext import commands
from discord.ext.commands import bot

class fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    #-------random a guy couple--------------#
    @commands.command(aliases=['homo'])
    @commands.guild_only()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gay(self, ctx):
        photo = random.choice(
            ['http://www2.pictures.zimbio.com/gi/Protestors+Take+Part+Group+Kiss+Outside+Pub+y3IUby_-eBVl.jpg',
             'https://images3.memedroid.com/images/UPLOADED331/5bbe267f5d509.jpeg',
             'https://images3.memedroid.com/images/UPLOADED100/5dcc138fe297b.jpeg',
             'http://www.codajoy.net/wp-content/uploads/2014/12/candy-cane.jpg',
             'https://media.giphy.com/media/3o72FiXBdWRy3aZHJm/giphy.gif',
            'https://media.giphy.com/media/2wV5GCMeSby2veFNSM/giphy.gif',
             'https://media.giphy.com/media/BRWSMceIfWMWk/giphy.gif',


            ])
        male_role = discord.utils.get(ctx.guild.roles, name="male")
        gay = random.choice(
            [x for x in male_role.members if not x.bot]
        )
        gay2 = random.choice(
            [x for x in male_role.members if not x.bot and gay ]
        )
        embed = discord.Embed(title = "Chúc mừng các bạn đã là vợ chồng :heart:",
                              description = f"<@{gay.id}> và <@{gay2.id}> đã là vợ chồng của nhau :ok_hand: :point_left: ",
                              color = 0x008080)

        embed.set_image(url=photo)
        await ctx.send(embed=embed)
    @gay.error
    async def gay_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            #msg = 'hãy thử lại sau {:.2f}s'.format(error.retry_after)
            member_id = ctx.message.author.id
            time_left = str(error.retry_after)
            timeleft = time_left[:2]
            await ctx.send(f"<@{member_id}> hãy thử lại sau {timeleft}s")
        else:
            raise error

    @commands.command(aliases=['ckimckuot'])
    async def kiss(self,ctx,member: discord.Member):
        photo = random.choice(
                             ['https://media.giphy.com/media/VGACXbkf0AeGs/giphy.gif',
                             'https://media.giphy.com/media/8VwWQkfmd7zoc/giphy.gif',
                             'https://media.giphy.com/media/10VrdmxFsFKwFO/giphy.gif',
                             'https://media.giphy.com/media/OKQD2eTLv1Rqo/giphy.gif',
                             'https://media.giphy.com/media/xT9IgFh732bmm00u1a/giphy.gif',
                             'https://media.giphy.com/media/2stFpADPSpfQQ/giphy.gif',
                             'https://media.giphy.com/media/3o7aDbX8g5rNzOzfyw/giphy.gif',
                             'https://media.giphy.com/media/3oz8xIZrAhijabg69a/giphy.gif',
                             'https://media.giphy.com/media/8ZoYsRJPZM2SQ/giphy.gif',
                             'https://media.giphy.com/media/8rQb6SegFDEas/giphy.gif',
                             'https://media.giphy.com/media/pU4fr1TOmANwY/giphy.gif',
                             'https://media.giphy.com/media/fUwWC4QFwjst8bisvk/giphy.gif',
                             'https://media.giphy.com/media/l2Je2M4Nfrit0L7sQ/giphy.gif',
                             'https://media.giphy.com/media/OIkf8C99QtIo8/giphy.gif',
                             'https://media.giphy.com/media/3o6wO1HLlV98LnouGc/giphy.gif',
                             'https://media.giphy.com/media/iICTmVeWGrVn2/giphy.gif',
                             'https://media.giphy.com/media/3ohzdFL21rgRTXKUuY/giphy.gif',
                              'https://media.giphy.com/media/14ikz1075QrHs4/giphy.gif',
                              'https://media.giphy.com/media/ijuNc5JLMP2YE/giphy.gif',
                              'https://media.giphy.com/media/BhpJw9vYlhjlm/giphy.gif',
                              'https://media.giphy.com/media/LCAFK9C16AsLe/giphy.gif',
                            ])
        embed = discord.Embed( description = f"{ctx.message.author.mention} is kissing {member.mention} :heart: , what a cute couple <3 <3 ",
                               color = 0xF894E1)
        embed.set_image(url=photo)
        await ctx.send(embed=embed)
    @kiss.error
    async def kiss_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('kissing in the air (♥ω♥*) ')
        else:
            raise error

    @commands.command()
    async def hug(self,ctx,member:discord.Member):
        photo = random.choice (
            [
            'https://media.giphy.com/media/7eQ8Ky3dAsRYA/giphy.gif',
            'https://media.giphy.com/media/AOa3xz03AH4kg/giphy.gif',
            'https://media.giphy.com/media/6CnPObgngfoqI/giphy.gif',
            'https://media.giphy.com/media/WIOVfLwOOjWX6/giphy.gif',
            'https://media.giphy.com/media/M6acKkLg6DwU8/giphy.gif',
            'https://media.giphy.com/media/73mxXVFaqg19K/giphy.gif',
            'https://media.giphy.com/media/KG5oq4vesf9r8JbBEN/giphy.gif',
            'https://media.giphy.com/media/RJEIl2fBX3jAJOqSau/giphy.gif',
            'https://media.giphy.com/media/TIWxMcRbtVeIU/giphy.gif',
            'https://media.giphy.com/media/AiiYv0AjSI3C35YVQL/giphy.gif',
            ])
        embed = discord.Embed(description=f"{ctx.message.author.mention} is hugging {member.mention} :heart: , what a cute couple <3 <3 ",
                              color=0xF894E1)
        embed.set_image(url=photo)
        await ctx.send(embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('huggin you ༼ つ ̥◕͙_̙◕͖ ͓༽つ ')
        else:
            raise error

    @commands.command()
    async def insult(self, ctx,member: discord.Member):
        photo = random.choice([
                                'https://media.giphy.com/media/C42N9xIM8xo6Q/giphy.gif',
                                'https://media.giphy.com/media/26BGQhPJAjWA7VVNm/giphy.gif',
                                'https://media.giphy.com/media/x1YWdcmUCIZmU/giphy.gif',
                                 'https://media.giphy.com/media/qWpMdM0rGVgpW/giphy.gif',
                                 'https://media.giphy.com/media/wyP2tPdpswWju/giphy.gif',
                                 'https://media.giphy.com/media/XaDbJ4ZJIRUic/giphy.gif',
                                 'https://media.giphy.com/media/65EfaiqtQ9ssVXTLN4/giphy.gif',
                                  'https://media.giphy.com/media/xI6PL9TeKuxgI/giphy.gif',
                                   ''
                                    ])
        embed = discord.Embed(description = f"{member.mention} u fucking retard",
                              color = 0x392D37)
        embed.set_image(url = photo)
        await ctx.send(embed = embed)
    @insult.error
    async def insult_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```insult who??? :D ??? go fuck urself!!!```')
        else:
            raise error



def setup(bot):
    bot.add_cog(fun(bot))