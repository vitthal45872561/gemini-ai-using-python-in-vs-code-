# 🤖 Gemini AI Chatbot

A simple and powerful **Python-based AI chatbot** powered by the **Google Gemini API**.
This project lets you interact with Gemini directly from your terminal using a clean and lightweight Python application.

---

## ✨ Features

* 🤖 Google Gemini AI integration
* 💬 Interactive terminal-based chat
* 🔑 Secure API key input
* 🔄 Automatic retry when Gemini temporarily becomes unavailable
* ⚡ Lightweight and fast
* 🛑 Type `exit` to close the chatbot
* 🐍 Built completely with Python

---

## 🛠️ Technologies Used

* **Python 3**
* **Google Gemini API**
* **Google GenAI Python SDK**

---

## 📁 Project Structure

```text
Gemini-AI-Chatbot/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Go inside the project folder:

```bash
cd Gemini-AI-Chatbot
```

---

### 2. Install Dependencies

Install the Google GenAI Python SDK:

```bash
pip install -U google-genai
```

Or install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key

You need a **Google Gemini API key** to run this project.

Get your API key from:

**Google AI Studio**

https://aistudio.google.com/

### Option 1 — Enter API key when running

Run:

```bash
python main.py
```

The program will ask:

```text
Enter your Gemini API key:
```

Paste your API key and press Enter.

---

### Option 2 — Environment Variable

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Then run:

```powershell
python main.py
```

---

## ▶️ Run the Project

```bash
python main.py
```

You should see:

```text
====================================
       GEMINI AI CHATBOT
====================================
Type 'exit' to close the program.

You:
```

Now type your question.

Example:

```text
You: What is Python?

Gemini: Python is a high-level, general-purpose programming language...
```

To stop the chatbot:

```text
You: exit
```

---

## 🔄 Error Handling

The chatbot includes automatic retry handling for temporary Gemini server errors such as:

```text
503 UNAVAILABLE
```

If the Gemini API is temporarily overloaded, the application waits and retries the request automatically.

Example:

```text
⚠️ Gemini server is busy.
Retrying in 1 seconds...
```

---

## 📦 requirements.txt

Create a file named:

```text
requirements.txt
```

and add:

```text
google-genai
```

Then install it using:

```bash
pip install -r requirements.txt
```

---

## 🔐 Security

**Never upload your Gemini API key to GitHub.**

Do NOT write your real API key directly inside:

```python
client = genai.Client(api_key="YOUR_REAL_API_KEY")
```

Instead, use an environment variable or enter the key when the program starts.

If you accidentally upload an API key to GitHub, **revoke/regenerate the key immediately**.

---

## 🎯 Future Improvements

Possible improvements for future versions:

* 🎙️ Voice input
* 🔊 AI voice responses
* 🧠 Conversation memory
* 🖥️ Graphical User Interface
* 🌐 Web interface
* 📂 File/document analysis
* 🖼️ Image understanding
* ⚡ Streaming responses
* 🤖 Personal AI assistant features

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add new feature"
```

5. Push the branch

```bash
git push origin feature/new-feature
```

6. Open a Pull Request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Vitthal Chandore**

Engineering Student | Developer | AI Enthusiast

---

⭐ If you find this project useful, consider giving the repository a **star**!

**Made with ❤️ and Python**
