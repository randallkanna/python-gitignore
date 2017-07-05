import os

def main():
    directory = os.getcwd()

    fileName = directory + "/.gitignore"
    gitIgnoreFile = open(fileName, "w")

    ignore = ['# Credit to https://github.com/github/gitignore', '', '# Byte-compiled / optimized / DLL files', '__pycache__/', '*.py[cod]', '*$py.class', '', '# C extensions', '*.so', '# Distribution / packaging', '.Python', 'build/', 'develop-eggs/', 'dist/', 'downloads/', '', '.eggs/', 'lib/', 'lib64/', 'parts/', 'sdist/', 'var/', 'wheels/', '*.egg-info/', '.installed.cfg', '*.egg', '# PyInstaller', '*.manifest', '*.spec', '', '# Installer logs', 'pip-log.txt', 'pip-delete-this-directory.txt', '', '# Unit test / coverage reports', 'htmlcov/', '.tox/', '.coverage', '.coverage.*', '.cache', 'nosetests.xml', 'coverage.xml', '*.cover', '.hypothesis/', '', '# Django stuff:', '*.log', 'local_settings.py', '', '# Flask stuff:', 'instance/', '.webassets-cache', '', '# Scrapy stuff:', '.scrapy', '', '# PyBuilder', 'target/', '# pyenv', '.python-version', '', '# Environments', '.env', '.venv', 'env/', 'venv/', 'ENV/', '# Spyder project settings', '.spyderproject', '.spyproject', '# Rope project settings', '.ropeproject', '# mkdocs documentation', '/site', '# mypy', '.mypy_cache/']

    for line in ignore:
        gitIgnoreFile.write(line)
        gitIgnoreFile.write("\n")

    gitIgnoreFile.close()