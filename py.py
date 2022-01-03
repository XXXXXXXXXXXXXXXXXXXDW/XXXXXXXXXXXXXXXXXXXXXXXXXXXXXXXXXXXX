import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "-")


token = "OTI2ODg4NDAyMTExMDQxNTc2.YdCOFw.IDTlIDFtWCtOtxQtxg_hpReKamc"


@client.command(aliases=['orderr','orderrrr'])
async def order(ctx):
    embed = discord.Embed(title = "questions:" , description = "answer there questions." , color = discord.Colour.red())
    embed.add_field(name='question #1', value = 'how much would you like to order', inline=False)
    embed.add_field(name='question #2', value = 'what payment method are you using', inline=False)
    embed.add_field(name='after answering', value = 'after answering all the questions please wait for a dhc seller to come and respond to your ticket. (can take a few hours) please be patient', inline=False)  
    await ctx.send(embed=embed)

@client.command(aliases=['ordergiftcodeee','ordergiftcodeeeeeeeeeeee'])
async def ordergiftcode(ctx):
    embed = discord.Embed(title = "questions:" , description = "answer there questions." , color = discord.Colour.red())
    embed.add_field(name='question #1', value = 'how much dhc gift code would u like to buy', inline=False)
    embed.add_field(name='question #2', value = 'what payment method are you using', inline=False)
    embed.add_field(name='after answering', value = 'after answering all the questions please wait for a giftcode seller to come and respond to your ticket. (can take a few hours) please be patient', inline=False)  
    await ctx.send(embed=embed)

@client.command(aliases=['r11','r111'])
@commands.has_permissions(manage_nicknames=True)
async def r1(ctx):
    await ctx.channel.send("oh here looks like theres a seller")
    await ctx.channel.send("wait for the seller to get ready")
    await ctx.channel.send("when the seller is ready the seller will ping you")

@client.command(aliases=['giftcodessss','giftcodessssssssss'])
@commands.has_permissions(manage_nicknames=True)
async def giftcodes(ctx):
    embed = discord.Embed(title = "current gift codes:", description = "the current gift codes for dhczz" , color = discord.Colour.red())
    embed.add_field(name='currently no codes', vlaue = 'currently no codes', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['giftcodeinfoo','giftcodeinfoooo'])
async def giftcodeinfo(ctx):
    embed = discord.Embed(title = "gift code info", description = "dhczz gift code is just like buying dhc normally but instead u get the dhc when u use the gift code and you can give anyone the gift code too like you can give it to your friend as a gift to get dhc", color = discord.Colour.red())
    embed.add_field(name='info:', value='the prices are the same as the normal dhc prices after buying gift code we will dm you the gift code', inline=False)
    embed.add_field(name='more info', value='dhc codes can be used as discounts for example u have a 5 mil dhc code and u wanna buy 10 mil dhc if u use the 5 mil dhczz code the 10 mil ur buying is gonna be 50 percent off', inline=False)
    embed.add_field(name='more more info', value='check description for more more info', inline=False)
    embed.add_field(name='use this command to buy the gift code', value='-buygiftcode', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['buygiftcodee','buygiftcodeee'])
async def buygiftcode(ctx):
    embed=discord.Embed(title="giftcode prices:", description="use the command: -giftcodeinfo for info about dhczz gift code", color = discord.Colour.red())
    embed.add_field(name="usd prices:", value="5$ = 9 mil dhc code", inline=False)
    embed.add_field(name=".", value="10$ = 18 mil dhc code", inline=False)
    embed.add_field(name=" rbx prices:", value=".", inline=False)
    embed.add_field(name="50 rbx ", value="1 mil dhc code", inline=True)
    embed.add_field(name="100 rbx ", value="2 mil dhc code", inline=True)
    embed.add_field(name="150 rbx ", value="3 mil dhc code", inline=True)
    embed.add_field(name="200 rbx ", value="4 mil dhc code", inline=True)
    embed.add_field(name="250 rbx", value="5 mil dhc code", inline=True)
    embed.add_field(name="300 rbx", value="6 mil dhc code", inline=True)
    embed.add_field(name="350 rbx", value="7 mil dhc code", inline=True)
    embed.add_field(name="400 rbx", value="9 mil dhc code", inline=True)
    embed.add_field(name="450 rbx ", value="10 mil dhc code", inline=True)
    embed.add_field(name="500 rbx", value="11 mil dhc code", inline=True)
    embed.add_field(name="550 rbx ", value="12 mil dhc code", inline=True)
    embed.add_field(name="600 rbx", value="13 mil dhc code", inline=True)
    embed.add_field(name="650 rbx ", value="14 mil dhc code", inline=True)
    embed.add_field(name="700 rbx", value="15 mil dhc code", inline=True)
    embed.add_field(name="750 rbx", value="16 mil dhc code", inline=True)
    embed.add_field(name="800 rbx", value="17 mil dhc code", inline=True)
    embed.add_field(name="850 rbx", value="18 mil dhc code", inline=True)
    embed.add_field(name="boost prices:", value=".", inline=True)
    embed.add_field(name="1 boost", value="5 mil dhc code", inline=True)
    embed.add_field(name="2 boost", value="10 mil dhc code", inline=True)
    embed.add_field(name="3 boost", value="15 mil dhc code", inline=True)
    embed.add_field(name="4 boost", value="20 mil dhc code", inline=True)
    embed.set_footer(text=".")
    await ctx.send(embed=embed)
    

@client.command(aliases=['invalid.link','invalid-link'])
@commands.has_permissions(manage_nicknames=True)
async def invalidlink(ctx):
    await ctx.channel.send("invalid link ):")
    await ctx.channel.send("looks like the private server link is invalid join our backup private server below")




@client.command(aliases=['privateserver1','privserver1'])
@commands.has_permissions(manage_nicknames=True)
async def priv1(ctx):
    embed = discord.Embed(title = "private server link!" , description = "heres the private server link make sure to join it a seller is waiting.." , color = discord.Colour.red())
    embed.add_field(name="link:", value=f'**[Click Here](https://shortest.link/2lXw)**', inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['private2','privserver2'])
@commands.has_permissions(manage_nicknames=True)
async def priv2(ctx):
    embed = discord.Embed(title = "backup private server link!" , description = "the other one was invalid so here is the backup one!" , color = discord.Colour.red())
    embed.add_field(name="link:", value=f'**[Click Here](https://www.roblox.com/games/2788229376?privateServerLinkCode=44445435435595271960685243489331)**', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['dhcpricess','dhcpricessss'])
async def dhcprices(ctx):
    embed=discord.Embed(title="dhc prices:", description="dhc prices!!", color = discord.Colour.red())
    embed.add_field(name="usd prices:", value="5$ = 9 mil dhc ", inline=False)
    embed.add_field(name=".", value="10$ = 18 mil dhc ", inline=False)
    embed.add_field(name=" rbx prices:", value=".", inline=False)
    embed.add_field(name="50 rbx ", value="1 mil dhc ", inline=True)
    embed.add_field(name="100 rbx ", value="2 mil dhc ", inline=True)
    embed.add_field(name="150 rbx ", value="3 mil dhc ", inline=True)
    embed.add_field(name="200 rbx ", value="4 mil dhc ", inline=True)
    embed.add_field(name="250 rbx", value="5 mil dhc", inline=True)
    embed.add_field(name="300 rbx", value="6 mil dhc", inline=True)
    embed.add_field(name="350 rbx", value="7 mil dhc", inline=True)
    embed.add_field(name="400 rbx", value="9 mil dhc ", inline=True)
    embed.add_field(name="450 rbx ", value="10 mil dhc", inline=True)
    embed.add_field(name="500 rbx", value="11 mil dhc", inline=True)
    embed.add_field(name="550 rbx ", value="12 mil dhc", inline=True)
    embed.add_field(name="600 rbx", value="13 mil dhc", inline=True)
    embed.add_field(name="650 rbx ", value="14 mil dhc ", inline=True)
    embed.add_field(name="700 rbx", value="15 mil dhc ", inline=True)
    embed.add_field(name="750 rbx", value="16 mil dhc ", inline=True)
    embed.add_field(name="800 rbx", value="17 mil dhc ", inline=True)
    embed.add_field(name="850 rbx", value="18 mil dhc ", inline=True)
    embed.add_field(name="boost prices:", value=".", inline=False)
    embed.add_field(name="1 boost", value="5 mil dhc ", inline=True)
    embed.add_field(name="2 boost", value="10 mil dhc ", inline=True)
    embed.add_field(name="3 boost", value="15 mil dhc ", inline=True)
    embed.add_field(name="4 boost", value="20 mil dhc", inline=True)
    embed.add_field(name="fast pass", value="go to #fast-pass to get the fast pass or use the command -fastpass", inline=False)
    embed.set_footer(text=".")
    await ctx.send(embed=embed)

@client.command(aliases=['fastpasss','fastpassss'])
async def fastpass(ctx):
    embed=discord.Embed(title="fast pass!!!", description=".", color = discord.Colour.red())
    embed.add_field(name="fast pass", value="fast pass means that were gonna do ur order faster and do it before non fast passers", inline=False)
    embed.add_field(name="normal fast pass ~", value="50 rbx", inline=True)
    embed.add_field(name="super fast pass ~", value="100 rbx", inline=True)
    embed.add_field(name="extreme super fast pass ~", value="150 rbx", inline=True)
    embed.add_field(name="OMEGA SUPER FAST PASS ~", value="200 rbx", inline=True)
    embed.add_field(name="note:", value="you can only buy a fast pass when u have a order/ claiming a dhc code", inline=True)
    embed.set_footer(text=".")
    await ctx.send(embed=embed)

@client.command()
async def ready(ctx, member: discord.Member):
    await ctx.channel.send("the seller is ready, please join the private server right now.")
    await ctx.channel.send(f'oi {member.mention} the seller is waiting for you ')
    await ctx.channel.send(f'{member.mention}')
    await ctx.channel.send(f'{member.mention}')
    await ctx.channel.send(f'{member.mention}')
    await ctx.channel.send(f'{member.mention}')
    await ctx.channel.send(f'{member.mention}')
    await ctx.channel.send(f'{member.mention}')
    await ctx.channel.send(f'{member.mention}')


@client.event
async def on_ready():
    print("ready")

client.run(token)