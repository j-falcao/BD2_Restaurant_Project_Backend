# BD2_Restaurant_Project

# Sempre que comecar a trabalhar 

# Para instalar novos pacotes
    pip install <<package_name>>
    pip freeze > requirements.txt

# Para rodar o programa
    pip install -r requirements.txt

# Criar base de dados com nome "main" no postgres
# Configurar o users, passwords e conexão à base de dados (copiar exemplo de .env.example)
# Rodar os seguintes comandos

    ./venv/Scripts/activate
    cd ./project
    python manage.py database --reset
    python manage.py runserver


    https://github.com/j-falcao/BD2_Restaurant_Project_Backend
    https://github.com/j-falcao/BD2_Restaurant_Project_Frontend