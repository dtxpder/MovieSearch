FROM node:18
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm cache clean --force \
    && npm install --legacy-peer-deps
COPY . .
CMD ["npm", "run", "dev"]
