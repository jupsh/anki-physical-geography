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
      "South Sudan, Sudan and Egypt to the Mediterranean Sea. The Blue Nile joins it at Khartoum. "
      "In Egypt, the Aswan High Dam holds back Lake Nasser.",
      "Which capital city stands at the head of the Nile delta?", "Cairo"),
    F("Blue Nile", R("Blue Nile", "Abay"), AF,
      "Flows from Lake Tana in the Ethiopian Highlands to Khartoum, Sudan, where it joins the "
      "White Nile. It provides most of the Nile's water. Ethiopia has built the huge Grand "
      "Ethiopian Renaissance Dam on it.",
      "In which country does the Blue Nile rise?", "Ethiopia"),
    F("Congo", R("Congo", "Lualaba"), AF,
      "Africa's second-longest river (about 4,700 km) and the deepest river in the world (over "
      "220 m). It crosses the Equator twice before reaching the Atlantic.",
      "Which two capital cities face each other across the Congo?", "Kinshasa (DR Congo) and Brazzaville (Republic of the Congo)"),
    F("Niger", R("Niger"), AF,
      "West Africa's main river (about 4,180 km). Rises in Guinea, arcs northeast through Mali "
      "past Timbuktu, then flows southeast through Niger and Nigeria to a delta on the Gulf of "
      "Guinea.",
      "Which two capital cities stand on the Niger?", "Bamako (Mali) and Niamey (Niger)"),
    F("Zambezi", R("Zambezi"), AF,
      "Flows about 2,570 km from Zambia, along the Zambia–Zimbabwe border and across Mozambique to "
      "the Indian Ocean. Victoria Falls is on that border stretch, and Lake Kariba is a reservoir "
      "on it.",
      "The Zambezi forms the border between which two countries?", "Zambia and Zimbabwe"),
    F("Orange", R("Orange"), AF,
      "South Africa's longest river. Rises in Lesotho and flows west to the Atlantic, forming the "
      "South Africa–Namibia border on its lower course.",
      "Which border does the lower Orange River form?", "South Africa–Namibia"),
    F("Limpopo", R("Limpopo"), AF,
      "Arcs around northern South Africa, then crosses Mozambique to the Indian Ocean.",
      "The Limpopo forms South Africa's border with which two countries?", "Botswana and Zimbabwe"),
    F("Okavango", R("Okavango"), AF,
      "Rises in Angola and flows southeast into Botswana, where it spreads into the Okavango "
      "Delta, a vast inland wetland in the Kalahari. It never reaches the sea.",
      "Which river spreads into a vast inland delta in Botswana and never reaches the sea?",
      "The Okavango"),
    F("Senegal", R("Sénégal"), AF,
      "Rises in Guinea, crosses western Mali and flows to the Atlantic at Saint-Louis.",
      "Which border does the Senegal River form on its lower course?", "Senegal–Mauritania"),

    # ------------------------------------------------------------------ Asia
    F("Yangtze", R("Yangtze", "Tongtian", "Tuotuo"), AS,
      "Longest river in Asia (about 6,300 km). Flows east from the Tibetan Plateau across China, "
      "through Chongqing and Wuhan, to Shanghai. The Three Gorges Dam on it is the world's largest "
      "power station.",
      "Into which sea does the Yangtze flow?", "The East China Sea"),
    F("Yellow River (Huang He)", R("Huang", "Yellow"), AS,
      "China's second-longest river (about 5,460 km). Flows from the Tibetan Plateau in a great "
      "loop north and back south, then east to the Bohai Sea.",
      "What is China's second-longest river?", "The Yellow River (Huang He)"),
    F("Mekong", R("Mekong", "Za"), AS,
      "Flows about 4,900 km from Tibet through China, along the borders of Myanmar, Laos and "
      "Thailand, and across Cambodia and Vietnam to the South China Sea.",
      "Which two capital cities stand on the Mekong?", "Vientiane (Laos) and Phnom Penh (Cambodia)"),
    F("Ganges", R("Ganges"), AS,
      "Flows from the Himalayas across the plains of northern India and through Bangladesh, "
      "forming the world's largest delta with the Brahmaputra. Sacred in Hinduism; the holy city "
      "of Varanasi stands on it.",
      "Into which bay does the Ganges flow?", "The Bay of Bengal"),
    F("Brahmaputra", R("Brahmaputra", "Dihang", "Damqogkanbab"), AS,
      "Rises in Tibet, flows east along the north side of the Himalayas, then cuts south into "
      "India (Assam) and joins the Ganges in Bangladesh.",
      "Which river rises in Tibet and joins the Ganges in Bangladesh?", "The Brahmaputra"),
    F("Indus", R("Indus"), AS,
      "Rises in Tibet, flows northwest through Ladakh and then the length of Pakistan to the "
      "Arabian Sea. Gave its name to India and to the Indus Valley Civilisation.",
      "Which country contains most of the Indus's course?", "Pakistan"),
    F("Tigris", R("Tigris", "Dicle"), AS,
      "Rises in eastern Turkey and flows southeast through Iraq past Mosul to join the Euphrates. "
      "The land between the two rivers is Mesopotamia.",
      "Which capital city stands on the Tigris?", "Baghdad"),
    F("Euphrates", R("Euphrates", "Firat", "Al Furat"), AS,
      "Flows about 2,800 km from Turkey through Syria and Iraq to join the Tigris. The joined "
      "river, the Shatt al-Arab, reaches the Persian Gulf.",
      "What is the longest river in Western Asia?", "The Euphrates"),
    F("Ob", R("Ob"), AS,
      "Flows north across the West Siberian Plain from the Altai to the Gulf of Ob. Its main "
      "tributary is the Irtysh, which rises in China and crosses Kazakhstan.",
      "Into which sea does the Ob flow?", "The Kara Sea"),
    F("Yenisei", R("Yenisey"), AS,
      "Flows north from Tuva across Siberia, along the boundary between the West Siberian Plain "
      "and the Central Siberian Plateau. Lake Baikal drains into it through the Angara.",
      "Into which sea does the Yenisei flow?", "The Kara Sea"),
    F("Lena", R("Lena"), AS,
      "Flows about 4,400 km north through eastern Siberia, past Yakutsk, one of the coldest cities "
      "on Earth, to a huge delta.",
      "Into which sea does the Lena flow?", "The Laptev Sea"),
    F("Amur", R("Amur"), AS,
      "Flows east and then north to the Sea of Okhotsk. Called the Heilong Jiang (Black Dragon "
      "River) in China.",
      "For most of its length, the Amur forms the border between which two countries?", "Russia and China"),
    F("Amu Darya", R("Amu Darya", "Panj"), AS,
      "Flows from the Pamirs along Afghanistan's northern border, then through Turkmenistan and "
      "Uzbekistan towards the Aral Sea.",
      "The Amu Darya forms most of the northern border of which country?", "Afghanistan"),
    F("Syr Darya", R("Syr Darya"), AS,
      "Rises in the Tian Shan, crosses the Fergana Valley and flows through Kazakhstan towards "
      "the Aral Sea.",
      "Irrigation from the Syr Darya and Amu Darya caused which lake to shrink dramatically?", "The Aral Sea"),
    F("Salween", R("Salween", "Nu"), AS,
      "Flows about 3,300 km from Tibet through Yunnan and along the Myanmar–Thailand border "
      "to the Andaman Sea. It is one of the longest free-flowing rivers in Asia. Called the "
      "Nu in China.",
      "Which river forms much of the Myanmar–Thailand border before reaching the Andaman Sea?",
      "The Salween"),
    F("Chao Phraya", R("Chao Phraya"), AS,
      "Thailand's main river. Formed by the Ping and Nan in the north, it flows south past "
      "Ayutthaya and Bangkok to the Gulf of Thailand.",
      "Which capital city stands near the mouth of the Chao Phraya?", "Bangkok"),
    F("Pearl River", R("Pearl"), AS,
      "Drains much of southern China through the Xi and its tributaries to a delta on the "
      "South China Sea, past Guangzhou, Hong Kong and Macau.",
      "Into which sea does the Pearl River flow?", "The South China Sea"),
    F("Kolyma", R("Kolyma"), AS,
      "Flows about 2,100 km northeast through Siberia to the East Siberian Sea. Gold mining "
      "along it used Gulag prison labour under Stalin.",
      "Into which sea does the Kolyma flow?", "The East Siberian Sea"),
    F("Godavari", R("Godävari"), AS,
      "The longest river of peninsular India (about 1,470 km). Rises near Mumbai and flows "
      "east across the Deccan Plateau to the Bay of Bengal.",
      "Into which bay does the Godavari flow?", "The Bay of Bengal"),
    F("Irrawaddy", R("Irrawaddy", "Irrawaddy Delta"), AS,
      "Myanmar's main river. Flows south through the length of the country, past the former royal "
      "capital Mandalay, to a large delta.",
      "Into which sea does the Irrawaddy flow?", "The Andaman Sea"),
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
      "What is Europe's second-longest river?", "The Danube"),
    F("Rhine", R("Rhine", "Rhein", "Rhin"), EU,
      "Flows about 1,230 km from the Swiss Alps through Lake Constance, along the French–German "
      "border and through Germany to the Netherlands, where Rotterdam stands at its mouth.",
      "Into which sea does the Rhine flow?", "The North Sea"),
    F("Dnieper", R("Dnieper", "Dnepre"), EU,
      "Flows about 2,200 km south from western Russia through Belarus and Ukraine to the Black Sea.",
      "Which capital city stands on the Dnieper?", "Kyiv"),
    F("Don", R("Don"), EU,
      "Flows south through western Russia past Rostov-on-Don. A canal links it to the Volga.",
      "Into which sea does the Don flow?", "The Sea of Azov"),
    F("Vistula", R("Vistula"), EU,
      "Poland's longest river (about 1,050 km). Flows north from the Carpathians past Kraków and "
      "Warsaw to the Baltic Sea near Gdańsk.",
      "Which capital city stands on the Vistula?", "Warsaw"),
    F("Elbe", R("Elbe"), EU,
      "Rises in the Czech Republic and flows northwest through Germany, past Dresden and Hamburg.",
      "Into which sea does the Elbe flow?", "The North Sea"),
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
      "Rises in a Swiss glacier and flows through Lake Geneva and southeastern France. The Saône "
      "joins it at Lyon.",
      "Into which sea does the Rhône flow?", "The Mediterranean Sea"),
    F("Oder", R("Oder"), EU,
      "Flows about 850 km from the Czech Republic through western Poland to the Baltic Sea. "
      "Its lower course forms much of the Poland–Germany border, the Oder–Neisse line.",
      "Which border does the lower Oder form?", "Poland–Germany"),
    F("Severn", R("Severn", within=(-6, 50, -2, 54)), EU,
      "The longest river in Great Britain (about 350 km). Rises in Wales and flows through "
      "Shrewsbury, Worcester and Gloucester to the Bristol Channel, with a famous tidal bore.",
      "What is the longest river in Great Britain?", "The Severn", span=1400),
    F("Tagus", R("Tagus", "Tajo"), EU,
      "The longest river of the Iberian Peninsula (about 1,010 km). Rises in Spain, crosses "
      "Portugal and reaches the Atlantic at Lisbon. Called the Tajo in Spanish.",
      "Which capital city stands at the mouth of the Tagus?", "Lisbon"),
    F("Po", R("Po"), EU,
      "Italy's longest river (about 650 km). Flows east from the Alps past Turin across the "
      "northern Italian plain.",
      "Into which sea does the Po flow?", "The Adriatic Sea"),

    # ------------------------------------------------------------------ North America
    F("Mississippi", R("Mississippi"), NA,
      "Flows south from Lake Itasca in Minnesota, past St. Louis, Memphis and New Orleans. Its "
      "longest tributary is the Missouri.",
      "Into which gulf does the Mississippi flow?", "The Gulf of Mexico"),
    F("Missouri", R("Missouri"), NA,
      "Flows about 3,770 km from the Rocky Mountains in Montana across the Great Plains to join "
      "the Mississippi near St. Louis.",
      "Which river is usually counted as North America's longest?", "The Missouri"),
    F("Ohio", R("Ohio"), NA,
      "Flows about 1,580 km southwest from Pittsburgh, where the Allegheny and Monongahela meet, "
      "to join the Mississippi at Cairo, Illinois.",
      "By volume, what is the Mississippi's largest tributary?", "The Ohio"),
    F("Colorado", R("Colorado", within=(-117, 31, -104, 42)), NA,
      "Flows about 2,330 km from the Rocky Mountains through the US Southwest and into Mexico, "
      "carving the Grand Canyon on the way. So much water is taken from it that it rarely reaches "
      "the sea.",
      "Into which gulf does the Colorado flow, when it reaches the sea?", "The Gulf of California"),
    F("Rio Grande", R("Rio Grande"), NA,
      "Flows from Colorado through New Mexico, then forms the US–Mexico border from El Paso to "
      "the Gulf of Mexico.",
      "The Rio Grande forms much of the border between which two countries?",
      "The United States and Mexico"),
    F("St. Lawrence", R("St. Lawrence"), NA,
      "Drains the Great Lakes, flowing northeast from Lake Ontario past Montreal and Quebec City "
      "to the Gulf of St. Lawrence.",
      "Which river drains the Great Lakes to the Atlantic?", "The St. Lawrence"),
    F("Mackenzie", R("Mackenzie", within=(-140, 55, -110, 72)), NA,
      "Canada's longest river. Flows northwest from Great Slave Lake through the Northwest "
      "Territories.",
      "Into which sea does the Mackenzie flow?", "The Beaufort Sea"),
    F("Yukon", R("Yukon"), NA,
      "Rises in British Columbia and flows northwest across Canada's Yukon territory and Alaska.",
      "Into which sea does the Yukon flow?", "The Bering Sea"),
    F("Snake River", R("Snake"), NA,
      "The largest tributary of the Columbia (about 1,740 km). Rises in Yellowstone, crosses "
      "Idaho past Twin Falls and cuts Hells Canyon, the deepest river gorge in North America, "
      "before joining the Columbia in Washington.",
      "Which river cuts Hells Canyon, the deepest river gorge in North America?",
      "The Snake River"),
    F("Fraser River", R("Fraser", within=(-130, 45, -115, 60)), NA,
      "British Columbia's longest river (about 1,370 km). Rises in the Rocky Mountains and "
      "reaches the Pacific at Vancouver, through the deep Fraser Canyon.",
      "What is British Columbia's longest river?", "The Fraser River"),
    # Natural Earth labels part of the Snake "Columbia"
    F("Columbia", R("Columbia", exclude=(-117.5, 42, -109, 45)), NA,
      "Rises in the Canadian Rockies and flows through Washington to the Pacific. Its many dams "
      "make it a major source of hydroelectric power.",
      "The lower Columbia forms the border between which two US states?", "Washington and Oregon"),

    # ------------------------------------------------------------------ South America
    F("Amazon", R("Amazonas", "Ucayali"), SA,
      "Rises in the Peruvian Andes and flows east across Brazil, past Manaus, to the Atlantic. "
      "Carries about a fifth of all river water reaching the oceans.",
      "Which river carries the most water of any in the world?", "The Amazon"),
    # Natural Earth labels part of the Paraguay "Paraná"
    F("Paraná", R("Paraná", within=(-62, -35, -44, -15), exclude=(-58.5, -22, -56.5, -19)), SA,
      "Flows about 4,880 km south from Brazil along the Paraguay and Argentina borders, then joins "
      "the Uruguay River to form the Río de la Plata. The huge Itaipu Dam stands on the "
      "Brazil–Paraguay stretch.",
      "Through or along which three countries does the Paraná flow?",
      "Brazil, Paraguay and Argentina"),
    F("Orinoco", R("Orinoco"), SA,
      "Flows in a wide arc through Venezuela, forming part of the Colombia–Venezuela border, to a "
      "delta on the Atlantic. A natural channel, the Casiquiare, links it to the Amazon basin.",
      "Which country contains most of the Orinoco?", "Venezuela"),
    F("São Francisco", R("São Francisco"), SA,
      "Flows about 2,900 km through eastern Brazil, rising in Minas Gerais and reaching the "
      "Atlantic between Alagoas and Sergipe. It is the longest river entirely in Brazil.",
      "What is the longest river entirely in Brazil?", "The São Francisco"),
    F("Tocantins", R("Tocantins"), SA,
      "Flows about 2,450 km north through central Brazil to the Pará estuary near Belém, "
      "largely parallel to and east of the Amazon.",
      "In which country is the Tocantins River?", "Brazil"),
    F("Madeira", R("Madeira"), SA,
      "The Amazon's largest tributary by discharge. Formed in Bolivia by Andean rivers, it "
      "joins the Amazon east of Manaus in Brazil.",
      "What is the Amazon's largest tributary by discharge?", "The Madeira"),
    # Natural Earth labels the Paraguay's course "Paraná"
    F("Paraguay River", R("Paraná", within=(-60, -28, -55, -14), exclude=(-57, -28, -54, -24)), SA,
      "Flows about 2,550 km south from the Pantanal in Brazil, through Paraguay past Asunción, "
      "and along the Paraguay–Argentina border to join the Paraná.",
      "Which capital city stands on the Paraguay River?", "Asunción"),
    F("Magdalena", R("Magdalena"), SA,
      "Colombia's main river. Flows north between the Andean ranges.",
      "Into which sea does the Magdalena flow?", "The Caribbean Sea"),

    # ------------------------------------------------------------------ Oceania
    F("Darling River", R("Darling"), OC,
      "The Murray's main tributary (about 1,470 km). Rises in northern New South Wales and "
      "flows southwest across dry plains to join the Murray at Wentworth.",
      "Which river is the Murray's main tributary?", "The Darling River"),
    F("Murray", R("Murray"), OC,
      "Australia's longest river (about 2,500 km). Rises in the Australian Alps and reaches the "
      "sea in South Australia. Its main tributary is the Darling.",
      "The Murray forms most of the border between which two Australian states?",
      "New South Wales and Victoria"),
]
