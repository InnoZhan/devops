# Best practices for docker

## Linters

For dockerfile i have used [linker](https://hadolint.github.io/hadolint/)
to check markdown format

## Multistage build

Build app on one stage and use it in other to save image size

## Rootless containers

Used new user to limit access and improve security
