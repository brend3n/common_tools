# Variables
PYTHON=python3
MODULE_DIR=scraper
MAIN_SCRIPT=__main__.py

# Default target
all: run

# Run the Python module
run:
	$(PYTHON) $(MODULE_DIR)/$(MAIN_SCRIPT)

# Clean up compiled Python files
clean:
	find . -name "*.pyc" -exec rm -f {} \;

# Open crontab editor
cronjob:
	EDITOR=vim crontab -e

.PHONY: all run clean cronjob
