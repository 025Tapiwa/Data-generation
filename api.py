from flask import Flask, jsonify
import random
from datetime import datetime, timedelta
from faker import Faker

app = Flask(__name__)
fake = Faker()

streaming_data = []

num_rows = 10000  # Number of rows of dummy data

# Generate dummy data
for _ in range(num_rows):
    entry = {
        "Timestamp": fake.date_time_this_decade(),
        "IP Address": fake.ipv4(),
        "Request Type": random.choice(["GET", "POST", "PUT", "DELETE"]),
        "Page Category": random.choice(["Sports", "News", "Olympic Events", "Highlights and Recaps", "Fan zone and community"]),
        "Requested page": fake.uri_page(),
        "Response Code": random.randint(200, 500),
        "User Agent": fake.user_agent(),
        "Sports Start Time": fake.time(),
        "Sports End Time": fake.time(),
        "Country of Visitors": fake.country(),
        "Advancement Status": random.choice(["Qualified", "Disqualified", "Pending"]),
        "Live on Demand": random.choice(["Live", "On Demand"]),
        "Sport Date": fake.date_between(start_date="-1y", end_date="today"),
        "Viewership": random.randint(100, 10000),
        "Medal": random.choice(["Gold", "Silver", "Bronze"]),
        "Country of participants": fake.country(),
        "Names of participants": fake.name(),
        "Sports type": random.choice(["Swimming", "Athletics", "Gymnastics", "Cycling", "Football", "Basketball", "Judo", "Hockey", "Taekwondo", "Badminton"]),
        "Gender of visitors": random.choice(["Male", "Female"])
    }
    streaming_data.append(entry)

@app.route('/', methods=['GET'])
def get_streaming_data():
    return jsonify(streaming_data)

if __name__ == '__main__':
    app.run(debug=True)
