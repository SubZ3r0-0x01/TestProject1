import requests
import git
import os

# LM Studio API endpoint (running locally on port 1234)
LM_STUDIO_URL = "http://localhost:1234/v1/completions"

# GitHub repository path (Change this to your local repo path)
REPO_PATH = r"C:\Users\parth\Downloads\AIGIT\GitRepos\TestProject1"

# Function to interact with LM Studio
def ask_ai(prompt):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "qwen-2.0-7b",  # Change this if using a different model
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 200
    }
    response = requests.post(LM_STUDIO_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return f"Error: {response.text}"

# Function to commit and push changes
def commit_and_push():
    repo = git.Repo(REPO_PATH)
    
    # Add all changes
    repo.git.add("--all")
    
    # Generate a commit message using AI
    commit_message = ask_ai("Generate a concise and meaningful Git commit message for the latest changes.")
    
    # Commit changes
    repo.index.commit(commit_message)
    print(f"✅ Committed with message: {commit_message}")
    
    # Push changes
    origin = repo.remote(name="origin")
    origin.push()
    print("🚀 Changes pushed to GitHub successfully!")

# Run the script
if __name__ == "__main__":
    commit_and_push()
