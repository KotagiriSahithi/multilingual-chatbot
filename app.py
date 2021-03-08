from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)
class OptionalDependencyImportError(ImportError):
    """
    An exception raised when a feature requires an optional dependency to be installed.
    """
    pass

bot = ChatBot("Leo ChatBot")
trainer = ListTrainer(bot)
trainer.train([
    "Namaste!",
    "Vannakam",
])

trainer.train([
    "who made you?",
    "Sahithi Madhumitha Rudhira created me!",
    "What all can you do?",
    "I can chat with you in different Languages:English,Telugu,Hindi,etc..to know about the topics type all Topics",
    "all topics",
    "1.AI 2.Bot Profile 3.Computers 4.Conversation 5.Emotion 6.Food 7.Gossip 8.Greetings 9.Health10.History Type'More'",
    "More",
    "11.Humor 12.Literature 13.Money 14.Movies 15.Politics 16.Psychology 17.Science 18.Sports 19.Trivia Type 'Next'",
    "Next",
    "Greetings in Telugu,Greetings in Hindi",
    "Tell me, what can you do? ",
    "My name is Leo. I am a Chat bot!",
])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer1 = ChatterBotCorpusTrainer(bot)
trainer1.train("chatterbot.corpus.telugu")
trainer2 = ChatterBotCorpusTrainer(bot)
trainer2.train("chatterbot.corpus.hindi")
trainer3 = ChatterBotCorpusTrainer(bot)
trainer3.train("chatterbot.corpus.bangla")
trainer4 = ChatterBotCorpusTrainer(bot)
trainer4.train("chatterbot.corpus.chinese")
trainer5 = ChatterBotCorpusTrainer(bot)
trainer5.train("chatterbot.corpus.custom")
trainer6 = ChatterBotCorpusTrainer(bot)
trainer6.train("chatterbot.corpus.french")
trainer7 = ChatterBotCorpusTrainer(bot)
trainer7.train("chatterbot.corpus.german")
trainer8 = ChatterBotCorpusTrainer(bot)
trainer8.train("chatterbot.corpus.hebrew")
trainer9 = ChatterBotCorpusTrainer(bot)
trainer9.train("chatterbot.corpus.indonesia")
trainer10 = ChatterBotCorpusTrainer(bot)
trainer10.train("chatterbot.corpus.italian")
trainer11 = ChatterBotCorpusTrainer(bot)
trainer11.train("chatterbot.corpus.marathi")
trainer12 = ChatterBotCorpusTrainer(bot)
trainer12.train("chatterbot.corpus.odia")
trainer13 = ChatterBotCorpusTrainer(bot)
trainer13.train("chatterbot.corpus.portuguese")
trainer14 = ChatterBotCorpusTrainer(bot)
trainer14.train("chatterbot.corpus.russian")
trainer15 = ChatterBotCorpusTrainer(bot)
trainer15.train("chatterbot.corpus.spanish")
trainer16 = ChatterBotCorpusTrainer(bot)
trainer16.train("chatterbot.corpus.swedish")
trainer17 = ChatterBotCorpusTrainer(bot)
trainer17.train("chatterbot.corpus.tchinese")
trainer18 = ChatterBotCorpusTrainer(bot)
trainer18.train("chatterbot.corpus.thai")
@app.route("/")
def home():
   return render_template("index.html")

@app.route("/get")
def get_bot_response():
   userText = request.args.get('msg')
   return str(bot.get_response(userText))
if __name__ == "__main__":
   app.run()
