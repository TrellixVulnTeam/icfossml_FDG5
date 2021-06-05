import pandas as pd
import streamlit as st
import pickle


def main():
    ratings = open('cleaned_data/ratings', 'rb')
    price = open('cleaned_data/price', 'rb')
    review = open('cleaned_data/review', 'rb')

    x = pickle.load(ratings)
    y = pickle.load(price)
    z = pickle.load(review)

    x.to_frame()
    y.to_frame()
    z.to_frame()

    x.plot(kind='bar')
    st.pyplot()

    



if __name__ == '__main__':
    main()


