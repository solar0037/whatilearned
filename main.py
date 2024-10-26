import streamlit as st
from st_pages import get_nav_from_toml


def main():
    st.set_page_config(layout="wide")
    nav = get_nav_from_toml(".streamlit/pages_sections.toml")
    pg = st.navigation(nav)
    pg.run()


if __name__ == '__main__':
    main()
