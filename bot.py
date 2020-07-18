import discord
import requests
from config import discord_api_key

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

_PREFIX = '$'

def parse_message(msg):
	commandList = msg.split()
	myDict = dict()
	myDict["init"] = commandList[0]

	flags = []
	for i in commandList:
		if i[0] == '-':
			flags.append(i)
	myDict["flags"] = flags

	args = []
	for i in commandList[1:]:
		if i[0] != '-':
			args.append(i)
	myDict["args"] = args

	return myDict

@client.event
async def on_message(message):
	global _PREFIX

	if message.author == client.user and message.content.startswith(_PREFIX) != True:
		print("here")
		return

	cmd = parse_message(message.content)
	print("ALL GOOD = ", message.content, message.content.startswith(_PREFIX))

	# if commandList[0] == _PREFIX + 'changePrefix':
	# 	if len(commandList) != 2:
	# 		await message.channel.send('**Error:** please use this format: `' + _PREFIX + 'changePrefix ' + '[newPrefix]`')
	# 		return
	# 	else:
	# 		_PREFIX = commandList[1]
	# 		await message.channel.send('The prefix has been changed to `' + _PREFIX + '`')
	# 		return
	# elif commandList[0] == _PREFIX + 'register':
	# 	if len(commandList) != 1:
	# 		await message.channel.send('**Error:** please use this format: `' + _PREFIX + 'register`')
	# 		return
	# 	else:
	# 		await message.author.create_dm()
	# 		await message.author.dm_channel.send('welcome to my Discord server!')
	# elif commandList[0] == _PREFIX + 'send':
	# 	if len(commandList) != 1:
	# 		await message.channel.send('**Error:** please use this format: `' + _PREFIX + 'send`')
	# 		return
	# 	else:
	# 		URL = 'http://localhost:9000/query?Method=post&discordName=DavidShoehashtag1775&valRank=plat1'
	# 		def check_valid_status_code(request):
	# 			if request.status_code == 200:
	# 				return request.text

	# 			return False
	# 		request = requests.get(URL)
	# 		data = check_valid_status_code(request)
	# 		print(data)
	# else:
	# 	await message.channel.send('**Error:** unknown command! Try ' + _PREFIX + 'commandList for a list of compatible commands.')
	# 	return

client.run(discord_api_key)
