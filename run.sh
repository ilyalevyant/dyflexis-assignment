#!/bin/bash
pip install to-requirements.txt
pytest -n 17 --username admin --password password123 test_booking.py
pytest test_ui_booking.py
