import subprocess

try:
    subprocess.call(['git', 'init', '--initial-branch', 'main'])
    subprocess.call(['git', 'commit', '--allow-empty', '-m', 'Root commit'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit from Cookiecutter template'])
    subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.project_repo }}'])
except Exception as e:
    print(f"An error occurred during initializing the git repo: {e}")
    print("Make sure to manually set up a git repository which is necessary for `hatch-vcs`")

print("\nProject successfully created!\nNext steps:")
print("1. cd {{ cookiecutter.project_slug }}")
print("2. Install hatch (if not already): https://hatch.pypa.io/latest/install/")
print("3. Create environments: hatch env create")
print("4. Install pre-commit hooks: hatch run pre-commit install --install-hooks")
print("5. Run tests with: hatch test --all")
print("6. See CONTRIBUTING.md for detailed development setup")

