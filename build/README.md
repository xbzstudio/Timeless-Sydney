# 打包说明

- 前置条件
  - 打包工具为 pyinstaller，建议打包时单独开一个虚拟环境，避免导入过多不必要的库
  - 需要根目录有 release 目录
  - 需要 static/images 目录中有 my-sydney.ico 文件
- 运行完成后会在 release 目录下生成 newbing-sydney 目录
- 在 newbing-sydney 目录中
  - cookie.json 需要填入自己的 cookie
  - newbing-sydney.exe 是启动程序
