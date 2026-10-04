from features import F
from geodata import Region as G

KIND = "Desert"
DECK = "Deserts"

AF, AS, NA, SA, OC = "Africa", "Asia", "North America", "South America", "Oceania"

FEATURES = [
    # ------------------------------------------------------------------ Africa
    F("Sahara", G("SAHARA"), AF,
      "The world's largest hot desert (about 9 million km²), covering most of North Africa from "
      "the Atlantic to the Red Sea.",
      "What is the semi-arid belt along the Sahara's southern edge called?", "The Sahel"),
    F("Nubian Desert", G("NUBIAN DESERT"), AF,
      "Eastern part of the Sahara in northeastern Sudan, between the Nile and the Red Sea."),
    F("Kalahari", G("KALAHARI DESERT"), AF,
      "Semi-arid sandy savanna covering most of Botswana and parts of Namibia and South Africa.",
      "Which great inland river delta lies in the northern Kalahari?", "The Okavango Delta"),
    F("Namib", G("NAMIB DESERT"), AF,
      "Coastal desert along the Atlantic coast of Namibia, reaching into Angola and South Africa. "
      "Possibly the world's oldest desert, with some of its tallest dunes.",
      "Which cold ocean current helps keep the Namib dry?", "The Benguela Current"),
    F("Danakil Desert", G("Danakil"), AF,
      "Lowland desert in the Afar region of Ethiopia, Eritrea and Djibouti. Parts lie over 100 m "
      "below sea level, and it is one of the hottest places on Earth."),

    # ------------------------------------------------------------------ Asia
    F("Rub' al Khali", G("RUB’ AL KHALI"), AS,
      "The largest continuous sand desert in the world, covering southern Saudi Arabia and parts "
      "of Oman, the UAE and Yemen.",
      "What does \"Rub' al Khali\" mean?", "The Empty Quarter"),
    F("Syrian Desert", G("SYRIAN DESERT"), AS,
      "Stony desert covering parts of Syria, Jordan, Iraq and Saudi Arabia, between the "
      "Euphrates valley and the Levant."),
    F("Negev", G("Negev Desert"), AS,
      "Rocky desert in the south of Israel, ending at the Gulf of Aqaba.",
      "The Negev covers more than half of which country?", "Israel"),
    F("Gobi", G("GOBI DESERT"), AS,
      "Cold desert of rock and gravel more than sand. Famous for dinosaur fossils, including the "
      "first dinosaur eggs to be recognised as such.",
      "Which two countries does the Gobi span?", "Mongolia and China"),
    F("Taklamakan", G("TAKLIMAKAN DESERT"), AS,
      "Sand desert in Xinjiang, western China, ringed by the Tian Shan and Kunlun Mountains. The "
      "Silk Road split to pass around its edges.",
      "Which basin does the Taklamakan fill?", "The Tarim Basin"),
    F("Karakum", G("GARAGUM DESERT"), AS,
      "Sand desert east of the Caspian Sea. Home to the Darvaza gas crater, the \"Door to Hell\".",
      "Which country does the Karakum cover about 70% of?", "Turkmenistan"),
    F("Kyzylkum", G("QIZILQUM DESERT"), AS,
      "Desert in Uzbekistan and Kazakhstan, southeast of the Aral Sea. The name means \"red sand\".",
      "Between which two rivers does the Kyzylkum lie?", "The Amu Darya and the Syr Darya"),
    F("Thar Desert", G("THAR DESERT"), AS,
      "The Great Indian Desert, on the India–Pakistan border.",
      "Which Indian state contains most of the Thar?", "Rajasthan"),
    F("Dasht-e Lut", G("LUT DESERT"), AS,
      "Desert in southeastern Iran. Satellites have measured some of the hottest ground "
      "temperatures on Earth here, above 70 °C."),
    F("Dasht-e Kavir", G("Kavir Desert"), AS,
      "The \"Great Salt Desert\" of central Iran, a plateau of salt crusts and marshes."),

    # ------------------------------------------------------------------ North America
    F("Sonoran Desert", G("SONORAN DESERT"), NA,
      "Desert in Arizona, southeastern California and northwestern Mexico, around the head of "
      "the Gulf of California.",
      "Which giant cactus is the symbol of the Sonoran Desert?", "The saguaro"),
    F("Chihuahuan Desert", G("CHIHUAHUAN DESERT"), NA,
      "The largest hot desert in North America, on the plateau of northern Mexico and reaching "
      "into Texas and New Mexico."),

    # ------------------------------------------------------------------ South America
    F("Atacama", G("DESIERTO DE ATACAMA"), SA,
      "The driest non-polar desert on Earth, along the Pacific coast. Some weather stations "
      "there have never recorded rain. The cold Humboldt Current helps keep it dry.",
      "Which country contains most of the Atacama?", "Chile"),

    # ------------------------------------------------------------------ Oceania
    F("Great Victoria Desert", G("GREAT VICTORIA DESERT"), OC,
      "Australia's largest desert, spanning Western Australia and South Australia."),
    F("Great Sandy Desert", G("GREAT SANDY DESERT"), OC,
      "Australia's second-largest desert, in the north of Western Australia."),
    F("Gibson Desert", G("Gibson Desert"), OC,
      "Desert in Western Australia, between the Great Sandy and Great Victoria Deserts.",
      span=4200),
    F("Simpson Desert", G("Simpson Desert"), OC,
      "Desert in central Australia, known for its long, parallel red sand dunes.",
      "Which three Australian states and territories meet in the Simpson Desert?",
      "Northern Territory, Queensland and South Australia", span=4200),
]
