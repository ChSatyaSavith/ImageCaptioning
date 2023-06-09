from flask import Flask, render_template, redirect, request
import ImageCaption
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route('/about')
def about():
    return  render_template("About.html")
@app.route('/')
def hello():
    return  render_template("index.html")

@app.route('/', methods=["POST"])
def image():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        caption = ImageCaption.caption_this_image(path)
        
        result_dic = {
            'image' : path,
            'caption' : caption
        }

    return render_template("generated.html",your_caption = result_dic)

if __name__ == '__main__':
    app.run(debug=True)