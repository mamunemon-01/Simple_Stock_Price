import yfinance as yf
import streamlit as st
import pandas as pd

# following method shows texts using markdown
st.write("""
	# Stock Price of Google
	This web app shows prices and volume of sales of Google stock.
""")

# a variable from yfinance
tickerSymbol='GOOGL'

tickerData = yf.Ticker(tickerSymbol)

# a dataframe
tickerDF = tickerData.history(period='id', start='2022-04-17', end='2023-04-17')

st.line_chart(tickerDF.Close)# shows closing prices
st.line_chart(tickerDF.Volume)# shows volume of sales