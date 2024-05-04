from flask import Flask, jsonify
import random
from datetime import datetime, timedelta
from faker import Faker
from threading import Thread
import time

app = Flask(__name__)
fake = Faker()

streaming_data = []

def generate_entry():
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
    return entry

def add_data_periodically():
    while True:
        new_entry = generate_entry()
        streaming_data.append(new_entry)
        time.sleep(1)  # Add new data every second

@app.route('/api/streaming', methods=['GET'])
def get_streaming_data():
    return jsonify(streaming_data)

if __name__ == '__main__':
    # Start the background task to add data periodically
    add_data_thread = Thread(target=add_data_periodically)
    add_data_thread.daemon = True
    add_data_thread.start()

    # Start Flask app without debugger
    app.run(debug=False)
