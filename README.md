
# 🤖 Gemini Telegram Bot

**Gemini Telegram Bot** is a conversational assistant powered by Google’s Gemini API and integrated with Telegram.  
Users can ask questions or interact with the bot directly in Telegram and receive intelligent, AI-generated responses — for free!

---

## 🚀 Features

- 💬 Chat with the Gemini model via Telegram  
- 🔐 Securely loads credentials from environment variables  
- 🧠 JSON-formatted responses parsed and delivered cleanly  
- 🎯 Easy to set up and run locally or you can deploy into [PythonAnyWhere](https://www.pythonanywhere.com/) for free.

---

## 🛠️ Tech Stack

- Python 3.7+
- Telegram Bot Tokenvia `FatherBot`
- [Gemini API (Google Generative Language)](https://ai.google.dev/)
- `.env` for secure API key management

---

## 📦 Setup Instructions

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/your-username/gemini-telegram-bot.git
cd gemini-telegram-bot
```

---

### 2. 🧪 Install Dependencies

```bash
pip install -r requirements.txt
```


---

### 3. 🔐 Create a `.env` File

Create a `.env` file in the project root directory and add the following:

```env
token=YOUR_TELEGRAM_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=gemini-pro
```

> 📝 You can get your Telegram bot token from [BotFather](https://t.me/BotFather), and your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

---

### 4. ▶️ Run the Bot

```bash
python bot.py
```

Expected output:

```
Bot has started
```

Open Telegram and start chatting with your bot!

---

## 💬 Example Interaction

**User:** What is the capital of France?  
**Bot:** Paris

---

## 🧩 Project Structure

```
gemini-telegram-bot/
│
├── bot.py             # Main script
├── .env               # Environment variables (not committed)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ⚠️ Notes

- Do **not** share your `.env` file or API keys publicly.
- This bot is for educational/demo purposes. Monitor your Gemini API usage limits.

---

## 📃 License

This project is open-source and available under the [MIT License](./LICENSE.md).

