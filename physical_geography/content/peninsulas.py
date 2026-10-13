from features import F
from geodata import Polygon
from geodata import Region as G

KIND = "Peninsula"
DECK = "Peninsulas"

AF, AS, EU, NA, OC, AN = "Africa", "Asia", "Europe", "North America", "Oceania", "Antarctica"

FEATURES = [
    # ------------------------------------------------------------------ Asia
    F("Arabian Peninsula", G("ARABIAN PENINSULA"), AS,
      "Holds Saudi Arabia, Yemen, Oman, the UAE, Qatar and Kuwait, between the Red Sea and the "
      "Persian Gulf. The island country of Bahrain lies just off its east coast.",
      "What is the largest peninsula in the world?", "The Arabian Peninsula"),
    F("Anatolia", G("ANATOLIA"), AS,
      "The Asian part of Turkey, between the Black Sea and the Mediterranean.",
      "Anatolia lies between which two seas?", "The Black Sea and the Mediterranean Sea"),
    F("Indochina", G("INDOCHINA PENINSULA"), AS,
      "Mainland Southeast Asia: Myanmar, Thailand, Laos, Cambodia and Vietnam.",
      "Which peninsula holds mainland Southeast Asia: Myanmar, Thailand, Laos, Cambodia and "
      "Vietnam?", "Indochina"),
    F("Malay Peninsula", G("MALAY PENINSULA"), AS,
      "Long peninsula running south from Indochina, through southern Myanmar and Thailand to "
      "Peninsular Malaysia. Its tip is the southernmost point of mainland Asia.",
      "Which city-state lies at the tip of the Malay Peninsula?", "Singapore"),
    # Natural Earth has no Sinai polygon; this outline follows its coasts (the Mediterranean,
    # the Gulfs of Suez and Aqaba) and the straight Egypt–Israel border.
    F("Sinai Peninsula", Polygon((34.27, 31.31), (33.0, 31.15), (32.30, 31.26), (32.55, 29.97),
                                 (33.0, 28.60), (33.85, 27.90), (34.25, 27.72), (34.85, 28.40),
                                 (34.97, 29.50)), (AS, AF),
      "Triangular peninsula of Egypt between the Mediterranean and the Red Sea, joining "
      "Africa and Asia. The Suez Canal runs along its western edge, and Mount Sinai stands "
      "in its southern mountains.",
      "Which canal runs along the western edge of the Sinai Peninsula?", "The Suez Canal"),
    F("Shandong Peninsula", G("Shandong Pen."), AS,
      "Large peninsula in eastern China reaching into the Bohai Sea and Yellow Sea, towards "
      "Korea. Qingdao stands on its southern coast.",
      "Into which two seas does the Shandong Peninsula reach?", "The Bohai Sea and the Yellow Sea"),
    F("Korean Peninsula", G("KOREA"), AS,
      "Between the Yellow Sea and the Sea of Japan, divided between North and South Korea."),
    F("Kamchatka", G("KAMCHATKA PENINSULA"), AS,
      "Peninsula in Russia's Far East, one of the most volcanically active places on Earth.",
      "Which sea lies west of Kamchatka?", "The Sea of Okhotsk"),
    F("Chukchi Peninsula", G("CHUKCHI PENINSULA"), AS,
      "The easternmost peninsula of Asia, in Russia's far northeast.",
      "Which strait separates the Chukchi Peninsula from Alaska?", "The Bering Strait"),
    F("Taymyr Peninsula", G("TAYMYR PENINSULA"), AS,
      "Arctic peninsula in north-central Siberia. Its tip, Cape Chelyuskin, is the northernmost "
      "point of mainland Eurasia.",
      "Between which two seas does the Taymyr Peninsula lie?", "The Kara Sea and the Laptev Sea"),
    F("Yamal Peninsula", G("YAMAL PENINSULA"), AS,
      "Arctic peninsula in northwestern Siberia with some of the world's largest natural gas "
      "reserves. Home of the reindeer-herding Nenets people.",
      "Which Arctic peninsula in northwestern Siberia holds some of the world's largest "
      "natural gas reserves?", "The Yamal Peninsula"),

    # ------------------------------------------------------------------ Europe
    F("Iberian Peninsula", G("PENÍNSULA IBÉRICA"), EU,
      "Holds Spain, Portugal, Andorra and Gibraltar. Cut off from France by the Pyrenees.",
      "Which strait separates the Iberian Peninsula from Africa?", "The Strait of Gibraltar"),
    F("Jutland", G("JUTLAND"), EU,
      "Peninsula between the North Sea and the Baltic, including northern Germany "
      "(Schleswig-Holstein).",
      "Which country makes up most of Jutland?", "Denmark"),
    F("Crimea", G("CRIMEA"), EU,
      "Peninsula in the Black Sea, joined to mainland Ukraine by the narrow Isthmus of Perekop. "
      "Annexed by Russia in 2014.",
      "Which sea lies northeast of Crimea?", "The Sea of Azov"),
    F("Kola Peninsula", G("KOLA PENINSULA"), EU,
      "Russian peninsula in the far northwest. The ice-free Arctic port of Murmansk stands at its "
      "base.",
      "Which two seas border the Kola Peninsula?", "The Barents Sea and the White Sea"),
    F("Peloponnese", G("Pelopónnisos"), EU,
      "Southern part of mainland Greece, home of ancient Sparta and Olympia.",
      "What joins (and, since a canal was cut, separates) the Peloponnese and the Greek mainland?",
      "The Isthmus of Corinth"),
    F("Brittany", G("Bretagne"), EU,
      "Peninsula in northwestern France, between the English Channel and the Bay of Biscay, with "
      "a Celtic language and culture."),

    # ------------------------------------------------------------------ Africa
    F("Horn of Africa", G("SOMALI PENINSULA"), AF,
      "Africa's easternmost projection, also called the Somali Peninsula. It includes Somalia "
      "and parts of Ethiopia, Djibouti and Eritrea.",
      "Which gulf lies north of the Horn of Africa?", "The Gulf of Aden"),

    # ------------------------------------------------------------------ North America
    F("Yucatán Peninsula", G("PEN. DE YUCATÁN"), NA,
      "Separates the Gulf of Mexico from the Caribbean. Shared by Mexico, Belize and Guatemala, "
      "with many Maya ruins.",
      "Which impact crater, linked to the extinction of the dinosaurs, is buried under the Yucatán?",
      "Chicxulub"),
    F("Baja California", G("BAJA CALIFORNIA"), NA,
      "Long, narrow Mexican peninsula south of California.",
      "Which gulf separates Baja California from mainland Mexico?", "The Gulf of California"),
    F("Florida", G("FLORIDA"), NA,
      "Peninsula in the southeastern US, between the Gulf of Mexico and the Atlantic. The "
      "Everglades wetland covers much of its southern tip."),
    F("Seward Peninsula", G("Seward Peninsula"), NA,
      "Peninsula on Alaska's western coast, reaching into the Bering Strait towards Russia. "
      "Nome, of the gold-rush and Iditarod fame, stands on its southern shore.",
      "Which strait does the Seward Peninsula reach into?", "The Bering Strait"),
    F("Alaska Peninsula", G("ALASKA PENINSULA"), NA,
      "Extends about 800 km southwest from mainland Alaska. The Aleutian Islands continue its "
      "line.",
      "Which two bodies of water does the Alaska Peninsula separate?",
      "The Pacific Ocean and the Bering Sea"),

    # ------------------------------------------------------------------ Oceania
    F("Cape York Peninsula", G("CAPE YORK PEN."), OC,
      "Northern tip of Queensland, Australia, pointing towards New Guinea.",
      "Which strait separates Cape York from New Guinea?", "The Torres Strait"),
    F("Arnhem Land", G("ARNHEM LAND"), OC,
      "Peninsula in the northeast of Australia's Northern Territory, largely owned by Aboriginal "
      "people."),

    # ------------------------------------------------------------------ Antarctica
    F("Antarctic Peninsula", G("Antarctic Peninsula"), AN,
      "The northernmost part of Antarctica, reaching towards South America. One of the "
      "fastest-warming places on Earth.",
      "Which passage separates the Antarctic Peninsula from South America?", "The Drake Passage"),
]
