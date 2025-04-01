class CommonResponse:
    @staticmethod
    def success(data=None, message="操作成功"):
        return {
            "code": 200,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(code=500, message="操作失败", data=None):
        return {
            "code": code,
            "message": message,
            "data": data
        }