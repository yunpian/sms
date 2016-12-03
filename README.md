# 贡献代码指南  
一般可以通过在Github上提交Pull Request来贡献代码。

## Pull Request要求  

必须添加测试！ - 如果没有测试，那么提交的PR是不会通过的。  
创建feature分支 - 最好不要从你的master分支提交 pull request 。 
一个feature提交一个pull请求 - 如果你的代码变更了多个操作，那就提交多个pull请求吧。
清晰的commit历史 - 保证你的pull请求的每次commit操作都是有意义的。如果你开发中需要执行多次的即时commit操作，那么请把它们放到一起再提交pull请求。

## 目录结构介绍  

官方的开源代码都放在`yunpian`目录下面，第三方的开源代码都放在`thirdparty`目录下面。  
里面均列出了比较流行的后端开发语言作为目录，不同语言的代码应该放到相应的语言目录下面。  
尽量做到不依赖第三方lib，可以通过修改配置文件达到配置APPKEY的目的，减少最终用户使用时的开发量。  

## 联系我们
[技术支持 QQ](https://static.meiqia.com/dist/standalone.html?eid=30951&groupid=0d20ab23ab4702939552b3f81978012f&metadata={"name":"github"})


