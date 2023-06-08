from flask import Flask, request
import json
import midjourney_scraper




app = Flask(__name__)


@app.route('/get/news', methods=['GET', "POST"])
def get_news():

    mj = midjourney_scraper.Midjourney()
    content = mj.getContent()
    
    return json.dumps(content)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9020, debug=True)
    

