# Clock Angle Solver Implementation Plan

This project will progress through four phases to turn a simple script into a live, interactive clock simulator.

## Phase 1: The Mathematical Engine (Pure Python)
Before touching Streamlit, the math engine needs to be reliable. Write a standalone Python function that takes hours and minutes and returns the acute angle.

### Logic Breakdown

- Hour hand position: a clock face is $360^\circ$. Each of the 12 hours represents $30^\circ$. The hour hand also moves slightly as minutes pass, specifically $0.5^\circ$ per minute.

$$H_{\text{angle}} = 30 \times (H \bmod 12) + 0.5 \times M$$

- Minute hand position: the minute hand moves $6^\circ$ per minute.

$$M_{\text{angle}} = 6 \times M$$

- Acute angle: find the absolute difference between the two positions. If the difference is greater than $180^\circ$, subtract it from $360^\circ$.

$$\theta = \min(|H_{\text{angle}} - M_{\text{angle}}|, 360^\circ - |H_{\text{angle}} - M_{\text{angle}}|)$$

Deliverable for Phase 1: a working Python script named `clock_logic.py` that can be tested in the terminal with manual inputs such as 3:00 should yield $90^\circ$ and 6:00 should yield $180^\circ$.

## Phase 2: Basic Streamlit UI Setup
Wrap the math engine in a basic user interface. Streamlit makes this fast because no HTML or CSS is required.

- Setup: create a main app file such as `app.py` and import Streamlit with `import streamlit as st`.
- Inputs: use `st.time_input()` for a native time picker, or use two separate `st.slider()` components for hours and minutes.
- Outputs: pass the widget values directly into the Phase 1 math function and display the resulting angle using `st.metric()` or `st.success()`.

Deliverable for Phase 2: a local web app that runs with `streamlit run app.py`, where changing the time instantly updates the displayed angle.

## Phase 3: The "Simulator" Visuals
A calculator gives a number, but a simulator helps visualize it. To make the app more engaging, dynamically draw the clock face.

- Use a plotting library such as matplotlib or plotly to render a basic polar plot or scatter plot that resembles a clock.
- Draw a circle for the clock face.
- Plot two vectors (lines) starting from the center $(0, 0)$ pointing toward coordinates calculated from the hour and minute angle formulas.
- Integrate the chart into Streamlit using `st.pyplot()` or `st.plotly_chart()`. Each time the user changes the time, the clock hands move in real time.

## Phase 4: Polish, Edge Cases, and Deployment
Make the app robust and share it with others.

- Handling edge cases: ensure the code gracefully handles 24-hour inputs such as 13:00 versus 1:00 PM by applying a modulo 12 to the hour input before calculations.
- UX enhancements: add an expander component with `with st.expander("Show the Math"):` that reveals the equations used to solve the problem.
- UX enhancements: display a prominent heading such as "What is the acute angle between the hour and minute hand at time [blank]?" where the blank is replaced dynamically with the user-selected time.
- Deployment: push the final code to a public GitHub repository, then deploy it through Streamlit Community Cloud to obtain a shareable live web link.
