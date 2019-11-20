import discord
import time
import asyncio
from discord.utils import get
import random
from discord.ext import commands
from discord.ext.commands import bot

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def server_report(guild):
        online = 0
        offline = 0
        total = 0
        for m in guild.members:
            total = total + 1
            if str(m.status) == "offline":
                offline = offline + 1
            else:
                online = online + 1
        return online, offline, total

    @commands.command()
    @commands.has_role('Discord Mod')
    @commands.has_permissions(administrator=True)
    async def kick(self,ctx, member:discord.Member, *, reasons = None):
        if member == self.bot.user:
            await ctx.send ("```kick con cac```")
            return
        if member.id == 376047361765670912:
            await ctx.send("```you cant do it comrade you fucking piece of shit lil bitch 凸(｀⌒´メ)凸 ``` ")
            return
        if member.id == ctx.message.author.id:
            await ctx.send("```wtf u cant kick urself fucking idiot ??(ο´･д･)?? ``` ")
            return
        await ctx.guild.kick(member)
        await ctx.send (f"lượn đi {member.mention} ( ︶︿︶)_╭∩╮ ")
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("```You are not allowed to kick people``` ```")
            return

#---------------------------ban a member---------------------------------------------------#

    @commands.command()
    @commands.has_role('Discord Mod')
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx, member:discord.Member,*,reasons = None,delete_message_days=0):
        if member == self.bot.user:
            await ctx.send ("```ban ur mom```")
            return
        if member.id == 376047361765670912:
            await ctx.send("```you cant do it comrade you fucking piece of shit lil bitch 凸(｀⌒´メ)凸  ```")
            return
        if member.id == ctx.message.author.id:
            await ctx.send("```ban urself ??? :D ???```")
            return
        await ctx.guild.ban(member)
        await ctx.send (f"{member.mention}, cút !!! ")
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("```You are not allowed to ban people```")


#--------------------mute member---------------------------------------------------#
    @commands.command()
    @commands.has_role('Discord Mod')
    @commands.has_permissions(administrator=True)
    async def mute(self,ctx, member : discord.Member,*,reasons = None):
        if member == self.bot.user:
            await ctx.send("mute ur mom")
            return
        elif member.id == 376047361765670912:
            await ctx.send("u cant do dis staph idiot -_-")
            return
        elif member.id == ctx.message.author.id:
            return
        elif not member:
            await ctx.send("mute cđgt????")
            return

        mute_role = discord.utils.get(ctx.guild.roles, name="muted")
        if mute_role is None:
                role = await ctx.guild.create_role(name="muted")
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(role, send_messages=False,)
        await member.add_roles(mute_role,reason = reasons)
        await ctx.send(f"{member.mention}, bạn đã bị ăn Global Silence bởi {ctx.message.author.mention}")

    @mute.error
    async def mute_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Không đủ mana để mute")
    @commands.command()
    @commands.has_role('Discord Mod')
    @commands.has_permissions(administrator=True)
    async def unmute(self,ctx, member: discord.Member):
        if not member:
            await ctx.send("unmute cđgt????")
            return
        mute_role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.remove_roles(mute_role)
        await ctx.send(f"{member.mention}, Global Silence đã hết, chạy ngay điiiiii.....")

    @mute.error
    async def unmute_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("stap stap stap u cant do dis shiet")

    @commands.command()
    @commands.has_role('Counselor')
    async def kickass(self,ctx,member:discord.Member,*,reason = None):
        if member == self.bot.user:
            await ctx.send ("```kick ur dad, ass ur mom```")
            return
        if member.id == 376047361765670912:
            await ctx.send("```you fucking cock-blocker, go the fuck away!!!!```")
            return

        kickass_role = discord.utils.get(ctx.guild.roles, name="bad bad u bad u fucking sinner")
        if kickass_role is None:
            role = await ctx.guild.create_role(name="bad bad u bad")
            for channel in ctx.guild.text_channels:
                if channel.name.startswith('cabin') == True:
                    await channel.set_permissions(role, send_messages=False, read_messages=False,)
        await member.add_roles(kickass_role)
    @commands.command()
    @commands.has_role('Counselor')
    async def unblock(self,ctx,member:discord.Member,*,reason = None):
        kickass_role = discord.utils.get(ctx.guild.roles, name="bad bad u bad")
        await member.remove_roles(kickass_role)
        await message.author.send('bạn đã được tha thứ, hãy vào lại cabin của bạn đi')


#---------------------shoot------------------------#
    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.has_role('Discord Mod')
    async def shoot(self,ctx, member : discord.Member,*, reason = None):
        if member == self.bot.user:
            await ctx.send ("```shoot ur mom```")
            return
        if member.id == 376047361765670912:
            await ctx.send("```you cant do it comrade you fucking piece of shit lil bitch 凸(｀⌒´メ)凸  ```")
            return
        if member.id == ctx.message.author.id:
            await ctx.send("```wanna shoot urself, try ```;rr```, noob!!!")
            return
        x = random.uniform(1.0, 10.0)
        if (x>7) :
            await ctx.guild.kick(member)
            await ctx.send (f"{member.mention} đã lên bảng đến số")
        else :
            await ctx.send (f"{member.mention}, bạn đã sống sót ")


#--------------------------- russian-roulette------------------#
    @commands.command()
    async def rr(self,ctx):
        bullet = random.uniform(1.0, 10.0)
        if ( bullet <= 5) :
            if (ctx.message.author.id == 376047361765670912 ) :
                await ctx.send("bất tử :ok_hand: :ok_hand:")
            else:
                await ctx.guild.kick(message.author)
                await ctx.send(f"{member.mention} đã lên bảng đến số")
        else :
            await ctx.send("đã sống :uwu: :ok_hand:")



#---------------coin-flip---------------------------#
    @commands.command()
    async def cf(self,ctx):
        choice = random.uniform(1.0, 10.0)
        if (choice >= 5) :
            await ctx.send("```tail```")
        else :
            await ctx.send ("```head```")

    @commands.command()
    async def ping(self,ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")

    @commands.command()
    async def server(self,ctx):
        server_info = bot.get_guild(541251950730018818)
        online, offline, total = server_report(server_info)
        server_info_embed = discord.Embed(description = f"Online: {online}\nOffline: {offline}\nTotal members: {total}" , color = 0x6666FF)
        await ctx.send(embed = server_info_embed)



    @commands.command(pass_context=True)
    async def info(self,ctx):
        info_embed = discord.Embed(description="Bot được dev bởi Tommy Vũ from server D2Q. Mọi hỗ trợ hãy liên hệ Cheshire#0101", color=0xCCCCFF)
        await ctx.send(embed = info_embed)

    # @commands.command()
    # async def block(self, ctx, member:discord.Member):
    #     if not member:  # checks if there is user
    #         return await ctx.send("block what??")
    #     if member is self.bot.user :
    #         await ctx.send("you fucking cock-blocker, go the fuck away!!!!")
    #     if member.id == 376047361765670912 :
    #         await ctx.send("block ur mom")
    #     if member.id is ctx.message.author.id:
    #     await ctx.set_permissions(member, send_messages=False)  # sets permissions for current channel
    #
    # @commands.command()
    # async def unblock(self, ctx, member: discord.Member):
    #     if not member:  # checks if there is user
    #         return await ctx.send("You must specify a user")
    #     await ctx.set_permissions(user, send_messages=True)  # gives back send messages permissions

def setup(bot):
    bot.add_cog(moderation(bot))