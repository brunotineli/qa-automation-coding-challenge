# Tests


## Tests based on the requirements

The focus here is to cover every acceptance criteria item.

Scenarios:
1. *Required page elements: page title, search input, search button, and search result section
1. *User flow for successful search results: 0 repo, 1 repo, N repos, and reports w/o description
1. *User flow for failure search results: user not found and unexpected error like network issues

*Highest priority scenarios because they are related to the core feature of the application

## Tests based on exploratory testing

The focus here is to explore based on the continuous usage of the application

Sessions with the help of the test heuristics:
1. Input data: empty, too short, too big, special chars, etc.
1. Multibrowser: Firefox and Chrome
1. Responsiveness: different browser windows sizes
1. Multidevices: test on Desktop and Mobile browsers
1. Non-functional insights: run LightHouse for performance and accessibility insights

# Test Strategy

## Unit Tests

The unit tests will cover mainly the page elements and form submit event in order to keep the page behavior

## System Tests

The system tests will cover the user flow mainly the search flows and their results.