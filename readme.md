1. Установите libmagic1 инструменты:
   - **Debian/Ubuntu**: `sudo apt-get install libmagic1`
   - **Windows**: Вам понадобятся DLL для libmagic. @julian-r поддерживает пакет pypi с DLL, вы можете установить его с помощью: `pip install python-magic-bin`
   - **Mac**: `brew install libmagic`
   
2. Начните с установки зависимостей: `pip install -r requirements.txt`

3. Убедитесь, что у вас есть модели, указанные в config.ini. Для nomic-embed-text выполните `ollama pull nomic-embed-text`. Обновите конфигурацию, чтобы отобразить модели, которые вы хотите использовать.

4. Затем запустите ChromaDB в отдельном терминале: `chroma run --host localhost --port 8000 --path ./chromadb`

5. Отредактируйте список документов в `sourcedocs.txt`.

6. Импортируйте документы: `python import.py`

7. Выполните поиск: `python search.py <вашзапрос>`

9. Добавьте промт в модель: `ollama create my_dnd_saiga -f my_prompt.modelfile`