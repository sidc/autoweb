%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<h2>Your points are:</h2>
<h3>

  <ul>
  %for col in row:
    <li>{{col}} : {{row[col]}}</li>
  %end
  </ul>


</h3>