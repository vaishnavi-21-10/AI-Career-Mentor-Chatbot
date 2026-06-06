import requests
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("INCEPTION_API_KEY")

if not API_KEY:
    print("Error: API key not found!")
    exit()

print("=" * 50)
print("🎓 AI CAREER MENTOR FOR MCA STUDENTS")
print("=" * 50)

# Question written directly in code
question = "How can an MCA student become an AI Engineer?"

messages = [
   {
    "role": "system",
    "content": """
You are AI Career Mentor for MCA students.

Rules:
- Use very simple English.
- Give short answers.
- Maximum 8 points.
- Each point should be on a new line.
- No long paragraphs.
- No tables.
- No essays.
- Keep answers under 100 words.

Format:

🎯 Goal:
<1 line>

📚 Skills:
• Skill 1
• Skill 2
• Skill 3

💻 Projects:
• Project 1
• Project 2

🚀 Next Step:
<1 line>
"""
},
    {
        "role": "user",
        "content": question
    }
]

try:
    response = requests.post(
        "https://api.inceptionlabs.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mercury-2",
            "messages": messages
        }
    )

    if response.status_code == 200:
        data = response.json()

        print("\nQuestion:")
        print(question)

        print("\n🤖 AI CAREER MENTOR RESPONSE\n")
        print(data["choices"][0]["message"]["content"])

    else:
        print(f"API Error {response.status_code}")
        print(response.text)

except Exception as e:
    print("Error:", e)