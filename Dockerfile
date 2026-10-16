FROM ://microsoft.com
WORKDIR /code
RUN pip install --no-cache-dir streamgrabber fastapi uvicorn
COPY main.py /code/main.py
EXPOSE 10000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
