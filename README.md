# rProxy

A reverse proxy to deliver my SaaS through https. Currently on development.

## Guide

1. Before initializing the compose file, we need to initialize a docker network,
   so the connection betweem services persist. This is
   done through+ `docker network create --driver bridge example-network`
2. For a brand new VPS or a VPS without SSL certificates, you need to make de
   proxy deployment in two steps:
   1. preSSL: Run the compose ngingx configuration for http traffic on port 80.
      _this is only used to get the certbot acme-challenge and pull the
      SSL certificates_. Theres no https redirection nor SSL certificates
      configuration. Run the compose command without the detach mode,
      so you can confirm that SSL certificates were succesfully pulled.
   2. After the SSL certificates were pulled, shut down the preSSL compose file.
   3. postSSL: Run the compose nginx configuration for http traffic on port 80.
      _this is only used to renew the SSL certificates,
      it also enforces https on http traffic_ and https traffic
      on port 443 to serve the SaaS. It will use the SSL certificates pulled with
      the past configuratio
3. I had a lot of problems while trying to deploy https on the VPS in a single
   step. This is currenlty the easistes way I have found with Nginx.
4. Ive tried to implement named volumes in the compose files, this didnt work
   since letsencrypt looks for these specific paths:
   `/etc/letsencrypt`: Used to store SSL certificates.
   `/var/www/certbot`: Used to store the acme-challenge.
5. Current implemenation does the certificate renowal through crontab:
   `crontab -e`
   `0 5 1 */2 *  /usr/bin/docker compose -f /var/docker/docker-compose.yml up certbot`
6. Original command _that did not work_ was:
   ```
   >
   sh -c "trap exit TERM; mkdir -p /var/www/html/.well-known/acme-challenge && while :; do
   sleep 6h & wait $${!};
   certbot certonly --webroot -w /var/www/html
   -d yamdynamics.dev --non-interactive --agree-tos --register-unsafely-without-email;
   done"
   ```

## Pendings

1.  SSL certificates need to be manually renewed
2.  Change the name of pre-containers and post-containers so you dont need to rm
    them
