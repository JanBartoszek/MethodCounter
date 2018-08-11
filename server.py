from flask import Flask, render_template, redirect, url_for, request
import logic

app = Flask(__name__)


@app.route('/')
def index():
    get_count = logic.get_count
    post_count = logic.post_count
    return render_template('main-page.html', get_count = get_count, post_count = post_count)


@app.route('/get')
def count_gets():
    logic.count_gets()
    return redirect(url_for('index'))


@app.route('/post', methods=['POST'])
def count_posts():
    logic.count_posts()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000 
            )