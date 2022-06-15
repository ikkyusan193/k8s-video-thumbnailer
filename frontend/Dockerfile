FROM node:16-alpine as builder
## Stage 1: Build the frontend

CMD mkdir /app
WORKDIR /app

COPY ./frontend/package.json ./

RUN npm install

COPY ./frontend ./

RUN npm run build

# Second stage, use nginx to serve files that have been built
# alpine is a small footprint linux image
FROM nginx:alpine

COPY  ./frontend/default.conf /etc/nginx/conf.d
COPY --from=builder /app/dist /usr/share/nginx/html/

# EXPOSE 8080 80
# CMD ["nginx","-g","daemon off;"]



