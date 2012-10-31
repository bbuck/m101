<!doctype html>
<html>
  <head>
    <title>Template Test</title>
  </head>

  <body>
    <h1>Welcome {{name}}</h1>
    <strong>Here is some fruit:</strong>
    <ul>
      %for fruit in fruits:
        <li>{{fruit}}</li>
      %end
    </ul>
    <br />
    <form action="/favorite_fruit" method="post">
      <label for="fruit">What is your favorite fruit?</label>
      <input type="text" name="fruit" />
      <br />
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
