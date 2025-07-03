# AI-Assisted DevOps Side Project

## 專案目的
- 利用 Copilot 加速 DevOps 工具與文件的產出效率
- 減少 YAML、Shell撰寫錯誤率
- 實作可快速部署、文件齊全的工作流程

## 專案結構說明
- `ansible/`：Ansible playbooks（如部署到遠端主機）
- `app/`：Flask app 主程式
- `db/`：MySQL 資料庫初始化
- `nginx/`：Nginx 配置檔
- `docs/`：部署說明書
- `docker-compose.yml`：Docker Compose 配置檔 (Flask + MySQL + Nginx)
- `Dockerfile`：Flask app Dockerfile (Install dependencies)

## 使用方式
1. 開啟任一目錄下檔案 → 輸入註解（prompt）
2. 接受 Copilot 提示補全內容
3. 手動驗證 / 修正後儲存結果

## 成效評估（摘要）
- 撰寫時間平均縮短 50% 以上
- 初學者錯誤率明顯下降
- 文件一致性與可維護性提升

## 延伸應用建議
- 導入 GitHub Actions 建立 CI/CD pipeline
- 增加 pytest 撰寫 API 測試、自動驗證部署結果
- 轉為 Kubernetes 架構，搭配 Copilot
