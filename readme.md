# Dungeons & Dragons Chatbot

Этот проект представляет собой чат-бота для игры в Dungeons & Dragons, который использует нейронную сеть Saiga/Llama3 8B  для генерации приключений и взаимодействия с пользователями. 
Бот может отвечать на запросы пользователей, предоставляя информацию и создавая интересные сюжетные линии.

## Функциональность

- Генерация ответов на основе запросов пользователей с использованием модели Ollama 0.3.10 и нейронной сети Saiga/Llama3 8B, в качестве эмбедера для rag был использован evilfreelancer/enbeddrus:latest.
- Взаимодействие с ChromaDB для хранения и поиска документов.
- Обработка сообщений и команд пользователей через интерфейс Telegram с помощью бота работающего на aiogram.
  
# Пример работы проекта

![1](https://github.com/user-attachments/assets/c2214d7f-c3af-4b69-b718-36a086bf531c)


![2](https://github.com/user-attachments/assets/bb0c74cd-e0b2-4146-b6ad-bfdb8483d8ad)



## Установка
1.Установите ollama version is 0.3.10

2. Установите libmagic1:
   - Debian/Ubuntu: `sudo apt-get install libmagic1`
   - Windows: Вам понадобятся DLL для libmagic. @julian-r поддерживает пакет pypi с DLL, вы можете установить его с помощью: `pip install python-magic-bin`
   - Mac: `brew install libmagic`
   
3. Установите зависимости: `pip install -r requirements.txt`

4. Убедитесь, что у вас есть модели, указанные в config.ini. Для evilfreelancer/enbeddrus:latest выполните `ollama pull evilfreelancer/enbeddrus:latest`. 

5. Затем запустите ChromaDB в отдельном терминале: `chroma run --host localhost --port 8000 --path ./chromadb`

6. Отредактируйте список документов которые вы хотите видеть в rag или оставте исходный в `sourcedocs.txt`.

7. Импортируйте документы: `python import.py`

8. Выполните поиск: `python search.py <вашзапрос>`

9. Добавьте промт в модель: `ollama create my_dnd_saiga -f my_prompt.modelfile`
10. Создайте себе личный токен для бота и добавте его в файл .env
11. Запустите бота и отправьте команду /start, чтобы начать взаимодействие.
