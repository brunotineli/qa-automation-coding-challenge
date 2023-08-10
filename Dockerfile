# Configure
FROM node:lts
WORKDIR /app

# Install
COPY . .
RUN yarn install --frozen-lockfile


# Run
EXPOSE 3000
CMD [ "yarn", "start" ]