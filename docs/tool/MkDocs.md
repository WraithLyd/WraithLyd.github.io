

# MkDocs使用记录
!!! Abstract "Reference"
	mkdocs-material官方文档 <https://squidfunk.github.io/mkdocs-material/>


[TOC]

## 准备阶段

### vscode配置
并推荐直接使用vscode，代码和终端控制可以同步进行，不过在vscode中，需要有python环境（即拓展 Pylance 和 Python）。

先在vscode中新建一个终端 <font color = grey>(Ctrl+Shift+`)</font>，执行以下命令，生成python环境。

```powershell
py -m venv venv
venv\Scripts\activate
```

执行以下命令下载mkdocs-material包
```powershell
pip install mkdocs-material
```

```shell
pip install mkdocs-git-revision-date-localized-plugin
```

### 准备github仓库

首先，需要在 [github](https://github.com/) 上新建一个仓库，仓库名格式为 `username`+`.github.io`，再将该仓库拷贝到本地，在本地仓库目录下新建`docs`文件夹和`mkdocs.yml`文件(也可以直接用mkdocs命令`mkdocs new`)。

## 编写网站

`docs` 文件夹中存储网站所需要的markdown文件、css文件等等，而 `mkdocs.yml` 则是来选择需要什么功能。

具体功能实现参考 [mkdocs-material官方文档](https://squidfunk.github.io/mkdocs-material/)。

在编写过程中，如果需要在浏览器中预览网站，那么需要在 `mkdocs.yml` 中添加`dev_addr`的值，作为预览的地址。如果没有给`dev_addr`赋值，那么系统会默认为`127.0.0.1:8000`，由于我的8000端口是占用的，所以我将其改为了5500端口。
```yml
dev_addr: '127.0.0.1:5500'
```
在由venv产生的python虚拟环境中执行指令，再在浏览器中打开所设立的地址。

```powershell
mkdocs serve
```

## 发布网站

在python环境中执行
```powershell
mkdocs build
mkdocs gh-deploy
```
网站便成功发布在了 [https://wraithlyd.github.io](https://wraithlyd.github.io/) 上。

## 高级功能
### 字体设置
首先在 `./docs/stylesheets` 目录下放入下载的字体文件，如`Font1.ttf`和`Font2.ttf`，再新建一个 `extra.css`，内容如下：
```css
@font-face {
    font-family:"Font1","Font2";
	src: url('./Font1.ttf'), format('ttf') ,"./Font2.ttf",format('ttf');
}

:root {
	--md-text-font: "Font1"; 
	--md-code-font: "Font2"; 
}
```

在 `mkdocs.yml` 中添加
```yml
theme:
	font: 
    	text: Font1 
    	code: Font2
extra_css:
  - stylesheets/extra.css
```
### C code in website

```markdown
 ```c linenums="1"
 printf("%d");
 for(i=0;i<n;i++)
  	 flag++;
 ```
```

This type can let website give you the orders of line. It displays:

```c linenums="1"
printf("%d");
for(i=0;i<n;i++)
	flag++;
```
If it doesn't content `linenums="1"`, it displays:
```c
printf("%d");
for(i=0;i<n;i++)
	flag++;
```
### 提示、警告栏

``` yml
# mkdocs.yml 相关配置
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

=== "note"

    !!! note

        默认note标签。

    !!! note "Phasellus posuere in sem ut cursus"

        自定义标题的note标签。

    !!! note ""

        木有标题的note标签。

	``` markdown
	!!! note

    	默认note标签。

	!!! note "Phasellus posuere in sem ut cursus"

    	自定义标题的note标签。

	!!! note ""

    	木有标题的note标签。
	```

=== "abstract"

	!!! abstract

    	abstract, summary, tldr.

		The three are able and use the same icon.

	``` markdown
	!!! abstract

    	abstract, summary, tldr.

		The three are able and use the same icon.
	```

=== "info"
    
	!!! info

    	info, todo.

		The three are able and use the same icon.
    
	``` markdown
    !!! info

    	info, todo.

		The two are able and use the same icon.
    ```

=== "tip"
    
    !!! tip

		tip, hint, important.

        The three are able and use the same icon.
    
    ``` markdown
    !!! tip

        tip, hint, important.

		The three are able and use the same icon.
    ```    

=== "success"
    
    !!! success

		success, check, done.

        The three are able and use the same icon.
    
    ``` markdown
    !!! success

        success, check, done.

		The three are able and use the same icon.
    ```       

=== "question"
    
    !!! question

		question, help, faq.

        The three are able and use the same icon.
    
    ``` markdown
    !!! question

        question, help, faq.

		The three are able and use the same icon.
    ```      

=== "warning"
    
    !!! warning

		warning, caution, attention.

        The three are able and use the same icon.
    
    ``` markdown
    !!! warning

        warning, caution, attention.

		The three are able and use the same icon.
    ```          

=== "failure"
    
    !!! failure

		failure, fail, missing.

		The three are able and use the same icon.

    ``` markdown
    !!! failure

        failure, fail, missing.

		The three are able and use the same icon.
    ```      

=== "danger"
    
    !!! danger

		danger, error

        The three are able and use the same icon.
    
    ``` markdown
    !!! danger

        danger, error.

		The three are able and use the same icon.
    ```     

=== "bug"
    
    !!! bug

        This is bug's style.
    
    ``` markdown
    !!! bug

        This is bug's style.
    ```     

=== "example"
    
    !!! example
        
		This is example's style.
    
    ``` markdown
    !!! example

        This is example's style.
    ```     

=== "quote"
    
    !!! quote

		quote, cite.

        The three are able and use the same icon.
    
	``` markdown
    	!!! quote

        	quote, cite.

			The three are able and use the same icon.
    ```     