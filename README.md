# TrainTicket

Webite written for sell/buy train station/railway tickets.

# Demo
* Running on: https://brief-coherent-punch.glitch.me
* Note: its on glitch Free Account. so The web app may be sleep.
Wait a few seconds, so that glitch wakes the server up.

# Language: HTML/CSS/Python-Django
Frontend is pure html/css/js and backend is imlemented by django framework.

Admins will add the available trains and their corresponding information, and buyers will see them; each user will buy the ticket according to him/her source and destination!

* Sections:
    * Home page: shows all the tickets available. These tickets are defined by admins/staff.

    * Search page: User can:
        * Search for tickets, by Source name
        * Search for tickets, by Destination name
        * Filter tickets within a date range
        * or a combination of these 3

    * About us: Obvious!
    * Contact Us: Contact Information + Contact form
    * Authentication Pages: Login/Register/Logout/Whatever!

* Todo:
    Contact Form is not connected to any api.

# How to run:
> python manage.py collectstatic

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver

# Template:
Original template is implemented by BeApp.
