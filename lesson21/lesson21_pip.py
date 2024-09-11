# Lesson 21 - Virtual Environments & Pip
# Pip is a package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library.
# In the terminal, type:
# py -m pip install requests - This command installs the requests package using pip.
# py -m pip install requests==2.30 - This command installs a specific version of the requests package.
# py -m pip install - U requests - This command upgrades the requests package to the latest version.
# py -m pip uninstall requests - This command uninstalls the requests package.

# Virtual environments are isolated Python environments. They allow you to install packages in an isolated environment for a specific project.
# To create a virtual environment, type:
# py -m venv .venv - This command creates a virtual environment in the current directory.
# To activate the virtual environment, type:
# source .venv/Scripts/activate - This command activates the virtual environment.
# To deactivate the virtual environment, type:
# deactivate - This command deactivates the virtual environment.
# When activated, there's no need to us py -m pip. You can use pip directly to install packages. pip list for example.

# pypi.org is the Python Package Index. It is a repository of software packages for Python. You can search for packages and find information about them on the website.

# Use the command pip freeze > requirements.txt to create a requirements.txt file that lists all the packages installed in the current environment.
