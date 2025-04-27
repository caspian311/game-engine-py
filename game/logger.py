from datetime import datetime

f = open("output.log", "w", encoding="UTF-8") # pylint: disable=consider-using-with

def log(message):
    f.write(f"{datetime.now()} - {message}\n")
    f.flush()
