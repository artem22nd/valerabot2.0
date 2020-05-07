import discord
from discord.ext import commands
from discord.utils import get
import random
import pyowm
import requests
import os

PREFIX = "."

client = commands.Bot(command_prefix = PREFIX  )
client.remove_command( "help" )

# WORDS
bad_words = ["хуй", "пизда","ублюдок","пидораст","ебать","ебта","епт","сука","бля","пиздец","пидр","ебаный","ёб","хуе","пиздел","ебал","пидар","пздц","оху","сук"]
hi_words = ["Здарова валера","привет валер", "валера здарова", "привет валера", "валера", "хай валера", "валера ты тут?", "валера ты тут"]
answer_words = ["команды","узнать информацию о сервере","узнать команды","что здесь делать","информация","посмотреть список комманд",] 
goodbye_words = ["всем пока", "пока","бай","всем удачи","я пошел","мне пора"]           
goodbye_answer = ["Удачи тебе :smile: ", "Ну пока :cry:", "возвращайся скорей :blush: ","пока,ты же вернешься :smiley: ","бай бай :wink: ", "будем ждать тебя :blush: "]  
valera_answer = ["привет что то хотел? :grinning: :grinning: ","че те надо я занят!!! :angry: :rage: ","Здарова чего хотел? :sunglasses: :sunglasses: ", "бип буп <_> я тут :computer: "]
valera_muted = ["ты что охренел так базарить!!!:angry::rage:","Попрошу впредь так не выражаться:relieved::blush:","Не Матерись 5 сек если не гомосек:satisfied::wink:","Не матерись если лубис маму:joy::joy:","Слышь васик ты не в вазисубане!:confused::confused:","Не материтесь будьте умными\n<The Maska>"]

#STATUS
@client.event
async def on_ready():
	print( "VALERA Connected")
	await client.change_presence( status = discord.Status.online, activity = discord.Game("Youtube, и Смотрит новое видео на канале The Maska"))

#TALK TO BOT
@client.event
async def on_message( message ):
	msg = message.content.lower()
	await client.process_commands( message )
	print(msg)

	if msg in hi_words:
		await message.channel.send(random.choice(valera_answer))

	if msg in answer_words:
		await message.channel.send("Пропиши команду .help, и узнаешь все команды")

	if msg in goodbye_words:
		await message.channel.send(random.choice(goodbye_answer))

	for i in bad_words:
		if i in msg:
			await message.delete()
			await message.channel.send(message.author.mention)
			await message.channel.send((random.choice(valera_muted)))

		
# WELCOME
@client.event

async def on_member_join( member ):
	channel = client.get_channel(  567785863161970711  )

	role = discord.utils.get( member.guild.roles, id  = 705409292295077910 )
	await member.add_roles( role )
	await channel.send(embed = discord.Embed(description = f"Добро пожаловать ``{ member.name }``, Я подписчик канала The Maska Надеюсь ты тоже",
		               color = 0xffd700 ))

# COPY
@client.command(pass_context = True)
async def copy(ctx,agr,amount = 1): 

	await ctx.channel.purge(limit = amount)
	author = ctx.message.author

	await ctx.send(f"{ author.mention } " + agr  )

# CLEAR
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 100):

	emb = discord.Embed( title = "Контент очищен", colour = discord.Color.green())
	await ctx.channel.purge(limit = amount)
	emb.set_footer(text= f"Очищено {amount} строк")
	await ctx.send( embed = emb )

@clear.error
async def clear_error( ctx, error ):
	if isinstance(error, commands.MissingPermissions ):

		await ctx.send(f"{ctx.author.name}, у вас недостаточно прав для выполнения этой команды")

# MUTE
@client.command(pass_context = True)
@commands.has_permissions( administrator = True )
async def mute( ctx, member: discord.Member ):
	await ctx.channel.purge( limit = 1 )

	mute_role = discord.utils.get( ctx.message.guild.roles, name = "muted" ) 

	await member.add_roles( mute_role )
	await ctx.send(f"У { member.mention }, ограничение чата, за нарушение прав!")


# MASKA
@client.command(pass_context = True)
async def maska(ctx, amount = 1):

	await ctx.channel.purge( limit = amount)
	emb = discord.Embed( title = "Лучший Канал Про Игры", colour = discord.Color.red(), url = "https://www.youtube.com/channel/UCTNI8vNs4rR3NTdOEty0jjQ")

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = "Заранее Спасибо за Подписку", icon_url = client.user.avatar_url )
	emb.set_image( url = "https://cdn.discordapp.com/attachments/620615708296085529/705696311994744852/1555420426521.png")
	emb.set_thumbnail( url = "https://yt3.ggpht.com/a/AATXAJwhTVlaDVtRr97j_WjulVBcy-RPv22qqBYT=s176-c-k-c0x00ffffff-no-rj-mo")

	await ctx.send( embed = emb)

# "SHEDEVR"
@client.command()
async def karlos(ctx , amount = 1):

	await ctx.channel.purge( limit = amount )
	emb = discord.Embed( title = "Рисунок Карла", colour = discord.Color.red())

	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = "Если хотите также уметь рисовать то лучше не надо, \nидите в Художественную школу и учитесь лучше там ", icon_url = ctx.author.avatar_url )
	emb.set_image( url = "https://media.discordapp.net/attachments/620615708296085529/705786748080357426/IMG_20200501_182422.jpg?width=347&height=463")
    
	await ctx.send( embed = emb )

# MATH
@client.command(pass_context = True)
async def math( ctx, a : int, arg, b :int, amount = 1 ):
	await ctx.channel.purge( limit = amount )
	emb1 = discord.Embed( title = f"{ctx.author.name}, Результат: { a + b }  ", colour = discord.Color.green())
	emb2 = discord.Embed( title = f"{ctx.author.name}, Результат: { a - b }  ", colour = discord.Color.green())
	emb3 = discord.Embed( title = f"{ctx.author.name}, Результат: { a / b }  ", colour = discord.Color.green())
	emb4 = discord.Embed( title = f"{ctx.author.name}, Результат: { a * b }  ", colour = discord.Color.green())

	if arg == "+":
		await ctx.send( embed = emb1 )
	if arg == "-":
		await ctx.send( embed = emb2 )
	if arg == "/":
		await ctx.send( embed = emb3 )
	if arg == "*":
		await ctx.send( embed = emb4 )

@math.error
async def math_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):

		await ctx.send(f"{ctx.author.name}, Введите Аргументы,Пример .math 5 * 5")

# WEATHER
@client.command(pass_context = True)
async def weather( ctx,arg, amount = 1 ):
	await ctx.channel.purge( limit = amount )
	owm = pyowm.OWM('1b2f7cd5a776233af24f186c4f52e4d0',language="ru")
	observation = owm.weather_at_place(arg)
	w = observation.get_weather()
	temperature=w.get_temperature('celsius')['temp']
	emb = discord.Embed( title = f"В городе {arg}, {w.get_detailed_status()} \nи {temperature} градусов по цельсию", colour = discord.Color.blue())
	emb.set_author( name = ctx.author.name, icon_url = ctx.author.avatar_url )
	emb.set_thumbnail(url = "https://images.chinahighlights.ru/2013/05/ab3de77f0a034f57809961d9-m.jpg")
	await ctx.send( embed = emb)

@weather.error
async def weather_error(ctx,error):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send(f"{ctx.author.name}, Введите Аргумент,Пример: .weather 'город'")

# RULES
@client.command(pass_context = True)
async def rules( ctx,amount = 1 ):
	await ctx.channel.purge( limit = amount )
	emb = discord.Embed( title = f"Правила", colour = discord.Color.green())
	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = "Хей! Это правила дискорд сервера <ТОП> Почему ТОП? Потому что он топовый а\nтеперь внимательно читай правила за нарушение правил даётся Kick Mute и Ban\nсмотря на сколько серьёзно вы нарушили правила и нарушили покой других\nучастников даже иногда лишения Уровня и Роли")
	
	await ctx.author.send(embed = emb)

# IP_INFO
@client.command(pass_context = True)
async def ipinfo( ctx, arg ):
	response = requests.get( f"http://ipinfo.io/{ arg }/json" )

	user_ip = response.json()[ "ip" ]
	user_city = response.json()[ "Город" ]
	user_region = response.json()[ "Область" ]
	user_country = response.json()[ "Страна" ]
	user_location = response.json()[ "Место нахождения"]
	user_org = response.json()[ "Организация" ]
	user_timezone = response.json()[ "Часовой пояс "]

	global all_info
	all_info = f'\n<INFO>\nIP : {user_ip}\nГород : {user_city}\nОбласть : {user_region}\nСтрана : {user_country}\nМесто Нахождения : {user_location}\nОрганизация : {user_org}\nЧасовой Пояс : {user_timezone}' 

	await ctx.channel.send( all_info )

# HELP
@client.command(pass_context = True)
async def help( ctx, amount = 1 ):

	await ctx.channel.purge( limit = amount )
	emb = discord.Embed( title = "Навигация по командам", colour = discord.Color.red())
    
	emb.add_field( name = "{}help :wave: ".format( PREFIX ), value = "Помощь по Командам :ok_hand: ,")
	emb.add_field( name = "{}copy :floppy_disk: ".format( PREFIX ), value = "Копирует текст и вставляет,")
	emb.add_field( name = "{}clear :pencil2: ".format( PREFIX ), value = "Удаляет прошлые сообщения'доступно только Админам,'")
	emb.add_field( name = "{}maska :thumbsup: :thumbsup: :thumbsup: ".format( PREFIX), value = "Лучший канал про игры,")
	emb.add_field( name = "{}karlos :sunrise_over_mountains: ".format( PREFIX ), value = "Рисунок Карла,")
	emb.add_field( name = "{}math :1234: :1234: ".format( PREFIX ), value = "Калькулятор,")
	emb.add_field( name = "{}weather :partly_sunny: :sunny: :snowflake: :umbrella: :zap: ".format( PREFIX ), value = "Прогноз погоды")
	await ctx.send( embed = emb )

# Connect

token = os.environ.get("token")
client.run( token )
