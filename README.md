# on docker

## env

```
cp env_sample .env
```

## build

```
script/docker/build.sh
```

## execute

```
echo "export ON_DOCKER_UTILS_BIN=<path>/on-docker/bin/execute_on_host_os.sh" >> ~/.zshrc
source ~/.zshrc
bash script/sample.sh
```

