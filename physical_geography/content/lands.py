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
      "What nickname does the Tibetan Plateau share with the Pamirs?", "The \"Roof of the World\""),
    F("Deccan Plateau", G("DECCAN PLATEAU"), AS,
      "Lies between the Western and Eastern Ghats. Ancient lava flows, the Deccan Traps, cover its "
      "northwest.",
      "Which plateau covers most of southern India?", "The Deccan Plateau"),
    F("Mongolian Plateau", G("MONGOLIAN PLATEAU"), AS,
      "High, dry plateau of steppe and desert covering Mongolia and Inner Mongolia (China). The "
      "Gobi lies on it."),
    F("Mesopotamia", G("Mesopotamia"), AS,
      "Lowland of modern Iraq, home to Sumer, Babylon and some of the earliest cities and writing.",
      "What does \"Mesopotamia\" mean in Greek?", "\"Between the rivers\" (the Tigris and Euphrates)"),
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
      "What huge explosion flattened forest on the Central Siberian Plateau in 1908?",
      "The Tunguska event"),
    F("Kazakh Steppe", G("KAZAKH STEPPE"), AS,
      "The world's largest dry steppe region, a grassland across northern and central Kazakhstan."),

    # ------------------------------------------------------------------ Europe
    F("North European Plain", G("NORTHERN EUROPEAN PLAIN"), EU,
      "Lowland stretching from Belgium and the Netherlands through northern Germany and Poland "
      "towards Russia. Its flat, open ground has been a route for armies for centuries."),

    # ------------------------------------------------------------------ Africa
    F("Sahel", G("SAHEL"), AF,
      "Semi-arid belt between the Sahara and the savannas to the south, stretching from Senegal "
      "to Sudan.",
      "What does \"Sahel\" mean in Arabic?", "\"Shore\" (of the Sahara)"),
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
    F("Great Plains", G("GREAT PLAINS"), NA,
      "Vast, flat grassland east of the Rocky Mountains, from Canada's Prairie Provinces to Texas. "
      "Now largely farmland."),
    F("Great Basin", G("GREAT BASIN"), NA,
      "Dry region mostly in Nevada and Utah, between the Sierra Nevada and the Wasatch Range.",
      "What is unusual about the Great Basin's rivers?", "None of them reach the sea; they end in lakes or evaporate"),
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
    F("Gran Chaco", G("GRAN CHACO"), SA,
      "Hot, semi-arid lowland of scrub forest shared by Paraguay, Bolivia and Argentina.",
      "Which two countries fought over the Gran Chaco in the 1930s Chaco War?", "Bolivia and Paraguay"),
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
    F("Nullarbor Plain", G("NULLARBOR PLAIN"), OC,
      "Flat, almost treeless limestone plain along the Great Australian Bight.",
      "What does \"Nullarbor\" mean?", "\"No tree\" (Latin <i>nulla arbor</i>)"),
    F("Great Artesian Basin", G("GREAT ARTESIAN BASIN"), OC,
      "The world's largest and deepest artesian basin, an underground water store beneath about "
      "a fifth of Australia."),
]
