% rebase('base.tpl', title='Igra')
<div id="igra">
    <p>POMEŠANA BESEDA JE: {{mesana_beseda}}</p>
    <p>Ima {{dolzina}} črk.</p>
    <p>Poskusili ste {{poskus}}-krat</p>
    % if rezultat:

    <h1>Zmaga!</h1>

    Uganili ste pravilno geslo. Čestitke!

    <form action="/nova_igra" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % elif poskus > 9:

    <h2>Izgubili ste!</h2>

    Pravilna beseda je bila: {{beseda}}

    <form action="/nova_igra" method="post">
        <button type="submit">Nova igra</button>
    </form>

    % else:
    <h1>Bi želeli pomoč?</h1>
    <form action="/pomoc" method="post">
        <button type="submit">Ja! </button>
    </form>
    <form action="/ugibaj" method="post">
        <input type="text" name="beseda" autofocus>
        <button type="submit">Ugibaj!</button>
    </form>
    <form action="/predaja" method="post">
        <button type="submit">Predaj se</button>
    </form>
    % end
</div>
