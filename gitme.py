import subprocess
import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    print("API key loaded successfully!")
else:
    print("Error: API key not found")
    
# set API key
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_git_diff():
    # get the latest Git diff
    result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    return result.stdout.strip()

def generate_commit_messages(diff):
    # use OpenAI to create commit messages based on the diff
    if not diff:
        return ["No staged changes detected."]
    
    prompt = f"""
    Generate 5 different concise Git commit messages based on the following code changes:
    
    {diff}

    Each commit message should be in imperative tense (e.g., "Initial commit", "Fix login bug", "Add new feature to dashboard", "Refactor user authentication").
    Separate each commit message with a newline.
    """
    
    try: 
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI that generates Git commit messages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=100,
            timeout=10
        )
        
        # split response into multiple commit message choices
        commit_messages = response.choices[0].message.content.strip().split("\n")
        return commit_messages[:5] # limit to 5 messages
    except Exception as e:
        return [f"Error generating commit messages: {e}"]
    
def main():
    diff = get_git_diff()
    if not diff:
        print("No staged changes found")
        return
    
    commit_messages = generate_commit_messages(diff)
    
    print("\nSuggested commit messages:")
    for i, msg in enumerate(commit_messages, 1):
        print(f"{i}. {msg}")
    
    # get user selection
    while True:
        choice = input("\nSelect a commit message (1-5) or enter 'n' to cancel: ")
        if choice.lower() == "n":
            print("Commit canceled")
            return
        elif choice.isdigit() and 1 <= int(choice) <= 5:
            commit_message = commit_messages[int(choice) - 1]
            break
        else:
            print("Invalid input. Please enter a number 1-5 or 'n' to cancel.")
    
    # commit using selected message
    subprocess.run(["git", "commit", "-m", commit_message])
    print(f"\n✅ Commit successful: {commit_message}")

if __name__ == "__main__":
    main()