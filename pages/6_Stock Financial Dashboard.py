#yahoo_fin has 2 modules: stock_info and options
import yahoo_fin.stock_info as si
import pandas as pd
import streamlit as st
import datetime as dt

st.set_page_config(
    page_title="Financial Dashboard",
    layout = "wide"
)

hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

class Company:
    def __init__(self, ticker):
        price_df = si.get_data(ticker, dt.datetime.now() -
        dt.timedelta(days=365), dt.datetime.date(dt.datetime.now()))

        overview_df = si.get_stats(ticker)
        overview_df = overview_df.set_index('Attribute')
        overview_dict = si.get_quote_table(ticker)
        
        income_statement = si.get_income_statement(ticker)
       
        self.year_end = overview_df.loc['Fiscal Year Ends'][0]        
        self.market_cap = '$' % overview_dict['Market Cap']
        
        self.prices = price_df['adjclose']
        self.price_earnings_ratio = overview_dict['PE Ratio (TTM)']
        self.dividend_yield = overview_dict['Forward Dividend & Yield']
        if 'n/a' in self.dividend_yield.lower():
            self.dividend_yield = 'N/A'
        else:
            self.dividend_yield = '${}'.format(self.dividend_yield)
        
        self.sales = income_statement.loc['totalRevenue'][0]
        self.gross_profit = income_statement.loc['grossProfit'][0]
        self.ebit = income_statement.loc['ebit'][0]
        self.interest = income_statement.loc['interestExpense'][0]
        self.net_profit = income_statement.loc['netIncome'][0]
     
    def get_profit_margins(self):
        self.gross_margin = (self.gross_profit/self.sales)*100
        self.operating_margin = (self.ebit/self.sales)*100
        self.net_margin = (self.net_profit/self.sales)*100
        self.profit_margin_dict = {
            'Value':[self.gross_margin, self.operating_margin, self.net_margin]
            }    

st.write('#### Stock Financial Dashboard')
st.write('___')

ticker = st.text_input('Enter a stock ticker:', max_chars=5)
search = st.button('Search', key={ticker})

if search or ticker:
    company = Company(ticker)                
    company.get_profit_margins()        
        
    st.info(f"##### {si.get_quote_data(ticker)['shortName']}")
    st.write('##### Company Overview')

    company_info = si.get_company_info(ticker)
    st.markdown(company_info.loc['longBusinessSummary'][0], 
        unsafe_allow_html=True)
                
    col1, col2 = st.columns(2)
    with col1:
        overview_index = ['Market cap', 'P/E ratio', 'Dividend Yield']
        overview = {'Value':[company.market_cap, company.price_earnings_ratio,
            company.dividend_yield]}
        overview_df = pd.DataFrame(overview, index = overview_index)
            
        st.line_chart(company.prices)
        st.table(overview_df)            

    with col2:
        with st.expander('Profit margins (as of {})'.format(company.year_end), expanded=1):
            profit_margin_index = ['Gross margin', 'Operating margin', 'Net margin']
            profit_margin = [company.gross_margin, company.operating_margin, company.net_margin]
            profit_margin = { \
                'Value:', \
                ['{:.2f}'.format(company.gross_margin), \
                '{:.2f}'.format(company.operating_margin), \
                '{:.2f}'.format(company.net_margin)]}
            
            profit_margin_df = pd.DataFrame(profit_margin, index = profit_margin_index)
            st.table(profit_margin_df)
                
            profit_margin_df = pd.DataFrame(company.profit_margin_dict, index = profit_margin_index)
            st.bar_chart(profit_margin_df)                   
    
    #except:
        #st.write('\N{cross mark} Stock ticker not found!')
