import os
import requests

LEETCODE_SESSION = os.environ['LEETCODE_SESSION']
CSRFTOKEN = os.environ['CSRFTOKEN']

headers = {
    'Cookie': f'LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN}',
    'x-csrftoken': CSRFTOKEN,
    'Referer': 'https://leetcode.com',
    'Content-Type': 'application/json'
}

response = requests.get('https://leetcode.com/api/submissions/', headers=headers)

if response.status_code == 200:
    submissions = response.json().get('submissions_dump', [])
    for submission in submissions:
        title = submission['title']
        code = submission['code']
        filename = f"{title.replace(' ', '_')}.py"
        with open(filename, 'w') as f:
            f.write(code)
else:
    print(f"Failed to fetch submissions: {response.status_code}")
