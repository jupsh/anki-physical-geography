from features import F
from geodata import Region as G

KIND = "Plateau, plain or region"
DECK = "Plateaus, Plains & Regions"

AF, AS, EU, NA, SA, OC = "Africa", "Asia", "Europe", "North America", "South America", "Oceania"

FEATURES = [
    # ------------------------------------------------------------------ Asia
    F("Tibetan Plateau", G("PLATEAU OF TIBET"), AS,
      "The world's highest and largest plateau, averaging over 4,500 m. The Yangtze, Yellow, "
      "Mekong, Indus and Brahmaputra all rise here.",
      "What is the world's highest and largest plateau?", "The Tibetan Plateau"),
    F("Deccan Plateau", G("DECCAN PLATEAU"), AS,
      "Lies between the Western and Eastern Ghats. Ancient lava flows, the Deccan Traps, cover its "
      "northwest.",
      "Which plateau covers most of southern India?", "The Deccan Plateau"),
    F("Mongolian Plateau", G("MONGOLIAN PLATEAU"), AS,
      "High, dry plateau of steppe and desert covering Mongolia and Inner Mongolia (China). The "
      "Gobi lies on it."),
    F("Mesopotamia", G("Mesopotamia"), AS,
      "Lowland of modern Iraq, home to Sumer, Babylon and some of the earliest cities and writing.",
      "Mesopotamia, between the Tigris and Euphrates, lies mostly in which modern country?",
      "Iraq"),
    F("Sichuan Basin", G("SICHUAN BASIN"), AS,
      "Fertile, densely populated basin, ringed by mountains. Chengdu and Chongqing are in it.",
      "Which fertile, mountain-ringed basin lies in southwestern China?", "The Sichuan Basin"),
    F("West Siberian Plain", G("WESTERN SIBERIAN PLAIN"), AS,
      "Lies between the Urals and the Yenisei; much of it is swamp. Drained by the Ob and the "
      "Irtysh. Novosibirsk, Russia's third-largest city, is on it.",
      "What is one of the world's largest areas of flat land, between the Urals and the Yenisei?",
      "The West Siberian Plain"),
    F("Central Siberian Plateau", G("CENTRAL SIBERIAN PLATEAU"), AS,
      "Vast upland of forest and permafrost in Siberia, between the Yenisei and the Lena.",
      "Which vast upland of forest and permafrost lies between the Yenisei and the Lena?",
      "The Central Siberian Plateau"),
    F("Kazakh Steppe", G("KAZAKH STEPPE"), AS,
      "The world's largest dry steppe region, a grassland across northern and central Kazakhstan."),
    F("Tarim Basin", G("TARIM BASIN"), AS,
      "Large endorheic basin in Xinjiang, western China, filled by the Taklamakan Desert and "
      "ringed by the Tian Shan, Pamirs and Kunlun. The Tarim River runs along its north.",
      "Which basin does the Taklamakan Desert fill?", "The Tarim Basin"),
    F("Loess Plateau", G("Loess Plateau"), AS,
      "Plateau in north-central China blanketed in wind-blown loess silt, cut by deep gullies. "
      "The Yellow River picks up most of its silt here.",
      "From which plateau does the Yellow River pick up most of its silt?", "The Loess Plateau"),
    F("North China Plain", G("NORTH CHINA PLAIN"), AS,
      "One of the most densely populated plains on Earth, built by Yellow River silt. Beijing "
      "stands at its northern edge and the Grand Canal crosses it.",
      "Which capital city stands at the northern edge of the North China Plain?", "Beijing"),
    F("Turan Lowland", G("TURAN LOWLAND"), AS,
      "Vast lowland of Central Asia east of the Caspian Sea, covering much of Turkmenistan, "
      "Uzbekistan and southern Kazakhstan. The Karakum and Kyzylkum deserts lie in it."),
    F("Ganges Plain", G("GANGES PLAIN"), AS,
      "Fertile, densely populated plain of the Ganges and its tributaries across northern "
      "India and Bangladesh, between the Himalayas and the Deccan Plateau."),

    # ------------------------------------------------------------------ Europe
    F("North European Plain", G("NORTHERN EUROPEAN PLAIN"), EU,
      "Lowland stretching from Belgium and the Netherlands through northern Germany and Poland "
      "towards Russia. Its flat, open ground has been a route for armies for centuries."),
    F("Pontic Steppe", G("PONTIC STEPPE"), (EU, AS),
      "The western end of the Eurasian steppe, grassland north of the Black and Caspian Seas "
      "across Ukraine and southern Russia towards Kazakhstan. Historic homeland of Cossacks "
      "and of horse nomads such as the Scythians.",
      "North of which two seas does the Pontic Steppe lie?", "The Black Sea and the Caspian Sea"),

    # ------------------------------------------------------------------ Africa
    F("Sahel", G("SAHEL"), AF,
      "Semi-arid belt between the Sahara and the savannas to the south, stretching from Senegal "
      "to Sudan.",
      "Which semi-arid belt south of the Sahara stretches from Senegal to Sudan?", "The Sahel"),
    F("Ethiopian Highlands", G("ETHIOPIAN HIGHLANDS"), AF,
      "Africa's largest area of high ground, sometimes called the \"Roof of Africa\". The Blue "
      "Nile rises here.",
      "Which capital city stands in the Ethiopian Highlands?", "Addis Ababa"),
    F("Congo Basin", G("CONGO BASIN"), AF,
      "Drainage basin of the Congo River in central Africa.",
      "Which is the world's second-largest tropical rainforest?", "The Congo Basin rainforest"),
    F("Great Rift Valley", G("GREAT RIFT VALLEY"), AF,
      "Series of rift valleys where the African continent is slowly splitting apart. Its East "
      "African branches hold Lakes Turkana, Tanganyika and Malawi."),

    # ------------------------------------------------------------------ North America
    F("Canadian Shield", G("CANADIAN SHIELD"), NA,
      "A vast expanse of ancient, exposed Precambrian rock around Hudson Bay, covering about "
      "half of Canada and reaching into the northern US. Its scraped, lake-dotted surface was "
      "shaped by ice-age glaciers.",
      "Around which bay is the Canadian Shield centred?", "Hudson Bay"),
    F("Great Plains", G("GREAT PLAINS"), NA,
      "Vast, flat grassland east of the Rocky Mountains, from Canada's Prairie Provinces to Texas. "
      "Now largely farmland."),
    F("Great Basin", G("GREAT BASIN"), NA,
      "Dry region mostly in Nevada and Utah, between the Sierra Nevada and the Wasatch Range.",
      "Which dry region in Nevada and Utah has no river that reaches the sea?", "The Great Basin"),
    F("Colorado Plateau", G("COLORADO PLATEAU"), NA,
      "High desert of red rock in the US Southwest, cut by the Grand Canyon. Centred on the Four "
      "Corners, where Arizona, Utah, Colorado and New Mexico meet."),

    # ------------------------------------------------------------------ South America
    F("Amazon Basin", G("AMAZON BASIN"), SA,
      "The largest drainage basin in the world (about 7 million km²), mostly covered by the "
      "Amazon rainforest."),
    F("Brazilian Highlands", G("BRAZILIAN HIGHLANDS"), SA,
      "Plateau covering much of eastern, central and southern Brazil."),
    F("Guiana Highlands", G("GUIANA HIGHLANDS"), SA,
      "Plateau in Venezuela, Guyana and Brazil. Angel Falls, the highest waterfall in the world, "
      "drops from one of its tepuis.",
      "Which plateau in northern South America is known for its tabletop mountains (tepuis)?",
      "The Guiana Highlands"),
    F("Altiplano", G("ALTIPLANO"), SA,
      "High plateau (about 3,750 m) in the Andes, with parts in Peru, Chile and Argentina. Lake "
      "Titicaca lies at its northern end and the huge Salar de Uyuni salt flat in its south.",
      "Which country contains most of the Altiplano?", "Bolivia"),
    F("Llanos", G("LLANOS"), SA,
      "Tropical grassland plains of the Orinoco basin in Venezuela and Colombia, flooded each "
      "wet season."),
    F("Caatinga", G("CAATINGAS"), SA,
      "Semi-arid scrub and dry forest in northeastern Brazil, between the Amazon and the "
      "Atlantic. Its name is Tupi for \"white forest\", from the pale, leafless trees of the "
      "dry season.",
      "What is the semi-arid dry forest of northeastern Brazil called?", "The Caatinga"),
    F("Gran Chaco", G("GRAN CHACO"), SA,
      "Hot, semi-arid lowland of scrub forest shared by Paraguay, Bolivia and Argentina.",
      "The Gran Chaco is shared by Paraguay, Bolivia and which third country?", "Argentina"),
    F("Pantanal", G("PANTANAL"), SA,
      "The world's largest tropical wetland, mostly in western Brazil and reaching into Bolivia "
      "and Paraguay."),
    F("Pampas", G("PAMPAS"), SA,
      "Fertile grassland lowlands of Argentina, Uruguay and southern Brazil; cattle country of "
      "the gauchos."),
    F("Patagonia", G("PATAGONIA"), SA,
      "The southern end of South America, from the Andes to the Atlantic: dry steppe in the east, "
      "glaciers and fjords in the west.",
      "Which two countries share Patagonia?", "Argentina and Chile"),

    # ------------------------------------------------------------------ Oceania
    F("Western Plateau", G("WESTERN PLATEAU"), OC,
      "A vast, old plateau covering most of western and central Australia. The Great Sandy, "
      "Gibson and Great Victoria Deserts and the Nullarbor Plain all lie on it."),
    F("Murray-Darling Basin", G("MURRAY-DARLING BASIN"), OC,
      "Drainage basin of the Murray and Darling rivers, covering about a seventh of Australia "
      "in the southeast interior. It produces a large share of the country's farm output.",
      "Which basin drains about a seventh of Australia through the Murray and Darling?",
      "The Murray-Darling Basin"),
    F("Nullarbor Plain", G("NULLARBOR PLAIN"), OC,
      "Flat, almost treeless limestone plain along the Great Australian Bight.",
      "Which almost treeless limestone plain lies along the Great Australian Bight?",
      "The Nullarbor Plain"),
    F("Great Artesian Basin", G("GREAT ARTESIAN BASIN"), OC,
      "The world's largest and deepest artesian basin, an underground water store beneath about "
      "a fifth of Australia."),
]
