docker build -t dx29-termsearch2:latest .

# Push image to ACR
az acr login --name <acr_name>
docker tag dx29-termsearch2:latest <acr_server>/dx29-termsearch2:<image_tag>
docker push <acr_server>/dx29-termsearch2:<image_tag>

# Run
docker run --rm -p 8080:8080 dx29-termsearch2:latest
docker run --rm -p 8080:8080 -it -m 1.5g --cpus 1.0 dx29-termsearch2:latest
