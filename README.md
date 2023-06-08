Онлайн платформа торговой сети электроники

Для запуска необходимо через терминал:
1. Создать и перейти диреторию "commercial_network";
2. Загрузить проект в диреторию "commercial_network". Можно используя командой: git clone <ссылка на удаленный репозиторий>
3. Установить зависимости проекта: pip install -r requirements.txt
4. Выполнить миграции: python3 manage.py migrate
5. Запустить сервер: python3 manage.py runserver

Для запонения базы данных можно использовать команды в слеующем порядке:
1. Заполнить пользователей: python3 manage.py add_users
2. Заполнить продукты: python3 manage.py add_products
3. Заполнить компании: python3 manage.py add_companies
