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

def fetch_all_submissions():
    submissions = []
    offset = 0
    limit = 20  # Number of submissions per page
    while True:
        url = f'https://leetcode.com/api/submissions/?offset={offset}&limit={limit}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch submissions at offset {offset}: {response.status_code}")
            break

        data = response.json()
        current_subs = data.get('submissions_dump', [])
        if not current_subs:
            break

        submissions.extend(current_subs)
        # If the API indicates there are no further submissions, break out
        if not data.get("has_next", False):
            break

        offset += limit

    return submissions

submissions = fetch_all_submissions()

for submission in submissions:
    title = submission.get('title', 'untitled')
    code = submission.get('code', '')
    submission_id = submission.get('id', '')
    # Append the submission ID to the filename to avoid overwriting files with the same title
    filename = f"{title.replace(' ', '_')}_{submission_id}.py" if submission_id else f"{title.replace(' ', '_')}.py"
    with open(filename, 'w') as f:
        f.write(code)
