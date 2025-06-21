import os
import telebot
from dotenv import load_dotenv
import requests
import json


load_dotenv()

API_KEY = os.getenv("token")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")
bot = telebot.TeleBot(API_KEY)

def gemini_response(text):
    try:
        prompt = f"""
        You are a helpful assistant. Answer the following question in JSON format. 
        Here is the user query: {text}.
        """

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
        headers = {
            "Content-Type": "application/json",
        }
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()

        generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
        generated_text = generated_text.replace("```json", "").replace("```", "").strip()
    
        return generated_text
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Set bot description before polling
bot.set_my_description("🤖 I am Gemini Bot. You can use Gemini from Telegram for free! 😍😍")

@bot.message_handler()
def reply(message):
    user_message = message.text
    response = gemini_response(user_message)
    if isinstance(response, str):
        try:
            response = json.loads(response)
        except json.JSONDecodeError:
            response = {"response": "Sorry, the AI response couldn't be parsed."}

    response_text = response.get("response", "Sorry, I couldn't generate a response.")
    bot.send_message(message.chat.id, response_text)

print("Bot has started")
bot.polling()
