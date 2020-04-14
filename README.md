# pytest-data-file

Pytest使用json,yaml等数据文件

---

### 如何使用

1. 安装 `pytest-data-file`

使用pip从github安装
```
pip install git+https://github.com/hanzhichao/pytest-data-file
```

2. 使用方法
准备数据文件(支持.json/.yaml), 如放到项目data目录下，格式如下：
```yaml
# data/test_data.yaml
test_a:  # must be same with test function name
  user: hanzhichao
  password: 123456
  skills: [Python,Java,Go]

test_b:
  number: 1
```
  
  
或在pytest.ini中配置
```
[pytest]
data_file=data/test_data.yaml
```
或命令行传入
```
$ pytest --data-file=data/test_data.yaml
```
支持传入项目相对路径和绝对路径，绝对路径必须以'/'开头或包含':'，例如：

```
$ pytest --data-file=/home/hanzhichao/data/test_data.yaml
```
或
```
$ pytest --data-file=D:\\data\\test_data.yaml
```

3. 使用fixture函数: data和case_data
```
def test_a(data):  # 所有数据
    my_data = data.get('test_a')
    print(my_data)
    
def test_b(case_data):  # 仅该用例数据
    print(case_data)    

```

---

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a> 
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`博客园 韩志超`</a>
- 简书: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`简书 韩志超`</a>

