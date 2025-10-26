from requests import get
from bs4 import BeautifulSoup
import csv
import sys
from typing import List, Tuple


def check_arguments() -> Tuple[str, str]:
    """
    Check and validate command-line arguments.

    The program expects exactly two arguments:
    1. A valid URL starting with 'http://' or 'https://'
    2. An output file name ending with '.csv'

    Returns:
        tuple[str, str]: (url, output_file)

    Exits the program if arguments are missing or invalid.
    """
    if len(sys.argv) != 3:
        print("Invalid input. Please provide URL and output file name.")
        sys.exit(1)

    url: str = sys.argv[1]
    output_file: str = sys.argv[2]

    # Validate URL format
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Invalid URL format.")
        sys.exit(1)

    # Validate output file extension
    if not output_file.endswith(".csv"):
        print("Output file must have a .csv extension.")
        sys.exit(1)

    return url, output_file


def load_header(url: str) -> List[str]:
    """
    Loads and parses the header row for the CSV file from the provided URL.

    Args:
        url (str): URL of the page containing header information.

    Returns:
        list[str]: Combined list of static and dynamic header names.
    """
    headers = {'User-Agent': 'MinimalWikiScript/1.0 (myemail@example.com)'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    # Start with static header fields
    header: List[str] = ["code", "location", "registered", "envelopes", "valid"]

    # Extract dynamic header fields (party names)
    dynamic_headers = [tag.text for tag in soup.select("td.overflow_name")]

    header.extend(dynamic_headers)
    return header


def load_main_page(url: str) -> Tuple[BeautifulSoup, List[str], List[str], List[str], str]:
    """
    Loads the main election results page and extracts municipality data.

    Args:
        url (str): Main election page URL.

    Returns:
        tuple: (soup, municipality_codes, municipality_names, url_list, full_url)
    """
    municipality_codes: List[str] = []
    municipality_names: List[str] = []
    url_list: List[str] = []

    headers = {'User-Agent': 'MinimalWikiScript/1.0 (myemail@example.com)'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    print("DOWNLOADING DATA FROM SELECTED URL:", url)

    base_url = "https://www.volby.cz/pls/ps2017nss/"

    # Extract all municipality codes, names and detail URLs
    for tag in soup.select("td.cislo > a"):
        municipality_codes.append(tag.text.strip())
    for tag in soup.select("td.overflow_name"):
        municipality_names.append(tag.text.strip())
    for tag in soup.select("td.cislo a"):
        full_url = base_url + tag["href"]
        url_list.append(full_url)

    return soup, municipality_codes, municipality_names, url_list, full_url


def main_program(
    output_file: str,
    header: List[str],
    municipality_codes: List[str],
    municipality_names: List[str],
    url_list: List[str],
) -> None:
    """
    Main processing function — downloads detailed results for each municipality and writes them to a CSV file.

    Args:
        output_file (str): Path to the output CSV file.
        header (list[str]): List of header names for CSV.
        municipality_codes (list[str]): List of municipality codes.
        municipality_names (list[str]): List of municipality names.
        url_list (list[str]): List of URLs for each municipality’s details.

    Returns:
        None
    """
    with open(output_file, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for code, name, address in zip(municipality_codes, municipality_names, url_list):
            headers = {'User-Agent': 'MinimalWikiScript/1.0 (myemail@example.com)'}
            response = get(address, headers=headers)
            soup = BeautifulSoup(response.text, features="html.parser")

            # Extract summary data for the municipality
            registered = soup.select_one('td.cislo[headers="sa2"]').text.strip()
            envelopes = soup.select_one('td.cislo[headers="sa5"]').text.strip()
            valid = soup.select_one('td.cislo[headers="sa6"]').text.strip()

            # Extract votes for each political party from two tables
            first_table_votes = [cell.text.strip() for cell in soup.select('td.cislo[headers="t1sa2 t1sb3"]')]
            second_table_votes = [cell.text.strip() for cell in soup.select('td.cislo[headers="t2sa2 t2sb3"]')]

            row = [code, name, registered, envelopes, valid] + first_table_votes + second_table_votes
            writer.writerow(row)


if __name__ == "__main__":
    # Entry point of the program
    url, output_file = check_arguments()
    soup, municipality_codes, municipality_names, url_list, full_url = load_main_page(url)
    header = load_header(full_url)
    main_program(output_file, header, municipality_codes, municipality_names, url_list)

    print("SAVING TO FILE:", output_file)
    print("FINISHED")
