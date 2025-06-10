import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_profile(text):
    prompt = f"""
    Analyze the following text and extract all possible personal and contextual information about the speaker. Include details such as:
    - Full Name, Age (if possible), Gender
    - Profession, Job Role, Skills, Industry
    - Education, Background, Nationality
    - Current Location, Places Mentioned
    - Personal Interests, Hobbies, Activities
    - Language(s) Spoken
    - People Mentioned (Relationships: friends, family, coworkers)
    - Organizations, Schools, Workplaces
    - Style of speaking (tone, formal/informal, humorous, serious)
    - Emotional state or personality hints
    - Common phrases, idioms, or expressions
    - Cultural context or setting
    - Any other relevant biographical or contextual insight

    Text: """
    {text}
    """
    Return the result in a well-structured JSON format.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        return json.loads(response.choices[0].message['content'])
    except:
        return {}