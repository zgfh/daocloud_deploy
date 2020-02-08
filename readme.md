#daocloud_deploy
发布 daocloud 应用



### build
```bash
docker build -t daocloud_deploy .
```

### run
更新应用test 的镜像版本到v1版本 （xxx 是daocloud的api token）

```bash
docker run -e DAOCLOUD_APITOKEN=xxx -e DAOCLOUD_APPNAME=test -e DAOCLOUD_APP_RELEASE=v1 daocloud_deploy
```
