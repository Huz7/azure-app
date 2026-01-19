# Azure Functions Python Demo

基于Python 3.10的Azure函数应用演示项目。

## 项目结构

```
.
├── function_app.py          # Azure函数应用主文件
├── requirements.txt         # Python依赖
├── host.json               # Azure Functions配置
├── local.settings.json     # 本地开发设置
└── .gitignore              # Git忽略文件
```

## 快速开始

### 1. 环境准备

```bash
# 安装Python 3.10+
python3 --version

# 安装Azure Functions Core Tools
brew tap azure/tap
brew install azure-functions-core-tools@4

# 克隆此仓库
git clone <your-repo-url>
cd demo

# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 本地运行

```bash
# 启动函数应用
func start
```

函数将在以下地址可用：
- `http://localhost:7071/api/hello`
- `http://localhost:7071/api/users/{user_id}`

### 3. 测试API

```bash
# 测试Hello函数
curl "http://localhost:7071/api/hello?name=World"

# POST请求
curl -X POST http://localhost:7071/api/hello \
  -H "Content-Type: application/json" \
  -d '{"name":"Azure"}'

# 获取用户信息
curl "http://localhost:7071/api/users/123"
```

## 上传到GitHub

### 1. 创建GitHub仓库

在GitHub上创建新仓库（不初始化README）

### 2. 推送代码

```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git branch -M main
git push -u origin main
```

## 部署到Azure

### 1. 创建Azure资源

```bash
# 登录
az login

# 创建资源组
az group create --name myResourceGroup --location eastus

# 创建存储账户
az storage account create \
  --name myfunctionstg \
  --resource-group myResourceGroup \
  --sku Standard_LRS

# 创建函数应用
az functionapp create \
  --resource-group myResourceGroup \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.10 \
  --functions-version 4 \
  --name myFunctionApp \
  --storage-account myfunctionstg
```

### 2. 连接GitHub部署

```bash
# 在Azure门户中：
# 函数应用 > 部署中心 > 来源 > GitHub > 授权 > 选择仓库和分支

# 或使用命令行
az functionapp deployment source config-github \
  --resource-group myResourceGroup \
  --name myFunctionApp \
  --repo-url https://github.com/YOUR-USERNAME/YOUR-REPO \
  --branch main
```

推送到GitHub的main分支时会自动部署。

## 环境变量

编辑 `local.settings.json` 配置本地环境：

```json
{
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "FUNCTIONS_WORKER_RUNTIME_VERSION": "3.10"
  }
}
```

## 参考资源

- [Azure Functions Python文档](https://docs.microsoft.com/zh-cn/azure/azure-functions/)
- [Azure CLI命令参考](https://docs.microsoft.com/zh-cn/cli/azure/)
- [Azure Functions本地调试](https://docs.microsoft.com/zh-cn/azure/azure-functions/functions-develop-local)
