% rebase('base.tpl', title='Igra')
<div id="igra">
    <h1>Tvoje geslo je bilo {{geslo}}</h1>
    <form action="/nova_igra" method="post">
        <button type="submit">Nova igra</button>
      </form>
</div>