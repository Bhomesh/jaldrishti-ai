.PHONY: test run clean

test:
	python3 -m unittest discover tests

run:
	python3 -m src.server 8081

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
