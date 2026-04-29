run:
	@uv run main.py

freeze:
	@uv pip freeze > requirements.txt
	@uv sync