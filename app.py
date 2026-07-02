from datetime import datetime
import re

import numpy as np
import streamlit as st
from matplotlib import pyplot as plt

from clock_logic import calculate_acute_angle


def plot_clock(hours, minutes):
    hour_angle = 30 * (hours % 12) + 0.5 * minutes
    minute_angle = 6 * minutes

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.axis("off")

    circle = plt.Circle((0, 0), 1, fill=False, color="black", linewidth=2)
    ax.add_artist(circle)

    for tick in range(12):
        angle_deg = tick * 30
        angle_rad = np.deg2rad(90 - angle_deg)
        x1, y1 = 0.85 * np.cos(angle_rad), 0.85 * np.sin(angle_rad)
        x2, y2 = 0.95 * np.cos(angle_rad), 0.95 * np.sin(angle_rad)
        ax.plot([x1, x2], [y1, y2], color="black", linewidth=1.5)

        label_angle = np.deg2rad(90 - angle_deg)
        label_radius = 0.72
        label_x = label_radius * np.cos(label_angle)
        label_y = label_radius * np.sin(label_angle)
        label_value = tick if tick != 0 else 12
        ax.text(label_x, label_y, str(label_value), ha="center", va="center", fontsize=10)

    def draw_hand(length, angle_deg, color, linewidth):
        angle_rad = np.deg2rad(90 - angle_deg)
        x, y = length * np.cos(angle_rad), length * np.sin(angle_rad)
        ax.plot([0, x], [0, y], color=color, linewidth=linewidth)

    draw_hand(0.55, hour_angle, "navy", 3)
    draw_hand(0.85, minute_angle, "crimson", 2)

    return fig


st.set_page_config(page_title="Clock Angle Solver", page_icon="🕒")
st.title("Clock Angle Solver")

default_time = datetime.now().strftime("%I:%M %p")
user_input = st.text_input("Enter a time (for example 3:15 or 03:15 PM)", value=default_time)

match = re.fullmatch(r"(\d{1,2})\s*:\s*(\d{1,2})\s*(AM|PM)?", user_input.strip(), flags=re.IGNORECASE)

if match:
    hours = int(match.group(1))
    minutes = int(match.group(2))
    period = match.group(3)

    if period and period.upper() == "PM" and hours != 12:
        hours += 12
    if period and period.upper() == "AM" and hours == 12:
        hours = 0

    if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
        st.warning("Please enter a valid time between 00:00 and 23:59.")
        hours = 12
        minutes = 0
    else:
        angle = calculate_acute_angle(hours, minutes)
        formatted_time = f"{hours % 12 or 12}:{minutes:02d} {'PM' if hours >= 12 else 'AM'}"
        st.markdown(f"## What is the acute angle between the hour and minute hand at time {formatted_time}?")
        st.metric("Acute angle", f"{angle:.1f}°")
        clock_fig = plot_clock(hours, minutes)
        st.pyplot(clock_fig)
        plt.close(clock_fig)
else:
    st.warning("Please enter a time in the format HH:MM, H:MM, or H:MM AM/PM.")
    angle = calculate_acute_angle(12, 0)
    formatted_time = "12:00 PM"
    st.markdown(f"## What is the acute angle between the hour and minute hand at time {formatted_time}?")
    st.metric("Acute angle", f"{angle:.1f}°")
    clock_fig = plot_clock(12, 0)
    st.pyplot(clock_fig)
    plt.close(clock_fig)

with st.expander("Show the Math"):
    st.latex(r"H_{angle} = 30 \times (H \bmod 12) + 0.5 \times M")
    st.latex(r"M_{angle} = 6 \times M")
    st.latex(r"\theta = \min(|H_{angle} - M_{angle}|, 360^\circ - |H_{angle} - M_{angle}|)")
