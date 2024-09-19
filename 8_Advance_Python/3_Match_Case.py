def describe_day(day: str):
    match day.lower():  # Convert input to lowercase
        case "monday":
            return "The first day of the week"
        case "tuesday" | "wednesday" | "thursday" | "friday":
            return "Just another weekday."
        case "saturday" | "sunday":  # Correct pattern matching for multiple values
            return "It's the weekend!"
        case _:
            return "Unknown day of the week."

# Testing
print(describe_day("Monday"))   # Output: The first day of the week
print(describe_day("Tuesday"))  # Output: Just another weekday.
print(describe_day("Saturday")) # Output: It's the weekend!
print(describe_day("sunday"))   # Output: It's the weekend!
