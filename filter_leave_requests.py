import csv
import json

input_file = 'emails.csv'
output_file = 'leave_request.json'

leave_requests = []

with open(input_file, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        subject = row['subject'].lower()
        body = row['body'].lower()
        if 'leave' in subject or 'leave' in body:
            leave_requests.append({
                'id': int(row['id']),
                'sender': row['sender'],
                'type': 'leave_request'
            })
with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(leave_requests, jsonfile, ensure_ascii=False, indent=2)

print(f"Đã xuất {len(leave_requests)} leave requests ra {output_file}")
