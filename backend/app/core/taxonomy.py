from enum import Enum


class JobArchtype(str, Enum):
    APPLIED__ENERGY_ANALYTIC = "Applied Energy Analytic"
    ENERGY_MARKET_MODELLING = "energy_market_modelling"
    DECISION_SUPPORT_CONSULTING = "decision_support_consulting"
    DATA_METHODS_INFO_MGMT = "data_methods_and_information_management"
    DATA_ENGINEERING_ENERGY = "data_engineering_energy"
    QUANT_FINANCE_TRADING = "quantitative_finance_trading"
    COMMODITIES_SALES_MARKETS = "commodities_sales_markets"