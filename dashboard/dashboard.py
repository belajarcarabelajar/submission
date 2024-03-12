import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data using the updated caching mechanism
@st.cache_data
def load_data():
    data = pd.read_csv('all_data.csv')
    return data

data = load_data()

# Sidebar - setup
st.sidebar.header('E-Commerce Public Dataset')
visualization = st.sidebar.selectbox('Select a visualization:', ['Top 3 Most Sold Products', 'Top 5 Cities by Number of Orders'])

# Main - setup
st.title(' E-Commerce Public Dataset by Olist')

if visualization == 'Top 3 Most Sold Products':
    # Data for top 3 most sold products
    top_products = data['product_category'].value_counts().head(3)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_products.index, y=top_products.values, palette='viridis')
    plt.title('Top 3 Most Sold Products', fontsize=16)
    plt.xlabel('Product Category', fontsize=14)
    plt.ylabel('Number of Products Sold', fontsize=14)
    plt.xticks(rotation=45)
    
    # Display the plot
    st.pyplot(plt)

elif visualization == 'Top 5 Cities by Number of Orders':
    # Data for cities with the highest number of orders
    top_cities = data['customer_city'].value_counts().head(5)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_cities.values, y=top_cities.index, palette='coolwarm')
    plt.title('Top 5 Cities by Number of Orders', fontsize=16)
    plt.xlabel('Number of Orders', fontsize=14)
    plt.ylabel('City', fontsize=14)
    
    # Display the plot
    st.pyplot(plt)

st.caption('Copyright © Iwan Kurniawan 2024')