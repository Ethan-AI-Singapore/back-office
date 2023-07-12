# Back-Office Application Documentation

## Table of Contents
- [Folder Structure](#folder-structure)
- [Environment Variables](#environment-variables)
- [Installation](#installation)
  
## Folder Structure
- **database**: This folder contains the code to connect to databases.
- **pages**: This folder holds the code to render the user interface (UI).
- **repository**: The repository folder holds classes that fetch data from specific tables.
- **services**: The services folder contains code for analyzing the tables.
- **utils**: The utils folder holds helper objects and functions.

## Environment Variables

The following environment variables are used in this application:

- `DB_HOST` : Database host.
- `DB_PORT` : Database port.
- `DB_DATABASE` : Database name.
- `DB_USER` : Database username.
- `DB_PASSWORD` : Database password.

Make sure to set these variables in the `.env` file before running the application.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Install the dependencies
```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory of the project and set the required environment variables (as mentioned in the Environment Variables section).

5. Run the application:
```bash
streamlit run Home_Page.py
```

6. Open your web browser and visit http://localhost:8501 to access the application.



