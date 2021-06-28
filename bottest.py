import os
import random
import discord
from discord.ext import commands

with open('token.txt' , 'r') as f:
	TOKEN = f.read().strip()

bot = commands.Bot(command_prefix='boo-')
print("Bot connected...")

@bot.command(name='joke' , help = "Here's your very own Dad Joke Teller! Type 'boo-joke' for a dad joke!")
async def tellJoke(ctx):
    l1 = ["What rock group has four men that don't sing? Mount Rushmore.","When I was a kid, my mother told me I could be anyone I wanted to be. Turns out, identity theft is a crime.",'A guy goes to his doctor because he can see into the future. The doctor asks him, "How long have you suffered from that condition?" The guy tells him, "Since next Monday."',
			"What do sprinters eat before a race? Nothing, they fast!",
			"What concert costs just 45 cents? 50 Cent featuring Nickelback!",
			"What do you call a mac 'n' cheese that gets all up in your face? Too close for comfort food!",
			"Why couldn't the bicycle stand up by itself? It was two tired!",
			"Did you hear about the restaurant on the moon? Great food, no atmosphere!",
			"Why do melons have weddings? Because they cantaloupe!",
			"What happens when you go to the bathroom in France? European.",
			"What's the difference between a poorly dressed man on a tricycle and a well-dressed man on a bicycle? Attire!",
			"How many apples grow on a tree? All of them!",
			"Did you hear the rumor about butter? Well, I'm not going to spread it!",
			"Did you hear about the guy who invented Lifesavers?  They say he made a mint!",
			"Last night I had a dream that I weighed less than a thousandth of a gram. I was like, 0mg.",
			"A cheese factory exploded in France. Da brie is everywhere!",
			"Why did the old man fall in the well? Because he couldn't see that well!",
			"What do you call a factory that sells passable products? A satisfactory!"
			"Why did the invisible man turn down the job offer? He couldn't see himself doing it!",
			"Want to hear a joke about construction? I'm still working on it!",
			'I was really angry at my friend Mark for stealing my dictionary. I told him, "Mark, my words!"',
			"How does Moses make his coffee? Hebrews it.",
			"I'm starting a new dating service in Prague. It's called Czech-Mate.",
			"I was just reminiscing about the beautiful herb garden I had when I was growing up. Good thymes.",
			'Do you know the last thing my grandfather said to me before he kicked the bucket? "Grandson, watch how far I can kick this bucket." ']

    response = random.choice(l1)
    await ctx.send(response)

@bot.command(name = "greet" , help = "Have Boo greet anyone by typing 'boo-greet <name>'!")
async def greetUser(ctx , name :str):
	greetings = ["Halo {}! How's it going?" , "Aur {}, kya haal chaal?" , "Hey {}! Nice to have you here!" , "Konnichi wa, {}!" , "Hello there, {}! Hope all's well..:)", "Namastey {}! Badhiya sab?"]
	await ctx.send(random.choice(greetings).format(name))

@bot.command(name = "flirt" , help = "Type 'boo-flirt <name>' and watch as Boo tries a cheeky pickup line on you!")
async def greetUser(ctx , name :str):
	lines = ["Hey {}, Are you a magician? Because whenever I look at you, everyone else disappears!",
				"Hey {}, I’m not a photographer, but I can picture me and you together.",
				"Hey {}, They say Disneyland is the happiest place on earth. Well apparently, no one has ever been standing next to you.",
				"Hey {}, I seem to have lost my phone number. Can I have yours?",
				"Hey {}, I’m lost. Can you give me directions to your heart?",
				"Hey {}, Are you sure you’re not tired? You’ve been running through my mind all day.",
				"Hey {}, Would you grab my arm, so I can tell my friends I’ve been touched by an angel?",
				"Hey {}, Is your name Google? Because you have everything I’ve been searching for.",
				"Hey {}, If nothing lasts forever, will you be my nothing?",
				"Hey {}, Can you take me to the doctor? Because I just broke my leg falling for you.",]
	await ctx.send(random.choice(lines).format(name))


bot.run(TOKEN)
