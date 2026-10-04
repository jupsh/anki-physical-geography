from features import F
from geodata import Region as G

KIND = "Mountain range"
DECK = "Mountain Ranges"

AF, AS, EU, NA, SA, OC, AN = ("Africa", "Asia", "Europe", "North America", "South America",
                              "Oceania", "Antarctica")

FEATURES = [
    # ------------------------------------------------------------------ Asia
    F("Himalayas", G("HIMALAYAS"), AS,
      "The world's highest range, stretching about 2,400 km across Pakistan, India, Nepal, Bhutan "
      "and Tibet (China). Home to most of the world's 8,000 m peaks; the highest is Mount Everest "
      "(8,849 m).",
      "What is the highest peak in the Himalayas (and the world)?", "Mount Everest"),
    F("Karakoram", G("KARAKORAM RA."), AS,
      "Range northwest of the Himalayas where Pakistan, India and China meet. Has some of the "
      "longest glaciers outside the polar regions. The highest peak is K2 (8,611 m).",
      "Which peak, the world's second highest, is in the Karakoram?", "K2"),
    F("Hindu Kush", G("HINDU KUSH"), AS,
      "Runs about 800 km southwest from the Pamirs into central Afghanistan. Its highest peak, "
      "Tirich Mir, is in Pakistan.",
      "Which country contains most of the Hindu Kush?", "Afghanistan"),
    F("Pamirs", G("PAMIRS"), AS,
      "High mountain knot where the Himalaya–Karakoram, Hindu Kush, Tian Shan and Kunlun ranges "
      "meet; called the \"Roof of the World\".",
      "Which country contains most of the Pamirs?", "Tajikistan"),
    F("Tian Shan", G("TIAN SHAN"), AS,
      "Stretches about 2,500 km from Kazakhstan and Kyrgyzstan east into Xinjiang, China, along "
      "the north side of the Tarim Basin.",
      "Which country is largely covered by the Tian Shan?", "Kyrgyzstan"),
    F("Kunlun Mountains", G("KUNLUN MOUNTAINS"), AS,
      "One of Asia's longest ranges, running about 3,000 km across western China.",
      "The Kunlun form the northern edge of which plateau?", "The Tibetan Plateau"),
    F("Altai Mountains", G("ALTAY MOUNTAINS"), AS,
      "Range in Central Asia where Russia, Kazakhstan, Mongolia and China meet.",
      "Which two great Siberian rivers rise in the Altai?", "The Ob and the Irtysh"),
    F("Zagros Mountains", G("ZAGROS MOUNTAINS"), AS,
      "Run about 1,600 km southeast from the Turkey–Iraq border region to the Strait of Hormuz.",
      "Which country contains most of the Zagros?", "Iran"),
    F("Alborz (Elburz)", G("ELBURZ MTS."), AS,
      "Range along the southern coast of the Caspian Sea in northern Iran, just north of Tehran. "
      "The highest peak is Mount Damavand (5,609 m).",
      "What is the highest peak of the Alborz, a volcano?", "Mount Damavand"),
    F("Western Ghats", G("WESTERN GHATS"), AS,
      "Run about 1,600 km along India's west coast. They catch heavy monsoon rain and are a "
      "biodiversity hotspot.",
      "Which lower range runs along India's east coast?", "The Eastern Ghats"),
    F("Annamite Range", G("CHAÎNE ANNAMITIQUE"), AS,
      "Run about 1,100 km through Indochina, between the Mekong valley and the South China Sea coast.",
      "The Annamite Range follows the border between which two countries?", "Laos and Vietnam"),

    # ------------------------------------------------------------------ Europe
    F("Ural Mountains", G("URAL MOUNTAINS"), (EU, AS),
      "Run about 2,500 km north–south through western Russia, from the Arctic coast to Kazakhstan.",
      "Which continental boundary do the Urals mark?", "The boundary between Europe and Asia"),
    F("Caucasus Mountains", G("CAUCASUS MTS."), (EU, AS),
      "Run between the Black and Caspian Seas across Russia, Georgia and Azerbaijan, with the "
      "Lesser Caucasus extending into Armenia. The highest peak is Mount Elbrus (5,642 m).",
      "What is the highest peak of the Caucasus, and of Europe?", "Mount Elbrus"),
    F("Alps", G("ALPS"), EU,
      "Arc about 1,200 km across France, Switzerland, Italy, Germany, Liechtenstein, Austria, "
      "Slovenia and Monaco. The highest peak is Mont Blanc (about 4,806 m).",
      "What is the highest peak in the Alps?", "Mont Blanc"),
    F("Pyrenees", G("PYRENEES"), EU,
      "Run from the Bay of Biscay to the Mediterranean, forming the border between France and "
      "Spain.",
      "Which microstate lies in the Pyrenees?", "Andorra"),
    F("Apennines", G("APPENNINI"), EU,
      "The backbone of Italy, running about 1,200 km down the length of the peninsula. The "
      "highest peak is Corno Grande (2,912 m) in the Gran Sasso."),
    F("Carpathian Mountains", G("CARPATHIAN MOUNTAINS"), EU,
      "Arc about 1,500 km across the Czech Republic, Slovakia, Poland, Ukraine and Romania, "
      "reaching Serbia.",
      "Which country contains the largest share of the Carpathians?", "Romania"),
    F("Dinaric Alps", G("Dinaric Alps"), EU,
      "Run along the Adriatic coast of the Balkans, from Slovenia through Croatia, Bosnia and "
      "Herzegovina and Montenegro to Albania."),
    F("Balkan Mountains", G("Balkan Mts."), EU,
      "Run east–west across Bulgaria to the Black Sea coast.",
      "Which peninsula takes its name from the Balkan Mountains?", "The Balkan Peninsula"),
    F("Scandinavian Mountains", G("KJØLEN MOUNTAINS"), EU,
      "Run about 1,700 km down the Scandinavian Peninsula. Their western side meets the sea in "
      "Norway's fjords.",
      "The Scandinavian Mountains follow the border between which two countries?", "Norway and Sweden"),

    # ------------------------------------------------------------------ Africa
    F("Atlas Mountains", G("ATLAS MOUNTAINS"), AF,
      "Stretch about 2,500 km across Morocco, Algeria and Tunisia. The highest peak is Toubkal "
      "(4,167 m) in Morocco.",
      "Which desert lies south of the Atlas Mountains?", "The Sahara"),
    F("Drakensberg", G("DRAKENSBERG"), AF,
      "The highest part of the escarpment along southern Africa's eastern edge, rising to "
      "3,482 m.",
      "Which country lies almost entirely in the Drakensberg highlands?", "Lesotho"),

    # ------------------------------------------------------------------ North America
    F("Rocky Mountains", G("ROCKY MOUNTAINS"), NA,
      "Stretch about 4,800 km from British Columbia in Canada to New Mexico in the US.",
      "Which major watershed divide runs along the Rockies?", "The Continental Divide"),
    F("Appalachian Mountains", G("APPALACHIAN MTS."), NA,
      "Old, worn-down range running about 2,400 km from Newfoundland and Quebec to Alabama, "
      "parallel to the Atlantic coast."),
    F("Sierra Nevada", G("SIERRA NEVADA"), NA,
      "Runs about 650 km through eastern California. Includes Yosemite and Lake Tahoe. The "
      "highest peak is Mount Whitney (4,421 m).",
      "What is the highest peak in the Sierra Nevada, and in the contiguous US?", "Mount Whitney"),
    F("Cascade Range", G("CASCADE RANGE"), NA,
      "Volcanic range running from British Columbia through Washington and Oregon to northern "
      "California. Includes Mount Rainier.",
      "Which Cascade volcano erupted catastrophically in 1980?", "Mount St. Helens"),
    F("Alaska Range", G("ALASKA RANGE"), NA,
      "Arc across southern Alaska, north of Anchorage. The highest peak is Denali (6,190 m).",
      "Which peak, the highest in North America, is in the Alaska Range?", "Denali"),
    F("Brooks Range", G("BROOKS RANGE"), NA,
      "The northernmost major range in North America, running across northern Alaska into "
      "Canada's Yukon, above the Arctic Circle."),
    F("Sierra Madre Occidental", G("SIERRA MADRE OCCIDENTAL"), NA,
      "Runs about 1,250 km down western Mexico, parallel to the Pacific and the Gulf of California."),
    F("Sierra Madre Oriental", G("SIERRA MADRE ORIENTAL"), NA,
      "Runs about 1,000 km down eastern Mexico, parallel to the Gulf of Mexico."),

    # ------------------------------------------------------------------ South America
    F("Andes", G("ANDES"), SA,
      "The world's longest continental range (about 7,000 km), along the west of South America "
      "through Venezuela, Colombia, Ecuador, Peru, Bolivia, Chile and Argentina. The highest peak "
      "is Aconcagua (6,961 m), in Argentina.",
      "What is the highest peak in the Andes, and in the Americas?", "Aconcagua"),

    # ------------------------------------------------------------------ Oceania
    F("Great Dividing Range", G("GREAT DIVIDING RANGE"), OC,
      "Runs about 3,500 km down eastern Australia from Cape York to Victoria, separating the "
      "coast from the interior. The highest peak is Mount Kosciuszko (2,228 m), at its southern end.",
      "Which peak, Australia's highest, is in the Great Dividing Range?", "Mount Kosciuszko"),
    F("Southern Alps", G("SOUTHERN ALPS"), OC,
      "Run down the length of New Zealand's South Island. The highest peak is Aoraki / Mount Cook "
      "(3,724 m).",
      "What is the highest peak in the Southern Alps and New Zealand?", "Aoraki / Mount Cook"),

    # ------------------------------------------------------------------ Antarctica
    F("Transantarctic Mountains", G("Transantarctic Mountains"), AN,
      "Run about 3,500 km across Antarctica, from the Ross Sea to the Weddell Sea region.",
      "Which two parts of Antarctica do the Transantarctic Mountains divide?", "East Antarctica and West Antarctica"),
]
