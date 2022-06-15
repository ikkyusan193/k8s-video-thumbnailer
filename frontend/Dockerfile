FROM node:16 as builder
## Stage 1: Build the frontend

CMD mkdir /app

## Set the working directory
WORKDIR /app

## Copy the package specifications
COPY ./frontend/package.json ./

## Install all relevant dependencies
RUN npm install

## Copy all the relevant files + source code
COPY ./frontend ./

## Carry out the build
RUN npm run build


## Second stage, use nginx to serve files that have been built
## alpine is a small footprint linux image
FROM nginx:1.21-alpine   
COPY default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html/

EXPOSE 8080
        
CMD ["nginx","-g","daemon off;"]



