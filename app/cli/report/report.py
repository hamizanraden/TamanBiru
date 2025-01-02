import os

Lapor = './app/cli/data/reportCounts.txt'

def mulai_laporan():
    if not os.path.exists(Lapor):
        with open(Lapor, 'w', encoding='utf-8') as file:
            file.write('')

def load_reports():
    """Load report data from file into a dictionary."""
    reports = {}
    if os.path.exists(Lapor):
        with open(Lapor, 'r', encoding='utf-8') as file:
            for line in file:
                if '|' in line:
                    parts = line.strip().split('|')
                    message = parts[0]
                    count = int(parts[1])
                    reporters = parts[2].split(',') if len(parts) > 2 else []
                    reports[message] = {'count': count, 'reporters': reporters}
    return reports

def save_reports(reports):
    """Save the reports dictionary to file."""
    with open(Lapor, 'w', encoding='utf-8') as file:
        for message, data in reports.items():
            reporters = ','.join(data['reporters'])
            file.write(f'{message}|{data["count"]}|{reporters}\n')

def report_message(message, reporter, chat_file='./app/cli/data/chatAll.txt', limit=3):
    """
    Report a message by a specific reporter in the specified chat file.
    If the report count exceeds the limit, the message is removed.
    """
    mulai_laporan()
    reports = load_reports()

    # Normalize the message
    normalized_message = message.strip()

    # Initialize report entry if not exists
    if normalized_message not in reports:
        reports[normalized_message] = {'count': 0, 'reporters': []}
        
    if reporter in reports[normalized_message]['reporters']:
        return 'already_reported'
    
    # Check if the reporter already reported this message
    if reporter in reports[normalized_message]['reporters']:
        print("Anda sudah melaporkan pesan ini.")
        return reports[normalized_message]['count']

    # Update report count and add reporter
    reports[normalized_message]['count'] += 1
    reports[normalized_message]['reporters'].append(reporter)

    # Check if report limit is exceeded
    if reports[normalized_message]['count'] >= limit:
        delete_message(normalized_message, chat_file)
        del reports[normalized_message]  # Remove from reports

    save_reports(reports)
    return 'succes'

def delete_message(message, chat_file):
    normalized_message = message.strip()

    if os.path.exists(chat_file):
        with open(chat_file, 'r', encoding='utf-8') as file:
            messages = file.readlines()
        with open(chat_file, 'w', encoding='utf-8') as file:
            for line in messages:
                if line.strip() != normalized_message:
                    file.write(line)
