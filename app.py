from chalice import Chalice

app = Chalice(app_name='helloworld')


print('a')
print('a')

@app.route('/')
def index():
    print('hello')
    return {'hello': 'world'}
