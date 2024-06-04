import os

import webview


class Api:
    pass


if __name__ == '__main__':
    import os
    import webview

    # 初始化API和webview窗口
    api = Api()

    # 构建HTML文件的路径
    html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pages/html/index.html')
    url = 'file://' + html_file_path

    # 创建并配置webview窗口，指定大小为900x400
    g_window = webview.create_window('电路', url=url, js_api=api, width=1200, height=800, resizable=False)
    webview.start(debug=True)
    # webview.start()

