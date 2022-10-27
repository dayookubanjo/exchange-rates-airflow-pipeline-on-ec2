# Foreign Exchange Rates Pipeline On Airflow

I've created this pipeline using Python, Airflow for orchestration deployed on AWS EC2 which extracts NGN exchange rates to GBP, EUR, USD, ETH, BTC, BNB, SOL, USDT and USDC from @naira_rates handle on twitter.

The tweet are cleaned and loaded into a s3 bucket for further transformations and analysis.