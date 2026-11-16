window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  // SVG 输出：公式以一整段 SVG 渲染，不依赖额外字体文件（CHTML 版本要另外下载 woff 字体，
  // 字体加载失败时会出现分数线错位、根号缺失等问题，所以改用 SVG）。
  svg: {
    fontCache: "global"
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.typesetPromise()
})
