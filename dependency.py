import subprocess

def check_dependency(dependency):
    try:
        subprocess.check_output(["pip", "show", dependency])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    with open('requirements.txt') as f:
        dependencies = f.read().splitlines()
    for dependency in dependencies:
        if not check_dependency(dependency):
            print(f"Dependency {dependency} is missing.")

if __name__ == "__main__":
    main()
