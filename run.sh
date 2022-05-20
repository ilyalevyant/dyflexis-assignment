pip install to-requirements.txt
pytest test_gists.py -n 15 -m "not serial"
pytest test_gists.py -m "serial"