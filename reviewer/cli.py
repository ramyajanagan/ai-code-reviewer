import os
import typer
from dotenv import load_dotenv  # 1. Import dotenv
from rich.console import Console
from rich.panel import Panel
from reviewer.git_utils import get_git_diff
from reviewer.review_engine import analyze_diff

# 2. Load environment variables from .env file
load_dotenv()

app = typer.Typer(help="AI-Powered Automated Code Review CLI")
console = Console()

@app.command()
def review(
    staged: bool = typer.Option(False, "--staged", "-s", help="Review staged changes only")
):
    """Run AI code review on your local git changes."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/bold red] OPENAI_API_KEY environment variable is missing.")
        raise typer.Exit(code=1)

    console.print("[bold blue]Scanning local Git repository...[/bold blue]")
    diff = get_git_diff(staged=staged)

    if not diff:
        console.print("[bold yellow]No changes found to review.[/bold yellow]")
        return

    console.print("[bold green]Analyzing diff with AI...[/bold green]")
    review_output = analyze_diff(diff, api_key)

    console.print(Panel(review_output, title="AI Code Review Summary", border_style="cyan"))

if __name__ == "__main__":
    app()
