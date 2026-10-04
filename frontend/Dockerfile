FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["sh", "-c", "echo 'Streamlit: http://localhost:8501' && streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=8501"]