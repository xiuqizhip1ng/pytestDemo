import allure
import pytest
from common.logger import logger
from operation.user import login_erp_user
from testcases.conftest import login_data


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():

    @allure.story("用例--登录用户")
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             login_data["test_login_user"])
    def test_login_user(self,base_url, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_erp_user(base_url,username, password)
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.get("code")))
        print(result.response)
        assert result.status_code == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_login_erp.py"])
