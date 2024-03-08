# Use an official Python runtime as a parent image
FROM python:3.11-alpine
LABEL author='francesco.fiduccia@gmail.com'


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SHARED_PATH=/abc/change_me

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the working directory in the container
WORKDIR /nc-cfs

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY ./app /nc-cfs/app
COPY ./scripts /nc-cfs/scripts
RUN ./scripts/create_shared_example_directory.sh
# Specify the command to run on container start
CMD ["python3", "-m", "app.main"]