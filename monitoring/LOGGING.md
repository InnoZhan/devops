## Logging

### Steps
- Create docker-compose with app, Promtail, Loki, Graphana containers
- Set them in the same network
- Create configuration for promtail
- Run "docker-compose up"
- Add "Loki" data source
- In the section "Explore" choose name of the container

### Best practices
Used:
- Set limit for logging file size
- Set new network instead of the default one
- Put custom labels on containers and images
