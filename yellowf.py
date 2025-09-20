name: Build EXE

on:
  push:
   branches: [ main ]
  workflow_dispatch:
jobs:
  build:
    runs-on: windows-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install tools and deps
        run: |
          python -m pip install --upgrade pip
          pip install pyinstaller
          if (Test-Path requirements.txt) { pip install -r requirements.txt }

      - name: Build (window app)
        run: |
          pyinstaller --onefile --windowed --name YellowFlowerDay yellowf.py
          # If you uploaded an icon named flower.ico, use this instead:
          # pyinstaller --onefile --windowed --icon flower.ico --name YellowFlowerDay yellowf.py
          # If tkinter/turtle ever fails, try adding:
          # pyinstaller --onefile --windowed --hidden-import tkinter --hidden-import turtle --name YellowFlowerDay yellowf.py

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: YellowFlowerDay-dist
          path: dist/
