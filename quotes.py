import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('div', class_='quote')[:10]  # Limit to the first 10 quotes
    data = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        data.append({
            'author': author,
            'text': text,
            'tags': tags
        })
    return data

def main():
    st.title("Quote Scraper")
    st.subheader("Scraping data from 'https://quotes.toscrape.com/'")
    st.write("Click the button below to scrape quotes:")
    if st.button("Scrape Quotes"):
        quotes = scrape_quotes()
        st.subheader("Scraped Quotes:")
        for quote in quotes:
            st.write(f"Author: {quote['author']}")
            st.write(f"Quote: {quote['text']}")
            st.write(f"Tags: {', '.join(quote['tags'])}")
            st.write("----")

if __name__ == '__main__':
    main()
