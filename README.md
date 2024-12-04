# rProxy

A reverse proxy to deliver my SaaS. Currently on development.

# REMEMBER

For production you need to create the SaaS network before the containers, so it persist even when the
containers shut down. Use this command: `docker network create --driver bridge saas-network`
