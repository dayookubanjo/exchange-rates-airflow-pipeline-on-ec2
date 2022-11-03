# Foreign Exchange Rates Pipeline On Airflow

I've created this pipeline using Python, Airflow for orchestration deployed on AWS EC2 which extracts NGN exchange rates to GBP, EUR, USD, ETH, BTC, BNB, SOL, USDT and USDC daily from @naira_rates handle on twitter.

The tweets are cleaned and loaded into a s3 bucket for further transformations and analysis.s

I've used AWS Glue to crawl the s3 bucket to infers schema on the data to make it available via Athena for querying with SQL and QuickSight dashboard to see fluctuations in exchange rates.
