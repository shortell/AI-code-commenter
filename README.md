# AI-code-commenter

Full Stack Web App

Flask Backend

React Front End

## Setup

1. install python 

2. Clone this repository

3. Navigate into the project directory

   $ cd AI-code-commenter

4. Create a new virtual environment

   $ python -m venv openai-env

   depending on the name of the folder in your venv directory run one of the following commands

   $ . openai-env/bin/activate

   OR

   $ . openai-env/Scripts/activate

5. Install the requirements

   $ pip install -r requirements.txt

6. Make a copy of the example environment variables file

   $ cp .env.example .env

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   $ flask run

   open http://localhost:5000