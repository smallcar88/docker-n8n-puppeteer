
## How to build custom `n8n-puppeteer`

### Create ssh key pairs to pull the private github 
Create ssh keys on `./ssh_keys` folder
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### Build Custom Windows n8n Docker
```
docker buildx build `
    --squash `
    --build-arg TARGETPLATFORM=linux/amd64 `
    --build-arg N8N_VERSION={LATEST} `
    -t n8n-puppeteer .
```