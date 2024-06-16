install:
	pip install -r requirements.txt  # Instaluje zależności (jeśli istnieją)

test:
	python test_app.py  # Uruchamia testy jednostkowe

run:
	python app.py  # Uruchamia aplikację

.PHONY: install test run
