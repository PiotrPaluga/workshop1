from flask import Flask, request

app = Flask(__name__)

html1 = """
<html>
<head>
    <mata charset="UTF-8">
    <title>Guess the number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <input type="submit" value="OK">
</form>
</body>
</html>
"""

html2 = """
<html>
<head>
    <mata charset="UTF-8">
    <title>Guess the number</title>
</head>
<body>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="you win!">
</form>
</body>
</html>
"""

html3 = """
<html>
<head>
    <mata charset="UTF-8">
    <title>Guess the number</title>
</head>
<body>
<h1>Hurra! I guessed! Your number is {guess}</h1>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    if request.method == "GET":
        return html1.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you win!":
            return html3.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return html2.format(guess=guess, min=min_number, max=max_number)


if __name__ == "__main__":
    app.run(debug=True)
