# Generated by Django 5.1.1 on 2024-11-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reporting", "0004_alter_report_station"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="station",
            field=models.CharField(
                choices=[
                    ("FLUSHING AV", "Flushing Av"),
                    ("WESTCHESTER SQ-E TREMONT AV", "Westchester Sq-E Tremont Av"),
                    ("PARKCHESTER", "Parkchester"),
                    ("BAY RIDGE AV", "Bay Ridge Av"),
                    ("74 ST-BROADWAY", "74 St-Broadway"),
                    ("W 4 ST-WASH SQ", "W 4 St-Wash Sq"),
                    ("62 ST", "62 St"),
                    ("34 ST-HUDSON YARDS", "34 St-Hudson Yards"),
                    ("METS-WILLETS POINT", "Mets-Willets Point"),
                    ("9 AV", "9 Av"),
                    ("GRAND ST", "Grand St"),
                    (
                        "FRANKLIN AV-MEDGAR EVERS COLLEGE",
                        "Franklin Av-Medgar Evers College",
                    ),
                    ("170 ST", "170 St"),
                    ("59 ST-COLUMBUS CIRCLE", "59 St-Columbus Circle"),
                    ("BROADWAY", "Broadway"),
                    ("DONGAN HILLS", "Dongan Hills"),
                    ("174 ST", "174 St"),
                    ("CLIFTON", "Clifton"),
                    ("BUHRE AV", "Buhre Av"),
                    ("FREEMAN ST", "Freeman St"),
                    ("WALL ST", "Wall St"),
                    ("ATLANTIC AV", "Atlantic Av"),
                    ("15 ST-PROSPECT PARK", "15 St-Prospect Park"),
                    ("25 ST", "25 St"),
                    ("1 AV", "1 Av"),
                    ("72 ST", "72 St"),
                    ("COURT SQ-23 ST", "Court Sq-23 St"),
                    ("LIVONIA AV", "Livonia Av"),
                    ("BAY TERRACE", "Bay Terrace"),
                    ("RICHMOND VALLEY", "Richmond Valley"),
                    ("34 ST-PENN STATION", "34 St-Penn Station"),
                    ("BAY RIDGE-95 ST", "Bay Ridge-95 St"),
                    ("FRANKLIN AV", "Franklin Av"),
                    ("79 ST", "79 St"),
                    ("CENTRAL PARK NORTH (110 ST)", "Central Park North (110 St)"),
                    ("MOSHOLU PKWY", "Mosholu Pkwy"),
                    ("40 ST-LOWERY ST", "40 St-Lowery St"),
                    ("KNICKERBOCKER AV", "Knickerbocker Av"),
                    ("LEXINGTON AV/63 ST", "Lexington Av/63 St"),
                    ("AVENUE M", "Avenue M"),
                    ("ATLANTIC AV-BARCLAYS CTR", "Atlantic Av-Barclays Ctr"),
                    ("LEXINGTON AV/59 ST", "Lexington Av/59 St"),
                    ("UTICA AV", "Utica Av"),
                    ("CYPRESS AV", "Cypress Av"),
                    ("BRIARWOOD", "Briarwood"),
                    ("FOREST AV", "Forest Av"),
                    ("COURT ST", "Court St"),
                    ("138 ST-GRAND CONCOURSE", "138 St-Grand Concourse"),
                    ("86 ST", "86 St"),
                    ("88 ST", "88 St"),
                    ("168 ST-WASHINGTON HTS", "168 St-Washington Hts"),
                    ("GRANT AV", "Grant Av"),
                    ("MIDDLETOWN RD", "Middletown Rd"),
                    ("SUTPHIN BLVD", "Sutphin Blvd"),
                    ("NEREID AV", "Nereid Av"),
                    ("135 ST", "135 St"),
                    ("116 ST", "116 St"),
                    ("191 ST", "191 St"),
                    ("BEACH 105 ST", "Beach 105 St"),
                    ("PELHAM BAY PARK", "Pelham Bay Park"),
                    ("RECTOR ST", "Rector St"),
                    ("QUEENS PLAZA", "Queens Plaza"),
                    ("52 ST", "52 St"),
                    ("QUEENSBORO PLAZA", "Queensboro Plaza"),
                    (
                        "PRESIDENT ST-MEDGAR EVERS COLLEGE",
                        "President St-Medgar Evers College",
                    ),
                    ("HUNTERS POINT AV", "Hunters Point Av"),
                    ("65 ST", "65 St"),
                    ("BAY PKWY", "Bay Pkwy"),
                    ("168 ST", "168 St"),
                    ("39 AV-DUTCH KILLS", "39 Av-Dutch Kills"),
                    ("53 ST", "53 St"),
                    ("COURT SQ", "Court Sq"),
                    ("80 ST", "80 St"),
                    ("HOYT ST", "Hoyt St"),
                    ("46 ST-BLISS ST", "46 St-Bliss St"),
                    ("68 ST-HUNTER COLLEGE", "68 St-Hunter College"),
                    ("SARATOGA AV", "Saratoga Av"),
                    ("BROAD CHANNEL", "Broad Channel"),
                    ("STEINWAY ST", "Steinway St"),
                    ("BEACH 60 ST", "Beach 60 St"),
                    ("JACKSON HTS-ROOSEVELT AV", "Jackson Hts-Roosevelt Av"),
                    ("BRIGHTON BEACH", "Brighton Beach"),
                    ("STAPLETON", "Stapleton"),
                    ("SHEEPSHEAD BAY", "Sheepshead Bay"),
                    ("ALABAMA AV", "Alabama Av"),
                    ("VERNON BLVD-JACKSON AV", "Vernon Blvd-Jackson Av"),
                    ("METROPOLITAN AV", "Metropolitan Av"),
                    ("CLASSON AV", "Classon Av"),
                    ("HIGH ST", "High St"),
                    ("GATES AV", "Gates Av"),
                    ("MT EDEN AV", "Mt Eden Av"),
                    ("33 ST", "33 St"),
                    ("GRAND AV-NEWTOWN", "Grand Av-Newtown"),
                    ("183 ST", "183 St"),
                    ("PRINCE ST", "Prince St"),
                    ("CONEY ISLAND-STILLWELL AV", "Coney Island-Stillwell Av"),
                    (
                        "42 ST-PORT AUTHORITY BUS TERMINAL",
                        "42 St-Port Authority Bus Terminal",
                    ),
                    ("NEWKIRK PLAZA", "Newkirk Plaza"),
                    ("AQUEDUCT-N CONDUIT AV", "Aqueduct-N Conduit Av"),
                    ("HUNTS POINT AV", "Hunts Point Av"),
                    ("ST LAWRENCE AV", "St Lawrence Av"),
                    ("BEDFORD PARK BLVD", "Bedford Park Blvd"),
                    ("7 AV", "7 Av"),
                    ("MORRISON AV-SOUNDVIEW", "Morrison Av-Soundview"),
                    ("85 ST-FOREST PKWY", "85 St-Forest Pkwy"),
                    ("28 ST", "28 St"),
                    ("PELHAM PKWY", "Pelham Pkwy"),
                    ("SUTTER AV-RUTLAND RD", "Sutter Av-Rutland Rd"),
                    ("30 AV", "30 Av"),
                    ("PLEASANT PLAINS", "Pleasant Plains"),
                    (
                        "MIDDLE VILLAGE-METROPOLITAN AV",
                        "Middle Village-Metropolitan Av",
                    ),
                    ("CHAUNCEY ST", "Chauncey St"),
                    ("EUCLID AV", "Euclid Av"),
                    ("KINGS HWY", "Kings Hwy"),
                    ("AVENUE J", "Avenue J"),
                    ("JAMAICA-VAN WYCK", "Jamaica-Van Wyck"),
                    ("5 AV/59 ST", "5 Av/59 St"),
                    ("59 ST", "59 St"),
                    ("71 ST", "71 St"),
                    ("3 AV", "3 Av"),
                    ("169 ST", "169 St"),
                    ("182-183 STS", "182-183 Sts"),
                    ("66 ST-LINCOLN CENTER", "66 St-Lincoln Center"),
                    ("163 ST-AMSTERDAM AV", "163 St-Amsterdam Av"),
                    ("JEFFERSON ST", "Jefferson St"),
                    ("25 AV", "25 Av"),
                    ("LEXINGTON AV/53 ST", "Lexington Av/53 St"),
                    (
                        "81 ST-MUSEUM OF NATURAL HISTORY",
                        "81 St-Museum of Natural History",
                    ),
                    (
                        "BEDFORD PARK BLVD-LEHMAN COLLEGE",
                        "Bedford Park Blvd-Lehman College",
                    ),
                    ("21 ST", "21 St"),
                    ("3 AV-149 ST", "3 Av-149 St"),
                    ("BEDFORD AV", "Bedford Av"),
                    ("BLEECKER ST", "Bleecker St"),
                    ("EASTERN PKWY-BROOKLYN MUSEUM", "Eastern Pkwy-Brooklyn Museum"),
                    ("ASTORIA-DITMARS BLVD", "Astoria-Ditmars Blvd"),
                    ("225 ST", "225 St"),
                    ("BROADWAY-LAFAYETTE ST", "Broadway-Lafayette St"),
                    ("BEACH 25 ST", "Beach 25 St"),
                    ("18 AV", "18 Av"),
                    ("GRAND ARMY PLAZA", "Grand Army Plaza"),
                    ("KOSCIUSZKO ST", "Kosciuszko St"),
                    ("233 ST", "233 St"),
                    ("LORIMER ST", "Lorimer St"),
                    ("KINGSTON-THROOP AVS", "Kingston-Throop Avs"),
                    ("NORWOOD-205 ST", "Norwood-205 St"),
                    ("PRINCE'S BAY", "Prince's Bay"),
                    ("KINGSBRIDGE RD", "Kingsbridge Rd"),
                    ("BOWLING GREEN", "Bowling Green"),
                    ("VAN CORTLANDT PARK-242 ST", "Van Cortlandt Park-242 St"),
                    ("CENTRAL AV", "Central Av"),
                    ("SOUTH FERRY", "South Ferry"),
                    ("DYCKMAN ST", "Dyckman St"),
                    ("CARROLL ST", "Carroll St"),
                    ("TREMONT AV", "Tremont Av"),
                    ("CORTELYOU RD", "Cortelyou Rd"),
                    ("NEWKIRK AV-LITTLE HAITI", "Newkirk Av-Little Haiti"),
                    ("JUNCTION BLVD", "Junction Blvd"),
                    ("AQUEDUCT RACETRACK", "Aqueduct Racetrack"),
                    ("GRANT CITY", "Grant City"),
                    ("INTERVALE AV", "Intervale Av"),
                    ("CHRISTOPHER ST-STONEWALL", "Christopher St-Stonewall"),
                    ("CLEVELAND ST", "Cleveland St"),
                    ("PARKSIDE AV", "Parkside Av"),
                    ("KINGSTON AV", "Kingston Av"),
                    ("SMITH-9 STS", "Smith-9 Sts"),
                    ("231 ST", "231 St"),
                    ("161 ST-YANKEE STADIUM", "161 St-Yankee Stadium"),
                    ("GRASMERE", "Grasmere"),
                    ("BAYCHESTER AV", "Baychester Av"),
                    ("EAST BROADWAY", "East Broadway"),
                    ("77 ST", "77 St"),
                    ("PENNSYLVANIA AV", "Pennsylvania Av"),
                    ("BEVERLEY RD", "Beverley Rd"),
                    ("CYPRESS HILLS", "Cypress Hills"),
                    ("BROOK AV", "Brook Av"),
                    ("61 ST-WOODSIDE", "61 St-Woodside"),
                    ("36 AV", "36 Av"),
                    ("HALSEY ST", "Halsey St"),
                    ("WINTHROP ST", "Winthrop St"),
                    ("NOSTRAND AV", "Nostrand Av"),
                    ("WAKEFIELD-241 ST", "Wakefield-241 St"),
                    ("TOTTENVILLE", "Tottenville"),
                    ("BEACH 44 ST", "Beach 44 St"),
                    ("BEDFORD-NOSTRAND AVS", "Bedford-Nostrand Avs"),
                    ("KEW GARDENS-UNION TPKE", "Kew Gardens-Union Tpke"),
                    ("MYRTLE AV", "Myrtle Av"),
                    ("103 ST-CORONA PLAZA", "103 St-Corona Plaza"),
                    ("AVENUE U", "Avenue U"),
                    ("BROADWAY JUNCTION", "Broadway Junction"),
                    ("ELTINGVILLE", "Eltingville"),
                    ("57 ST", "57 St"),
                    ("E 180 ST", "E 180 St"),
                    ("ST GEORGE", "St George"),
                    ("2 AV", "2 Av"),
                    ("LONGWOOD AV", "Longwood Av"),
                    ("NEPTUNE AV", "Neptune Av"),
                    ("GRAHAM AV", "Graham Av"),
                    ("MARCY AV", "Marcy Av"),
                    ("BOTANIC GARDEN", "Botanic Garden"),
                    ("SENECA AV", "Seneca Av"),
                    ("47-50 STS-ROCKEFELLER CTR", "47-50 Sts-Rockefeller Ctr"),
                    ("CROWN HTS-UTICA AV", "Crown Hts-Utica Av"),
                    ("MONTROSE AV", "Montrose Av"),
                    ("BEACH 67 ST", "Beach 67 St"),
                    ("96 ST", "96 St"),
                    ("JACKSON AV", "Jackson Av"),
                    ("DEKALB AV", "DeKalb Av"),
                    ("14 ST-UNION SQ", "14 St-Union Sq"),
                    ("PROSPECT AV", "Prospect Av"),
                    ("ROCKAWAY AV", "Rockaway Av"),
                    ("20 AV", "20 Av"),
                    ("AVENUE N", "Avenue N"),
                    ("14 ST", "14 St"),
                    ("BOROUGH HALL", "Borough Hall"),
                    ("LIBERTY AV", "Liberty Av"),
                    ("NASSAU AV", "Nassau Av"),
                    ("HUGUENOT", "Huguenot"),
                    ("6 AV", "6 Av"),
                    ("BAY 50 ST", "Bay 50 St"),
                    ("WEST FARMS SQ-E TREMONT AV", "West Farms Sq-E Tremont Av"),
                    ("69 ST", "69 St"),
                    ("JUNIUS ST", "Junius St"),
                    ("GUN HILL RD", "Gun Hill Rd"),
                    ("149 ST-GRAND CONCOURSE", "149 St-Grand Concourse"),
                    ("GREENPOINT AV", "Greenpoint Av"),
                    ("145 ST", "145 St"),
                    ("ROCKAWAY BLVD", "Rockaway Blvd"),
                    ("WTC CORTLANDT", "WTC Cortlandt"),
                    ("DELANCEY ST-ESSEX ST", "Delancey St-Essex St"),
                    ("AVENUE P", "Avenue P"),
                    ("8 AV", "8 Av"),
                    ("FORT HAMILTON PKWY", "Fort Hamilton Pkwy"),
                    ("SIMPSON ST", "Simpson St"),
                    ("WORLD TRADE CENTER", "World Trade Center"),
                    ("BEACH 98 ST", "Beach 98 St"),
                    ("NORTHERN BLVD", "Northern Blvd"),
                    ("219 ST", "219 St"),
                    ("TOMPKINSVILLE", "Tompkinsville"),
                    ("BURNSIDE AV", "Burnside Av"),
                    ("BOWERY", "Bowery"),
                    ("MYRTLE-WYCKOFF AVS", "Myrtle-Wyckoff Avs"),
                    ("36 ST", "36 St"),
                    ("75 ST-ELDERTS LN", "75 St-Elderts Ln"),
                    ("OLD TOWN", "Old Town"),
                    ("WHITLOCK AV", "Whitlock Av"),
                    ("33 ST-RAWSON ST", "33 St-Rawson St"),
                    ("215 ST", "215 St"),
                    ("181 ST", "181 St"),
                    ("JAMAICA CENTER-PARSONS/ARCHER", "Jamaica Center-Parsons/Archer"),
                    ("FLATBUSH AV-BROOKLYN COLLEGE", "Flatbush Av-Brooklyn College"),
                    ("WHITEHALL ST-SOUTH FERRY", "Whitehall St-South Ferry"),
                    ("NORWOOD AV", "Norwood Av"),
                    ("GREAT KILLS", "Great Kills"),
                    ("SHEPHERD AV", "Shepherd Av"),
                    ("82 ST-JACKSON HTS", "82 St-Jackson Hts"),
                    ("OCEAN PKWY", "Ocean Pkwy"),
                    ("21 ST-QUEENSBRIDGE", "21 St-Queensbridge"),
                    ("WILSON AV", "Wilson Av"),
                    ("CATHEDRAL PKWY (110 ST)", "Cathedral Pkwy (110 St)"),
                    ("SPRING ST", "Spring St"),
                    ("MORRIS PARK", "Morris Park"),
                    ("125 ST", "125 St"),
                    ("GRAND CENTRAL-42 ST", "Grand Central-42 St"),
                    ("PARK PL", "Park Pl"),
                    ("BERGEN ST", "Bergen St"),
                    ("BROOKLYN BRIDGE-CITY HALL", "Brooklyn Bridge-City Hall"),
                    ("BURKE AV", "Burke Av"),
                    ("67 AV", "67 Av"),
                    (
                        "SUTPHIN BLVD-ARCHER AV-JFK AIRPORT",
                        "Sutphin Blvd-Archer Av-JFK Airport",
                    ),
                    ("238 ST", "238 St"),
                    ("110 ST", "110 St"),
                    ("157 ST", "157 St"),
                    ("JEFFERSON AV", "Jefferson Av"),
                    ("190 ST", "190 St"),
                    ("174-175 STS", "174-175 Sts"),
                    ("LAFAYETTE AV", "Lafayette Av"),
                    ("121 ST", "121 St"),
                    ("RALPH AV", "Ralph Av"),
                    ("JAY ST-METROTECH", "Jay St-MetroTech"),
                    ("MYRTLE-WILLOUGHBY AVS", "Myrtle-Willoughby Avs"),
                    ("ASTOR PL", "Astor Pl"),
                    ("57 ST-7 AV", "57 St-7 Av"),
                    ("4 AV-9 ST", "4 Av-9 St"),
                    ("FULTON ST", "Fulton St"),
                    ("46 ST", "46 St"),
                    ("ROOSEVELT ISLAND", "Roosevelt Island"),
                    ("104 ST", "104 St"),
                    ("FLUSHING-MAIN ST", "Flushing-Main St"),
                    ("AVENUE H", "Avenue H"),
                    ("HARLEM-148 ST", "Harlem-148 St"),
                    ("5 AV/53 ST", "5 Av/53 St"),
                    ("NEVINS ST", "Nevins St"),
                    ("UNION ST", "Union St"),
                    ("VAN SICLEN AV", "Van Siclen Av"),
                    ("207 ST", "207 St"),
                    ("INWOOD-207 ST", "Inwood-207 St"),
                    ("CASTLE HILL AV", "Castle Hill Av"),
                    ("ROCKAWAY PARK-BEACH 116 ST", "Rockaway Park-Beach 116 St"),
                    ("3 AV-138 ST", "3 Av-138 St"),
                    ("ANNADALE", "Annadale"),
                    ("CHAMBERS ST", "Chambers St"),
                    ("ARTHUR KILL", "Arthur Kill"),
                    ("8 ST-NYU", "8 St-NYU"),
                    ("51 ST", "51 St"),
                    ("FRESH POND RD", "Fresh Pond Rd"),
                    ("NEW DORP", "New Dorp"),
                    ("PARSONS BLVD", "Parsons Blvd"),
                    ("NECK RD", "Neck Rd"),
                    ("42 ST-BRYANT PK", "42 St-Bryant Pk"),
                    ("63 DR-REGO PARK", "63 Dr-Rego Park"),
                    ("EAST 105 ST", "East 105 St"),
                    ("HOYT-SCHERMERHORN STS", "Hoyt-Schermerhorn Sts"),
                    ("FRANKLIN ST", "Franklin St"),
                    ("ELDER AV", "Elder Av"),
                    ("CHURCH AV", "Church Av"),
                    ("176 ST", "176 St"),
                    ("ASTORIA BLVD", "Astoria Blvd"),
                    ("TIMES SQ-42 ST", "Times Sq-42 St"),
                    ("111 ST", "111 St"),
                    ("JAMAICA-179 ST", "Jamaica-179 St"),
                    ("EASTCHESTER-DYRE AV", "Eastchester-Dyre Av"),
                    ("103 ST", "103 St"),
                    ("BEVERLY RD", "Beverly Rd"),
                    ("WOODLAWN", "Woodlawn"),
                    ("175 ST", "175 St"),
                    ("BROAD ST", "Broad St"),
                    ("MORGAN AV", "Morgan Av"),
                    ("FAR ROCKAWAY-MOTT AV", "Far Rockaway-Mott Av"),
                    ("HOUSTON ST", "Houston St"),
                    ("NEW LOTS AV", "New Lots Av"),
                    ("BEACH 90 ST", "Beach 90 St"),
                    ("18 ST", "18 St"),
                    ("55 ST", "55 St"),
                    ("137 ST-CITY COLLEGE", "137 St-City College"),
                    ("34 ST-HERALD SQ", "34 St-Herald Sq"),
                    ("CANAL ST", "Canal St"),
                    ("CRESCENT ST", "Crescent St"),
                    ("MARBLE HILL-225 ST", "Marble Hill-225 St"),
                    ("ALLERTON AV", "Allerton Av"),
                    ("OZONE PARK-LEFFERTS BLVD", "Ozone Park-Lefferts Blvd"),
                    ("75 AV", "75 Av"),
                    ("PARK PLACE", "Park Place"),
                    ("45 ST", "45 St"),
                    ("DITMAS AV", "Ditmas Av"),
                    ("BUSHWICK AV-ABERDEEN ST", "Bushwick Av-Aberdeen St"),
                    ("WOODHAVEN BLVD", "Woodhaven Blvd"),
                    ("BEACH 36 ST", "Beach 36 St"),
                    ("167 ST", "167 St"),
                    ("23 ST", "23 St"),
                    ("SUTTER AV", "Sutter Av"),
                    ("HOWARD BEACH-JFK AIRPORT", "Howard Beach-JFK Airport"),
                    ("HEWES ST", "Hewes St"),
                    ("5 AV", "5 Av"),
                    ("BRONX PARK EAST", "Bronx Park East"),
                    ("CLARK ST", "Clark St"),
                    ("OAKWOOD HEIGHTS", "Oakwood Heights"),
                    ("CORTLANDT ST", "Cortlandt St"),
                    ("NEW UTRECHT AV", "New Utrecht Av"),
                    ("AVENUE X", "Avenue X"),
                    ("49 ST", "49 St"),
                    ("STERLING ST", "Sterling St"),
                    ("ZEREGA AV", "Zerega Av"),
                    ("E 143 ST-ST MARY'S ST", "E 143 St-St Mary's St"),
                    ("FOREST HILLS-71 AV", "Forest Hills-71 Av"),
                    ("CANARSIE-ROCKAWAY PKWY", "Canarsie-Rockaway Pkwy"),
                    ("FORDHAM RD", "Fordham Rd"),
                    ("CITY HALL", "City Hall"),
                    ("ELMHURST AV", "Elmhurst Av"),
                    ("155 ST", "155 St"),
                    ("YORK ST", "York St"),
                    ("E 149 ST", "E 149 St"),
                    ("CLINTON-WASHINGTON AVS", "Clinton-Washington Avs"),
                    ("50 ST", "50 St"),
                    ("AVENUE I", "Avenue I"),
                    ("PROSPECT PARK", "Prospect Park"),
                    ("116 ST-COLUMBIA UNIVERSITY", "116 St-Columbia University"),
                    ("W 8 ST-NY AQUARIUM", "W 8 St-NY Aquarium"),
                    ("90 ST-ELMHURST AV", "90 St-Elmhurst Av"),
                ],
                max_length=40,
            ),
        ),
    ]
