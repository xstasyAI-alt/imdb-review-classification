from time import sleep, time

import pandas as pd
import streamlit as st
from joblib import load

from common.preprocess_text import preprocess_text

df_test = pd.read_csv("data/test.csv", nrows=10)

model = load("models/clf.joblib")

st.write("# Movie Review Classifier")


def classify_text(text: str):
    text = preprocess_text(text)
    with st.spinner("Let me guess..."):
        sleep(1)
    start_time = time()
    pred = model.predict_proba([text])[0]
    print(time() - start_time)
    st.success("Done!")
    return {"text": text, "pred": pred}


input_container = st.container()
input_container.title("Input")

output_container = st.container()
output_container.title("Output")


def print_output():

    text = st.session_state.get("text_in")
    pred = classify_text(text)
    output_container.write(pred)


# input_container.selectbox(
#     "Select an example",
#     (df_test["review"][i] for i in range(5)),
#     key="text_in",
#     on_change=print_output,
# )

input_container.text_input(
    "Enter something",
    placeholder="The movie was so good, etc.",
    on_change=print_output,
    key="text_in",
)
