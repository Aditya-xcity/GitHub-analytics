# GitHub Language Analyzer with Secure Token Handling

"""
Name - ADITYA BHARDWAJ
Section - D2
Roll No - 07
Course – B TECH
Branch – CSE
"""

import requests
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

if not USERNAME or not TOKEN:
    print("Missing GITHUB_USERNAME or GITHUB_TOKEN in .env file.")
    exit()

HEADERS = {"Authorization": f"token {TOKEN}"}


def get_repositories():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Failed to fetch repositories:", response.status_code)
        return []

    return response.json()


def get_languages(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/languages"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return {}

    return response.json()


def analyze_profile():
    repos = get_repositories()
    total_languages = {}

    for repo in repos:
        if repo["fork"]:
            continue

        repo_name = repo["name"]
        languages = get_languages(repo_name)

        for lang, bytes_count in languages.items():
            total_languages[lang] = total_languages.get(lang, 0) + bytes_count

    return total_languages


def plot_pie_chart(language_data):
    if not language_data:
        print("No language data available.")
        return

    labels = list(language_data.keys())
    sizes = list(language_data.values())

    plt.figure()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title(f"{USERNAME} - Language Usage Distribution")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    language_data = analyze_profile()
    plot_pie_chart(language_data)