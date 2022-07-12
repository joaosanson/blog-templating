from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    for blog_post in all_posts:
        if blog_post['id'] == post_id:
            current_post = blog_post
    return render_template("post.html", post=current_post)


if __name__ == "__main__":
    app.run(debug=True)
