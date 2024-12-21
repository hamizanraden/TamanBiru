import os

REPORT_FILE = './app/cli/data/reportCounts.txt'

def initialize_reports():
    """Ensure report file exists."""
    if not os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, 'w', encoding='utf-8') as file:
            file.write('')

def load_reports():
    """Load report data into a dictionary."""
    if not os.path.exists(REPORT_FILE):
        initialize_reports()
    with open(REPORT_FILE, 'r', encoding='utf-8') as file:
        return {line.split('|')[0]: int(line.split('|')[1]) for line in file if '|' in line}

def save_reports(reports):
    """Save the reports dictionary to file."""
    with open(REPORT_FILE, 'w', encoding='utf-8') as file:
        for message, count in reports.items():
            file.write(f'{message}|{count}\n')

def report_message(message, chat_file='./app/cli/data/chatAll.txt', limit=3):
    """
    Report a message in the specified chat file.
    If the report count exceeds the limit, the message is removed.
    """
    initialize_reports()
    reports = load_reports()

    # Normalize the message
    normalized_message = message.strip()

    # Update report count for the message
    reports[normalized_message] = reports.get(normalized_message, 0) + 1

    # Check if report limit is exceeded
    if reports[normalized_message] >= limit:
        delete_message(normalized_message, chat_file)
        del reports[normalized_message]  # Remove from reports

    save_reports(reports)
    return reports.get(normalized_message, 0)

def delete_message(message, chat_file):
    """Delete the reported message from the specified chat file."""
    normalized_message = message.strip()

    if os.path.exists(chat_file):
        with open(chat_file, 'r', encoding='utf-8') as file:
            messages = file.readlines()
        with open(chat_file, 'w', encoding='utf-8') as file:
            for line in messages:
                if line.strip() != normalized_message:
                    file.write(line)
