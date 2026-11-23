FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./

COPY index.html *.js *.css *.svg ./
COPY images ./images
COPY public ./public

RUN npm install \
    && npm install -g serve \
    && npm run build \
    && rm -fr node_modules
    

EXPOSE 4000


CMD ["serve", "-s", "dist", "-l", "4000"]