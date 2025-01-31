# Generated by Django 5.1.1 on 2024-11-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reporting", "0014_alter_report_station"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="station",
            field=models.CharField(
                choices=[
                    ("WOODLAWN", "Woodlawn"),
                    ("75 ST-ELDERTS LN", "75 St-Elderts Ln"),
                    ("BEACH 25 ST", "Beach 25 St"),
                    ("NORTHERN BLVD", "Northern Blvd"),
                    ("30 AV", "30 Av"),
                    ("LIBERTY AV", "Liberty Av"),
                    ("231 ST", "231 St"),
                    ("110 ST", "110 St"),
                    ("GRAHAM AV", "Graham Av"),
                    ("COURT ST", "Court St"),
                    ("LORIMER ST", "Lorimer St"),
                    ("65 ST", "65 St"),
                    ("39 AV-DUTCH KILLS", "39 Av-Dutch Kills"),
                    ("36 ST", "36 St"),
                    ("JAMAICA-179 ST", "Jamaica-179 St"),
                    ("WHITEHALL ST-SOUTH FERRY", "Whitehall St-South Ferry"),
                    ("PARKSIDE AV", "Parkside Av"),
                    ("HOWARD BEACH-JFK AIRPORT", "Howard Beach-JFK Airport"),
                    ("20 AV", "20 Av"),
                    ("42 ST-BRYANT PK", "42 St-Bryant Pk"),
                    ("36 AV", "36 Av"),
                    ("79 ST", "79 St"),
                    ("SUTTER AV-RUTLAND RD", "Sutter Av-Rutland Rd"),
                    ("233 ST", "233 St"),
                    ("BAY RIDGE AV", "Bay Ridge Av"),
                    ("ROCKAWAY AV", "Rockaway Av"),
                    ("ELTINGVILLE", "Eltingville"),
                    ("3 AV-149 ST", "3 Av-149 St"),
                    ("NEVINS ST", "Nevins St"),
                    ("GREAT KILLS", "Great Kills"),
                    ("2 AV", "2 Av"),
                    ("ATLANTIC AV-BARCLAYS CTR", "Atlantic Av-Barclays Ctr"),
                    ("YORK ST", "York St"),
                    ("AVENUE I", "Avenue I"),
                    ("EAST BROADWAY", "East Broadway"),
                    ("DELANCEY ST-ESSEX ST", "Delancey St-Essex St"),
                    (
                        "PRESIDENT ST-MEDGAR EVERS COLLEGE",
                        "President St-Medgar Evers College",
                    ),
                    ("FRANKLIN AV", "Franklin Av"),
                    ("BEACH 90 ST", "Beach 90 St"),
                    ("PARK PLACE", "Park Place"),
                    ("181 ST", "181 St"),
                    ("5 AV", "5 Av"),
                    ("MYRTLE-WILLOUGHBY AVS", "Myrtle-Willoughby Avs"),
                    ("EASTERN PKWY-BROOKLYN MUSEUM", "Eastern Pkwy-Brooklyn Museum"),
                    ("TOMPKINSVILLE", "Tompkinsville"),
                    ("INWOOD-207 ST", "Inwood-207 St"),
                    ("21 ST-QUEENSBRIDGE", "21 St-Queensbridge"),
                    ("JAMAICA CENTER-PARSONS/ARCHER", "Jamaica Center-Parsons/Archer"),
                    ("FLUSHING-MAIN ST", "Flushing-Main St"),
                    ("25 ST", "25 St"),
                    ("53 ST", "53 St"),
                    ("FOREST AV", "Forest Av"),
                    ("51 ST", "51 St"),
                    ("BRIGHTON BEACH", "Brighton Beach"),
                    ("ZEREGA AV", "Zerega Av"),
                    ("MOSHOLU PKWY", "Mosholu Pkwy"),
                    ("BOWLING GREEN", "Bowling Green"),
                    ("GUN HILL RD", "Gun Hill Rd"),
                    ("BROADWAY-LAFAYETTE ST", "Broadway-Lafayette St"),
                    ("JEFFERSON ST", "Jefferson St"),
                    ("HOYT-SCHERMERHORN STS", "Hoyt-Schermerhorn Sts"),
                    ("RALPH AV", "Ralph Av"),
                    ("CRESCENT ST", "Crescent St"),
                    ("168 ST", "168 St"),
                    ("KINGSTON-THROOP AVS", "Kingston-Throop Avs"),
                    ("FOREST HILLS-71 AV", "Forest Hills-71 Av"),
                    ("PROSPECT AV", "Prospect Av"),
                    ("NECK RD", "Neck Rd"),
                    ("18 ST", "18 St"),
                    ("BROAD ST", "Broad St"),
                    ("LEXINGTON AV/53 ST", "Lexington Av/53 St"),
                    ("DEKALB AV", "DeKalb Av"),
                    ("155 ST", "155 St"),
                    ("25 AV", "25 Av"),
                    (
                        "81 ST-MUSEUM OF NATURAL HISTORY",
                        "81 St-Museum of Natural History",
                    ),
                    ("MT EDEN AV", "Mt Eden Av"),
                    ("103 ST-CORONA PLAZA", "103 St-Corona Plaza"),
                    ("NEREID AV", "Nereid Av"),
                    ("238 ST", "238 St"),
                    ("145 ST", "145 St"),
                    ("LEXINGTON AV/63 ST", "Lexington Av/63 St"),
                    ("JAMAICA-VAN WYCK", "Jamaica-Van Wyck"),
                    ("5 AV/53 ST", "5 Av/53 St"),
                    ("FORT HAMILTON PKWY", "Fort Hamilton Pkwy"),
                    ("176 ST", "176 St"),
                    ("WEST FARMS SQ-E TREMONT AV", "West Farms Sq-E Tremont Av"),
                    ("BEVERLEY RD", "Beverley Rd"),
                    ("ALABAMA AV", "Alabama Av"),
                    ("CITY HALL", "City Hall"),
                    ("BROADWAY JUNCTION", "Broadway Junction"),
                    ("SIMPSON ST", "Simpson St"),
                    ("CHAMBERS ST", "Chambers St"),
                    ("CLARK ST", "Clark St"),
                    (
                        "MIDDLE VILLAGE-METROPOLITAN AV",
                        "Middle Village-Metropolitan Av",
                    ),
                    ("104 ST", "104 St"),
                    ("71 ST", "71 St"),
                    ("COURT SQ", "Court Sq"),
                    ("121 ST", "121 St"),
                    ("KEW GARDENS-UNION TPKE", "Kew Gardens-Union Tpke"),
                    ("CROWN HTS-UTICA AV", "Crown Hts-Utica Av"),
                    ("9 AV", "9 Av"),
                    ("PELHAM BAY PARK", "Pelham Bay Park"),
                    ("68 ST-HUNTER COLLEGE", "68 St-Hunter College"),
                    ("HUNTERS POINT AV", "Hunters Point Av"),
                    ("ALLERTON AV", "Allerton Av"),
                    ("82 ST-JACKSON HTS", "82 St-Jackson Hts"),
                    ("BAYCHESTER AV", "Baychester Av"),
                    ("COURT SQ-23 ST", "Court Sq-23 St"),
                    ("ASTOR PL", "Astor Pl"),
                    ("QUEENSBORO PLAZA", "Queensboro Plaza"),
                    ("149 ST-GRAND CONCOURSE", "149 St-Grand Concourse"),
                    ("111 ST", "111 St"),
                    ("JACKSON HTS-ROOSEVELT AV", "Jackson Hts-Roosevelt Av"),
                    ("DYCKMAN ST", "Dyckman St"),
                    ("JUNIUS ST", "Junius St"),
                    ("15 ST-PROSPECT PARK", "15 St-Prospect Park"),
                    ("KINGS HWY", "Kings Hwy"),
                    ("EAST 105 ST", "East 105 St"),
                    ("HARLEM-148 ST", "Harlem-148 St"),
                    ("ATLANTIC AV", "Atlantic Av"),
                    ("WOODHAVEN BLVD", "Woodhaven Blvd"),
                    ("CHAUNCEY ST", "Chauncey St"),
                    ("TREMONT AV", "Tremont Av"),
                    ("AVENUE N", "Avenue N"),
                    ("69 ST", "69 St"),
                    ("HUNTS POINT AV", "Hunts Point Av"),
                    ("CASTLE HILL AV", "Castle Hill Av"),
                    ("88 ST", "88 St"),
                    ("RECTOR ST", "Rector St"),
                    ("AQUEDUCT RACETRACK", "Aqueduct Racetrack"),
                    ("CORTELYOU RD", "Cortelyou Rd"),
                    ("59 ST-COLUMBUS CIRCLE", "59 St-Columbus Circle"),
                    ("BEDFORD-NOSTRAND AVS", "Bedford-Nostrand Avs"),
                    ("BROOKLYN BRIDGE-CITY HALL", "Brooklyn Bridge-City Hall"),
                    ("90 ST-ELMHURST AV", "90 St-Elmhurst Av"),
                    ("EASTCHESTER-DYRE AV", "Eastchester-Dyre Av"),
                    ("46 ST-BLISS ST", "46 St-Bliss St"),
                    ("40 ST-LOWERY ST", "40 St-Lowery St"),
                    (
                        "42 ST-PORT AUTHORITY BUS TERMINAL",
                        "42 St-Port Authority Bus Terminal",
                    ),
                    ("MORRIS PARK", "Morris Park"),
                    ("METS-WILLETS POINT", "Mets-Willets Point"),
                    ("AVENUE M", "Avenue M"),
                    ("161 ST-YANKEE STADIUM", "161 St-Yankee Stadium"),
                    ("BEVERLY RD", "Beverly Rd"),
                    ("LONGWOOD AV", "Longwood Av"),
                    ("219 ST", "219 St"),
                    ("ASTORIA BLVD", "Astoria Blvd"),
                    ("BRONX PARK EAST", "Bronx Park East"),
                    ("CHRISTOPHER ST-STONEWALL", "Christopher St-Stonewall"),
                    ("PRINCE'S BAY", "Prince's Bay"),
                    ("CANARSIE-ROCKAWAY PKWY", "Canarsie-Rockaway Pkwy"),
                    ("ST GEORGE", "St George"),
                    ("52 ST", "52 St"),
                    ("CLIFTON", "Clifton"),
                    ("28 ST", "28 St"),
                    (
                        "SUTPHIN BLVD-ARCHER AV-JFK AIRPORT",
                        "Sutphin Blvd-Archer Av-JFK Airport",
                    ),
                    ("ST LAWRENCE AV", "St Lawrence Av"),
                    ("E 143 ST-ST MARY'S ST", "E 143 St-St Mary's St"),
                    ("125 ST", "125 St"),
                    ("CLASSON AV", "Classon Av"),
                    ("CHURCH AV", "Church Av"),
                    ("57 ST", "57 St"),
                    ("PELHAM PKWY", "Pelham Pkwy"),
                    ("LAFAYETTE AV", "Lafayette Av"),
                    ("GRAND AV-NEWTOWN", "Grand Av-Newtown"),
                    ("50 ST", "50 St"),
                    ("116 ST", "116 St"),
                    ("74 ST-BROADWAY", "74 St-Broadway"),
                    ("WALL ST", "Wall St"),
                    ("137 ST-CITY COLLEGE", "137 St-City College"),
                    ("OLD TOWN", "Old Town"),
                    ("PARKCHESTER", "Parkchester"),
                    ("FREEMAN ST", "Freeman St"),
                    ("W 8 ST-NY AQUARIUM", "W 8 St-NY Aquarium"),
                    ("135 ST", "135 St"),
                    ("3 AV-138 ST", "3 Av-138 St"),
                    ("ELDER AV", "Elder Av"),
                    ("77 ST", "77 St"),
                    ("67 AV", "67 Av"),
                    ("DITMAS AV", "Ditmas Av"),
                    ("8 ST-NYU", "8 St-NYU"),
                    ("103 ST", "103 St"),
                    ("NORWOOD AV", "Norwood Av"),
                    ("BURKE AV", "Burke Av"),
                    ("SHEEPSHEAD BAY", "Sheepshead Bay"),
                    ("163 ST-AMSTERDAM AV", "163 St-Amsterdam Av"),
                    ("GRAND ST", "Grand St"),
                    ("GRAND ARMY PLAZA", "Grand Army Plaza"),
                    ("BROADWAY", "Broadway"),
                    ("W 4 ST-WASH SQ", "W 4 St-Wash Sq"),
                    ("SOUTH FERRY", "South Ferry"),
                    ("NORWOOD-205 ST", "Norwood-205 St"),
                    ("NEW LOTS AV", "New Lots Av"),
                    ("8 AV", "8 Av"),
                    ("85 ST-FOREST PKWY", "85 St-Forest Pkwy"),
                    ("VERNON BLVD-JACKSON AV", "Vernon Blvd-Jackson Av"),
                    ("BAY RIDGE-95 ST", "Bay Ridge-95 St"),
                    ("GRANT CITY", "Grant City"),
                    ("MORRISON AV-SOUNDVIEW", "Morrison Av-Soundview"),
                    ("45 ST", "45 St"),
                    ("CLINTON-WASHINGTON AVS", "Clinton-Washington Avs"),
                    ("VAN CORTLANDT PARK-242 ST", "Van Cortlandt Park-242 St"),
                    ("STEINWAY ST", "Steinway St"),
                    ("TOTTENVILLE", "Tottenville"),
                    ("GRANT AV", "Grant Av"),
                    (
                        "BEDFORD PARK BLVD-LEHMAN COLLEGE",
                        "Bedford Park Blvd-Lehman College",
                    ),
                    ("BEACH 44 ST", "Beach 44 St"),
                    ("138 ST-GRAND CONCOURSE", "138 St-Grand Concourse"),
                    ("WESTCHESTER SQ-E TREMONT AV", "Westchester Sq-E Tremont Av"),
                    ("FRESH POND RD", "Fresh Pond Rd"),
                    ("BERGEN ST", "Bergen St"),
                    ("BAY TERRACE", "Bay Terrace"),
                    ("JUNCTION BLVD", "Junction Blvd"),
                    ("INTERVALE AV", "Intervale Av"),
                    ("96 ST", "96 St"),
                    ("175 ST", "175 St"),
                    ("HALSEY ST", "Halsey St"),
                    ("FRANKLIN ST", "Franklin St"),
                    ("VAN SICLEN AV", "Van Siclen Av"),
                    ("47-50 STS-ROCKEFELLER CTR", "47-50 Sts-Rockefeller Ctr"),
                    ("55 ST", "55 St"),
                    ("LEXINGTON AV/59 ST", "Lexington Av/59 St"),
                    ("STERLING ST", "Sterling St"),
                    ("NEW DORP", "New Dorp"),
                    ("AQUEDUCT-N CONDUIT AV", "Aqueduct-N Conduit Av"),
                    ("ROOSEVELT ISLAND", "Roosevelt Island"),
                    ("NASSAU AV", "Nassau Av"),
                    ("169 ST", "169 St"),
                    ("59 ST", "59 St"),
                    ("ELMHURST AV", "Elmhurst Av"),
                    ("207 ST", "207 St"),
                    ("BEACH 36 ST", "Beach 36 St"),
                    ("FULTON ST", "Fulton St"),
                    ("191 ST", "191 St"),
                    ("SMITH-9 STS", "Smith-9 Sts"),
                    ("14 ST-UNION SQ", "14 St-Union Sq"),
                    ("215 ST", "215 St"),
                    ("49 ST", "49 St"),
                    ("BUHRE AV", "Buhre Av"),
                    ("75 AV", "75 Av"),
                    ("EUCLID AV", "Euclid Av"),
                    ("21 ST", "21 St"),
                    ("KNICKERBOCKER AV", "Knickerbocker Av"),
                    ("GREENPOINT AV", "Greenpoint Av"),
                    ("PARK PL", "Park Pl"),
                    ("BEACH 67 ST", "Beach 67 St"),
                    ("E 180 ST", "E 180 St"),
                    ("BOROUGH HALL", "Borough Hall"),
                    ("WORLD TRADE CENTER", "World Trade Center"),
                    ("SARATOGA AV", "Saratoga Av"),
                    ("FLATBUSH AV-BROOKLYN COLLEGE", "Flatbush Av-Brooklyn College"),
                    ("JEFFERSON AV", "Jefferson Av"),
                    ("170 ST", "170 St"),
                    ("86 ST", "86 St"),
                    ("HEWES ST", "Hewes St"),
                    ("HUGUENOT", "Huguenot"),
                    ("6 AV", "6 Av"),
                    ("5 AV/59 ST", "5 Av/59 St"),
                    ("CENTRAL PARK NORTH (110 ST)", "Central Park North (110 St)"),
                    ("167 ST", "167 St"),
                    ("BRIARWOOD", "Briarwood"),
                    ("BEACH 98 ST", "Beach 98 St"),
                    ("34 ST-HERALD SQ", "34 St-Herald Sq"),
                    ("ASTORIA-DITMARS BLVD", "Astoria-Ditmars Blvd"),
                    ("HIGH ST", "High St"),
                    ("PENNSYLVANIA AV", "Pennsylvania Av"),
                    ("BAY 50 ST", "Bay 50 St"),
                    ("4 AV-9 ST", "4 Av-9 St"),
                    ("CONEY ISLAND-STILLWELL AV", "Coney Island-Stillwell Av"),
                    ("7 AV", "7 Av"),
                    ("JAY ST-METROTECH", "Jay St-MetroTech"),
                    ("PROSPECT PARK", "Prospect Park"),
                    ("MIDDLETOWN RD", "Middletown Rd"),
                    ("KINGSBRIDGE RD", "Kingsbridge Rd"),
                    ("METROPOLITAN AV", "Metropolitan Av"),
                    ("FORDHAM RD", "Fordham Rd"),
                    ("FAR ROCKAWAY-MOTT AV", "Far Rockaway-Mott Av"),
                    (
                        "FRANKLIN AV-MEDGAR EVERS COLLEGE",
                        "Franklin Av-Medgar Evers College",
                    ),
                    ("NEWKIRK AV-LITTLE HAITI", "Newkirk Av-Little Haiti"),
                    ("WHITLOCK AV", "Whitlock Av"),
                    ("CYPRESS AV", "Cypress Av"),
                    ("NEWKIRK PLAZA", "Newkirk Plaza"),
                    ("MYRTLE-WYCKOFF AVS", "Myrtle-Wyckoff Avs"),
                    ("NOSTRAND AV", "Nostrand Av"),
                    ("KOSCIUSZKO ST", "Kosciuszko St"),
                    ("UTICA AV", "Utica Av"),
                    ("46 ST", "46 St"),
                    ("MARBLE HILL-225 ST", "Marble Hill-225 St"),
                    ("ANNADALE", "Annadale"),
                    ("AVENUE J", "Avenue J"),
                    ("WILSON AV", "Wilson Av"),
                    ("182-183 STS", "182-183 Sts"),
                    ("OZONE PARK-LEFFERTS BLVD", "Ozone Park-Lefferts Blvd"),
                    ("WINTHROP ST", "Winthrop St"),
                    ("CARROLL ST", "Carroll St"),
                    ("MONTROSE AV", "Montrose Av"),
                    ("33 ST-RAWSON ST", "33 St-Rawson St"),
                    ("MARCY AV", "Marcy Av"),
                    ("BOWERY", "Bowery"),
                    ("BEDFORD AV", "Bedford Av"),
                    ("BEDFORD PARK BLVD", "Bedford Park Blvd"),
                    ("BUSHWICK AV-ABERDEEN ST", "Bushwick Av-Aberdeen St"),
                    ("57 ST-7 AV", "57 St-7 Av"),
                    ("18 AV", "18 Av"),
                    ("MORGAN AV", "Morgan Av"),
                    ("174 ST", "174 St"),
                    ("BEACH 60 ST", "Beach 60 St"),
                    ("SHEPHERD AV", "Shepherd Av"),
                    ("WTC CORTLANDT", "WTC Cortlandt"),
                    ("STAPLETON", "Stapleton"),
                    ("E 149 ST", "E 149 St"),
                    ("RICHMOND VALLEY", "Richmond Valley"),
                    ("PARSONS BLVD", "Parsons Blvd"),
                    ("FLUSHING AV", "Flushing Av"),
                    ("CATHEDRAL PKWY (110 ST)", "Cathedral Pkwy (110 St)"),
                    ("168 ST-WASHINGTON HTS", "168 St-Washington Hts"),
                    ("GRAND CENTRAL-42 ST", "Grand Central-42 St"),
                    ("116 ST-COLUMBIA UNIVERSITY", "116 St-Columbia University"),
                    ("62 ST", "62 St"),
                    ("OAKWOOD HEIGHTS", "Oakwood Heights"),
                    ("GATES AV", "Gates Av"),
                    ("BOTANIC GARDEN", "Botanic Garden"),
                    ("BLEECKER ST", "Bleecker St"),
                    ("CYPRESS HILLS", "Cypress Hills"),
                    ("UNION ST", "Union St"),
                    ("14 ST", "14 St"),
                    ("61 ST-WOODSIDE", "61 St-Woodside"),
                    ("BROAD CHANNEL", "Broad Channel"),
                    ("HOUSTON ST", "Houston St"),
                    ("190 ST", "190 St"),
                    ("MYRTLE AV", "Myrtle Av"),
                    ("WAKEFIELD-241 ST", "Wakefield-241 St"),
                    ("AVENUE U", "Avenue U"),
                    ("PRINCE ST", "Prince St"),
                    ("72 ST", "72 St"),
                    ("63 DR-REGO PARK", "63 Dr-Rego Park"),
                    ("225 ST", "225 St"),
                    ("1 AV", "1 Av"),
                    ("SUTTER AV", "Sutter Av"),
                    ("23 ST", "23 St"),
                    ("SENECA AV", "Seneca Av"),
                    ("80 ST", "80 St"),
                    ("ROCKAWAY BLVD", "Rockaway Blvd"),
                    ("OCEAN PKWY", "Ocean Pkwy"),
                    ("PLEASANT PLAINS", "Pleasant Plains"),
                    ("174-175 STS", "174-175 Sts"),
                    ("CANAL ST", "Canal St"),
                    ("CORTLANDT ST", "Cortlandt St"),
                    ("SUTPHIN BLVD", "Sutphin Blvd"),
                    ("KINGSTON AV", "Kingston Av"),
                    ("34 ST-PENN STATION", "34 St-Penn Station"),
                    ("AVENUE H", "Avenue H"),
                    ("ROCKAWAY PARK-BEACH 116 ST", "Rockaway Park-Beach 116 St"),
                    ("CLEVELAND ST", "Cleveland St"),
                    ("66 ST-LINCOLN CENTER", "66 St-Lincoln Center"),
                    ("33 ST", "33 St"),
                    ("LIVONIA AV", "Livonia Av"),
                    ("QUEENS PLAZA", "Queens Plaza"),
                    ("BROOK AV", "Brook Av"),
                    ("ARTHUR KILL", "Arthur Kill"),
                    ("AVENUE P", "Avenue P"),
                    ("SPRING ST", "Spring St"),
                    ("BAY PKWY", "Bay Pkwy"),
                    ("3 AV", "3 Av"),
                    ("157 ST", "157 St"),
                    ("CENTRAL AV", "Central Av"),
                    ("DONGAN HILLS", "Dongan Hills"),
                    ("AVENUE X", "Avenue X"),
                    ("JACKSON AV", "Jackson Av"),
                    ("TIMES SQ-42 ST", "Times Sq-42 St"),
                    ("HOYT ST", "Hoyt St"),
                    ("GRASMERE", "Grasmere"),
                    ("BEACH 105 ST", "Beach 105 St"),
                    ("183 ST", "183 St"),
                    ("NEPTUNE AV", "Neptune Av"),
                    ("34 ST-HUDSON YARDS", "34 St-Hudson Yards"),
                    ("NEW UTRECHT AV", "New Utrecht Av"),
                    ("BURNSIDE AV", "Burnside Av"),
                ],
                max_length=40,
            ),
        ),
    ]
