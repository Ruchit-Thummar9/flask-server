# Flask Hello World Server

## Overview

This project is a basic Python Flask server that returns a **Hello World** response.
The purpose of this project is to demonstrate a simple build and run process that can be easily checked out from Git and executed with a small set of commands.

---

## Project Structure

```
flask-server/
│
├── server.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requirements

* Python 3.x
* pip (Python package manager)

---

## Setup and Build Process

### 1. Clone the Repository

```
git clone <repository-url>
```

### 2. Navigate to the Project Directory

```
cd flask-server
```

### 3. Create a Virtual Environment

```
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```
venv\Scripts\activate
```

Linux / Mac:

```
source venv/bin/activate
```

### 5. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Server

Start the Flask server:

```
python server.py
```

The server will start on:

```
http://127.0.0.1:5000
```

Open this URL in your browser to see the **Hello World** response.

---

## Purpose

This server acts as a simple starting point that can later be expanded to include additional components and functionality.
