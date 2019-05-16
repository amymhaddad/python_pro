"""Get the day and time. Use this information to greet customers"""

from datetime import datetime

def _current_day():
    """Get the current day of the week"""
    return datetime.now().strftime("%A")


def _part_of_the_day():
    """
    Get the current hour of the day
    and whether it's AM or PM.
    Return a response based on the part of day.
    """

    hour_am_or_pm = datetime.now().strftime("%I %p").split(' ')
    current_hour = int(hour_am_or_pm[0])
    am_pm = hour_am_or_pm[1]

    if am_pm == 'AM' and current_hour < 12:
        return "morning"
    elif (am_pm == "PM") and (current_hour == 12 or current_hour <= 5):
        return "afternoon"
    else:
        return "evening"


class Greeter():
    """Greet store customers"""

    def greet(self, store):
        """Print a nice customer greeting"""

        print(f"""
        Hi, welcome to {store}! 
        How's your {_current_day()} {_part_of_the_day()} going? 
        Here's a coupon for 20% off!
        """)

store = 'walmart'
greet_person = Greeter()
greet_person.greet(store)
