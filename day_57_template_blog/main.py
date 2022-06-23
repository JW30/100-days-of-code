from flask import Flask, render_template
import requests

app = Flask(__name__)

npoint_url: str = "https://api.npoint.io/a80477dc1b54d8f49bd9"
blog_posts = requests.get(url=npoint_url).json()


@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/<post_id>')
def show_blog_post(post_id):
    return render_template("post.html", blog_post=blog_posts[f"{post_id}"])


if __name__ == "__main__":
    app.run(debug=True)
