% rebase('base.tpl', title='Landing')
<div id="content_header"></div>
    <div id="site_content">
      <div id="banner"></div>
	  <div id="sidebar_container">
        <div class="sidebar">
          <div class="sidebar_top"></div>
          <div class="sidebar_item">
            <!-- insert your sidebar items here -->
            <h3>Najnovejše</h3>
            <h4>Nova igra</h4>
            <h5>1. oktober 2021</h5>
            <p>Igraj igro ugibanja. Več o njej lahko vprašaš mene.<br /><a href="https://www.facebook.com/pavlanovakk/">Klikni, če želiš izvedeti več.</a></p>
          </div>
          <div class="sidebar_base"></div>
        </div>
        <div class="sidebar">
          <div class="sidebar_top"></div>
          <div class="sidebar_item">
            <h3>Uporabne povezave</h3>
            <ul>
              <li><a href="http://matija.pretnar.info/uvod-v-programiranje/09-tekstovni-vmesnik.html">link 1</a></li>
            </ul>
          </div>
          <div class="sidebar_base"></div>
        </div>
        <div class="sidebar">
          <div class="sidebar_top"></div>
          <div class="sidebar_item">
            <h3>Search</h3>
            <form method="post" action="#" id="search_form">
              <p>
                <input class="search" type="text" name="search_field" value="Enter keywords....." />
                <input name="search" type="image" style="border: 0; margin: 0 0 -9px 5px;" src="{{ get_url('views', path='style/search.png') }}" alt="Search" title="Search" />
              </p>
            </form>
          </div>
          <div class="sidebar_base"></div>
        </div>
      </div>
      <div id="content">
        <!-- insert the page content here -->
        <h1>Pozdravljen/a v igro ugibanja!</h1>
        <p>To je program, ki je narejen pod okriljem predmeta Uvod v programiranje v prvem letniku Finančne matematike na Fakulteti za matematiko in fiziko.</p>
        <p>Pravila igre so sila preprosta, podane so ti črke, ti pa iz njih poskušaš sestaviti besedo, ki jo je moč najti v slovarju slovenskega knjižnega jezika.</p>
        <p>Imaš 10 poskusov, pri ugibanju ti s pomočjo črke lahko pomaga računalnik.</p>
        <p><strong>Vso srečo!</strong></p>
          <form action="/nova_igra" method="post">
            <button type="submit">Nova igra</button>
          </form>
      </div>
    </div>