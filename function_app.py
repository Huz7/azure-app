import azure.functions as func
import json

app = func.FunctionApp()


@app.route("hello", methods=["GET", "POST"])
def hello(req: func.HttpRequest) -> func.HttpResponse:
    """
    简单的Hello函数
    GET: /api/hello?name=World
    POST: /api/hello with {"name":"World"}
    """
    try:
        name = req.params.get('name')
        if not name:
            try:
                req_body = req.get_json()
                name = req_body.get('name')
            except ValueError:
                pass
        
        if name:
            return func.HttpResponse(json.dumps({"message": f"Hello, {name}!"}), mimetype="application/json")
        else:
            return func.HttpResponse(json.dumps({"error": "Please pass a name"}), status_code=400, mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(json.dumps({"error": str(e)}), status_code=500, mimetype="application/json")


@app.route("users/{user_id}", methods=["GET", "POST"])
def get_user(req: func.HttpRequest) -> func.HttpResponse:
    """
    处理用户相关请求
    GET /api/users/123
    POST /api/users/123 with JSON body
    """
    try:
        user_id = req.route_params.get('user_id')
        
        if req.method == "GET":
            return func.HttpResponse(
                json.dumps({"user_id": user_id, "name": "Demo User", "email": f"user{user_id}@example.com"}),
                mimetype="application/json"
            )
        
        if req.method == "POST":
            req_body = req.get_json()
            return func.HttpResponse(
                json.dumps({"status": "created", "user_id": user_id, "data": req_body}),
                status_code=201,
                mimetype="application/json"
            )
    except Exception as e:
        return func.HttpResponse(json.dumps({"error": str(e)}), status_code=500, mimetype="application/json")


@app.schedule_expression("0 */5 * * * *")
def timer_trigger(myTimer: func.TimerRequest) -> None:
    """定时触发器 - 每5分钟执行一次"""
    if myTimer.past_due:
        print('Timer is past due!')
    print(f'Timer trigger executed')
