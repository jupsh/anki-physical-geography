from features import F
from geodata import Lake as L

KIND = "Lake"
DECK = "Lakes"

AF, AS, EU, NA, SA, OC = "Africa", "Asia", "Europe", "North America", "South America", "Oceania"

FEATURES = [
    # ------------------------------------------------------------------ North America
    F("Lake Superior", L("Superior"), NA,
      "The largest and deepest of the Great Lakes, shared by the US and Canada.",
      "What is the largest freshwater lake in the world by area?", "Lake Superior (about 82,000 km²)"),
    F("Lake Michigan", L("Michigan"), NA,
      "One of the Great Lakes. Chicago and Milwaukee are on its shores.",
      "Which Great Lake lies entirely within the United States?", "Lake Michigan"),
    F("Lake Huron", L("Huron"), NA,
      "The second-largest Great Lake, shared by the US and Canada. Includes Georgian Bay.",
      "Which Great Lake is joined to Lake Michigan by the Straits of Mackinac?", "Lake Huron"),
    F("Lake Erie", L("Erie"), NA,
      "The shallowest of the Great Lakes, shared by the US and Canada.",
      "Water from Lake Erie flows to Lake Ontario over which falls?", "Niagara Falls"),
    F("Lake Ontario", L("Ontario"), NA,
      "The smallest Great Lake by area, and the last before the St. Lawrence River.",
      "Which major Canadian city stands on Lake Ontario?", "Toronto"),
    F("Great Bear Lake", L("Great Bear"), NA,
      "Lake in Canada's Northwest Territories, on the Arctic Circle.",
      "What is the largest lake entirely within Canada?", "Great Bear Lake"),
    F("Great Slave Lake", L("Great Slave"), NA,
      "Lake in Canada's Northwest Territories, and the deepest lake in North America (about 614 m).",
      "Which river flows out of Great Slave Lake?", "The Mackenzie"),
    F("Lake Winnipeg", L("Winnipeg"), NA,
      "Large, shallow lake in Manitoba, Canada. It drains through the Nelson River to Hudson Bay."),
    F("Great Salt Lake", L("Great Salt"), NA,
      "The largest salt lake in the Western Hemisphere, a remnant of a much larger Ice Age lake.",
      "In which US state is the Great Salt Lake?", "Utah"),
    F("Lake Nicaragua", L("Nicaragua"), NA,
      "The largest lake in Central America. It has volcanic islands and bull sharks that swim up "
      "from the Caribbean."),

    # ------------------------------------------------------------------ South America
    F("Lake Titicaca", L("Titicaca"), SA,
      "Lies in the Andes at about 3,810 m. The largest lake in South America by volume, and often "
      "called the highest navigable lake in the world.",
      "Which two countries share Lake Titicaca?", "Peru and Bolivia"),

    # ------------------------------------------------------------------ Africa
    F("Lake Victoria", L("Lake Victoria"), AF,
      "Africa's largest lake (about 68,800 km²) and the main source of the White Nile.",
      "Which three countries share Lake Victoria?", "Uganda, Kenya and Tanzania"),
    F("Lake Tanganyika", L("Tanganyika"), AF,
      "The world's longest freshwater lake (about 670 km) and second-deepest (about 1,470 m), in "
      "the Great Rift Valley.",
      "Which four countries border Lake Tanganyika?", "Tanzania, DR Congo, Burundi and Zambia"),
    F("Lake Malawi", L("Malawi"), AF,
      "Deep Rift Valley lake with more species of fish than any other lake, most of them cichlids.",
      "Which three countries border Lake Malawi?", "Malawi, Mozambique and Tanzania"),
    F("Lake Chad", L("Chad"), AF,
      "Shallow lake on the edge of the Sahara. It has shrunk by about 90% since the 1960s.",
      "Which four countries border Lake Chad?", "Chad, Cameroon, Niger and Nigeria"),
    F("Lake Turkana", L("Turkana"), AF,
      "The world's largest permanent desert lake, in the Great Rift Valley. Its northern tip "
      "reaches Ethiopia.",
      "Which country contains most of Lake Turkana?", "Kenya"),
    F("Lake Tana", L("Tana"), AF,
      "Ethiopia's largest lake, in the Ethiopian Highlands.",
      "Which river flows out of Lake Tana?", "The Blue Nile"),

    # ------------------------------------------------------------------ Asia
    F("Lake Baikal", L("Baikal"), AS,
      "Lake in southern Siberia, Russia. The oldest lake on Earth (about 25 million years) and "
      "holds about a fifth of the world's unfrozen fresh surface water.",
      "What is the deepest lake in the world?", "Lake Baikal (about 1,640 m)"),
    F("Lake Balkhash", L("Balkhash"), AS,
      "Long lake in southeastern Kazakhstan. Its western half is fresh and its eastern half salty."),
    F("Issyk-Kul", L("Issyk-Kul"), AS,
      "Large high-altitude lake in the Tian Shan. Slightly salty, it never freezes despite the "
      "cold winters.",
      "In which country is Issyk-Kul?", "Kyrgyzstan"),
    F("Qinghai Lake", L("Qinghai"), AS,
      "China's largest lake, a salt lake on the northeastern edge of the Tibetan Plateau."),
    F("Tonlé Sap", L("Tonlé Sap"), AS,
      "The largest freshwater lake in Southeast Asia, in Cambodia. It grows several times larger "
      "in the wet season.",
      "What unusual thing happens to the Tonlé Sap river each wet season?",
      "Its flow reverses: Mekong floodwater pushes water back up into the lake"),

    # ------------------------------------------------------------------ Europe
    F("Lake Ladoga", L("Ladoga"), EU,
      "Lake in northwestern Russia, near St. Petersburg.",
      "What is the largest lake in Europe?", "Lake Ladoga (about 17,700 km²)"),
    F("Lake Onega", L("Onega"), EU,
      "Europe's second-largest lake, in northwestern Russia, east of Lake Ladoga."),
    F("Vänern", L("Vänern"), EU,
      "Lake in southwestern Sweden, draining to the Kattegat at Gothenburg.",
      "What is the largest lake in the European Union?", "Vänern (Sweden)"),
    F("Lake Geneva", L("Lake Geneva"), EU,
      "Crescent-shaped lake on the north side of the Alps. The Rhône flows through it.",
      "Which two countries share Lake Geneva?", "Switzerland and France"),
    F("Lake Constance", L("Constance"), EU,
      "Lake on the Rhine at the northern foot of the Alps. Called the Bodensee in German.",
      "Which three countries border Lake Constance?", "Germany, Austria and Switzerland"),

    # ------------------------------------------------------------------ Oceania
    F("Lake Eyre (Kati Thanda)", L("Eyre North"), OC,
      "Australia's largest lake when it fills, which is rare; usually a dry salt pan. It is in "
      "South Australia.",
      "What is the lowest point in Australia?", "Lake Eyre (about 15 m below sea level)"),
]
