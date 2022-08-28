FILE_NAME = 'request_counts.txt'


def read_request_counts():
    data = {}

    with open(FILE_NAME) as file:
        for line in file:
            method = line.split(':')[0].strip()
            count = int(line.split(':')[1].strip())
            data[method] = count
    return data


def save_request_counts(data):
    with open(FILE_NAME, 'w') as file:
        for method, count in data.items():
            file.write(f"{method}: {count}\n")