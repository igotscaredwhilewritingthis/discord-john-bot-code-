import discord
import json
from discord.ext import commands

class Boinks(commands.Cog):
    @commands.command(name="fetch_channels")
    async def fetch_channels(self, ctx):
        if not self.boink_counts:
            await ctx.send("No channels tracked yet!")
            return

        for channel_id in self.boink_counts.keys():
            channel = self.bot.get_channel(channel_id)
            if channel:
                print(f"ID: {channel_id}: Name = #{channel.name}")
            else:
                print(f"ID: {channel_id} -> Why can I not find anything")
        
        await ctx.send("hop on idle mate")




  
