import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew in cherry leaves are caused by the fungus Podosphaera clandestina.\n"
        f"Powdery mildew appears as patches of white, a powdery substance or a fungus-like growth.\n"
        f"* In order to determine whether a cherry tree is infested with powdery mildew, individual leaves are collected"
        f"and examined. Visual criteria are used to detect powdery mildew.\n"
        f"This in order to save manual labour by doing a manual check of cherry trees individually.\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 images from collected samples from cherry trees, that are healthy,"
        f"as well as infested with powdery mildew."
    )
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/hebjornberg/mildew-detector/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf" 
        f" that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew."
        )