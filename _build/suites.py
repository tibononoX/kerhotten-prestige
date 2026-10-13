"""Generates _build/pages/<suite>.html from the facts below (all taken from www.gitesdekerhotten.fr).
Capacities / sizes = home-page figures; other pages of the current site differ (see README)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
S = [
 dict(slug='le-saule', key='saule', fr='Le Saule', en='Willow', hero='saule-ext',
  title='Le Saule (Willow) – penty breton 5 personnes face au lac · Gîtes de Kerhotten || Le Saule (Willow) – Breton cottage for 5 facing the lake · Gîtes de Kerhotten || Le Saule (Willow) – bretonisches Cottage für 5 Personen am See · Gîtes de Kerhotten',
  desc='Le Saule, penty breton exposé plein sud face au lac du Dordu : 5 personnes, 90 m², deux chambres, terrasse avec barbecue. Hameau de Kerhotten, Morbihan. || Le Saule, a south-facing Breton cottage overlooking Lac du Dordu: 5 guests, 90 m², two bedrooms, terrace with barbecue. Kerhotten hamlet, Morbihan. || Le Saule, nach Süden ausgerichtetes bretonisches Cottage am Lac du Dordu: 5 Personen, 90 m², zwei Schlafzimmer, Terrasse mit Grill. Weiler Kerhotten, Morbihan.',
  alt='Le Saule, penty breton face au lac || Le Saule, a Breton cottage facing the lake || Le Saule, bretonisches Cottage mit Seeblick',
  specs=[('Capacité || Sleeps || Personen','5 + lit bébé || 5 + baby cot || 5 + Babybett'),('Surface || Size || Fläche','90 m² || 90 m² || 90 m²'),('Exposition || Aspect || Ausrichtung','Plein sud, face au lac || South-facing, lake view || Südlage, Seeblick')],
  intro='Ce penty breton bénéficie d’un joli point de vue face au lac du Dordu, exposé plein sud. Un intérieur chaleureux et cosy, une terrasse avec barbecue. || This Breton penty enjoys a lovely south-facing view over Lac du Dordu. A warm, cosy interior and a terrace with barbecue. || Dieses bretonische Penty genießt einen schönen, nach Süden ausgerichteten Blick auf den Lac du Dordu. Ein warmes, gemütliches Interieur und eine Terrasse mit Grill.',
  layout=[
   ('Rez-de-chaussée || Ground floor || Erdgeschoss','Cuisine entièrement équipée (lave-linge, lave-vaisselle) ouverte sur un vaste séjour cosy, TV satellite Astra 19. || Fully equipped kitchen (washing machine, dishwasher) open to a spacious, cosy living room; Astra 19 satellite TV. || Voll ausgestattete Küche (Waschmaschine, Geschirrspüler), offen zum großzügigen, gemütlichen Wohnraum; Sat-TV Astra 19.'),
   ('Étage || Upstairs || Obergeschoss','Une chambre avec lit double king size, une chambre d’enfants avec lits superposés, salle de bain avec baignoire et douche. || A bedroom with a king-size double bed, a children’s room with bunk beds, bathroom with bath and shower. || Ein Schlafzimmer mit Kingsize-Doppelbett, ein Kinderzimmer mit Etagenbetten, Bad mit Wanne und Dusche.'),
   ('Extérieur || Outside || Außen','Terrasse avec salon de jardin, barbecue et parasol. || Terrace with garden furniture, barbecue and parasol. || Terrasse mit Gartenmöbeln, Grill und Sonnenschirm.')],
  gallery=[('saule-ext','Le Saule, côté lac || Le Saule, lake side || Le Saule, Seeseite'),('saule-sejour','Le séjour cosy || The cosy living room || Der gemütliche Wohnraum'),('saule-cuisine','La cuisine équipée || The fitted kitchen || Die Einbauküche'),('saule-chambre','Chambre avec lit double || Double bedroom || Doppelzimmer'),('saule-enfants','Chambre d’enfants, lits superposés || Children’s room with bunk beds || Kinderzimmer mit Etagenbetten'),('saule-plan','Plan du gîte || Floor plan || Grundriss'),('saule-coucher-soleil','Coucher de soleil sur le lac du Dordu || Sunset over Lac du Dordu || Sonnenuntergang am Lac du Dordu')]),
 dict(slug='la-chataigne', key='chataigne', fr='La Châtaigne', en='Chestnut', hero='chataigne-ext',
  title='La Châtaigne (Chestnut) – longère 8 à 10 personnes · Gîtes de Kerhotten || La Châtaigne (Chestnut) – longhouse for 8–10 guests · Gîtes de Kerhotten || La Châtaigne (Chestnut) – Langhaus für 8–10 Personen · Gîtes de Kerhotten',
  desc='La Châtaigne, la plus grande maison du hameau de Kerhotten : 8 à 10 personnes, 130 m², cheminée en pierre et poêle à bois, deux terrasses. Morbihan. || La Châtaigne, the largest house in the Kerhotten hamlet: 8–10 guests, 130 m², stone fireplace and wood stove, two terraces. Morbihan. || La Châtaigne, das größte Haus des Weilers Kerhotten: 8–10 Personen, 130 m², Steinkamin und Holzofen, zwei Terrassen. Morbihan.',
  alt='La Châtaigne, longère en granit || La Châtaigne, a granite longhouse || La Châtaigne, Langhaus aus Granit',
  specs=[('Capacité || Sleeps || Personen','8 à 10 + lits bébé || 8–10 + baby cots || 8–10 + Babybetten'),('Surface || Size || Fläche','130 m² || 130 m² || 130 m²'),('Chambres || Bedrooms || Schlafzimmer','4 + clic-clac || 4 + sofa bed || 4 + Schlafsofa')],
  intro='La plus longue et la plus grande maison du hameau, pensée pour les familles nombreuses et les groupes d’amis, autour d’une grande cheminée bretonne. || The longest and largest house in the hamlet, made for large families and groups of friends, gathered around a great Breton fireplace. || Das längste und größte Haus des Weilers, ideal für große Familien und Freundesgruppen, rund um einen großen bretonischen Kamin.',
  layout=[
   ('Rez-de-chaussée || Ground floor || Erdgeschoss','Une chambre double avec sa salle de bain et WC. Cuisine entièrement équipée (lave-vaisselle, lave-linge, réfrigérateur) ouverte sur un séjour breton avec auge et cheminée en pierre de pays, poêle à bois ; TV Astra 19, lecteur DVD, barre de son. || A double bedroom with its own bathroom and WC. Fully equipped kitchen (dishwasher, washing machine, fridge) open to a Breton living room with a stone trough, local-stone fireplace and wood stove; Astra 19 TV, DVD player, soundbar. || Ein Doppelzimmer mit eigenem Bad und WC. Voll ausgestattete Küche (Geschirrspüler, Waschmaschine, Kühlschrank), offen zum bretonischen Wohnraum mit Steintrog, Kamin aus Naturstein und Holzofen; TV Astra 19, DVD-Player, Soundbar.'),
   ('Étage || Upstairs || Obergeschoss','Une grande chambre double (clic-clac possible), deux chambres à deux lits simples, salle de bain et WC, coin repos en mezzanine avec livres. || A large double bedroom (sofa bed possible), two twin bedrooms, bathroom and WC, a reading mezzanine with books. || Ein großes Doppelzimmer (Schlafsofa möglich), zwei Zweibettzimmer, Bad und WC, eine Leseecke auf der Galerie.'),
   ('Extérieur || Outside || Außen','Deux terrasses, jardin avec vue sur la campagne et les hortensias, barbecue, salon de jardin et parasol. || Two terraces, a garden overlooking the countryside and hydrangeas, barbecue, garden furniture and parasol. || Zwei Terrassen, Garten mit Blick auf die Landschaft und die Hortensien, Grill, Gartenmöbel und Sonnenschirm.')],
  gallery=[('chataigne-ext','La Châtaigne, façade en granit || La Châtaigne, granite façade || La Châtaigne, Granitfassade'),('chataigne-cheminee','Le séjour et la cheminée en pierre || The living room and stone fireplace || Wohnraum mit Steinkamin'),('chataigne-salon','Le salon || The lounge || Der Salon'),('chataigne-cuisine','Cuisine ouverte sur le séjour || Kitchen open to the living room || Küche, offen zum Wohnraum'),('chataigne-chambre','Chambre double || Double bedroom || Doppelzimmer'),('chataigne-chambre-rdc','Chambre double du rez-de-chaussée || Ground-floor double bedroom || Doppelzimmer im Erdgeschoss'),('chataigne-twin','Chambre à deux lits simples || Twin bedroom || Zweibettzimmer'),('chataigne-sdb','Salle de bain avec douche || Bathroom with shower || Bad mit Dusche'),('chataigne-plan','Plan du gîte || Floor plan || Grundriss')]),
 dict(slug='la-grange', key='grange', fr='La Grange', en='Granary', hero='grange-piscine',
  title='La Grange (Granary) – grange de 1697, 7 personnes · Gîtes de Kerhotten || La Grange (Granary) – a 1697 barn for 7 guests · Gîtes de Kerhotten || La Grange (Granary) – Scheune von 1697 für 7 Personen · Gîtes de Kerhotten',
  desc='La Grange, ancienne grange de 1697 rénovée : 7 personnes, 95 m², poêle à bois, baie vitrée, jardinet d’hortensias. Hameau de Kerhotten, Morbihan. || La Grange, a renovated barn from 1697: 7 guests, 95 m², wood stove, bay window, a small hydrangea garden. Kerhotten hamlet, Morbihan. || La Grange, renovierte Scheune von 1697: 7 Personen, 95 m², Holzofen, Fensterfront, kleiner Hortensiengarten. Weiler Kerhotten, Morbihan.',
  alt='La Grange au-dessus de la piscine || La Grange above the pool || La Grange oberhalb des Pools',
  specs=[('Capacité || Sleeps || Personen','7 + lit bébé || 7 + baby cot || 7 + Babybett'),('Surface || Size || Fläche','95 m² || 95 m² || 95 m²'),('Bâtie en || Built in || Erbaut','1697 || 1697 || 1697')],
  intro='Cette ancienne grange, rénovée dans les règles de l’art, a gardé son caractère d’antan : la pierre de granit du pignon porte encore son année de construction. || This former barn, renovated with great care, has kept its old-time character: the granite stone on its gable still bears the year it was built. || Diese ehemalige Scheune wurde fachgerecht renoviert und hat ihren ursprünglichen Charakter bewahrt: Der Granitstein am Giebel trägt noch ihr Baujahr.',
  layout=[
   ('Rez-de-chaussée || Ground floor || Erdgeschoss','Cuisine style « brocante vintage » avec mur en granit, lave-linge et lave-vaisselle, ouverte sur un vaste séjour avec poêle à bois et baie vitrée ; TV (chaînes françaises, anglaises et européennes), DVD, jeux et livres. || A “vintage brocante” kitchen with granite wall, washing machine and dishwasher, open to a large living room with wood stove and bay window; TV (French, British and European channels), DVDs, games and books. || Küche im „Vintage-Brocante“-Stil mit Granitwand, Waschmaschine und Geschirrspüler, offen zum großen Wohnraum mit Holzofen und Fensterfront; TV (französische, britische und europäische Sender), DVDs, Spiele und Bücher.'),
   ('Étage || Upstairs || Obergeschoss','Une chambre double spacieuse, une chambre avec un lit double et un lit simple, une chambre à deux lits simples (pouvant devenir double) ; salle de bain avec douche, WC ; prêt de lit bébé. || A spacious double bedroom, a room with a double and a single bed, a twin room (can become a double); bathroom with shower, WC; baby cot on loan. || Ein geräumiges Doppelzimmer, ein Zimmer mit Doppel- und Einzelbett, ein Zweibettzimmer (auch als Doppelzimmer); Bad mit Dusche, WC; Babybett auf Anfrage.'),
   ('Extérieur || Outside || Außen','Jardinet privatif entouré d’hortensias bleus et de crocosmias ; deux terrasses avec salon de jardin, barbecue et parasol. || A private little garden framed by blue hydrangeas and crocosmia; two terraces with garden furniture, barbecue and parasol. || Ein kleiner Privatgarten mit blauen Hortensien und Montbretien; zwei Terrassen mit Gartenmöbeln, Grill und Sonnenschirm.')],
  gallery=[('grange-piscine','La Grange et la piscine || La Grange and the pool || La Grange und der Pool'),('grange-ext','La Grange, façade en pierre || La Grange, stone façade || La Grange, Steinfassade'),('grange-sejour','Séjour avec poêle à bois et baie vitrée || Living room with wood stove and bay window || Wohnraum mit Holzofen und Fensterfront'),('grange-salon','Le séjour || The living room || Der Wohnraum'),('grange-cuisine','Cuisine ouverte sur le séjour || Kitchen open to the living room || Küche, offen zum Wohnraum'),('grange-chambre','Chambre double || Double bedroom || Doppelzimmer'),('grange-chambre-simple','Chambre avec vue sur la piscine et la campagne || Bedroom overlooking the pool and countryside || Zimmer mit Blick auf Pool und Landschaft'),('grange-sdb','Salle de bain || Bathroom || Bad'),('grange-plan','Plan du gîte || Floor plan || Grundriss')]),
]

import json as _json, os as _os
_MAN=_json.load(open(_os.path.join(_os.path.dirname(__file__),'manifest.json')))
def _srcset(n):
    return ', '.join(f"assets/img/{n}-{w}.webp {w}w" for w in _MAN[n]['w'])

LINKS={'saule': '<a class="btn btn-dark" href="https://www.abritel.fr/location-vacances/p1782928" target="_blank" rel="noopener">[[Réserver sur Abritel || Book on Abritel || Buchen auf Abritel]]<span class="sr"> [[(nouvel onglet) || (new tab) || (neuer Tab)]]</span></a><a class="btn btn-dark" href="https://www.vrbo.com/1782928a" target="_blank" rel="noopener">[[Réserver sur Vrbo || Book on Vrbo || Buchen auf Vrbo]]<span class="sr"> [[(nouvel onglet) || (new tab) || (neuer Tab)]]</span></a>', 'chataigne': '<a class="btn btn-dark" href="https://www.vrbo.com/1781689a" target="_blank" rel="noopener">[[Réserver sur Vrbo || Book on Vrbo || Buchen auf Vrbo]]<span class="sr"> [[(nouvel onglet) || (new tab) || (neuer Tab)]]</span></a>', 'grange': '<a class="btn btn-dark" href="https://www.abritel.fr/location-vacances/p1781639" target="_blank" rel="noopener">[[Réserver sur Abritel || Book on Abritel || Buchen auf Abritel]]<span class="sr"> [[(nouvel onglet) || (new tab) || (neuer Tab)]]</span></a><a class="btn btn-dark" href="https://www.vrbo.com/1781639a" target="_blank" rel="noopener">[[Réserver sur Vrbo || Book on Vrbo || Buchen auf Vrbo]]<span class="sr"> [[(nouvel onglet) || (new tab) || (neuer Tab)]]</span></a>', 'hameau': '<a class="btn btn-dark" href="https://www.abritel.fr/location-vacances/p2062126" target="_blank" rel="noopener">[[Réserver sur Abritel || Book on Abritel || Buchen auf Abritel]]<span class="sr"> [[(nouvel onglet) || (new tab) || (neuer Tab)]]</span></a>'}
def page(s, others):
    specs = '\n'.join(f'<div><dt>[[{a}]]</dt><dd>[[{b}]]</dd></div>' for a, b in s['specs'])
    layout = '\n'.join(f'<div class="lay rv"><h3>[[{a}]]</h3><p>[[{b}]]</p></div>' for a, b in s['layout'])
    gal = '\n'.join(f'<!--gal {n}|{c}-->' for n, c in s['gallery'])
    oth = '\n'.join(f'<li><a href="{o["slug"]}.html"><span class="o-en">{o["en"]}</span><span class="o-fr">{o["fr"]}</span></a></li>' for o in others)
    return f'''@title {s['title']}
@desc {s['desc']}
@bodyclass suite-page
@preload <link rel="preload" as="image" type="image/webp" imagesrcset="{_srcset(s['hero'])}" imagesizes="(min-width: 900px) 55vw, 100vw" fetchpriority="high">
<nav class="crumbs wrap" {{{{aria-label: Fil d'Ariane || Breadcrumb || Brotkrumen}}}}><a href="index.html">Kerhotten</a> <span aria-hidden="true">/</span> <a href="index.html#suites">[[Les suites || The suites || Die Suiten]]</a> <span aria-hidden="true">/</span> <span aria-current="page">{s['fr']}</span></nav>
<section class="s-hero wrap" aria-labelledby="h1">
  <div class="s-hero-img"><!--img {s['hero']}|(min-width: 900px) 55vw, 100vw|cover|eager|{s['alt']}--></div>
  <div class="s-hero-txt">
    <p class="kicker kicker-dark">[[Suite || Suite || Suite]] · {s['en']}</p>
    <h1 id="h1">{s['fr']}</h1>
    <p class="lead">[[{s['intro']}]]</p>
    <dl class="specs">
{specs}
    </dl>
    <p class="ph-box"><span class="ph-tag">[[À compléter || To be completed || Zu ergänzen]]</span> [[Tarifs par saison : non publiés sur le site actuel. || Seasonal rates: not published on the current site. || Saisonpreise: auf der aktuellen Website nicht veröffentlicht.]]</p>
    <div class="s-cta">
      {LINKS[s['key']]}
      <a class="btn btn-line-dark" href="#galerie">[[Voir la galerie || View the gallery || Galerie ansehen]]</a>
    </div>
  </div>
</section>
<section class="sec layout-sec" aria-labelledby="h-lay">
  <div class="wrap">
    <h2 id="h-lay" class="rv">[[L'agencement || The layout || Die Aufteilung]]</h2>
    <div class="lay-grid">
{layout}
    </div>
  </div>
</section>
<section class="sec gallery-sec" id="galerie" aria-labelledby="h-gal">
  <div class="wrap">
    <h2 id="h-gal" class="rv">[[Galerie || Gallery || Galerie]]</h2>
    <p class="small">[[Cliquez sur une photo pour l'agrandir ; flèches du clavier pour naviguer, Échap pour fermer. || Click a photo to enlarge it; use the arrow keys to browse and Escape to close. || Klicken Sie auf ein Foto, um es zu vergrößern; Pfeiltasten zum Blättern, Esc zum Schließen.]]</p>
    <ul class="gallery" data-gallery>
{gal}
    </ul>
  </div>
</section>
<section class="sec others" aria-labelledby="h-oth">
  <div class="wrap">
    <h2 id="h-oth">[[Les autres suites || The other suites || Die anderen Suiten]]</h2>
    <ul class="others-list">
{oth}
      <li><a href="privatisation.html"><span class="o-en">[[Groupes || Groups || Gruppen]]</span><span class="o-fr">[[Le hameau entier || The whole hamlet || Der ganze Weiler]]</span></a></li>
    </ul>
  </div>
</section>
'''

def generate():
    for s in S:
        others = [o for o in S if o is not s]
        open(os.path.join(HERE, 'pages', s['slug'] + '.html'), 'w').write(page(s, others))

if __name__ == '__main__':
    generate()
