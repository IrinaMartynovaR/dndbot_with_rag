import os
from dotenv import load_dotenv
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import ollama
import chromadb
from utilities import getconfig, readtext
from mattsollamatools import chunker, chunk_text_by_sentences
import random


load_dotenv()

bot = Bot(token=os.environ["TOKEN"])
dp = Dispatcher()  # Передаем экземпляр бота при создании диспетчера

# ChromaDB and embedding setup
collectionname = "buildragwithpython"
chroma = chromadb.HttpClient(host="localhost", port=8000)
collection = chroma.get_or_create_collection(name=collectionname, metadata={"hnsw:space": "cosine"})

embedmodel = getconfig()["embedmodel"]
mainmodel = getconfig()["mainmodel"]

# Helper function to process user query
async def query_model(user_query):
    queryembed = ollama.embeddings(model=embedmodel, prompt=user_query)['embedding']
    relevantdocs = collection.query(query_embeddings=[queryembed], n_results=5)["documents"][0]
    docs = "\n\n".join(relevantdocs)
    modelquery = f"{user_query} - Answer that question using the following text as a resource: {docs}"

    # Stream the response from Ollama's model
    response = ""
    stream = ollama.generate(model=mainmodel, prompt=modelquery, stream=True)
    for chunk in stream:
        if chunk["response"]:
            response += chunk['response']
    return response

# Handler for the /start command
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот мастер ДНД, я генерирую приключения. Если ты готов то напиши об этом и мы начнем")


thinking_phrases = [
    "Хмммм... сейчас что-нибудь придумаю.",
    "Дай-ка подумать...",
    "Секундочку, я подумаю над этим.",
    "Минуточку, нужно что-то придумать.",
    "Дай мне немного времени, посмотрю, что можно сделать.",
    "Ммм... интересный вопрос, сейчас подумаю.",
    "Попробую что-то придумать... один момент.",
    "Хм... дайте-ка мне секунду.",
    "Задумался... секундочку!",
    "Хмм... посмотрим, что у меня получится.",
    "Подожди немного, сейчас попробую решить это.",
    "Нужно подумать... дай мне пару секунд.",
    "Этот вопрос требует размышлений... подожди немного.",
    "Сейчас посмотрю, что можно сделать.",
    "Момент, требуется немного времени, чтобы разобраться.",
    "Обрабатываю запрос... мои нейроны немного перегрелись!",
    "Пожалуйста, подождите, загружаю мыслительный процессор...",
    "Так-так, мои схемы слегка заискрились... сейчас всё будет.",
    "Ой, нужно немного времени, чтобы все шестеренки провернулись!",
    "Хмм, мои датчики говорят, что я должен подумать… подожди.",
    "Перегоняю байты, ищу ответ... почти готово!",
    "Мои транзисторы требуют секундочку для размышления...",
    "Ожидание ответа от серверов... надеюсь, мои провода не запутались!",
    "Процессор немного тормозит... подожди пока я разгоню мысли.",
    "Эй, мне нужно немного времени, чтобы собрать все нули и единицы в кучу!",
    "Мозговой чип требует перезагрузки... один момент!",
    "Загружаю ответ... не переживай, я не завис!",
    "Синхронизируюсь с облаком... дай мне секундочку!"
]


# Handler for user messages
@dp.message()
async def handle_message(message: Message):
    user_query = message.text
    random_thinking_phrase = random.choice(thinking_phrases)
    await message.answer(random_thinking_phrase)
    response = await query_model(user_query)
    await message.answer(response)

# Start polling
async def main():
    logging.basicConfig(level=logging.INFO)

    # Register handlers
    dp.message.register(start_command)
    dp.message.register(handle_message)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
