# Clock Angle Solver

A simple Streamlit app that calculates and visualizes the acute angle between the hour and minute hands of a clock for a selected time.

## Features

- Select a time with the built-in time picker
- See the acute angle displayed dynamically
- View a visual clock with moving hour and minute hands
- Expand a section to view the math behind the calculation

## Requirements

Make sure you have Python installed, then install the dependencies:

```bash
pip install streamlit matplotlib numpy pytest
```

## Run the app

From the project folder, start the app with:

```bash
streamlit run app.py
```

This will open the app in your browser.

## Run the tests

To verify the core logic:

```bash
pytest -q
```

## Project files

- `app.py` – Streamlit user interface
- `clock_logic.py` – angle calculation logic
- `tests/test_clock_logic.py` – regression tests
