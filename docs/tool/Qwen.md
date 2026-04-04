# Qwen Code

!!! note
	Windows环境下


## 1 安装Node.js

在[Node.js下载](https://nodejs.org/zh-cn/download/)中下载windows安装程序.msi，安装好后检查

```shell linenums="1"
node -v
npm -v
```

接下来配置npm的环境变量，执行

```shell linenums="1"
npm config get prefix
```

获取npm安装位置，并将npm加入系统的PATH环境变量。

## 2 安装Qwen Code

在管理员模式下cmd中运行

```text
curl -fsSL -o %TEMP%\install-qwen.bat https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen.bat && %TEMP%\install-qwen.bat

npm install -g @qwen-code/qwen-code@latest
```

## 3 开始使用 Qwen Code

```
# 进入qwen
qwen
```

后续按提示配置。

```
/language output 中文
```

可切换输出语言为中文。
