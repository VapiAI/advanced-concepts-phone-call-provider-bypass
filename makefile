install:
	# Install requirements 
	pip install --upgrade pip &&\
		pip install -r requirements.txt
dev:
	# Start server
	fastapi dev ./app/main.py   
