# Docker image for hands-on

This is a Docker image which contains libraries/softwares to run the hands-on programs.

The image is pre-installed with

- Python 3.7
- node.js 12.0
- AWS CLI
- AWS CDK

## Launching the container in an interactive mode

```bash
docker run -it registry.gitlab.com/tomomano/intro-aws:latest
```

Once launched, download the latest hands-on code from GitLab:

```bash
git clone https://gitlab.com/tomomano/intro-aws.git
```

Then, `cd` into the `handson` directory, and run the programs. Have fun!
