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
      "Which range holds Mount Everest?", "The Himalayas"),
    F("Karakoram", G("KARAKORAM RA."), AS,
      "Range northwest of the Himalayas where Pakistan, India and China meet. Has some of the "
      "longest glaciers outside the polar regions. The highest peak is K2 (8,611 m).",
      "Which range holds K2, the world's second-highest peak?", "The Karakoram"),
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
      "One of Asia's longest ranges, running about 3,000 km across western China along the "
      "northern edge of the Tibetan Plateau.",
      "In which country are the Kunlun Mountains?", "China"),
    F("Altai Mountains", G("ALTAY MOUNTAINS"), AS,
      "Range in Central Asia where Russia, Kazakhstan, Mongolia and China meet; the source of the "
      "Ob and Irtysh rivers. The highest peak is Belukha (4,506 m).",
      "In which range do Russia, Kazakhstan, Mongolia and China meet?", "The Altai Mountains"),
    F("Zagros Mountains", G("ZAGROS MOUNTAINS"), AS,
      "Run about 1,600 km southeast from the Turkey–Iraq border region to the Strait of Hormuz.",
      "Which country contains most of the Zagros?", "Iran"),
    F("Alborz (Elburz)", G("ELBURZ MTS."), AS,
      "Range along the southern coast of the Caspian Sea in northern Iran, just north of Tehran. "
      "The highest peak is Mount Damavand (5,609 m).",
      "Which capital city lies at the southern foot of the Alborz?", "Tehran"),
    F("Western Ghats", G("WESTERN GHATS"), AS,
      "Run about 1,600 km along India's west coast. They catch heavy monsoon rain and are a "
      "biodiversity hotspot. The lower Eastern Ghats run along the east coast.",
      "Along which sea do the Western Ghats run?", "The Arabian Sea"),
    F("Pontic Mountains", G("PONTIC MOUNTAINS"), AS,
      "Run about 1,000 km along Turkey's Black Sea coast, rising steeply from the shore and "
      "catching its rain. Tea and hazelnuts grow on their lower slopes.",
      "Along which sea do the Pontic Mountains run?", "The Black Sea"),
    F("Kopet Dag", G("Kopet Dag Mts ."), AS,
      "Range on the Turkmenistan–Iran border, northeast of the Caspian Sea. Ashgabat stands "
      "at its foot.",
      "The Kopet Dag forms the border between which two countries?", "Turkmenistan and Iran"),
    F("Verkhoyansk Range", G("VERKHOYANSK RANGE"), AS,
      "Long arc in northeastern Siberia, east of the Lena. Winters near it, around Verkhoyansk "
      "and Oymyakon, are among the coldest in the inhabited world.",
      "Which Siberian range stands near Verkhoyansk and Oymyakon, among the coldest inhabited "
      "places on Earth?", "The Verkhoyansk Range"),
    F("Sikhote-Alin Range", G("SIKHOTE-ALIN’ RANGE"), AS,
      "Runs about 900 km along Russia's Pacific coast, inland from Vladivostok. A large "
      "meteorite fell in it in 1947.",
      "Along which country's Pacific coast does the Sikhote-Alin Range run?", "Russia"),
    F("Eastern Ghats", G("EASTERN GHATS"), AS,
      "Broken chain of hills along India's east coast, lower and older than the Western Ghats. "
      "The Godavari, Krishna and Kaveri cut through it to the Bay of Bengal.",
      "Along which bay do the Eastern Ghats run?", "The Bay of Bengal"),
    F("Barisan Mountains", G("Barisan Mountains"), AS,
      "Run the length of Sumatra, parallel to its southwest coast. They hold many active "
      "volcanoes, including Mount Kerinci.",
      "In which country are the Barisan Mountains?", "Indonesia"),
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
      "Which range holds Mount Elbrus, Europe's highest peak?", "The Caucasus Mountains"),
    F("Alps", G("ALPS"), EU,
      "Arc about 1,200 km across France, Switzerland, Italy, Germany, Liechtenstein, Austria, "
      "Slovenia and Monaco. The highest peak is Mont Blanc (about 4,806 m).",
      "Which range arcs across France, Switzerland, Italy and Austria and holds Mont Blanc?",
      "The Alps"),
    F("Pyrenees", G("PYRENEES"), EU,
      "Run from the Bay of Biscay to the Mediterranean, forming the border between France and "
      "Spain.",
      "Which range forms the border between France and Spain?", "The Pyrenees"),
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
      "Which range runs east–west across Bulgaria to the Black Sea?", "The Balkan Mountains"),
    F("Massif Central", G("Massif Central"), EU,
      "Ancient volcanic upland in south-central France, between the Rhône and the plains of "
      "the west. The Loire and several other French rivers rise in it.",
      "Which upland in south-central France is the source of the Loire?", "The Massif Central"),
    F("Scandinavian Mountains", G("KJØLEN MOUNTAINS"), EU,
      "Run about 1,700 km down the Scandinavian Peninsula. Their western side meets the sea in "
      "Norway's fjords.",
      "The Scandinavian Mountains follow the border between which two countries?", "Norway and Sweden"),

    # ------------------------------------------------------------------ Africa
    F("Atlas Mountains", G("ATLAS MOUNTAINS"), AF,
      "Stretch about 2,500 km across Morocco, Algeria and Tunisia. The highest peak is Toubkal "
      "(4,167 m). The Sahara lies to the south.",
      "Which three countries do the Atlas Mountains cross?", "Morocco, Algeria and Tunisia"),
    F("Tibesti Mountains", G("TIBESTI MTS."), AF,
      "Volcanic massif in the central Sahara, in northern Chad and southern Libya. Its highest "
      "peak, Emi Koussi (3,415 m), is the highest point in the Sahara.",
      "Which massif holds Emi Koussi, the highest point in the Sahara?", "The Tibesti Mountains"),
    F("Ahaggar Mountains", G("AHAGGAR MTS."), AF,
      "High volcanic plateau in the Sahara of southern Algeria, also called the Hoggar. Its "
      "highest peak is Mount Tahat (2,908 m).",
      "In which country are the Ahaggar Mountains?", "Algeria"),
    F("Ruwenzori Range", G("Ruwenzori Range"), AF,
      "Small, high range on the Uganda–DR Congo border, the legendary \"Mountains of the Moon\". "
      "Its glaciers sit almost on the Equator. The highest peak is Mount Stanley (5,109 m).",
      "The Ruwenzori Range forms the border between which two countries?",
      "Uganda and DR Congo", span=1700),
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
      "Runs about 650 km through eastern California. Includes Yosemite and Lake Tahoe. The highest "
      "peak is Mount Whitney (4,421 m).",
      "Which range holds Mount Whitney, the highest peak in the contiguous US?", "The Sierra Nevada"),
    F("Cascade Range", G("CASCADE RANGE"), NA,
      "Volcanic range running from British Columbia through Washington and Oregon to northern "
      "California. Includes Mount Rainier and Mount St. Helens, which erupted catastrophically in "
      "1980.",
      "Which volcanic range includes Mount Rainier and Mount St. Helens?", "The Cascade Range"),
    F("Alaska Range", G("ALASKA RANGE"), NA,
      "Arc across southern Alaska, north of Anchorage. The highest peak is Denali (6,190 m).",
      "Which range holds Denali, North America's highest peak?", "The Alaska Range"),
    F("Brooks Range", G("BROOKS RANGE"), NA,
      "The northernmost major range in North America, running across northern Alaska into "
      "Canada's Yukon, above the Arctic Circle."),
    F("Sierra Madre Occidental", G("SIERRA MADRE OCCIDENTAL"), NA,
      "Runs about 1,250 km down western Mexico, parallel to the Pacific and the Gulf of California."),
    F("Coast Mountains", G("COAST MOUNTAINS"), NA,
      "Run about 1,600 km along the Pacific coast of British Columbia into the Alaska "
      "Panhandle, cut by fjords. Mount Waddington (4,019 m) is their highest peak.",
      "In which country are most of the Coast Mountains?", "Canada"),
    F("Sierra Madre del Sur", G("Sierra Madre del Sur"), NA,
      "Runs about 1,000 km along Mexico's Pacific coast, through Guerrero and Oaxaca, south "
      "of the main Sierra Madre ranges.",
      "Along which ocean does the Sierra Madre del Sur run?", "The Pacific Ocean"),
    F("Sierra Madre Oriental", G("SIERRA MADRE ORIENTAL"), NA,
      "Runs about 1,000 km down eastern Mexico, parallel to the Gulf of Mexico."),

    # ------------------------------------------------------------------ South America
    F("Andes", G("ANDES"), SA,
      "The world's longest continental range (about 7,000 km), along the west of South America "
      "through Venezuela, Colombia, Ecuador, Peru, Bolivia, Chile and Argentina. The highest peak "
      "is Aconcagua (6,961 m), in Argentina.",
      "Which range holds Aconcagua, the highest peak in the Americas?", "The Andes"),

    # ------------------------------------------------------------------ Oceania
    F("New Guinea Highlands", G("NEW GUINEA HIGHLANDS"), OC,
      "Chain of ranges down the centre of New Guinea, shared by Indonesia and Papua New "
      "Guinea. Puncak Jaya (4,884 m), the highest peak in Oceania, rises at its western end.",
      "Which highlands hold Puncak Jaya, the highest peak in Oceania?", "The New Guinea Highlands"),
    F("Great Dividing Range", G("GREAT DIVIDING RANGE"), OC,
      "Runs about 3,500 km down eastern Australia from Cape York to Victoria, separating the coast "
      "from the interior. The highest peak is Mount Kosciuszko (2,228 m), at its southern end.",
      "Which range holds Mount Kosciuszko, Australia's highest peak?", "The Great Dividing Range"),
    F("Southern Alps", G("SOUTHERN ALPS"), OC,
      "Run down the length of New Zealand's South Island. The highest peak is Aoraki / Mount Cook "
      "(3,724 m).",
      "Which range holds Aoraki / Mount Cook, New Zealand's highest peak?", "The Southern Alps"),

    # ------------------------------------------------------------------ Antarctica
    F("Transantarctic Mountains", G("Transantarctic Mountains"), AN,
      "Run about 3,500 km across Antarctica, from the Ross Sea to the Weddell Sea region.",
      "Which two parts of Antarctica do the Transantarctic Mountains divide?", "East Antarctica and West Antarctica"),
]
