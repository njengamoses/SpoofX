import argparse
from .parser import parse_email
from .analyzer import analyze_email
from .scorer import score_email
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def main():
    parser = argparse.ArgumentParser(description="SpoofX - Email Spoofing & Phishing Analyzer")
    parser.add_argument("file", help="Path to email text file")
    args = parser.parse_args()

    # Parse and analyze
    email = parse_email(args.file)
    analysis = analyze_email(email)
    score, category = score_email(analysis)

    # Build table
    table = Table(title="SpoofX Analysis Report", show_header=True, header_style="bold magenta")
    table.add_column("Check", style="cyan", no_wrap=True)
    table.add_column("Result", style="green")

    for key, value in analysis.items():
        table.add_row(str(key), str(value))

    # Display table and summary panel
    console.print(table)
    console.print(Panel(f"[bold red]Overall Risk Score: {score}[/bold red]\n[bold yellow]Risk Category: {category}[/bold yellow]",
                        title="Summary", border_style="bright_blue"))

if __name__ == "__main__":
    main()
