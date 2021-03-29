# Flask-Auth

## Setting up

### Clone the repo

Clone the repo and open folder in terminal.

```bash
git clone https://github.com/diyor-bek/Flask-Auth.git
cd Flask-Auth
```

### Install dependencies

- Python 3.x
- (Optional) Database system, like `postgresql`

### PIP dependencies

In the cloned `Flask-Auth` directory, run the following code to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

## Run the server

Setting up `DATABASE_URL` environment variable for your database path.

```bash
export DATABASE_URL=<YOUR_DATABASE_PATH>
```

Run the development server

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
