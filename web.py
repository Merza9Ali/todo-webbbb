import streamlit as st
import functions_corrected as fc


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write(todos, filepath)


filepath = "Activities.txt"
todos = fc.read(filepath)

st.title("Welcome in Python Al-Bahrain")
st.subheader("Seef Area")
st.write("Third floor")

for index, t in enumerate(todos):
    cb = st.checkbox(t, key=t)
    if cb:
        todos.pop(index)
        fc.write(todos, filepath)
        del st.session_state[t]
        st.rerun()

st.text_input(label="Text Test", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")
