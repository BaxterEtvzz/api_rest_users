local-build: 
 docker compose build
local-build-cache: 
 docker compose build --no-cache
local-up: 
 docker compose up
local-up-cache: 
 docker compose up --build