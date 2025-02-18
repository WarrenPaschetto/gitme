# 📄 GitMe - AI-Powered Commit Message Generator
🚀 **GitMe** is a CLI tool that **automatically generates commit messages** based on your staged Git changes using OpenAI’s GPT API.


## 📌 Features
✅ Analyzes Git diffs to understand code changes

✅ Uses AI to generate 5 commit message options

✅ Interactive CLI for easy selection

✅ Follows Git best practices (imperative tense)

✅ Prevents committing secrets with .gitignore



## 🛠 Installation
1. **Clone the Repository**
```
git clone https://github.com/WarrenPaschetto/gitme.git
cd gitme
```
2. **Install Dependencies**
```
pip install openai python-dotenv
```
3. **Create a .env file**
```
touch .env
```
Then open it in a text editor and add your OpenAI API key (or any other env variables):
```
OPENAI_API_KEY="your-openai-api-key"
```
🚨 Warning: Never commit your .env file! It's already ignored in .gitignore.

## 🚀 Usage
1. **Stage Your Changes**
Before generating a commit message, **stage your changes**:
```
git add .
```
2. **Run GitMe**
```
python gitme.py
```
or (if using Python 3):
```
python3 gitme.py
```
3. **Select a Commit Message**
GitMe will generate **5 AI-powered commit messages** to choose from:
```
Suggested commit messages:
1. Fix login authentication issue
2. Refactor database connection handling
3. Update API request error handling
4. Improve user profile update logic
5. Remove unnecessary console logs

Select a commit message (1-5) or enter 'n' to cancel:
```
- **Enter a number (1-5)** to choose a commit message
or
- **Enter 'n'** to cancel the commit and manually enter your own commit and message

4. **Push Your Changes**
```
git push origin main
```

## 📌 Troubleshooting
### ❌ OpenAI API Errors
If you see:
```
Error generating commit messages: OpenAI API key not found
```
➡️ **Solution:** Ensure your .env file contains the correct API key.
### ❌ Git Push Rejected (Secret Detected)
If GitHub blocks your push:
```
Push cannot contain secrets
```
➡️ Solution:

1. Remove .env from Git:
```
git rm --cached .env
```
2. Rewrite commit history:
```
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
```
3. Force oush the cleaned repository:
```
git push origin main --force
```
### ❌ OpenAI API Slow or Freezing
If gitme.py takes too long: ➡️ Solution: Reduce model load by using gpt-3.5-turbo instead of gpt-4 in gitme.py.

## 📜 License
📄 This project is licensed under the MIT License.
