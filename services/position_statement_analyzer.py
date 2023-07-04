from utils.mapping import ticker_mapping
import streamlit as st
import pandas as pd


class PositionStatementAnalyzer:

    def __init__(self, position_statements, eod_prices):
        self.position_statements = position_statements
        self.eod_prices = eod_prices

    @staticmethod
    def calculate_percentage_change(mtm_price, close_price):
        """
        Calculate and return the percentage change between mtm_price and close_price.
        """
        return round((mtm_price - close_price) / close_price * 100, 2) if close_price != 0 else 0
    
    @staticmethod
    def santize_ticker(ticker_id):
        """
        Sanitize and return the ticker_id.
        """
        try:
            ticker_id_formatted = ticker_mapping.get(ticker_id, ticker_id)
            if ticker_id_formatted is None:
                return None
            if ticker_id_formatted not in ["BRK-B.US"]:
                ticker_id_formatted = ticker_id_formatted.replace('_', '.').replace('-', '.').replace(' ', '.')
            return ticker_id_formatted
        except Exception as e:
            return None

    def run(self, date, asset_class, client_name, custodian_name, threshold):
        """
        Run the analyzer and display the results using Streamlit.
        """
        position_records = self.position_statements.get_records(date, asset_class, client_name, custodian_name)
        
        significant_changes = []
        not_found_tickers = []
        for record in position_records:
            security_id = record[0]
            mtm_price = record[1]
            security_id = self.santize_ticker(security_id)
            eod_price = self.eod_prices.get_records(date, security_id)
            
            if eod_price != 0:
                difference = self.calculate_percentage_change(mtm_price, eod_price)
                if abs(difference) >= threshold:
                    significant_changes.append((security_id, mtm_price, eod_price, difference))
            else:
                not_found_tickers.append((security_id, mtm_price, eod_price, 0))

        
        st.title("Significant Changes")
        df = pd.DataFrame(significant_changes, columns=["Security ID", "MTM Price", "Close Price", "Difference"])
        st.dataframe(df, use_container_width=True)

        st.title("Not Found Tickers")
        df = pd.DataFrame(not_found_tickers, columns=["Security ID", "MTM Price", "Close Price", "Difference"])
        st.dataframe(df, use_container_width=True)