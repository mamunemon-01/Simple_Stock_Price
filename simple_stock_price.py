import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, timedelta

# following method shows texts using markdown
st.write("""
	# Stock Price of Google
	This web app shows prices and volume of sales of Google stock in the last 1 year (365 days) period.
""")

# a variable from yfinance
tickerSymbol='GOOGL'

tickerData = yf.Ticker(tickerSymbol)

# today's date
current_date = date.today()

one_year_ago_date = current_date - timedelta(days = 365)

# a dataframe
tickerDF = tickerData.history(period='id', start = one_year_ago_date, end = current_date)#start='2022-04-17', end='2023-04-17')

st.line_chart(tickerDF.Close)# shows closing prices
st.line_chart(tickerDF.Volume)# shows volume of sales