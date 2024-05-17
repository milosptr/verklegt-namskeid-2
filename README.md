# verklegt-namskeid-2

# Pre-requisites

### Install Python
Get the latest version of Python at https://www.python.org/downloads/ or with your operating system’s package manager

### Get your database running
- Make sure you have PostgreSQL installed and running on your machine. You can download it at https://www.postgresql.org/download/.
- For using PostgreSQL, you’ll need the [psycopg](https://www.psycopg.org/psycopg3/) or [psycopg2](https://www.psycopg.org/) package. Refer to the [PostgreSQL notes](https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes) for further details.


## Clone the repository
Clone the repository to your local machine by running the following command in your terminal:
```
git clone https://github.com/milosptr/verklegt-namskeid-2.git
```

### Install the virtual environment
Navigate to the project folder and run the following command to install the virtual environment:
```
python3 -m venv venv
```
Once you have installed virtualenv, you can create a virtual environment by running:

**On Mac**:
```
source venv/bin/activate
```

# Running the project
1. Navigate to the project directory
2. Run the following command to install the required packages:
```
pip install -r requirements.txt
```
3. Run the following command to start the server:
```
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

## Updating static files
If you are making changes to the static files in `static/jarvis` (CSS, JS, etc.), you will need to run the following command to update the static files:
```
python3 manage.py collectstatic
```

# Seed the database
This step is required (_ONLY IF DATABASE IS TRUNCATED FULLY_) to seed the database. Run the following commands:

**Note that we are seeding only Icelandic cities for simplicity**

```
python3 manage.py loaddata src/seed/0001_types.json
python3 manage.py loaddata src/seed/0001_skills.json
python3 manage.py loaddata src/seed/0001_countries.json 
python3 manage.py loaddata src/seed/0001_cities_is.json 
python3 manage.py loaddata src/seed/0001_companies_is.json
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

# Extra requirements
1. Like job offer
2. Job application guide
3. Report a bug
4. About the authors section
5. Share a job offer by copying a link
6. Invite applicants to interview
7. Delete job offer
8. Mark applications that have been reviewed as reviewed
9. Contact Jarvis
10. View list of applied jobs
11. Add details about a company
12. Create job offer
13. Login using email and password
14. Change password
15. Create a profile
16. Edit job offer
17. View list of interview invites


