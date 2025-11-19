import argparse
from rich.console import Console
from rich.table import Table
from .parser import parse_headers
from .analyzer import analyze_headers
from .scorer import calculate_score

console = Console()

def main():
    parser = argparse.ArgumentParser(description="SpoofX - Email Spoof Detection Tool")
    parser.add_argument("header_file", help="Path to the email header file")
    args = parser.parse_args()

    headers = parse_headers(args.header_file)
    analysis = analyze_headers(headers)
    score = calculate_score(analysis)

    table = Table(title="SpoofX Analysis Report")

    for key, value in analysis.items():
        table.add_row(str(key), str(value))

    console.print(table)
    console.print(f"\n[bold red]Risk Score: {score}/100[/bold red]")

if __name__ == "__main__":
    main()
