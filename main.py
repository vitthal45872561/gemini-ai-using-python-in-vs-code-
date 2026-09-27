import os
import time
from google import genai

# ==========================================
# GEMINI API KEY
# ==========================================

API_KEY = os.getenv("")

if not API_KEY:
    API_KEY = input("Enter your Gemini API key: ").strip()

if not API_KEY:
    print("❌ API key is required.")
    exit()

# ==========================================
# GEMINI CLIENT
# ==========================================

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.8-flash"


# ==========================================
# GEMINI REQUEST WITH RETRY
# ==========================================

def ask_gemini(question):

    max_retries = 5

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=question
            )

            return response.text

        except Exception as e:

            error = str(e)

            # 503 = temporary server overload
            if "503" in error or "UNAVAILABLE" in error:

                if attempt < max_retries - 1:

                    wait_time = 2 ** attempt

                    print(
                        f"\n⚠️ Gemini server is busy."
                        f"\nRetrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:

                    return (
                        "❌ Gemini server is currently busy. "
                        "Please try again after some time."
                    )

            else:

                return f"❌ Error: {error}"


# ==========================================
# CHAT LOOP
# ==========================================

print("\n====================================")
print("       GEMINI AI CHATBOT")
print("====================================")
print("Type 'exit' to close the program.\n")


while True:

    try:

        question = input("You: ").strip()

        if question.lower() == "exit":

            print("\nGoodbye! 👋")
            break

        if not question:

            continue

        print("\nGemini: ", end="", flush=True)

        answer = ask_gemini(question)

        print(answer)
        print()

    except KeyboardInterrupt:

        print("\n\nGoodbye! 👋")
        break

    except Exception as e:

        print(f"\n❌ Error: {e}")