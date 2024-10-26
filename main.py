import streamlit as st


def main():
    home_page = st.Page("home.py", title="Home", icon=":material/home:")
    op_amp_page = st.Page("electronics/op_amp.py", title="Op Amp", icon=":material/add_circle:")
    sorting_page = st.Page("algorithms/sorting.py", title="Sorting Algorithms", icon=":material/add_circle:")

    pg = st.navigation([home_page, op_amp_page, sorting_page])
    pg.run()


if __name__ == '__main__':
    main()
