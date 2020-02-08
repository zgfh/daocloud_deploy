#daocloud_deploy
发布 daocloud 应用

### 参数
DAOCLOUD_APITOKEN daocloud api token
DAOCLOUD_APPNAME 应用名，发布多个用',' 隔空，如："app1,app2"
DAOCLOUD_APP_RELEASE 镜像版本

### build
```bash
docker build -t daocloud_deploy .
```

### run
更新应用app1 的镜像版本到v1版本 （xxx 是daocloud的api token）

```bash
docker run -e DAOCLOUD_APITOKEN=xxx -e DAOCLOUD_APPNAME=app1 -e DAOCLOUD_APP_RELEASE=v1 daocloud_deploy
```
