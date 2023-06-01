import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('div', class_='quote')[:10]  # Limit to the first 10 quotes
    data = []
    tags = set()  # Create a set to store unique tags
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quote_tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        tags.update(quote_tags)  # Add tags to the set
        data.append({
            'author': author,
            'text': text,
            'tags': quote_tags
        })
    top_tags = [tag for tag in tags if tag in ['love', 'inspirational', 'life', 'reading', 'books', 'simile', 'truth', 'friendship']][:10]
    return data, top_tags

def main():
    st.title("Quote Scraper")
    st.subheader("Scraping data from 'https://quotes.toscrape.com/'")
    st.write("Click the button below to scrape quotes and tags:")
    if st.button("Scrape Quotes and Tags"):
        quotes, tags = scrape_quotes()
        st.subheader("Scraped Quotes:")
        for quote in quotes:
            st.write(f"Author: {quote['author']}")
            st.write(f"Quote: {quote['text']}")
            st.write(f"Tags: {', '.join(quote['tags'])}")
            st.write("----")
        st.subheader("Top Tags:")
        for tag in tags:
            st.write(tag)

if __name__ == '__main__':
    main()
