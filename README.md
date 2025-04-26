# 📝 Task Manager API - FastAPI Project

A simple and clean **Task Manager API** built using **FastAPI** 🚀  
It allows you to create, view, update, and delete tasks securely using an API key authentication system.

---

## 📚 Features

- ✅ Create a Task
- ✅ View All Tasks
- ✅ View Task by ID
- ✅ Update a Task
- ✅ Delete a Task
- ✅ API Key Authentication (header-based security)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MiabhishekPatidar/TaskManagerAPI.git
cd TaskManagerAPI
```

### 2. Setup Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

Server will start at:  
👉 `http://127.0.0.1:8000`

---

## 🔐 API Key Authentication

All API requests must include an API Key in the headers.

Example Header:

```text
x-api-key: your-secret-api-key
```

> ⚡ **Note:** The API key is hardcoded in the backend for now. Update it in the code if needed.

---

## 🛠 API Endpoints

| Method | Endpoint          | Description         |
|:------:|:------------------|:--------------------|
| POST   | `/tasks/`          | Create a new task    |
| GET    | `/tasks/`          | Get all tasks        |
| GET    | `/tasks/{task_id}` | Get task by ID       |
| PUT    | `/tasks/{task_id}` | Update task by ID    |
| DELETE | `/tasks/{task_id}` | Delete task by ID    |

✅ **All endpoints require the `x-api-key` header.**

---

## 🛠 Technologies Used

- FastAPI
- Uvicorn
- Python 3.12+

---

## 🌟 Author

- GitHub: [MiabhishekPatidar](https://github.com/MiabhishekPatidar)

---

## 📜 License

This project is open source and free to use!

---
