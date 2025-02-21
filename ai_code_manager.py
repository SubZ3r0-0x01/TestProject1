import os
import requests
import json
import re
import subprocess

# LM Studio API URL
LM_STUDIO_API = "http://localhost:1234/v1/chat/completions"

# GitHub repo folder path
REPO_PATH = r"C:\Users\parth\Downloads\AIGIT\GitRepos\TestProject1"

# Define the AI prompt
PROMPT = "Generate a Java login application using Swing with a simple authentication system. Only return the Java code inside triple backticks."

def get_ai_generated_code():
    """Sends a request to LM Studio and retrieves only the Java code."""
    payload = {
        "model": "qwen2-7b-chat",  # Update if needed
        "messages": [{"role": "user", "content": PROMPT}],
        "temperature": 0.7
    }
    
    response = requests.post(LM_STUDIO_API, json=payload)
    response_data = response.json()

    if "choices" in response_data:
        full_response = response_data["choices"][0]["message"]["content"]
        
        # Extract code using regex (text inside triple backticks)
        code_match = re.search(r"```java\n(.*?)```", full_response, re.DOTALL)
        
        if code_match:
            return code_match.group(1)  # Extracted Java code
        else:
            print("❌ Error: No Java code found in response.")
            return None
    else:
        print("❌ Error: Failed to retrieve AI response.")
        return None

def save_code_to_file(code, filename="LoginApp.java"):
    """Saves AI-generated Java code to the GitHub repo."""
    file_path = os.path.join(REPO_PATH, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code)
    print(f"✅ Code saved to {file_path}")

def push_changes_to_git():
    """Commits and pushes changes to GitHub automatically."""
    os.chdir(REPO_PATH)
    
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "🤖 Auto-update: AI-generated code"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    
    print("🚀 Code pushed to GitHub successfully!")

def main():
    """Main automation function."""
    print("🤖 Fetching AI-generated code from LM Studio...")
    ai_code = get_ai_generated_code()
    
    if ai_code:
        save_code_to_file(ai_code)
        push_changes_to_git()
    else:
        print("❌ Skipping Git push due to an error.")

if __name__ == "__main__":
    main()
