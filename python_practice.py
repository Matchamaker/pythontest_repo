import requests 
params = {'userId': 2}
headers = {'Accept': 'application/json'}    
response = requests.get('https://jsonplaceholder.typicode.com/todos', params=params,headers=headers,timeout=5)

response.raise_for_status()
data = response.json()

C = 0
I = 0
for todo in data:
    if todo['completed']:
        C += 1
    else:
        I += 1
        print(f"ID: {todo['id']},Title: {todo['title']}")

Total = len(data)
print(f"Total todos: {Total}")
print(f"Total completed todos: {C}")
print(f"Total incomplete todos: {I}")


for todo in data:
    if todo['id'] == 35:
        print("ID :", todo['id'])
        print("Title :", todo['title'])
        print("Completed :", todo['completed'])


percentage = C/Total*100
print("percentage of completion",percentage)        