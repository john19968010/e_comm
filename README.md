## 開發流程

### 前置設定
- 開啟新專案
django-admin e_commerce 

- 建立auto format 的設定擋
mkdir .vscode 
cd / .vscode
touch settings.json 
touch .flake8


- 撰寫Dockerfile & docker-compose.yml 
touch Dockerfile
touch docker-compose.yml

- 利用pipenv下載package
(pipenv 套件管理工具)
https://medium.com/citycoddee/python-%E5%B7%A5%E5%85%B7%E7%AE%B1-1-%E5%B0%88%E6%A1%88%E5%BF%85%E5%82%99-pipenv-a517e292f6c

- 創建不同env
mkdir env
cd /env
touch prod.env && touch dev.env



## 操作流程

### 下載docker & docker-compose 
- Download them, depend on your system's way

## Initial
```bash
git clone .....
cd e_commerce
docker build -t e_comm/be:prod .
```

### 啟動containter 
```bash
docker-compose -f docker-compose.yml up -d
```
