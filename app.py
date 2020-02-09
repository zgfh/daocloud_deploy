#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 16/3/5 上午1:43
"""
import requests
import os


class dao_api():

    def __init__(self, token):
        self.__token__ = token
        self.__base_url__ = 'https://openapi.daocloud.io/v1'

    def set_token(self, wechat_open_id):
        # TODO  get token with source(wechat openId)
        token = ''
        self.__token__ = token

    def build_flows(self):
        return requests.get(self.__base_url__ + '/build-flows',
                            headers={"Authorization": "token " + self.__token__}).json()

    def build_flow_by_name(self, name):
        tmp_build_flows = requests.get(self.__base_url__ + '/build-flows',
                                       headers={"Authorization": "token " + self.__token__}).json()
        result_build_flows = []
        for tmp_build_flow in tmp_build_flows['build_flows']:
            if name in tmp_build_flow['name'].encode("utf-8"):
                result_build_flows.append(tmp_build_flow)
        return {'build_flows': result_build_flows}

    def build_flow(self, id):
        return requests.get(self.__base_url__ + '/build-flows/' + str(id),
                            headers={"Authorization": "token " + self.__token__}).json()

    def build_flow_rebuild(self, id):
        # TODO
        return 'dao api developing'

    def apps(self):
        return requests.get(self.__base_url__ + '/apps', headers={"Authorization": "token " + self.__token__}).json()

    def app_by_name(self, name):
        tmpapps = requests.get(self.__base_url__ + '/apps', headers={"Authorization": "token " + self.__token__}).json()
        result_apps = []
        for tmpapp in tmpapps['app']:
            if name == tmpapp['name']:
                result_apps.append(tmpapp)
        return {'app': result_apps}

    def app(self, id):
        return requests.get(self.__base_url__ + '/apps/' + str(id),
                            headers={"Authorization": "token " + self.__token__}).json()

    def app_start(self, id):
        return requests.post(self.__base_url__ + '/apps/' + str(id) + '/actions/start',
                             headers={"Authorization": "token " + self.__token__}).json()

    def app_stop(self, id):
        return requests.post(self.__base_url__ + '/apps/' + str(id) + '/actions/stop',
                             headers={"Authorization": "token " + self.__token__}).json()

    def app_restart(self, id):
        result = requests.post(self.__base_url__ + '/apps/' + str(id) + '/actions/restart',
                               headers={"Authorization": "token " + self.__token__}).json()

    def app_redeploy(self, id, release_name):
        return requests.post(self.__base_url__ + '/apps/' + str(id) + '/actions/redeploy',
                             json={"release_name": release_name},
                             headers={"Authorization": "token " + self.__token__}).json()

    def actions(self, id, action_id):
        return requests.get(self.__base_url__ + '/apps/' + str(id) + '/actions/' + str(action_id),
                            headers={"Authorization": "token " + self.__token__}).json()


if __name__ == '__main__':
    import os
    import time

    DAOCLOUD_APITOKEN = os.getenv('DAOCLOUD_APITOKEN', "x")
    DAOCLOUD_APP_NAME_STR = os.getenv('DAOCLOUD_APP_NAME', "x")
    DAOCLOUD_APP_RELEASE = os.getenv('DAOCLOUD_APP_RELEASE', "x")
    for DAOCLOUD_APP_NAME in DAOCLOUD_APP_NAME_STR.split(','):
        start_time = time.time()
        daoapi = dao_api(DAOCLOUD_APITOKEN)
        app = daoapi.app_by_name(DAOCLOUD_APP_NAME)
        print("find app %s", app)
        app_redeploy_result = daoapi.app_redeploy(app['app'][0]['id'], DAOCLOUD_APP_RELEASE)
        print("app_redeploy result:", app_redeploy_result)
        if 'action_id' not in app_redeploy_result:
            exit(1)
        for i in range(1, 15):
            result = daoapi.actions(daoapi.app_by_name(DAOCLOUD_APP_NAME)['app'][0]['id'],
                                    app_redeploy_result['action_id'])
            print("app_redeploy result:", result)
            if result['state'] == 'success':
                print("app_redeploy success: %s s", time.time() - start_time)
                break
            time.sleep(5)
