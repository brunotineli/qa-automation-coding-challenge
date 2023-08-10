# App Setup

## Prerequisites

- Node 16.x installed
- Yarn
- docker
- docker compose

## Run the app locally
1. Fork and clone the repository.
2. At the root directory of the repo, install dependencies by running `yarn` (if needed, [install yarn first](https://yarnpkg.com/getting-started))
3. Run the app by running `yarn start`

You can add more scripts (or change existing ones) in the [`package.json`](./package.json) file.

## Run the app with docker

``` terminal
# folder qa-automation-coding-challenge
docker build -t app .
docker run -p 3000:3000 app
```