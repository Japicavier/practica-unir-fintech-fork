run:
	python3 main.py casa perro arbol coche

docker:
	docker build -t fintech-sorter .
	docker run fintech-sorter
