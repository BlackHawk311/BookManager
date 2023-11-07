FROM python:3

WORKDIR /app/

# we copy first the requirements.txt so that we can install packages needed first
# & it will remain in docker cache layers
# (= `docker build` re-runs will hit the cache as long as we don't modify requirements.txt)
# (= faster builds)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# This commands will copy every files (from host) into the container (in the workdir folder)
# It also prevent docker cache layers from being used (for this instruction & the following)
COPY . .

# start up the web app
# --host 0.0.0.0 = allow any external process to access the API
CMD ["uvicorn", "--host", "0.0.0.0", "--app-dir", "src", "main:app", "--reload"]

