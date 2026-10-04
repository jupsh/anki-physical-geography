from features import F
from geodata import River as R

KIND = "River"
DECK = "Rivers"

AF, AS, EU, NA, SA, OC = "Africa", "Asia", "Europe", "North America", "South America", "Oceania"

FEATURES = [
    # ------------------------------------------------------------------ Africa
    F("Nile", R("Nile", "White Nile", "Mountain Nile", "Albert Nile", "Victoria Nile",
                "Rosetta Branch", "Damietta Branch"), AF,
      "Longest river in Africa (about 6,650 km). Flows north from Lake Victoria through Uganda, "
      "South Sudan, Sudan and Egypt to the Mediterranean Sea.",
      "Which two rivers meet at Khartoum to form the Nile?", "The White Nile and the Blue Nile"),
    F("Blue Nile", R("Blue Nile", "Abay"), AF,
      "Flows from Lake Tana in the Ethiopian Highlands to Khartoum, Sudan, where it joins the "
      "White Nile. It provides most of the Nile's water.",
      "From which lake does the Blue Nile flow?", "Lake Tana (Ethiopia)"),
    F("Congo", R("Congo", "Lualaba"), AF,
      "Africa's second-longest river (about 4,700 km) and the deepest river in the world (over "
      "220 m). It crosses the Equator twice before reaching the Atlantic.",
      "Which two capital cities face each other across the Congo?", "Kinshasa (DR Congo) and Brazzaville (Republic of the Congo)"),
    F("Niger", R("Niger"), AF,
      "West Africa's main river (about 4,180 km). Rises in Guinea, arcs northeast through Mali "
      "past Timbuktu, then flows southeast through Niger and Nigeria to a delta on the Gulf of Guinea.",
      "Which historic trading city lies near the northernmost bend of the Niger?", "Timbuktu (Mali)"),
    F("Zambezi", R("Zambezi"), AF,
      "Flows about 2,570 km from Zambia, along the Zambia–Zimbabwe border and across Mozambique "
      "to the Indian Ocean. Lake Kariba is a reservoir on it.",
      "Which famous waterfall is on the Zambezi?", "Victoria Falls"),
    F("Orange", R("Orange"), AF,
      "South Africa's longest river. Rises in Lesotho and flows west to the Atlantic, forming the "
      "South Africa–Namibia border on its lower course.",
      "Which border does the lower Orange River form?", "South Africa–Namibia"),
    F("Limpopo", R("Limpopo"), AF,
      "Arcs around northern South Africa, then crosses Mozambique to the Indian Ocean.",
      "The Limpopo forms South Africa's border with which two countries?", "Botswana and Zimbabwe"),
    F("Senegal", R("Sénégal"), AF,
      "Rises in Guinea, crosses western Mali and flows to the Atlantic at Saint-Louis.",
      "Which border does the Senegal River form on its lower course?", "Senegal–Mauritania"),

    # ------------------------------------------------------------------ Asia
    F("Yangtze", R("Yangtze", "Tongtian", "Tuotuo"), AS,
      "Longest river in Asia (about 6,300 km). Flows east from the Tibetan Plateau across China, "
      "through Chongqing and Wuhan, to the East China Sea at Shanghai.",
      "Which dam on the Yangtze is the world's largest power station?", "The Three Gorges Dam"),
    F("Yellow River (Huang He)", R("Huang", "Yellow"), AS,
      "China's second-longest river (about 5,460 km). Flows from the Tibetan Plateau in a great "
      "loop north and back south, then east to the Bohai Sea.",
      "Where does the Yellow River get its colour?", "Silt (loess) picked up crossing the Loess Plateau"),
    F("Mekong", R("Mekong", "Za"), AS,
      "Flows about 4,900 km from Tibet through China, along the borders of Myanmar, Laos and "
      "Thailand, and across Cambodia and Vietnam to the South China Sea.",
      "Which two capital cities stand on the Mekong?", "Vientiane (Laos) and Phnom Penh (Cambodia)"),
    F("Ganges", R("Ganges"), AS,
      "Flows from the Himalayas across the plains of northern India and through Bangladesh to the "
      "Bay of Bengal. Sacred in Hinduism.",
      "With which river does the Ganges form the world's largest delta?", "The Brahmaputra"),
    F("Brahmaputra", R("Brahmaputra", "Dihang", "Damqogkanbab"), AS,
      "Rises in Tibet, flows east along the north side of the Himalayas, then cuts south into "
      "India (Assam) and joins the Ganges in Bangladesh.",
      "What is the Brahmaputra called in Tibet?", "The Yarlung Tsangpo"),
    F("Indus", R("Indus"), AS,
      "Rises in Tibet, flows northwest through Ladakh and then the length of Pakistan to the "
      "Arabian Sea. Gave its name to India and to the Indus Valley Civilisation.",
      "Which country contains most of the Indus's course?", "Pakistan"),
    F("Tigris", R("Tigris", "Dicle"), AS,
      "Rises in eastern Turkey and flows southeast through Iraq past Mosul to join the Euphrates. "
      "The land between the two rivers is Mesopotamia.",
      "Which capital city stands on the Tigris?", "Baghdad"),
    F("Euphrates", R("Euphrates", "Firat", "Al Furat"), AS,
      "Longest river in Western Asia (about 2,800 km). Flows from Turkey through Syria and Iraq "
      "to join the Tigris.",
      "What is the joined Tigris–Euphrates called before it reaches the Persian Gulf?", "The Shatt al-Arab"),
    F("Ob", R("Ob"), AS,
      "Flows north across the West Siberian Plain from the Altai to the Gulf of Ob on the Kara Sea.",
      "What is the Ob's main tributary, which rises in China and crosses Kazakhstan?", "The Irtysh"),
    F("Yenisei", R("Yenisey"), AS,
      "Flows north from Tuva across Siberia to the Kara Sea, along the boundary between the West "
      "Siberian Plain and the Central Siberian Plateau.",
      "Lake Baikal drains into the Yenisei through which river?", "The Angara"),
    F("Lena", R("Lena"), AS,
      "Flows about 4,400 km north through eastern Siberia to a huge delta on the Laptev Sea.",
      "Which Siberian city, one of the coldest on Earth, stands on the Lena?", "Yakutsk"),
    F("Amur", R("Amur"), AS,
      "Flows east and then north to the Sea of Okhotsk. Called the Heilong Jiang (Black Dragon "
      "River) in China.",
      "For most of its length, the Amur forms the border between which two countries?", "Russia and China"),
    F("Amu Darya", R("Amu Darya", "Panj"), AS,
      "Flows from the Pamirs along Afghanistan's northern border, then through Turkmenistan and "
      "Uzbekistan towards the Aral Sea.",
      "What was the Amu Darya called in antiquity?", "The Oxus"),
    F("Syr Darya", R("Syr Darya"), AS,
      "Rises in the Tian Shan, crosses the Fergana Valley and flows through Kazakhstan towards "
      "the Aral Sea.",
      "Irrigation from the Syr Darya and Amu Darya caused which lake to shrink dramatically?", "The Aral Sea"),
    F("Irrawaddy", R("Irrawaddy", "Irrawaddy Delta"), AS,
      "Myanmar's main river. Flows south through the length of the country to a delta on the "
      "Andaman Sea.",
      "Which former royal capital, now Myanmar's second city, stands on the Irrawaddy?", "Mandalay"),
    F("Jordan", R("Jordan"), AS,
      "Short river (about 250 km) that flows south from the slopes of Mount Hermon and forms part "
      "of the borders of Israel, the West Bank and Jordan.",
      "Which two lakes does the Jordan connect?", "The Sea of Galilee and the Dead Sea",
      span=1300),

    # ------------------------------------------------------------------ Europe
    F("Volga", R("Volga"), EU,
      "Europe's longest river (about 3,530 km). Flows entirely within Russia, past Kazan and "
      "Volgograd.",
      "Into which body of water does the Volga flow?", "The Caspian Sea"),
    F("Danube", R("Danube"), EU,
      "Europe's second-longest river (about 2,850 km). Rises in Germany's Black Forest and passes "
      "through or along ten countries to a delta in Romania on the Black Sea. Four capitals stand "
      "on it: Vienna, Bratislava, Budapest and Belgrade.",
      "Which capital's name joins those of two towns on opposite banks of the Danube?", "Budapest"),
    F("Rhine", R("Rhine", "Rhein", "Rhin"), EU,
      "Flows about 1,230 km from the Swiss Alps through Lake Constance, along the French–German "
      "border and through Germany to the North Sea in the Netherlands.",
      "Which major port lies at the mouth of the Rhine?", "Rotterdam"),
    F("Dnieper", R("Dnieper", "Dnepre"), EU,
      "Flows about 2,200 km south from western Russia through Belarus and Ukraine to the Black Sea.",
      "Which capital city stands on the Dnieper?", "Kyiv"),
    F("Don", R("Don"), EU,
      "Flows south through western Russia past Rostov-on-Don. A canal links it to the Volga.",
      "Into which sea does the Don flow?", "The Sea of Azov"),
    F("Vistula", R("Vistula"), EU,
      "Poland's longest river (about 1,050 km). Flows north from the Carpathians to the Baltic "
      "Sea near Gdańsk.",
      "Which two Polish cities, the current and a former capital, stand on the Vistula?", "Warsaw and Kraków"),
    F("Elbe", R("Elbe"), EU,
      "Rises in the Czech Republic and flows northwest through Germany, past Dresden, to the "
      "North Sea.",
      "Which major German port stands on the Elbe?", "Hamburg"),
    F("Loire", R("Loire"), EU,
      "France's longest river (about 1,010 km). Flows north and then west from the Massif "
      "Central past Orléans, Tours and Nantes. Its valley is famous for its châteaux.",
      "Into which body of water does the Loire flow?", "The Bay of Biscay (Atlantic Ocean)"),
    F("Seine", R("Seine"), EU,
      "Flows about 780 km northwest across northern France, through Paris, and reaches the sea "
      "at Le Havre.",
      "Into which body of water does the Seine flow?", "The English Channel"),
    F("Thames", R("Thames"), EU,
      "England's best-known river (about 350 km). Flows east through Oxford and London.",
      "Into which sea does the Thames flow?", "The North Sea", span=1300),
    F("Rhône", R("Rhône"), EU,
      "Rises in a Swiss glacier and flows through Switzerland and southeastern France, past Lyon, "
      "to the Mediterranean.",
      "Which large lake does the Rhône flow through?", "Lake Geneva"),
    F("Po", R("Po"), EU,
      "Italy's longest river (about 650 km). Flows east from the Alps past Turin across the "
      "northern Italian plain.",
      "Into which sea does the Po flow?", "The Adriatic Sea"),

    # ------------------------------------------------------------------ North America
    F("Mississippi", R("Mississippi"), NA,
      "Flows south from Lake Itasca in Minnesota, past St. Louis and Memphis, to the Gulf of "
      "Mexico below New Orleans.",
      "What is the Mississippi's longest tributary?", "The Missouri"),
    F("Missouri", R("Missouri"), NA,
      "Usually counted as North America's longest river (about 3,770 km). Flows from the Rocky "
      "Mountains in Montana across the Great Plains to join the Mississippi.",
      "Near which city does the Missouri join the Mississippi?", "St. Louis"),
    F("Ohio", R("Ohio"), NA,
      "Flows about 1,580 km southwest from Pittsburgh to join the Mississippi at Cairo, Illinois. "
      "By volume it is the Mississippi's largest tributary.",
      "In which city does the Ohio begin?", "Pittsburgh (where the Allegheny and Monongahela meet)"),
    F("Colorado", R("Colorado", within=(-117, 31, -104, 42)), NA,
      "Flows about 2,330 km from the Rocky Mountains through the US Southwest and into Mexico. "
      "So much water is taken from it that it rarely reaches the sea.",
      "Which famous canyon has the Colorado carved?", "The Grand Canyon"),
    F("Rio Grande", R("Rio Grande"), NA,
      "Flows from Colorado through New Mexico, then forms the US–Mexico border from El Paso to "
      "the Gulf of Mexico.",
      "What is the Rio Grande called in Mexico?", "Río Bravo (del Norte)"),
    F("St. Lawrence", R("St. Lawrence"), NA,
      "Drains the Great Lakes, flowing northeast past Montreal and Quebec City to the Gulf of "
      "St. Lawrence.",
      "From which of the Great Lakes does the St. Lawrence flow?", "Lake Ontario"),
    F("Mackenzie", R("Mackenzie", within=(-140, 55, -110, 72)), NA,
      "Canada's longest river. Flows northwest through the Northwest Territories to the "
      "Beaufort Sea.",
      "From which lake does the Mackenzie flow?", "Great Slave Lake"),
    F("Yukon", R("Yukon"), NA,
      "Rises in British Columbia and flows northwest across Canada's Yukon territory and Alaska.",
      "Into which sea does the Yukon flow?", "The Bering Sea"),
    # Natural Earth labels part of the Snake "Columbia"
    F("Columbia", R("Columbia", exclude=(-117.5, 42, -109, 45)), NA,
      "Rises in the Canadian Rockies and flows through Washington to the Pacific. Its many dams "
      "make it a major source of hydroelectric power.",
      "The lower Columbia forms the border between which two US states?", "Washington and Oregon"),

    # ------------------------------------------------------------------ South America
    F("Amazon", R("Amazonas", "Ucayali"), SA,
      "The world's largest river by volume, carrying about a fifth of all river water reaching "
      "the oceans. Rises in the Peruvian Andes and flows east across Brazil to the Atlantic.",
      "Which Brazilian city stands where the Rio Negro meets the Amazon?", "Manaus"),
    # Natural Earth labels part of the Paraguay "Paraná"
    F("Paraná", R("Paraná", within=(-62, -35, -44, -15), exclude=(-58.5, -22, -56.5, -19)), SA,
      "Flows about 4,880 km south from Brazil along the Paraguay and Argentina borders, then "
      "joins the Uruguay River to form the Río de la Plata.",
      "Which huge dam on the Paraná sits on the Brazil–Paraguay border?", "Itaipu"),
    F("Orinoco", R("Orinoco"), SA,
      "Flows in a wide arc through Venezuela, forming part of the Colombia–Venezuela border, to "
      "a delta on the Atlantic.",
      "Which natural channel links the Orinoco to the Amazon basin?", "The Casiquiare"),
    F("Magdalena", R("Magdalena"), SA,
      "Colombia's main river. Flows north between the Andean ranges.",
      "Into which sea does the Magdalena flow?", "The Caribbean Sea"),

    # ------------------------------------------------------------------ Oceania
    F("Murray", R("Murray"), OC,
      "Australia's longest river (about 2,500 km). Rises in the Australian Alps, forms most of "
      "the New South Wales–Victoria border and reaches the sea in South Australia.",
      "What is the Murray's main tributary?", "The Darling"),
]
