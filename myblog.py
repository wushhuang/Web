from app import app
#防止被引用后执行，只在当前模块中才可以使用
if __name__ =='__main__':
    app.run(host='172.16.11.13',debug=True)