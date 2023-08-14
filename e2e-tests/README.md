# E2E Test Automation

## Automated Test Plan

The objective is to provide an overall vision of the test automation for the system/e2e-tests.

### Flows to be tested

- Search for existing GitHub user with at least 1 repo

### Flows that won't be tested

- Search with non-existing GitHub user

### Assumptions

- Website available to run the tests
- Web browser to run the tests
- GitHub's user at least 1 repo

### Test specifications

[Link](../testable-flows.md)

## Test Automation

### Solution

- Programming language: [Python 3.10](https://www.python.org/)
- Test runner: [pytest](https://docs.pytest.org/en/6.2.x/)
- Webdriver: [Selenium Webdriver](https://www.selenium.dev/)
- Reports: [pytest-html](https://pypi.org/project/pytest-html/)
- Containers: [Docker](https://www.docker.com/)
- CI/CD: GitHub actions pipelines

### Prerequisites

- Git
- Python 3.10
- pip3
- Firefox
- Chrome
- Geckodriver
- Docker
- Docker-compose

### Approaches

1. Automate only the main critical flows
2. Run the automated tests using docker
3. Develop using Firefox in local environment
4. The tests were written using DAMP principle instead of DRY. For more information, please, read [here](https://enterprisecraftsmanship.com/posts/dry-damp-unit-tests/)

## How to run the tests

### Configuration

1. Run the app. Please, follow the [app setup](../setup.md) file.
2. Set up the selenium grid with the nodes  
- Run the selenium grid and their nodes
```Command
# folder qa-automation-coding-challenge
docker-compose -f e2e-tests/docker/docker-compose.yml up -d
```
- Monitor the test execution locally at ***<http://localhost:4444/ui/index.html#/>***

### Testing with docker

1. Run the tests
```commandline
# folder e2e-tests
pytest
```

### Testing with docker compose

1. Set up the infrastructure:

```Command
# folder qa-automation-coding-challenge
docker-compose -f e2e-tests/docker/docker-compose.yml up -d --build
```

2. Running the tests:

```Command
# folder qa-automation-coding-challenge
docker-compose -f e2e-tests/docker/docker-compose.yml up --build e2e-tests
```

### Repo Structure

├── **docker**\ docker and/or docker-compose definition(s)  
├── **src**\  
├──── **pages**\ pages objects definitions  
├──── **resources**\ static test data  
└──── **tests**\ automated test scripts

### TODOs

- Add test reports for the GitHub actions jobs