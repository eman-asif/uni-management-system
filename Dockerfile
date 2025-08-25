# Use official slim Python image
FROM python:3.12-slim
# Expose port
EXPOSE 8000
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=True
ENV SECRET_KEY=django-insecure--p&b^c_7vhr8^_g$9phxkvx#fzu@w0cm@4wz^#trnu@n20e@13
ENV DATABASE_URL=postgres://eman:eman49@db:5432/ums2

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    libjpeg-dev \
    zlib1g-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput



# Run Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]


# FROM python:3.12-slim
# EXPOSE 8000

# # Prevent Python from writing pyc files & buffer logs
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV DEBUG=True
# ENV SECRET_KEY=django-insecure--p&b^c_7vhr8^_g$9phxkvx#fzu@w0cm@4wz^#trnu@n20e@13
# ENV DATABASE_URL=postgres://eman:eman49@localhost:5432/ums2
# # Set working directory
# WORKDIR /app

# # Install system dependencies for psycopg2
# RUN apt-get update && apt-get install -y \
#     python3-dev \
#     build-essential \
#     gcc \
#     libpq-dev \
#     libffi-dev \
#     libssl-dev \
#     curl \
#     netcat-openbsd \
#     libjpeg-dev \
#     zlib1g-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# COPY . .
# RUN pip install --upgrade pip setuptools wheel

# # Install Python dependencies
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # RUN python manage.py collectstatic --noinput
# RUN python manage.py collectstatic --noinput

# # Run Gunicorn
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]