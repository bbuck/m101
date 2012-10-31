<!doctype html>
<html>
  <head>
    <title>Sign Up</title>
    <style>
      tr td:first-child {
        text-align: right;
      }
    </style>
  </head>

  <body>
    <p class="disclaimer">Already a user? <a href="/login">Login</a></p>
    <h1>Sign Up</h1>
    <form action="/users" method="post">
      <table>
        <tr>
          <td><label for="username">Username</label></td>
          <td><input type="text" name="username" /></td>
        </tr>
        <tr>
          <td><label for="password">Password</label></td>
          <td><input type="password" name="password"></td>
        </tr>
        <tr>
          <td><label for="verify_password">Verify Password</label></td>
          <td><input type="password" name="verify_password" /></td>
        </tr>
        <tr>
          <td><label for="email">Email (optional)</label></td>
          <td><input type="email" name="email" /></td>
        </tr>
      </table>
      <button type="submit">Submit</button>
    </form>
  </body>
</html>
