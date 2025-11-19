import argparse
import os
from .parser import parse_email
from .analyzer import analyze_email
from .scorer import score_email
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def process_email(file_path):
    email = parse_email(file_path)
    analysis = analyze_email(email)
    score, category = score_email(analysis)

    table = Table(title=f"SpoofX Report: {os.path.basename(file_path)}", show_header=True, header_style="bold magenta")
    table.add_column("Check", style="cyan", no_wrap=True)
    table.add_column("Result", style="green")

    for key, value in analysis.items():
        table.add_row(str(key), str(value))

    console.print(table)
    console.print(Panel(f"[bold red]Overall Risk Score: {score}[/bold red]\n[bold yellow]Risk Category: {category}[/bold yellow]",
                        title="Summary", border_style="bright_blue"))

def main():
    parser = argparse.ArgumentParser(description="SpoofX - Email Spoofing & Phishing Analyzer")
    parser.add_argument("paths", nargs="+", help="Path(s) to email file(s) or folder(s)")
    args = parser.parse_args()

    for path in args.paths:
        if os.path.isfile(path):
            process_email(path)
        elif os.path.isdir(path):
            # Process all files inside the directory
            for root, dirs, files in os.walk(path):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    if os.path.isfile(file_path):
                        process_email(file_path)
        else:
            console.print(f"[bold red]Path not found: {path}[/bold red]")

if __name__ == "__main__":
    main()
