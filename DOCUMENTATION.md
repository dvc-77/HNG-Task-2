# Installation and Setup

## Prerequisites

Before you proceed, make sure you have the following prerequisites installed on your development environment:

1. **PYTHON**: Run this command `python --version` to check you have Python installed on your machine. Otherwise, Download and install Python on your machine here: https://www.python.org/downloads/. 

2. **Database**: FastAPI supports multiple database systems, including PostgreSQL, MySQL, SQLite, Oracle, Microsoft SQL Server, etc. Ensure you have one of these databases installed and configured. PostgreSQL was used for this project. Download and install Postgres here: https://www.postgresql.org/download/

3. **Git**: Git is a version control system for managing the project's source code. Download and install git here: https://git-scm.com/downloads

The remaining prerequisites are libraries. These will be installed from the requirements.txt file in the project as we proceed.

## Cloning and Preparing the FastAPI Application

Follow these steps to clone and prepare the application:

### 1\. Clone the Repository

Clone the repository from Github using the following commands:

```bash
git clone https://github.com/adelajaOlamilekan/hng10_task2.git
 ```

### 2\. Navigate to Your Project Directory

Change your current working directory to the cloned project folder:

```bash
cd hng10_task2
 ```

### 3\. Install Project Dependencies

Use pip to install the project's dependencies:

```bash
pip install -r requirements.txt
 ```

### 4\. Copy the Environment File

Make a copy of the provided `.env.example` file and name it `.env`:

```bash
cp .env.example .env
 ```

Edit the `.env` file to configure your database connection, application URL, and any other necessary configuration options.

### 5\. Migrate the Database

Run the database migrations to create the necessary database tables:

```bash
alembic init alembic
 ```
```
alembic revision --autogenerate -m "Initial Migration"
```

### 8\. Start the Development Server

To start a development server, use the following command:

```bash
uvicorn main:app --reload
 ```

This will start a development server at `http://localhost:8000`. Access your application by visiting this URL in your web browser.

_Voila!_
