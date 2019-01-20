# spider_indeed

使用anaconda时 安装wordcloud 和 jieba 模块时，注意当前路径及环境配置
1.直接在cmd窗口运行

pip install jieba
2.使用conda自带的安装工具

conda install jieba
3.有一些模块是无法使用以上两种方式安装上，这时就需要首先寻找模块，再安装

anaconda search -t conda jieba
这时会出现该模块的很多版本的信息如下图，找到合适的版本


zhangguanqindeMacBook-Pro:~ zhangguanqin$ anaconda show conda-forge/jieba
Using Anaconda API: https://api.anaconda.org
Name:    jieba
Summary: Chinese Words Segementation Utilities
Access:  public
Package Types:  conda
Versions:
   + 0.38
   + 0.39
To install this package with conda run:
     conda install --channel https://conda.anaconda.org/conda-forge jieba
  
 %%注意%%
 版本环境则是另外一回事。注意使用，当前路径，如果创建了多条模拟环境，此处不限于envs pyenv  virtrlenv等
 
 
 切换到另一个环境(activate/deactivate)
为了切换到另一个环境，键入下列命令以及所需环境的名字。

Linux，OS X:
source activate [your env]

Windows：
activate [your env]

如果要从你当前工作环境的路径切换到系统根目录时，键入： 
- Linux，OS X:
source deactivate
Windows:
deactivate

详情：as
https://blog.csdn.net/a857553315/article/details/81410142
https://blog.csdn.net/u012343179/article/details/76146815#t9

 