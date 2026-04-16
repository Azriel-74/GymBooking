from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'iron_core_dark_secret'

# Mock Data
CLASSES = [
    {"id": 1, "name": "Midnight HIIT", "time": "11:00 PM", "instructor": "Dante", "spots": 12, "image": "hiit"},
    {"id": 2, "name": "Power Yoga", "time": "06:00 AM", "instructor": "Selena", "spots": 15, "image": "yoga"},
    {"id": 3, "name": "Heavy Lifting", "time": "05:00 PM", "instructor": "Thor", "spots": 8, "image": "lifting"},
    {"id": 4, "name": "Iron Boxing", "time": "07:30 PM", "instructor": "Rocky", "spots": 10, "image": "boxing"},
]

MEMBERSHIP_PLANS = [
    {"id": "basic", "name": "Basic Core", "price": "$29.99/mo", "features": ["Gym Access", "Locker Room", "1 Free Class"]},
    {"id": "pro", "name": "Iron Pro", "price": "$59.99/mo", "features": ["24/7 Access", "All Classes", "Personal Trainer"]},
    {"id": "elite", "name": "Elite Titan", "price": "$99.99/mo", "features": ["VIP Lounge", "Spa & Sauna", "Nutrition Plan"]},
]

MEMBERS = [
    {"id": "M001", "name": "Alice Smith", "status": "Active", "plan": "Iron Pro"},
    {"id": "M002", "name": "Bob Johnson", "status": "Active", "plan": "Basic Core"},
    {"id": "M003", "name": "Charlie Brown", "status": "Expired", "plan": "Elite Titan"},
]

BOOKINGS = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classes')
def classes():
    return render_template('classes.html', classes=CLASSES)

@app.route('/membership')
def membership():
    return render_template('membership.html', plans=MEMBERSHIP_PLANS)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/book/<int:class_id>', methods=['GET', 'POST'])
def book(class_id):
    gym_class = next((c for c in CLASSES if c['id'] == class_id), None)
    if not gym_class:
        return redirect(url_for('classes'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        BOOKINGS.append({"class_id": class_id, "name": name, "email": email})
        return redirect(url_for('payment', item=f"Booking for {gym_class['name']}"))
    
    return render_template('booking.html', gym_class=gym_class)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    item = request.args.get('item', 'Membership')
    if request.method == 'POST':
        # Simulated payment success
        return redirect(url_for('success', message=f"Payment for {item} was processed successfully!"))
    return render_template('payment.html', item=item)

# Owner-Only Routes
@app.route('/owner')
def owner_dashboard():
    # In a real app, this would check if the user is logged in as an admin
    return render_template('owner_dashboard.html', members=MEMBERS, bookings=BOOKINGS)

@app.route('/owner/checkin', methods=['GET', 'POST'])
def checkin():
    checked_in_member = None
    error = None
    if request.method == 'POST':
        member_id = request.form.get('member_id')
        member = next((m for m in MEMBERS if m['id'] == member_id), None)
        if member:
            if member['status'] == 'Active':
                checked_in_member = member
            else:
                error = f"Member {member_id} has an expired membership."
        else:
            error = f"Member ID {member_id} not found."
    
    return render_template('checkin.html', member=checked_in_member, error=error)

@app.route('/success')
def success():
    message = request.args.get('message', 'Action completed successfully!')
    return render_template('success.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
