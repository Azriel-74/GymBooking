# Gym Booking Website V2 - Dark & Dynamic

## Project Enhancements
1. **Professional Dark Theme**: Modern, high-contrast dark aesthetic using deep grays, blacks, and vibrant accents (Neon Red/Orange).
2. **Moving Templates (CSS Animations)**: Subtle hover effects, fade-ins, and animated transitions to create a premium feel without JavaScript.
3. **Additional Pages**:
   - `membership.html`: Detailed membership plans.
   - `contact.html`: Contact form for inquiries.
   - `owner_dashboard.html`: Separate view for gym owners.
4. **User Distinction**:
   - **Customer**: Access to homepage, classes, membership booking, and payment.
   - **Owner**: Access to member check-in and a summary dashboard (protected by a simple prefix or route).

## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3 (Advanced animations)
- **Database**: In-memory data (easily portable)

## Directory Structure
```
gym_website_v2/
├── app.py
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── classes.html
    ├── membership.html
    ├── contact.html
    ├── booking.html
    ├── payment.html
    ├── owner_dashboard.html
    ├── checkin.html
    └── success.html
```
