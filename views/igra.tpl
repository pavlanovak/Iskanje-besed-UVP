% rebase('base.tpl', title='Igra')
<div id="igra">
    <p>POMESANA BESEDA JE: {{mesana_beseda}}</p>
    <h1>ODSTRANI ME: {{beseda}}</h1>
    <p>Poskusili ste {{poskus}} krat</p>

    % if rezultat:

    <h1>Zmaga!</h1>

    Uganili ste pravilno geslo. Čestitke!

    <form action="/nova_igra" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % elif poskus > 10:

    <h2>Izgubili ste!</h2>

    Pravilna beseda je bila: {{beseda}}

    <form action="/nova_igra" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % else:
    <form action="/ugibaj" method="post">
        <input type="text" name="beseda" autofocus>
        <button type="submit">Ugibaj!</button>
    </form>

    % end
</div>