# vscode 配置相关

## launch.json
最近开发环境从 `idea` 转为 `vscode` ，发现默认的运行方式没法像 `idea` 那样在任意子目录正确导入 `package` 。
查阅资料后发现是 `PYTHONPATH` 的问题，虽然 `vscode` 也有 `pythonPath` 配置项，但是和这个意义不同，正确的配置应该是 `env.PYTHONPATH`。
为了以后不踩坑，记录一下。  
另外提供配置好的 [launch.json](vscode_/launch.json)
