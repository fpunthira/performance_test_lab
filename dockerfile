FROM node:12

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
RUN npm install -g artillery --ignore-scripts

WORKDIR /home/node/app
COPY package*.json ./

USER node
RUN npm install

COPY . .
RUN chown -R node:node /home/node/app

EXPOSE 3000

CMD [ "node", "app.js" ]