# verklegt-namskeid-2

# Pre-requisites

### Install Python
Get the latest version of Python at https://www.python.org/downloads/ or with your operating system’s package manager

### Get your database running
- Make sure you have PostgreSQL installed and running on your machine. You can download it at https://www.postgresql.org/download/.
- For using PostgreSQL, you’ll need the [psycopg](https://www.psycopg.org/psycopg3/) or [psycopg2](https://www.psycopg.org/) package. Refer to the [PostgreSQL notes](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes) for further details.

### Install the Django code
This is the recommended way to install Django.

1. Install [pip](https://pip.pypa.io/). The easiest is to use the [standalone pip installer](https://pip.pypa.io/en/latest/installation/). If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.
2. Take a look at [venv](https://docs.python.org/3/tutorial/venv.html). This tool provides isolated Python environments, which are more practical than installing packages systemwide. It also allows installing packages without administrator privileges. The contributing tutorial walks through how to create a virtual environment.
3. After you’ve created and activated a [virtual environment](https://docs.djangoproject.com/en/5.0/intro/contributing/), enter the command:

**For Linux/Mac:**
```
$ python -m pip install Django
or
$ python3 -m pip install Django
```
**For Windows:**
```
...\> py -m pip install Django
```

## Clone the repository
Clone the repository to your local machine by running the following command in your terminal:
```
git clone https://github.com/milosptr/verklegt-namskeid-2.git
```

# Running the project
1. Navigate to the project directory
2. Run the following command to install the required packages:
```
pip install -r requirements.txt
```
3. Run the following command to start the server:
```
python manage.py runserver
----------- or -----------
python3 manage.py runserver
```
4. Open your browser and navigate to provided URL (usually http://127.0.0.1:8000/)
5. Enjoy the project!

## Running migrations
If you are making changes to the models, you will need to run the following command to apply the changes to the database:
```
python3 manage.py makemigrations src
python3 manage.py migrate src
```

# Seed the database (countries and cities)
This step is required (_ONLY IF DATABASE IS TRUNCATED FULLY_) to seed the database with countries and cities. Run the following commands:

**Note that we are seeding only Icelandic cities for simplicity**
```
python3 manage.py loaddata src/seed/0001_countries.json 
python3 manage.py loaddata src/seed/0001_cities_is.json 
```
# 🔴 DON'Ts 🔴
1. **DO NOT** push directly to the main branch. Create a new branch and make a pull request.
2. **DO NOT** manually change or add data to the database. Use Django's ORM to make changes to the database.
3. **DO NOT** manually edit or add files in the `src/seed` directory. Use Django's fixtures to seed the database.
4. **DO NOT** manually edit or add files in the `src/migrations` directory. Use Django's migrations to make changes to the database schema.

# 🟢 DOs 🟢
1. **DO** create a new branch for your feature or bug fix.
2. **DO** make a pull request to the main branch when you are ready to merge your changes.
3. **DO** use Django's ORM to make changes to the database.
4. **DO** use Tailwind CSS for styling.
