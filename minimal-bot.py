import interactions
from interactions import Embed, OptionType, slash_option, slash_command, Client, Intents, listen, SlashContext, SlashCommandChoice
import scraper

import os
script_dir = os.path.dirname(__file__)
rel_path = "/images"

bot = Client(intents=Intents.DEFAULT)

# this command will display a list of commands the user can type
@slash_command(name="help", description="lists available commands")
async def help(ctx:SlashContext):
    embed = restaurant_embed("Pookie's Cookies", "My glorious snuggle pookie bear LeBooBoo James", \
                             "https://assets-global.website-files.com/646218c67da47160c64a84d5/64633998101622cb2b3fca4b_06.png")
    embed.set_image(url="https://media.tenor.com/T2sgUDZt6CcAAAAM/hi-hello.gif")

    # Send the embed to the user
    await ctx.send(embed=embed)

# returns a restuarant embed given a name, description, and image url (obtained from webscraping)
def restaurant_embed(name, description, image_url):
    embed = Embed(
        title = name,
        description = description,
        color = interactions.Colour.from_rgb(100, 100, 100)
    )
    embed.set_image(url = image_url)
    return embed

# a command for searching for a halal restaurant by cuisine type and location
@slash_command(name="find-restaurants", description='finds restaurants')
@slash_option(
    name = "cuisine", 
    description = "What cuisine do you want?",
    required = True,
    opt_type = OptionType.STRING
)
@slash_option(
    name = "location",
    description = "Where do you want to eat?",
    required = True,
    opt_type = OptionType.STRING
)
async def find_restaurants(ctx: SlashContext, cuisine: str, location: str):
    # ask the user for the type of food they're craving
    await ctx.send("What type of food are you craving?")
    result = scraper.getRestaurants(cuisine, location)
    await ctx.send(result)

# ask the user what price range they want, and display restaurants based on their choice
@slash_command(name="price", description="check prices")
@slash_option(
    name="price_option",
    description="Price Option",
    required=True,
    opt_type=OptionType.INTEGER,
    choices=[
        SlashCommandChoice(name="$", value=1),
        SlashCommandChoice(name="$$", value=2),
        SlashCommandChoice(name="$$$", value=3),
    ]
)
async def my_command_function(ctx: SlashContext, price_option: int):
    if price_option == 1:
        await ctx.send(f"A list of budget friendly options:\nGhareeb Nawaz\nJerusalem Cafe")
    elif price_option == 2:
        await ctx.send(f"A list of middle-range priced options:\nShahana Steakhouse\nHalal Burger")
    elif price_option == 3:
        await ctx.send(f"A list of expensive options:\nElisa Steak House\nMagical Taste of China")

# display the credits of the Roti Boys who worked on the RotiBot
@slash_command(name="credits", description="show credits")
async def show_credits(ctx=SlashContext):
    await ctx.send("The dear Roti Boys who contributed to Roti Bot:\nZayd Khan \
                   \nBen Cruz\nDaniya Safdar\nIsabella Chou")

# check if it is ready
@interactions.listen
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Triggered when anyone sends a message
@interactions.listen
async def on_message(message):
    # If sender is bot, ignore it
    if message.author == bot.user:
        return
    
    # If message starts with 'hello', bot will respond:
    if message.content.startswith('hello'):
        await message.channel.send(f'Hello dear Roti Boy, {message.author.mention}!\n \
                                   I am RotiBot!\nType /help to get a list of commands.')
    # Any other message, bot will respond:
    else:
        await message.channel.send(f'Lets get halal!')

bot.start('insert token here')