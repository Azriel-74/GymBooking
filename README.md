# Iron Core Gym Elite - Dark Edition

A professional, high-performance gym management website featuring a modern dark theme, advanced CSS animations, and a multi-page architecture. Built with Python (Flask) and pure HTML5/CSS3.

## New Features
- **Professional Dark Aesthetic**: Deep blacks, neon accents, and high-contrast layouts.
- **Moving Templates**: Advanced CSS animations (fade-ins, slide-ups, zoom-on-hover) for a premium feel.
- **Owner Dashboard**: A specialized management view for tracking members and bookings.
- **Enhanced Pages**: Added Membership Plans, Contact Portal, and an expanded Class Schedule.

## How the Systems Work

### 1. Payment System (Simulated)
The payment system is integrated into the booking and membership flows:
- **Flow**: When a user clicks "Book Now" or "Select Plan," they are directed to a confirmation page. After confirming their details, they are sent to the `payment.html` portal.
- **Simulation**: In this version, the payment is simulated. Any input in the card fields will be "processed" by the Flask backend, which then redirects the user to a success page.
- **Real-World Ready**: To make this real, you would replace the simulation logic in `app.py` with a payment gateway like Stripe or PayPal's API.

### 2. User Distinction (Customer vs. Owner)
The website distinguishes between users through **Route Separation**:
- **Customer View**: Customers see the public-facing pages (Home, Classes, Membership, Contact). They interact with the front-end forms to book and pay.
- **Owner View**: The **Owner Portal** (`/owner`) is a separate area designed for the gym owner. It provides access to:
  - **Member Database**: A table of all registered members and their status.
  - **Check-in Portal**: A specialized tool where the owner enters a Member ID to verify if someone is allowed to enter the gym.
- **Access Control**: In this basic version, the distinction is made by having a specific "Owner Portal" link in the navigation. In a full system, this would be protected by a login page that only the owner has credentials for.

## How to Run in VS Code

### 1. Setup
1. Open the `gym_website_v2` folder in VS Code.
2. Open a terminal in VS Code (`Ctrl + \``).

### 2. Install Dependencies
```bash
python -m pip install flask
```

### 3. Launch
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

## Test Data
- **Member IDs for Check-in**: `M001` (Active), `M002` (Active), `M003` (Expired).
- **Owner Portal**: Click "Owner Portal" in the top right of the navigation bar.
