import requests

repo = input("enter the repository name (e.g., torvalds/linux): ")
try:
    response = requests.get(f'https://api.github.com/repos/{repo}',timeout=5)
    response.raise_for_status()
except requests.exceptions.ConnectionError:
     print("Connection error occurred. Please check your internet connection.")
     exit(1)
except requests.exceptions.Timeout:
    exit(1)
    print("Request timed out. Please try again later.")
except requests.exceptions.HTTPError as e:           
    print(f"Error fetching repository information: {e}")
    exit(1)

data = response.json()

N = data['name']
S = data['stargazers_count']
O = data['open_issues_count']
F = data['forks_count']
D = data['description']
FN = data['full_name']

print(f"Repository Name: {N}")
print(f"Full Name: {FN}")
print(f"Description: {D}")
print(f"Stars: {S}")
print(f"Open Issues: {O}")
print(f"Forks: {F}")   