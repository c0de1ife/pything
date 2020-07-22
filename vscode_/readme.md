# vscode 配置相关

## launch.json
最近开发环境从 `idea` 转为 `vscode` ，发现默认的运行方式没法像 `idea` 那样在任意子目录正确导入 `package` 。
查阅资料后发现是 `PYTHONPATH` 的问题，虽然 `vscode` 也有 `pythonPath` 配置项，但是和这个意义不同，正确的配置应该是 `env.PYTHONPATH`。
为了以后不踩坑，记录一下。  
另外提供配置好的 [launch.json](launch.json)

## settings.json
最近把通过 `vscode` 的 `Remote Development` 插件把开发环境从 `Windows` 中迁移到了 `Centos` ，发现 `python` 的代码跳转和提示功能消失了，
经过排查，发现是 `settings.json` 少配了 `python.autoComplete.extraPaths`，可用的 `settings.json` 文件如下：
```json
{
    "python.pythonPath": "/usr/bin/python",
    "python.autoComplete.extraPaths":[
        "/usr/lib/python2.7/site-packages"
    ]
}
```
