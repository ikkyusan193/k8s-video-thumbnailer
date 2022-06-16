FROM node:16-alpine as builder
## Stage 1: Build the frontend

ARG APP_BASEPATH
ENV APP_BASEPATH=${APP_BASEPATH}

CMD mkdir /app
WORKDIR /app

COPY ./frontend/package.json ./
COPY ./frontend/package*.json ./
COPY ./frontend/yarn.lock ./

RUN yarn install

COPY ./frontend ./

RUN yarn build

# Second stage, use nginx to serve files that have been built
# alpine is a small footprint linux image
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html/dist
COPY  ./frontend/default.conf /etc/nginx/conf.d

# EXPOSE 8080 80
# CMD ["nginx","-g","daemon off;"]



