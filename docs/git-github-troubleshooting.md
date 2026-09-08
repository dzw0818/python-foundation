# Git + GitHub 访问故障排查备忘（国内网络）

今天（2026-09-08）踩过的坑与解决办法，下次遇到直接照做。

## 坑 1：无法连接 GitHub（port 443 超时）

```
fatal: unable to access 'https://github.com/...': Failed to connect to github.com port 443
```

**原因**：GitHub 在国内直连不稳定，需要走本地代理。

**排查**：先确认代理软件在跑，并找到端口（Clash 类一般是 7890 / 7897）：

```bash
netstat -ano | findstr LISTENING | findstr "7897"
```

**解决**（仓库级，只对当前项目生效）：

```bash
git config http.proxy http://127.0.0.1:7897
git config https.proxy http://127.0.0.1:7897
```

想让所有项目都走代理（全局）：

```bash
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897
```

关掉代理软件后 git 会连不上，需撤销：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 坑 2：推送被拒 403（Permission denied）

```
remote: Permission to dzw0818/python-foundation.git denied to dzw0818.
fatal: ... The requested URL returned error: 403
```

**原因**：GitHub 不接受账号密码推送；旧 token 没有 `repo` 权限也会 403。

**解决**：
1. 删除 Windows 凭据管理器里旧的 GitHub 凭据：
   - GUI：Win 键 → 凭据管理器 → Windows 凭据 → 删除 `git:https://github.com`
   - 或命令行：`cmdkey /list | findstr github` → `cmdkey /delete:git:https://github.com`
2. 启用凭证管理器，重新授权（浏览器登录最省事）：

```bash
git config --global credential.helper manager
git push -u origin main   # 会弹出浏览器授权窗口
```

3. 或者手动建新 token：GitHub → Settings → Developer settings → Personal access tokens（classic）→ 勾选 `repo` → 推送时 Username 填用户名，Password 粘贴 token。
4. 顺手在 GitHub 网页删掉旧 token，避免误用。

## 坑 3：HTTP/2 报错（stream not closed cleanly）

```
fatal: ... HTTP/2 stream 1 was not closed cleanly before end of the underlying stream
```

**原因**：代理网络下 HTTP/2 连接被中途掐断，常见于国内网络。

**注意**：这经常是**假失败**——数据可能已经传完。先对比本地和远程是否一致：

```bash
git rev-parse HEAD            # 本地提交号
git ls-remote origin refs/heads/main   # 远程提交号
```

一致 = 已经推送成功，无需任何操作。

**解决（强制 HTTP/1.1，一劳永逸）**：

```bash
git config http.version HTTP/1.1
```

## 日常提交命令速记

```bash
git add .
git commit -m "feat: 描述本次改动"
git push
```

提交信息规范：`feat` 新功能 / `fix` 修 bug / `docs` 文档 / `chore` 杂务 / `refactor` 重构。
