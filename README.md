# Super Simple Stock Market

This project includes part of the core functionality of a simple stock market.

Run `tests/test_story1.py` to test the functionality of following requirements:

- For a given stock,
    - Given any price as input, calculate the dividend yield
    - Given any price as input, calculate the P/E Ratio
    - Record a trade, with timestamp, quantity, buy or sell indicator and price
    - Calculate Volume Weighted St ock Price based on trades in past 5 minutes
- Calculate the GBCE All Share Index using the geometric mean of the Volume Weighted Stock Price for all stocks

## Project Structure

The project structure follows a Spring Boot like approach of separation of concerns: UI -- Controller -- Service --
Repository -- Storage. In this implementation the UI, Controller and Storage layers are left out completely.

Content of the project:

- `src/exception`: Contains custom exceptions.
- `src/model`: Contains models.
- `src/entity`: Contains entities stock and trade.
- `src/service`: Contains the business logic implementation.
- `src/repositoy`: Contains the data access layer implementation.
- `tests`: `test_story1.py` integration test for requirements. Other files are classical unit tests.

## Assumptions made:

- Fixed dividends only occur in stocks with type preferred.
- The formula to calculate the P/E Ratio is unclear regarding the `Dividend` variable. This project
  uses `Last Dividend`.
- All calculations are rounded to 5 digits.
- One stock can only exist once.
- If a database exist, stocks and trades would have a one-to-many relationship. The table trade would include stock ids
  as foreign keys. 