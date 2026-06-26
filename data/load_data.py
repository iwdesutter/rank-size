import csv
import json

def get_states_pops_demo_am():
  return {
    "ARG": [2960976, 1148305, 1111811, 894645, 641541, 572769, 520647, 519707, 509445, 470604, 466755, 407506, 367099, 346620, 342796, 299022, 289142, 257766, 255145, 228199, 206848, 201943, 181318, 167078, 153855, 141496, 133741, 123672, 121739, 119492, 114752, 110269],
    "BOL": [784976, 767260, 448756, 446189, 201831, 144994, 123327],
    "BRA": [9842059, 5547033, 2174072, 2060804, 1846955, 1601094, 1364320, 1314857, 1297592, 1280114, 1078277, 957564, 878690, 831210, 807774, 792917, 738327, 683451, 666071, 639160, 636904, 627850, 590896, 584140, 565943, 526086, 513740, 478317, 468678, 450690, 442786, 435647, 430350, 425974, 419477, 405116, 402341, 399327, 397553, 388483, 385068, 372203, 370279, 351441, 339641, 318305, 310161, 302498, 300283, 299927, 299592, 296770, 294628, 294444, 290641, 289047, 285955, 281464, 278873, 277482, 276149, 273759, 267448, 266858, 262422, 259879, 252533, 247385, 245870, 242026, 239429, 239378, 236369, 234344, 227266, 226534, 221329, 220980, 220690, 220244, 217489, 217418, 213968, 213370, 202684, 201872, 201222, 197459, 195943, 194237, 192255, 185671, 185122, 184692, 180568, 180013, 179682, 179273, 178483, 177411, 177159, 176891, 176446, 174507, 173624, 172047, 170931, 170690, 170349, 168655, 167838, 167302, 166731, 166269, 166215, 164921, 164792, 159979, 159557, 159197, 157260, 156928, 156865, 154896, 154214, 153840, 153455, 151385, 151064, 149512, 149160, 148572, 148272, 147215, 146638, 145961, 143005, 142873, 142046, 141929, 140221, 138270, 137108, 134606, 133257, 131518, 131239, 130923, 127953, 127091, 125686, 125266, 124447, 122288, 121981, 121866, 121146, 120441, 118967, 117773, 117432, 117241, 116951, 116894, 116674, 114056, 113051, 112939, 112477, 112041, 109220, 109166, 108544, 108326, 107584, 106882, 106784, 106457, 106183, 106111, 105804, 105246, 103761, 103315, 102852, 102164, 102072, 101842, 101447, 101034, 100377, 100249, 100016],
    "CAN": [1017666, 710677, 635395, 616790, 616741, 562564, 524598, 471844, 463388, 341322, 318499, 314398, 313987, 309993, 245173, 234445, 191435, 186058, 179178, 168282, 167517, 158858, 153811, 140525, 129874, 129575, 129344, 129300, 126624, 114670, 114455, 113946, 111359, 107627, 102696, 101677],
    "CHL": [4229970, 350268, 322220, 318898, 282168, 260915, 239340, 236730, 206315, 193755, 173336, 169448, 157083, 152592, 123055, 122399, 119431, 117983, 117206, 110340],
    "COL": [3974813, 1452392, 1369331, 917486, 513986, 383584, 351687, 283365, 280638, 241927, 211203, 203742, 192409, 181157, 179908, 175687, 168291, 165829, 162556, 162056, 150838, 149019, 142153, 141516, 139050, 122484, 103123, 100691]
  }

def get_states_pops_demo_as():
  return {
    "AFG": [1424400, 225500, 177300, 130600],
    "CHN": [8205598, 7362426, 6190000, 5804023, 5124868, 4655280, 3918010, 3832536, 3824748, 3597404, 3483834, 3473832, 3350851, 3273010, 3204669, 3191974, 3181985, 3122704, 3037535, 2985978, 2980870, 2872539, 2769300, 2613804, 2610594, 2589504, 2484206, 2478650, 2403946, 2251848, 2224580, 2215666, 1844471, 1827593, 1827306, 1814936, 1770370, 1769568, 1769315, 1752374, 1736869, 1733287, 1701059, 1664709, 1650419, 1617761, 1611969, 1602029, 1590160, 1578461, 1531117, 1521879, 1484515, 1484085, 1465656, 1413036, 1409748, 1400591, 1395739, 1395094, 1391056, 1388427, 1388011, 1377391, 1372109, 1368850, 1361240, 1358733, 1350134, 1328950, 1323410, 1293507, 1289184, 1286664, 1280027, 1277310, 1271268, 1262031, 1259604, 1255045, 1228772, 1228052, 1202192, 1199382, 1198295, 1160775, 1159099, 1154798, 1099523, 1097616, 1078010, 1077721, 1056597, 1048720, 1039750, 1027724, 1027570, 1024589, 1018911, 1017021, 1006665, 1004712, 996866, 992399, 989749, 987301, 980541, 977147, 962955, 945648, 944932, 938470, 937805, 892235, 888631, 884543, 882236, 875176, 872657, 869242, 863999, 859913, 859165, 838309, 836105, 835496, 828191, 824137, 817331, 797432, 791224, 769958, 768944, 766268, 764267, 759557, 752742, 751311, 750585, 744584, 743720, 743165, 738722, 736869, 736297, 733795, 729893, 727256, 722896, 721841, 719672, 712574, 697780, 695040, 693148, 685477, 685192, 677045, 673606, 672759, 672267, 667707, 660518, 657856, 648605, 647021, 644494, 644301, 642474, 639553, 639436, 631572, 619521, 616803, 608213, 607781, 594966, 593451, 585646, 583805, 582690, 581982, 579415, 574832, 571513, 571068, 569378, 563064, 557742, 557346, 552932, 552255, 546290, 544846, 537355, 535823, 534147, 532715, 525580, 522725, 518912, 511326, 511239, 502080, 494656, 492291, 492286, 489178, 488343, 486589, 481196, 477127, 474835, 469959, 469903, 467127, 466995, 464112, 460413, 454971, 452849, 452286, 448140, 446324, 445216, 444586, 441706, 434062, 433621, 432235, 430513, 429410, 429351, 428314, 425973, 417667, 417154, 416926, 416634, 416043, 414031, 412211, 411073, 410530, 410050, 408466, 403897, 403684, 402418, 400823, 396001, 394516, 394321, 391837, 391454, 386325, 384703, 384569, 382654, 382026, 377346, 376521, 374600, 369995, 369335, 366998, 365519, 361223, 360813, 360045, 353330, 351645, 348857, 345502, 344348, 343909, 341637, 339371, 335043, 331065, 329781, 324831, 324040, 323933, 321381, 321271, 317313, 316362, 315487, 314842, 314392, 311336, 310037, 309543, 306948, 302077, 300428, 298915, 298694, 297590, 297377, 295202, 294080, 293069, 289844, 288501, 284935, 284344, 282945, 279611, 279456, 279178, 274689, 273175, 270435, 257705, 257073, 256458, 249162, 248303, 248163, 245718, 244581, 243448, 243141, 238713, 235667, 233917, 232349, 232098, 230621, 229907, 229136, 215040, 214624, 212104, 208038, 206620, 206594, 203025, 200092, 199600, 193085, 191447, 187792, 183755, 178480, 173926, 170631, 168714, 167570, 165360, 163710, 158610, 156907, 147026, 139822, 137824, 137790, 137236, 135222, 129952, 128626, 123095, 122579, 116470, 114600, 112756, 109987, 105841, 102109],
    "IND": [9925891, 7206704, 4399819, 3841396, 2964638, 2876710, 2660088, 1874409, 1624752, 1619115, 1566651, 1498817, 1062771, 1042740, 1031346, 950435, 940989, 929270, 917243, 891790, 816321, 803389, 792858, 753778, 752037, 708835, 701827, 690765, 656925, 648298, 617717, 604215, 599306, 587211, 586038, 584342, 573272, 564589, 559407, 537371, 524006, 505566, 504094, 480692, 480520, 471051, 454156, 447657, 438639, 429214, 425836, 421576, 419831, 416289, 411542, 406370, 403418, 402700, 402338, 387223, 386159, 379070, 374945, 369077, 366712, 362266, 342595, 333683, 328034, 326399, 324851, 316606, 308571, 304952, 304099, 301297, 291675, 278317, 275990, 275083, 273304, 270159, 266082, 262188, 253225, 245391, 245079, 243742, 241107, 241034, 240609, 238368, 237713, 236800, 235661, 232811, 226691, 226105, 224821, 218391, 216950, 216096, 215128, 214950, 214384, 212866, 210418, 205086, 203065, 202013, 201323, 199854, 197408, 195346, 194567, 193197, 191212, 190255, 190084, 186939, 184474, 183965, 183375, 182477, 181339, 179833, 179258, 177989, 175061, 174924, 174666, 174369, 173751, 172710, 172677, 169336, 167051, 164364, 163431, 161482, 160359, 159232, 159110, 159042, 157551, 157358, 157082, 156630, 155240, 154367, 151806, 151789, 151045, 150869, 150645, 150112, 148583, 148519, 148272, 147305, 147217, 147124, 146514, 146262, 145143, 145133, 144561, 144346, 143922, 143726, 140408, 139852, 139483, 139204, 138903, 137061, 137028, 136877, 136842, 136697, 136182, 135825, 135400, 134051, 133914, 133462, 133265, 133102, 132701, 131719, 131138, 129904, 128981, 127992, 127201, 126089, 125498, 125371, 125199, 125037, 124501, 124437, 124072, 123930, 123359, 123289, 122705, 121842, 121629, 121486, 121463, 121314, 121110, 120378, 120265, 120127, 119813, 119796, 119338, 118080, 117675, 116833, 116695, 116671, 115483, 115144, 114912, 114876, 114202, 114085, 113285, 112841, 112434, 110266, 109956, 109755, 109470, 109196, 108578, 108304, 108277, 108016, 107592, 107425, 107163, 106605, 106523, 105363, 104651, 104585, 104195, 103579, 102985, 102176, 101660, 101656, 101409, 100836, 100490, 100347, 100223, 100079, 96813, 96322, 95661, 90803, 90357, 86006, 85442, 82054, 80861, 80440, 74604, 72434, 65238, 63155, 61997, 57909, 57165, 49692, 43326],
    "IDN": [9160500, 2701300, 2368200, 1909700, 1366500, 1352300, 1198300, 1091800, 832400, 763400, 721500, 558200, 536100, 534600, 516500, 449100, 435000, 419500, 416200, 410400, 398900, 341400, 313400, 313100, 306600, 291300, 285000, 284275, 262300, 262100, 261300, 230900, 206800, 190100, 180400, 170900, 168200, 162800, 148700, 132900, 129300, 125400, 124000, 123100, 122600, 114700, 109700, 107100, 106600, 103000],
    "IRN": [6750043, 1964489, 1220595, 1166203, 1042801, 828380, 780453, 665636, 588287, 419886, 413299, 406070, 396392, 383515, 378597, 374475, 349626, 329869, 306268, 298705, 280691, 277370, 271314, 239716, 212056, 202004, 192912, 185899, 182028, 178080, 166080, 160755, 154796, 154511, 153473, 152536, 149774, 140615, 136759, 133216, 128717, 127415, 125661, 120224, 114944, 109224],
    "IRQ": [3841268, 664221, 521444, 485968, 464151, 418624, 406296, 364096, 309010, 296705, 268834, 265937, 244545, 235554, 208797, 196519, 192556, 183183]
  }

def get_full_name_world():
  return {
    "AFG": "Afghanistan",
    "ALB": "Albania",
    "DZA": "Algeria",
    "ASM": "American Samoa",
    "AND": "Andorra",
    "AGO": "Angola",
    "AIA": "Anguilla",
    "ATA": "Antarctica",
    "ATG": "Antigua and Barbuda",
    "ARG": "Argentina",
    "ARM": "Armenia",
    "ABW": "Aruba",
    "AUS": "Australia",
    "AUT": "Austria",
    "AZE": "Azerbaijan",
    "BHS": "Bahamas (the)",
    "BHR": "Bahrain",
    "BGD": "Bangladesh",
    "BRB": "Barbados",
    "BLR": "Belarus",
    "BEL": "Belgium",
    "BLZ": "Belize",
    "BEN": "Benin",
    "BMU": "Bermuda",
    "BTN": "Bhutan",
    "BOL": "Bolivia (Plurinational State of)",
    "BES": "Bonaire, Sint Eustatius and Saba",
    "BIH": "Bosnia and Herzegovina",
    "BWA": "Botswana",
    "BVT": "Bouvet Island",
    "BRA": "Brazil",
    "IOT": "British Indian Ocean Territory (the)",
    "BRN": "Brunei Darussalam",
    "BGR": "Bulgaria",
    "BFA": "Burkina Faso",
    "BDI": "Burundi",
    "CPV": "Cabo Verde",
    "KHM": "Cambodia",
    "CMR": "Cameroon",
    "CAN": "Canada",
    "CYM": "Cayman Islands (the)",
    "CAF": "Central African Republic (the)",
    "TCD": "Chad",
    "CHL": "Chile",
    "CHN": "China",
    "CXR": "Christmas Island",
    "CCK": "Cocos (Keeling) Islands (the)",
    "COL": "Colombia",
    "COM": "Comoros (the)",
    "COD": "Congo (the Democratic Republic of the)",
    "COG": "Congo (the)",
    "COK": "Cook Islands (the)",
    "CRI": "Costa Rica",
    "HRV": "Croatia",
    "CUB": "Cuba",
    "CUW": "Curaçao",
    "CYP": "Cyprus",
    "CZE": "Czechia",
    "CIV": "Côte d'Ivoire",
    "DNK": "Denmark",
    "DJI": "Djibouti",
    "DMA": "Dominica",
    "DOM": "Dominican Republic (the)",
    "ECU": "Ecuador",
    "EGY": "Egypt",
    "SLV": "El Salvador",
    "GNQ": "Equatorial Guinea",
    "ERI": "Eritrea",
    "EST": "Estonia",
    "SWZ": "Eswatini",
    "ETH": "Ethiopia",
    "FLK": "Falkland Islands (the) [Malvinas]",
    "FRO": "Faroe Islands (the)",
    "FJI": "Fiji",
    "FIN": "Finland",
    "FRA": "France",
    "GUF": "French Guiana",
    "PYF": "French Polynesia",
    "ATF": "French Southern Territories (the)",
    "GAB": "Gabon",
    "GMB": "Gambia (the)",
    "GEO": "Georgia",
    "DEU": "Germany",
    "GHA": "Ghana",
    "GIB": "Gibraltar",
    "GRC": "Greece",
    "GRL": "Greenland",
    "GRD": "Grenada",
    "GLP": "Guadeloupe",
    "GUM": "Guam",
    "GTM": "Guatemala",
    "GGY": "Guernsey",
    "GIN": "Guinea",
    "GNB": "Guinea-Bissau",
    "GUY": "Guyana",
    "HTI": "Haiti",
    "HMD": "Heard Island and McDonald Islands",
    "VAT": "Holy See (the)",
    "HND": "Honduras",
    "HKG": "Hong Kong",
    "HUN": "Hungary",
    "ISL": "Iceland",
    "IND": "India",
    "IDN": "Indonesia",
    "IRN": "Iran (Islamic Republic of)",
    "IRQ": "Iraq",
    "IRL": "Ireland",
    "IMN": "Isle of Man",
    "ISR": "Israel",
    "ITA": "Italy",
    "JAM": "Jamaica",
    "JPN": "Japan",
    "JEY": "Jersey",
    "JOR": "Jordan",
    "KAZ": "Kazakhstan",
    "KEN": "Kenya",
    "KIR": "Kiribati",
    "PRK": "Korea (the Democratic People's Republic of)",
    "KOR": "Korea (the Republic of)",
    "KWT": "Kuwait",
    "KGZ": "Kyrgyzstan",
    "LAO": "Lao People's Democratic Republic (the)",
    "LVA": "Latvia",
    "LBN": "Lebanon",
    "LSO": "Lesotho",
    "LBR": "Liberia",
    "LBY": "Libya",
    "LIE": "Liechtenstein",
    "LTU": "Lithuania",
    "LUX": "Luxembourg",
    "MAC": "Macao",
    "MDG": "Madagascar",
    "MWI": "Malawi",
    "MYS": "Malaysia",
    "MDV": "Maldives",
    "MLI": "Mali",
    "MLT": "Malta",
    "MHL": "Marshall Islands (the)",
    "MTQ": "Martinique",
    "MRT": "Mauritania",
    "MUS": "Mauritius",
    "MYT": "Mayotte",
    "MEX": "Mexico",
    "FSM": "Micronesia (Federated States of)",
    "MDA": "Moldova (the Republic of)",
    "MCO": "Monaco",
    "MNG": "Mongolia",
    "MNE": "Montenegro",
    "MSR": "Montserrat",
    "MAR": "Morocco",
    "MOZ": "Mozambique",
    "MMR": "Myanmar",
    "NAM": "Namibia",
    "NRU": "Nauru",
    "NPL": "Nepal",
    "NLD": "Netherlands (the)",
    "NCL": "New Caledonia",
    "NZL": "New Zealand",
    "NIC": "Nicaragua",
    "NER": "Niger (the)",
    "NGA": "Nigeria",
    "NIU": "Niue",
    "NFK": "Norfolk Island",
    "MNP": "Northern Mariana Islands (the)",
    "NOR": "Norway",
    "OMN": "Oman",
    "PAK": "Pakistan",
    "PLW": "Palau",
    "PSE": "Palestine, State of",
    "PAN": "Panama",
    "PNG": "Papua New Guinea",
    "PRY": "Paraguay",
    "PER": "Peru",
    "PHL": "Philippines (the)",
    "PCN": "Pitcairn",
    "POL": "Poland",
    "PRT": "Portugal",
    "PRI": "Puerto Rico",
    "QAT": "Qatar",
    "MKD": "Republic of North Macedonia",
    "ROU": "Romania",
    "RUS": "Russian Federation (the)",
    "RWA": "Rwanda",
    "REU": "Réunion",
    "BLM": "Saint Barthélemy",
    "SHN": "Saint Helena, Ascension and Tristan da Cunha",
    "KNA": "Saint Kitts and Nevis",
    "LCA": "Saint Lucia",
    "MAF": "Saint Martin (French part)",
    "SPM": "Saint Pierre and Miquelon",
    "VCT": "Saint Vincent and the Grenadines",
    "WSM": "Samoa",
    "SMR": "San Marino",
    "STP": "Sao Tome and Principe",
    "SAU": "Saudi Arabia",
    "SEN": "Senegal",
    "SRB": "Serbia",
    "SYC": "Seychelles",
    "SLE": "Sierra Leone",
    "SGP": "Singapore",
    "SXM": "Sint Maarten (Dutch part)",
    "SVK": "Slovakia",
    "SVN": "Slovenia",
    "SLB": "Solomon Islands",
    "SOM": "Somalia",
    "ZAF": "South Africa",
    "SGS": "South Georgia and the South Sandwich Islands",
    "SSD": "South Sudan",
    "ESP": "Spain",
    "LKA": "Sri Lanka",
    "SDN": "Sudan (the)",
    "SUR": "Suriname",
    "SJM": "Svalbard and Jan Mayen",
    "SWE": "Sweden",
    "CHE": "Switzerland",
    "SYR": "Syrian Arab Republic",
    "TWN": "Taiwan (Province of China)",
    "TJK": "Tajikistan",
    "TZA": "Tanzania, United Republic of",
    "THA": "Thailand",
    "TLS": "Timor-Leste",
    "TGO": "Togo",
    "TKL": "Tokelau",
    "TON": "Tonga",
    "TTO": "Trinidad and Tobago",
    "TUN": "Tunisia",
    "TUR": "Turkey",
    "TKM": "Turkmenistan",
    "TCA": "Turks and Caicos Islands (the)",
    "TUV": "Tuvalu",
    "UGA": "Uganda",
    "UKR": "Ukraine",
    "ARE": "United Arab Emirates (the)",
    "GBR": "United Kingdom of Great Britain and Northern Ireland (the)",
    "UMI": "United States Minor Outlying Islands (the)",
    "USA": "United States of America (the)",
    "URY": "Uruguay",
    "UZB": "Uzbekistan",
    "VUT": "Vanuatu",
    "VEN": "Venezuela (Bolivarian Republic of)",
    "VNM": "Viet Nam",
    "VGB": "Virgin Islands (British)",
    "VIR": "Virgin Islands (U.S.)",
    "WLF": "Wallis and Futuna",
    "ESH": "Western Sahara",
    "YEM": "Yemen",
    "ZMB": "Zambia",
    "ZWE": "Zimbabwe",
    "ALA": "Åland Islands"
  }

def get_full_name_usa():
  return {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Is",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "VI": "Virgin Islands",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
  }

def get_states_pops(file, state_header, pop_header):
  
  text = []
  with open(file, "r", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file)

    counter = 0
    for line in csv_reader:
      text.append(line)
      counter += 1
  ##    if counter > 1000:
  ##      break

  header = text.pop(0)
  indexState = header.index(state_header)
  indexPop = header.index(pop_header)

  statesDict = {}
  for row in text:
    currentState = row[indexState]
    currentPop = row[indexPop].replace(",","")

    # if currentState == "GBR":
    #   print(currentState, currentPop)
    #   print("    ", currentPop.isnumeric())

    # checks current pop, converts to integer
    if currentPop.isnumeric():
      currentPop = int(currentPop)
    else:
      continue

    # creates/adds country with pops to list
    if currentState in statesDict:
      statesDict[currentState].append(currentPop)
    else:
      statesDict[currentState] = [currentPop]

    # print(currentState, currentPop)

  # print(statesDict["GBR"])
  return statesDict

def get_indicators(file, state_header, indicator_header):
  
  text = []
  with open(file, "r", newline = "") as csv_file:
    csv_reader = csv.reader(csv_file)

    counter = 0
    for line in csv_reader:
      text.append(line)
      counter += 1

  header = text.pop(0)
  indexState = header.index(state_header)
  indexIndicator = header.index(indicator_header)

  indicatorsDict = {}
  for row in text:
    currentState = row[indexState]
    currentIndicator = row[indexIndicator].replace(",","")
    # print(currentState, currentIndicator)

    # checks current indicator, converts to float
    if currentIndicator.replace(".","").isnumeric():
      currentIndicator = float(currentIndicator)
    else:
      continue

    indicatorsDict[currentState] = currentIndicator

  return indicatorsDict

def export_csv(data_lyst, path):
  with open(path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data_lyst)

def export_cities(dictionary, path):
  with open(path, "w") as file:
    json.dump(dictionary, file, indent = 2)