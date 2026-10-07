import subprocess

def get_git_diff(staged: bool = False) -> str:
    """Fetch uncommitted or staged changes from the local Git repository."""
    cmd = ["git", "diff", "--staged"] if staged else ["git", "diff"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""
