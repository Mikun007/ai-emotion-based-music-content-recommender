# 1. Base image
FROM python:3.10-slim

# 2. Install system dependencies needed by OpenCV
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# 3/ Security: set up the hugging face user
#RUN useradd -m -u 1000 user
#USER user
#ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# 4. Copy and install Python dependencies
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the app
COPY . .

EXPOSE 7860

# 7. Run Flask
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]