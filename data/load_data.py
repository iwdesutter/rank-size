import csv

def get_states_pops_demo_am():
  return {
    "IL": [2960976, 1148305, 1111811, 894645, 641541, 572769, 520647, 519707, 509445, 470604, 466755, 407506, 367099, 346620, 342796, 299022, 289142, 257766, 255145, 228199, 206848, 201943, 181318, 167078, 153855, 141496, 133741, 123672, 121739, 119492, 114752, 110269],
    "BOL": [784976, 767260, 448756, 446189, 201831, 144994, 123327],
    "BRA": [9842059, 5547033, 2174072, 2060804, 1846955, 1601094, 1364320, 1314857, 1297592, 1280114, 1078277, 957564, 878690, 831210, 807774, 792917, 738327, 683451, 666071, 639160, 636904, 627850, 590896, 584140, 565943, 526086, 513740, 478317, 468678, 450690, 442786, 435647, 430350, 425974, 419477, 405116, 402341, 399327, 397553, 388483, 385068, 372203, 370279, 351441, 339641, 318305, 310161, 302498, 300283, 299927, 299592, 296770, 294628, 294444, 290641, 289047, 285955, 281464, 278873, 277482, 276149, 273759, 267448, 266858, 262422, 259879, 252533, 247385, 245870, 242026, 239429, 239378, 236369, 234344, 227266, 226534, 221329, 220980, 220690, 220244, 217489, 217418, 213968, 213370, 202684, 201872, 201222, 197459, 195943, 194237, 192255, 185671, 185122, 184692, 180568, 180013, 179682, 179273, 178483, 177411, 177159, 176891, 176446, 174507, 173624, 172047, 170931, 170690, 170349, 168655, 167838, 167302, 166731, 166269, 166215, 164921, 164792, 159979, 159557, 159197, 157260, 156928, 156865, 154896, 154214, 153840, 153455, 151385, 151064, 149512, 149160, 148572, 148272, 147215, 146638, 145961, 143005, 142873, 142046, 141929, 140221, 138270, 137108, 134606, 133257, 131518, 131239, 130923, 127953, 127091, 125686, 125266, 124447, 122288, 121981, 121866, 121146, 120441, 118967, 117773, 117432, 117241, 116951, 116894, 116674, 114056, 113051, 112939, 112477, 112041, 109220, 109166, 108544, 108326, 107584, 106882, 106784, 106457, 106183, 106111, 105804, 105246, 103761, 103315, 102852, 102164, 102072, 101842, 101447, 101034, 100377, 100249, 100016],
    "CAN": [1017666, 710677, 635395, 616790, 616741, 562564, 524598, 471844, 463388, 341322, 318499, 314398, 313987, 309993, 245173, 234445, 191435, 186058, 179178, 168282, 167517, 158858, 153811, 140525, 129874, 129575, 129344, 129300, 126624, 114670, 114455, 113946, 111359, 107627, 102696, 101677],
    "CHL": [4229970, 350268, 322220, 318898, 282168, 260915, 239340, 236730, 206315, 193755, 173336, 169448, 157083, 152592, 123055, 122399, 119431, 117983, 117206, 110340]
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
    print(currentState, currentIndicator)

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