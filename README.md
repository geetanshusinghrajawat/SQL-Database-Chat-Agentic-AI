# 💬 Chat with SQL Database using LangChain & Groq

An AI-powered SQL chatbot built with **LangChain**, **Groq LLM**, **Streamlit**, and **SQLAlchemy**. This application allows users to interact with SQL databases using natural language, eliminating the need to write SQL queries manually.

The chatbot supports both **SQLite** and **MySQL** databases and uses a LangChain SQL Agent to translate user questions into SQL queries, execute them, and return human-readable answers.

---

## 🚀 Features

- 🤖 Natural language to SQL using LangChain SQL Agent
- ⚡ Powered by Groq's Llama 3.3 70B Versatile model
- 🗄️ Supports both SQLite and MySQL databases
- 💬 Interactive chat interface with message history
- 🔍 Automatic SQL query generation and execution
- 📊 Displays responses in a user-friendly format
- 🔄 Option to clear chat history

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain SQL Agent
- Groq API
- SQLAlchemy
- SQLite
- MySQL
- MySQL Connector
- dotenv

---

## 📂 Project Workflow

1. Select the database type (SQLite or MySQL).
2. Enter your Groq API key.
3. Connect to the selected database.
4. Ask questions in plain English.
5. The LangChain SQL Agent:
   - Understands the user's question.
   - Generates the required SQL query.
   - Executes the query on the database.
   - Sends the results to the Groq LLM.
6. The LLM converts the SQL output into a natural language response.

---

## 🗃️ Supported Databases

### SQLite
- Uses the included `student.db` database.
- Read-only connection for safe querying.
- Works out of the box without additional setup.

### MySQL
Users can provide:
- Host
- Username
- Password
- Database Name

The application establishes a connection dynamically using SQLAlchemy before creating the SQL Agent.

---

## 📸 Demo

### Example Questions

- Show all students.
- How many students are enrolled?
- List students older than 20.
- Which student scored the highest marks?
- What is the average age of students?

---

## ▶️ Running Locally

Clone the repository

```bash
git clone https://github.com/yourusername/chat-with-sql.git
cd chat-with-sql
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Or simply enter the API key through the Streamlit sidebar while running the application.

---

## ⚠️ Streamlit Cloud Deployment

The application works **fully in local/offline mode**, including SQLite and MySQL support.

The **SQLite version** can be deployed without issues.

However, the **MySQL version is intended for local use** because it requires access to a running MySQL server. Streamlit Community Cloud cannot directly access a MySQL server running on your local machine (`localhost`). To use MySQL in the cloud, the database must be hosted on a publicly accessible server or cloud database service.

For this reason, the complete MySQL functionality is demonstrated and tested in the local environment.

---

## 📁 Project Structure

```
.
├── app.py
├── student.db
├── requirements.txt
├── .env
└── README.md
```

---

## 📌 Future Improvements

- Support PostgreSQL
- Multi-database connections
- Conversation memory
- Query history
- SQL query visualization
- User authentication
- Export query results as CSV/Excel

---

## 🙌 Acknowledgements

- LangChain
- Groq
- Streamlit
- SQLAlchemy

---

## ⭐ If you found this project helpful, consider giving it a star!
