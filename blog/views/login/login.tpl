
<!doctype html>
<html>
  <head>
    <title>Login</title>
    <style>
      tr td:first-child {
        text-align: right;
      }
    </style>
  </head>

  <body>
    <h1>Login</h1>
    <form action="/login" method="post">
      <table>
        <tr>
          <td><label for="username">Username</label></td>
          <td><input type="text" name="username" /></td>
        </tr>
        <tr>
          <td><label for="password">Password</label></td>
          <td><input type="password" name="password"></td>
        </tr>
      </table>
      <button type="submit">Login</button>
    </form>
  </body>
</html>
