from PyZest.telegram import SimpleBot
bot = SimpleBot("TOKEN")
@bot.command("start")
bot.start()
