import csv
import requests
from requests.exceptions import RequestException


def read_csv_file() -> list:
    """Read URLs from the CSV file and return as a list."""
    try:
        with open(file="Task 2 - Intern.csv", mode="r", encoding="utf-8") as file:
            urls = []
            csv_file = csv.reader(file)
            next(csv_file)  # Skip header row
            for line in csv_file:
                if (
                    line and line[0].strip()
                ):  # Check if line exists and URL is not empty
                    urls.append(line[0].strip())
        return urls
    except FileNotFoundError:
        print("Error: 'Task 2 - Intern.csv' file not found")
        return []


def check_url_status(url: str) -> str:
    """Check the status of a URL and return formatted output."""
    try:
        response = requests.get(url, timeout=30)
        return f"({response.status_code}) {url}"
    except RequestException as e:
        return f"(ERROR) {url} - {str(e)}"


def main():
    """Main function to process URLs and print their status."""
    urls = read_csv_file()
    if not urls:
        return

    print("Checking URL status codes...")
    for url in urls:
        result = check_url_status(url)
        print(result)


if __name__ == "__main__":
    main()
