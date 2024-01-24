import subprocess
import pkg_resources

# Get a list of all installed packages
installed_packages = [pkg.key for pkg in pkg_resources.working_set]

# Filter top-level packages
top_level_packages = set()
for package in installed_packages:
    # use pip show to get package details
    result = subprocess.run(['pip', 'show', package], capture_output=True)
    output = result.stdout.decode('utf-8')
    print(output)

    # Check if 'Required by' line is empty
    if 'Required-by:' in output:
        required_by = output.split('Required-by:')[1].split('\n')[0].strip()
        if not required_by:
            print(f'Found top-level package: {package}')
            top_level_packages.add(package)

# Wrrite top-level packages to requirements.txt
with open('requirements.txt', 'w') as f:
    for package in top_level_packages:
        f.write(f'{package}\n')
