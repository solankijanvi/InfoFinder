import wikipedia
from flask import Flask, render_template, request


app = Flask(__name__)

app.jinja_env.filters["zip"] = zip


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def find(keyword):
    results = wikipedia.search(keyword, results=8)
    print(f"Total Results fetched {len(results)}")
   
    title = []
    links = []
    info = []
    for x in results:
        try:
            title.append(x)
            
            getlink = wikipedia.page(x, auto_suggest=False, redirect=False).url
            links.append(getlink)
            page_summary = wikipedia.summary(x, sentences=1, auto_suggest=False, redirect=False)
            info.append(page_summary)
        except wikipedia.exceptions.PageError:
            print(f"wikipedia.page({x}).url not found.")
        except wikipedia.exceptions.DisambiguationError:
            pass
        
    return title, links, info

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method != "POST":
        return render_template("index.html")
    userinput = request.form.get("pswd")
    heading, links, info = find(userinput)
    userinput = userinput.capitalize()
    
    return render_template("index.html", si=userinput, lol=zip(heading, links, info), sz=list(zip(heading, links, info)))

if __name__ == "__main__":
    app.run()
