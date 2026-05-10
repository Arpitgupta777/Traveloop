# ✈️ Traveloop - Personalized Travel Planning Made Easy

Welcome to **Traveloop**, a user-centric, responsive application designed to simplify the complexity of planning multi-city travel. Built as a comprehensive hackathon solution, Traveloop empowers users to dream, design, and organize trips with ease by offering an end-to-end travel planning tool that combines flexibility and interactivity.

---

## 🚀 Features
The application includes a comprehensive set of features to ensure a rich and user-friendly experience across all devices:

1. **Authentication:** Secure Login & Signup screens to manage personal travel plans.
2. **Dashboard:** A central hub showing upcoming trips, recent trips, and quick actions like "Plan New Trip".
3. **Trip Creation & Management:** Form to initiate new trips (name, dates, description) and a list view to access existing/upcoming trips.
4. **Interactive Itinerary Builder:** Interface to add cities, dates, and assign activities for each stop, allowing users to construct full day-wise plans.
5. **City & Activity Search:** Add cities and enriching activities categorized by interest, cost, and duration.
6. **Budget & Cost Breakdown:** Summarized financial view tracking transport, stay, activities, and meals to help travelers stay within budget.
7. **Packing Checklist:** A per-trip checklist to add, categorize, and mark items as packed, ensuring nothing essential is forgotten.
8. **Trip Notes/Journal:** A text note-taking screen to jot down important details, reminders, or hotel check-in info.
9. **Shared/Public Itineraries:** Public pages displaying a read-only version of an itinerary so others can view and get inspired.
10. **User Profile:** Settings page to update profile information, and photos.
11. **Admin/Analytics Dashboard:** Admin-only interface to track user trends, trip data, and platform usage.

---

## 💻 Tech Stack
* **Backend:** Python, Django Framework
* **Frontend:** HTML5, Tailwind CSS, FontAwesome Icons, Django Templates
* **Database:** SQLite (Development) / PostgreSQL (Production ready)
* **Architecture:** MVT (Model-View-Template) demonstrating proper use of relational databases

---

## 👥 Team Workload & Contribution Guide

This project was built collaboratively during the hackathon by team: 

1. **Dharmesh Gupta - Frontend & UI/UX Developer**

2. **Yash Variya - Backend Developer (Views & Logic)**

3. **Arpit Gupta - Database Administrator & Modeler**

4. **Anant Koli - QA, Testing & DevOps**

---

## 🛠️ Installation & Setup

Follow these steps to run the Traveloop project locally:

1. **Clone the repository:**

```bash
   git clone [https://github.com/](https://github.com/)[your-github-username]/traveloop.git
   cd traveloop
```

2. **Create and activate a virtual environment:**
   
```bash
  python -m venv venv
  # On Windows:
  venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate
```


3. **Install dependencies:**
   
```bash
  pip install -r requirements.txt
```


4. **Run Database Migrations:**
   
```bash
  python manage.py makemigrations
  python manage.py migrate
```


5. **Create a Superuser (For Admin Dashboard):**
   
```bash
  python manage.py createsuperuser
```


6. **Start the Development Server:**

```bash
  python manage.py runserver
```


7. **Access the App:**
Open your browser and navigate to `http://127.0.0.1:8000`.

---

*Built with ❤️ for the Hackathon.*
