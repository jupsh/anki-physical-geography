from features import F
from geodata import Peak as P

KIND = "Volcano"
DECK = "Volcanoes"

AF, AS, EU, NA, SA, OC, AN = ("Africa", "Asia", "Europe", "North America", "South America",
                              "Oceania", "Antarctica")

FEATURES = [
    # ------------------------------------------------------------------ Europe
    F("Mount Etna", P("Mount Etna"), EU,
      "One of the world's most active volcanoes (about 3,350 m), on the east coast of Sicily. "
      "In almost constant activity, with frequent lava flows down its flanks.",
      "Which volcano on Sicily is one of the most active in the world?", "Mount Etna"),
    F("Mount Vesuvius", P("Mount Vesuvius"), EU,
      "Volcano overlooking the Bay of Naples (about 1,280 m). Its eruption in AD 79 buried the "
      "Roman cities of Pompeii and Herculaneum.",
      "Which volcano buried Pompeii in AD 79?", "Mount Vesuvius"),
    F("Teide", P("Teide"), AF,
      "Volcano on Tenerife in the Canary Islands (3,718 m). The highest peak in Spain, and the "
      "third-largest volcano in the world from its base on the ocean floor.",
      "What is the highest peak in Spain?", "Teide"),

    # ------------------------------------------------------------------ Asia
    F("Mount Fuji", P("Mount Fuji"), AS,
      "Japan's highest peak (3,776 m), a symmetrical stratovolcano southwest of Tokyo. Sacred in "
      "Shinto tradition and last erupted in 1707.",
      "What is Japan's highest peak?", "Mount Fuji"),
    F("Klyuchevskaya Sopka", P("Klyuchevskaya Sopka"), AS,
      "The highest active volcano in Eurasia (about 4,750 m), on Russia's Kamchatka Peninsula, "
      "one of the most volcanically active regions on Earth.",
      "Which volcano is the highest active volcano in Eurasia?", "Klyuchevskaya Sopka"),
    F("Krakatoa", P("Krakatoa"), AS,
      "Volcanic island in the Sunda Strait between Java and Sumatra. Its 1883 eruption was one "
      "of the loudest sounds ever recorded, and a new cone, Anak Krakatau, has grown in its caldera.",
      "Which volcano in the Sunda Strait erupted catastrophically in 1883?", "Krakatoa",
      span=1600),
    F("Tambora", P("Tambora"), AS,
      "Volcano on Sumbawa island. Its 1815 eruption was the largest in recorded history and "
      "caused the global \"Year Without a Summer\" in 1816.",
      "Which volcano's 1815 eruption caused the \"Year Without a Summer\"?", "Tambora",
      span=1600),
    F("Mount Pinatubo", P("Mount Pinatubo"), AS,
      "Volcano on Luzon in the Philippines. Its 1991 eruption was the second-largest of the "
      "20th century and cooled the global climate for several years.",
      "Which Philippine volcano erupted massively in 1991?", "Mount Pinatubo", span=1600),

    # ------------------------------------------------------------------ Africa
    F("Mount Kilimanjaro", P("Mount Kilimanjaro"), AF,
      "A dormant stratovolcano in northern Tanzania (5,895 m) and Africa's highest peak. Its "
      "summit glaciers are shrinking rapidly.",
      "What is Africa's highest peak?", "Mount Kilimanjaro"),

    # ------------------------------------------------------------------ North America
    F("Popocatépetl", P("Popocatépetl"), NA,
      "Active stratovolcano (about 5,420 m) between Mexico City and Puebla, and one of Mexico's "
      "most closely watched volcanoes. Its name is Nahuatl for \"Smoking Mountain\".",
      "Which active volcano, one of Mexico's most watched, stands between Mexico City and "
      "Puebla?", "Popocatépetl"),
    F("Mount Rainier", P("Mount Rainier"), NA,
      "The most heavily glaciated peak in the contiguous US (4,392 m), a Cascade volcano "
      "overlooking Seattle and Tacoma.",
      "Which Cascade volcano overlooks Seattle and Tacoma?", "Mount Rainier"),

    # ------------------------------------------------------------------ South America
    F("Chimborazo", P("Chimborazo"), SA,
      "An inactive stratovolcano in Ecuador (6,263 m) and the country's highest peak. Because "
      "Earth bulges at the Equator, its summit is the farthest point from Earth's centre.",
      "Which summit is the farthest point from Earth's centre?", "Chimborazo"),

    # ------------------------------------------------------------------ Oceania
    F("Mount Ruapehu", P("Mount Ruapehu"), OC,
      "New Zealand's largest active volcano (2,797 m), at the southern end of the Taupō Volcanic "
      "Zone on the North Island. It holds a crater lake between eruptions.",
      "What is New Zealand's largest active volcano?", "Mount Ruapehu", span=1600),

    # ------------------------------------------------------------------ Antarctica
    F("Mount Erebus", P("Mount Erebus"), AN,
      "The world's southernmost active volcano (3,794 m), on Ross Island. It holds one of the "
      "few long-lived lava lakes on Earth.",
      "What is the world's southernmost active volcano?", "Mount Erebus", span=1600),
]
