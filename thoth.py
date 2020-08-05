import discord
from discord.ext import commands
from googlesearch import search
import random
import wikipedia
from googletrans import Translator
from PyDictionary import PyDictionary
import os

bot = commands.Bot(command_prefix = "T>")

@bot.event
async def on_ready():
    print('start')

@bot.command()
async def LookFor(ctx, arg):
	query = arg
	for R in search(query, tld="com", num= 3, stop=3, pause=1): 
		await ctx.send(R)

@bot.command()
async def WhatIs(ctx, arg):
	S = wikipedia.search(arg)
	R = wikipedia.summary(arg, sentences = 3)
	await ctx.send(R)

@bot.command()
async def Trans(ctx, arg1, arg2):
	Tr = Translator()
	trans = Tr.translate(arg1, dest = arg2)
	await ctx.send(trans.text)

@bot.command()
async def Define(ctx, arg):
	dictionary=PyDictionary()
	
	D = dictionary.meaning(arg)
	await ctx.send(D)

@bot.command()
async def Help(ctx):
	H = """
	use T> before commands
	LookFor = Google search something
	WhatIs = a summary about something 
	Trans = translate a word/phrase
	Define = get the definition
	put the phrase between quotes"""
	await ctx.send(H)

bot.run(os.environ["token"])



