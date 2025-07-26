def log_message(message):
    with open("logs/scraper.log", "a") as log_file:
        log_file.write(message + "\n")