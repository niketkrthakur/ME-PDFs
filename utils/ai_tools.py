from groq import Groq
import os

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)

def generate_summary(text, mode="standard", tone="formal"):

    if mode == "short":
        instruction = "Provide a short structured summary."
    elif mode == "bullet":
        instruction = "Provide structured bullet point summary."
    elif mode == "detailed":
        instruction = "Provide a detailed structured professional summary."
    else:
        instruction = "Provide a clean structured summary."

    tone_instruction = {
        "formal": "Use professional formal tone.",
        "student": "Use simple language suitable for students.",
        "executive": "Use executive-level concise business tone."
    }.get(tone, "Use professional formal tone.")    

    prompt = f"""
You are a professional document summarizer.

{instruction}
{tone_instruction}

IMPORTANT RULES:
- Return ONLY clean HTML.
- Do NOT use markdown symbols like **, ###, --- or pipes.
- Use proper HTML tags: <h2>, <h3>, <p>, <ul>, <li>, <strong>.
- Format nicely with sections.
- Make it clean and readable.
- No backticks.
- No code blocks.

Document:
{text[:8000]}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content

def rewrite_text(text, action="rewrite"):

    action_prompts = {
        "rewrite": "Rewrite the following text clearly and professionally.",
        "improve": "Improve the writing quality and clarity.",
        "simplify": "Simplify the language for easy understanding.",
        "professional": "Make the tone more professional and executive.",
        "shorten": "Shorten the text while keeping key information.",
        "expand": "Expand the text with more details and explanation."
    }

    instruction = action_prompts.get(action, action_prompts["rewrite"])

    prompt = f"""
You are a professional writing assistant.

{instruction}

IMPORTANT:
- Return clean HTML only.
- Use <p>, <h2>, <ul>, <li> if needed.
- No markdown symbols.
- No backticks.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return response.choices[0].message.content

def translate_text(text, target_language="Hindi"):

    prompt = f"""
You are a professional translator.

Translate the following text into {target_language}.

IMPORTANT:
- Preserve meaning accurately.
- Keep formatting structure.
- Return clean HTML only.
- Use <p>, <h2>, <ul>, <li> if needed.
- Do NOT use markdown symbols.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content

def detect_language(text):

    prompt = f"""
Detect the language of the following text.

Respond ONLY with the language name in English.
Example: English, Hindi, Spanish, French, German, Japanese, Chinese.

Text:
{text[:2000]}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content.strip()

import json
import re

def chat_with_pdf(pdf_text, question):

    prompt = f"""
You are an AI assistant answering questions strictly based on the provided PDF content.

Return ONLY valid JSON (no markdown, no explanation):

{{
  "section": "Section Name",
  "snippet": "Exact paragraph from document",
  "answer": "Clear structured answer in HTML"
}}

PDF Content:
{pdf_text[:12000]}

User Question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()

    # Remove markdown JSON fences if present
    content = re.sub(r"```json", "", content)
    content = re.sub(r"```", "", content)

    try:
        parsed = json.loads(content)
        return parsed
    except Exception as e:
        print("JSON parsing failed:", e)
        return {
            "section": "Unknown",
            "snippet": "",
            "answer": content
        }
    
def generate_document(prompt, doc_type="document"):

    instruction = {
        "resume": "Create a professional resume with sections like Summary, Skills, Experience, Education.",
        "report": "Create a structured professional report with headings and sections.",
        "letter": "Create a professional formal letter.",
        "notes": "Create well structured study notes.",
        "document": "Create a well structured professional document."
    }.get(doc_type, "Create a professional document.")

    full_prompt = f"""
You are a professional document writer.

{instruction}

User request:
{prompt}

IMPORTANT RULES:
- Return ONLY clean HTML.
- Use tags like <h1>, <h2>, <p>, <ul>, <li>.
- Do NOT use markdown.
- Make the document structured and readable.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": full_prompt}],
        temperature=0.6,
    )

    return response.choices[0].message.content    

def generate_presentation(prompt):

    prompt_text = f"""
You are a professional presentation creator.

Create a structured presentation.

Rules:
- Return ONLY JSON
- Format:

[
  {{
    "title": "Slide Title",
    "points": ["Point 1", "Point 2", "Point 3"]
  }}
]

Topic:
{prompt}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt_text}],
        temperature=0.5,
    )

    import json
    import re

    content = response.choices[0].message.content

    content = re.sub(r"```json", "", content)
    content = re.sub(r"```", "", content)

    return json.loads(content)    

import requests
from bs4 import BeautifulSoup

def extract_website_text(url):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator="\n")

    lines = [line.strip() for line in text.splitlines() if line.strip()]

    return "\n".join(lines[:8000])

def summarize_website(content):

    prompt = f"""
You are an expert analyst.

Summarize this website content into a structured report.

Rules:
- Return clean HTML
- Use <h1>, <h2>, <p>, <ul>, <li>
- Organize into sections:
    Overview
    Key Points
    Important Details
    Conclusion

Content:
{content}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return response.choices[0].message.content

def pdf_to_excel_ai(text):
    from groq import Groq
    import os

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
Extract structured data from this text and convert into JSON array.

Instructions:
- Detect columns intelligently
- Normalize keys (e.g., Name, Age, Date)
- Ignore garbage text
- Return ONLY JSON array

Example:
[
  {{"Name": "John", "Age": 25}},
  {{"Name": "Alice", "Age": 30}}
]

Text:
{text[:12000]}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",  # 🔥 best for structured output
        messages=[
            {"role": "system", "content": "You are a data extraction AI. Output only JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content    

def pdf_to_ppt_ai(text):
    from openai import OpenAI
    import os, json

    client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    prompt = f"""
    Convert this text into professional presentation slides.

    Return ONLY JSON in this format:
    [
      {{
        "title": "Slide Title",
        "points": ["bullet 1", "bullet 2"],
        "notes": "Speaker notes for presenter"
      }}
    ]

    Rules:
    - 6–10 slides
    - Short bullet points
    - Clean titles
    - Add useful speaker notes

    Text:
    {text[:6000]}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)