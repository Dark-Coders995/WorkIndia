
# Project Setup and Usage

## Prerequisites

- **Operating System**: Linux or WSL (Windows Subsystem for Linux)
- **Python**: Ensure Python is installed.

## Steps to Set Up the Project

### 1. Create and Activate a Virtual Environment

1. **Open a Terminal**: Ensure you are using a Linux or WSL terminal.

2. **Navigate to the Project Directory** (if not already there):

   ```bash
   cd /path/to/your/project
   ```

3. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment**:

   ```bash
   source venv/bin/activate
   ```

### 2. Install Dependencies

1. **Install Required Packages**:

   Ensure you have a `requirements.txt` file in your project directory. Install the dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

### 3. Configure Environment Variables

1. **Create a `.env` File**:

   Navigate to the project root directory and create a `.env` file with the following content:

   ```plaintext
   DB_USERNAME=USERNAME
   DB_PASSWORD=PASSWORD
   ```

   Replace `USERNAME` with your PostgreSQL username and `PASSWORD` with your PostgreSQL password.

### 4. Initialize the Database

1. **Navigate to the Database Directory**:

   ```bash
   cd database
   ```

2. **Run the Database Initialization Script**:

   ```bash
   python init_db.py
   ```

### 5. Start the Flask Application

1. **Open a New Terminal Window**:

   Ensure you are still within your virtual environment.

2. **Navigate to the Project Directory** (if not already there):

   ```bash
   cd /path/to/your/project
   ```

3. **Run the Flask Application**:

   ```bash
   python app.py
   ```

### 6. Verify the Application with Postman

1. **Open Postman**:

   - Go to Postman to test your API endpoints.
   - You can create a collection in Postman to manage and test all API endpoints provided in `app.py`.

### 7. Update HTML Pages

- HTML pages related to the project can be found and updated in the `Update` directory.

## Additional Information

- Ensure that your PostgreSQL server is running and accessible with the credentials provided in the `.env` file.
- For detailed API documentation, refer to the endpoints defined in `app.py`.

---

This `README.md` file should guide users through the setup and usage of your project effectively. Feel free to adjust any paths or instructions to better fit your project structure.
