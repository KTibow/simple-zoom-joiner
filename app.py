from flask import Flask
app = Flask(__name__)

jiggle_style = """<style>
@keyframes jiggle {
0% {
transform: skewX(9deg);
}
10% {
transform: skewX(-8deg);
}
20% {
transform: skewX(7deg);
}
30% {
transform: skewX(-6deg);
}
40% {
transform: skewX(5deg);
}
50% {
transform: skewX(-4deg);
}
60% {
transform: skewX(3deg);
}
70% {
transform: skewX(-2deg);
}
80% {
transform: skewX(1deg);
}
90% {
transform: skewX(0deg);
}
100% {
transform: skewX(0deg);
}
}
</style>"""

@app.route("/")
def tutorial():
    return """
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap" rel="stylesheet">
<style>
h1, h2 {
    font-family: Quicksand, sans-serif;
}
p {
    font-family: sans-serif;
}
</style>
<h1 style='color: #84F;'>Simple zoom joiner</h1>
<p>Join meetings without bloated webpages.</p>
<h2>/j/&lt;meeting_number&gt;</h2>
<p>Join plain Zoom meetings, without passwords. Just take the zoom.us/j/&lt;thing&gt; and put it into simple-zoom-joiner.herokuapp.com/j/&lt;thing&gt;.</p>
<h2>/j/&lt;meeting_number&gt;?pwd=&lt;password&gt;</h2>
<p>Join with passwords. The password is the encoded thing from zoom.us/j/&lt;thing&gt;?pwd=&lt;thing&gt;.</p>
<h2>/custom/&lt;meeting_protocol&gt;/&lt;path&gt;</h2>
<p>Join with custom protocols, like for webex meetings. So wbx://woof would be simple-zoom-joiner.herokuapp.com/custom/wbx/woof.</p>
<h2>/redirect/&lt;domain_name&gt;/&lt;path&gt;</h2>
<p>Redirect to websites. So doxy.me/adoctor would be simple-zoom-joiner.herokuapp.com/redirect/doxy.me/adoctor.</p>
<p>I'm not affiliated with Zoom, Webex, or anything else. What's theirs it theirs; what's mine is mine.</p>
"""


@app.route("/j/<meeting_number>")
def join_plain(meeting_number):
    return f"""
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap" rel="stylesheet">
<h1 style='font-family: Quicksand, sans-serif; color: #84F; animation: infinite 1s jiggle;'>Joining...</h1>
{jiggle_style}
<iframe src='zoommtg://zoom.us/join?confno={meeting_number}' style='display: none;'></iframe>
"""

@app.route("/j/<meeting_number>?pwd=<meeting_password>")
def join_password(meeting_number, meeting_password):
    return f"""
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap" rel="stylesheet">
<h1 style='font-family: Quicksand, sans-serif; color: #84F; animation: infinite 1s jiggle;'>Joining...</h1>
{jiggle_style}
<iframe src='zoommtg://zoom.us/join?confno={meeting_number}&pwd={meeting_password}' style='display: none;'></iframe>
"""

@app.route("/custom/<meeting_protocol>/<path>")
def join_custom(meeting_protocol, path):
    return f"""
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap" rel="stylesheet">
<h1 style='font-family: Quicksand, sans-serif; color: #84F; animation: infinite 1s jiggle;'>Joining...</h1>
{jiggle_style}
<iframe src='<meeting_protocol>://<path>' style='display: none;'></iframe>
"""

@app.route("/redirect/<domain_name>/<path>")
def join_redirect(domain_name, path):
    return f"""
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap" rel="stylesheet">
<h1 style='font-family: Quicksand, sans-serif; color: #84F; animation: infinite 1s jiggle;'>Joining...</h1>
{jiggle_style}
<script>
window.location = "https://{domain_name}/{path}";
</script>
"""
