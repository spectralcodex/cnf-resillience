FROM python:3.12-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync && uv sync --no-cache --frozen

# Expose port for ECS mapping
EXPOSE 80

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "80", "--host", "0.0.0.0"]

