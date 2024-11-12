# 1.服务器渲染：网页源代码内嵌入数据
# 页面源代码中有数据
# 2.客户端渲染：网页源代码内无嵌入数据，需要用户进行二次请求
# 初次只有html网页源代码，看不到具体数据
# 第二次针对数据请求
from http.cookiejar import Cookie

# 请求的内容：
# 1.User-Agent: 位于Network下，Request Headers
# 2.Query String Parameters
# 2.Cookie: