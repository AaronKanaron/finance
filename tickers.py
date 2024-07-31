import json

def parse_line(line):
    parts = line.strip().split('\t')
    if len(parts) == 4:
        return {
            "symbol": parts[0],
            "name": parts[1],
            "sector": parts[2],
            "market_cap": parts[3]
        }
    return None

def text_to_json(text):
    lines = text.strip().split('\n')
    data = []
    for line in lines:
        parsed = parse_line(line)
        if parsed:
            data.append(parsed)
    return json.dumps(data, indent=2)

# Your sample data
text_content = """
A	Agilent Technologies, Inc.	Diagnostics & Research	40.29B
AA	Alcoa Corporation	Aluminum	5.67B
AACG	ATA Creativity Global	Education & Training Services	20.56M
AACI	Armada Acquisition Corp. I	Shell Companies	67.99M
AACT	Ares Acquisition Corporation II	Shell Companies	670.00M
AADI	Aadi Bioscience, Inc.	Biotechnology	38.55M
AAGR	African Agriculture Holdings Inc.	Farm Products	9.12M
AAL	American Airlines Group Inc.	Airlines	7.10B
AAMC	Altisource Asset Management Corporation	Mortgage Finance	6.51M
AAME	Atlantic American Corporation	Insurance - Life	31.21M
AAN	The Aaron's Company, Inc.	Rental & Leasing Services	314.43M
AAOI	Applied Optoelectronics, Inc.	Communication Equipment	316.71M
AAON	AAON, Inc.	Building Products & Equipment	7.03B
AAP	Advance Auto Parts, Inc.	Specialty Retail	3.72B
AAPL	Apple Inc	Consumer Electronics	3,329.34B
AAT	American Assets Trust, Inc.	REIT - Diversified	1.52B
AB	AllianceBernstein Holding L.P.	Asset Management	3.97B
ABAT	American Battery Technology Company	Other Industrial Metals & Mining	59.18M
ABBV	AbbVie Inc.	Drug Manufacturers - General	328.80B
ABCB	Ameris Bancorp	Banks - Regional	4.23B
ABCL	AbCellera Biologics Inc.	Biotechnology	943.91M
ABEO	Abeona Therapeutics Inc.	Biotechnology	198.26M
ABEV	Ambev S.A.	Beverages - Brewers	32.83B
ABG	Asbury Automotive Group, Inc.	Auto & Truck Dealerships	5.18B
ABIO	ARCA biopharma, Inc.	Biotechnology	43.52M
ABL	Abacus Life, Inc.	Insurance - Life	724.65M
ABLV	Able View Inc.	Advertising Agencies	49.00M
ABM	ABM Industries Incorporated	Specialty Business Services	3.50B
ABNB	Airbnb, Inc.	Travel Services	89.23B
ABOS	Acumen Pharmaceuticals, Inc.	Biotechnology	195.92M
ABR	Arbor Realty Trust, Inc.	REIT - Mortgage	2.57B
ABSI	Absci Corporation	Biotechnology	482.87M
ABT	Abbott Laboratories	Medical Devices	182.43B
ABTS	Abits Group Inc.	Capital Markets	20.28M
ABUS	Arbutus Biopharma Corporation	Biotechnology	714.29M
ABVC	ABVC BioPharma, Inc.	Biotechnology	8.85M
ABVE	Above Food Ingredients Inc.	Packaged Foods	36.98M
ABVX	Abivax SA	Biotechnology	743.37M
AC	Associated Capital Group, Inc.	Asset Management	727.23M
ACA	Arcosa, Inc.	Engineering & Construction	4.45B
ACAB	Atlantic Coastal Acquisition Corp. II	Shell Companies	89.51M
ACAC	Acri Capital Acquisition Corporation	Shell Companies	45.63M
ACAD	ACADIA Pharmaceuticals Inc.	Biotechnology	3.05B
ACB	Aurora Cannabis Inc.	Drug Manufacturers - Specialty & Generic	320.75M
ACCD	Accolade, Inc.	Health Information Services	319.63M
ACCO	ACCO Brands Corporation	Business Equipment & Supplies	492.54M
ACDC	ProFrac Holding Corp.	Oil & Gas Equipment & Services	1.31B
ACEL	Accel Entertainment, Inc.	Gambling	925.40M
ACET	Adicet Bio, Inc.	Biotechnology	131.07M
ACGL	Arch Capital Group Ltd.	Insurance - Diversified	36.92B
ACHC	Acadia Healthcare Company, Inc.	Medical Care Facilities	6.23B
ACHL	Achilles Therapeutics plc	Biotechnology	33.28M
ACHR	Archer Aviation Inc.	Aerospace & Defense	1.42B
ACHV	Achieve Life Sciences, Inc.	Biotechnology	167.93M
ACI	Albertsons Companies, Inc.	Grocery Stores	11.55B
ACIC	American Coastal Insurance Corporation	Insurance - Property & Casualty	580.88M
ACIU	AC Immune SA	Biotechnology	402.74M
ACIW	ACI Worldwide, Inc.	Software - Infrastructure	4.53B
ACLS	Axcelis Technologies, Inc.	Semiconductor Equipment & Materials	3.86B
ACLX	Arcellx, Inc.	Biotechnology	3.28B
ACM	AECOM	Engineering & Construction	12.28B
ACMR	ACM Research, Inc.	Semiconductor Equipment & Materials	1.09B
ACN	Accenture plc	Information Technology Services	205.96B
ACNB	ACNB Corporation	Banks - Regional	335.67M
ACNT	Ascent Industries Co.	Steel	100.79M
ACON	Aclarion, Inc.	Health Information Services	2.54M
ACR	ACRES Commercial Realty Corp.	REIT - Mortgage	115.12M
ACRE	Ares Commercial Real Estate Corporation	REIT - Mortgage	423.79M
ACRS	Aclaris Therapeutics, Inc.	Diagnostics & Research	94.78M
ACRV	Acrivon Therapeutics, Inc.	Biotechnology	253.81M
ACST	Acasti Pharma Inc.	Biotechnology	25.57M
ACT	Enact Holdings, Inc.	Insurance - Specialty	5.39B
ACTG	Acacia Research Corporation	Business Equipment & Supplies	532.44M
ACU	Acme United Corporation	Household & Personal Products	163.14M
ACVA	ACV Auctions Inc.	Auto & Truck Dealerships	2.80B
ACXP	Acurx Pharmaceuticals, Inc.	Biotechnology	33.86M
ADAG	Adagene Inc.	Biotechnology	106.25M
ADAP	Adaptimmune Therapeutics plc	Biotechnology	347.47M
ADBE	Adobe Inc.	Software - Infrastructure	237.11B
ADC	Agree Realty Corporation	REIT - Retail	7.02B
ADCT	ADC Therapeutics SA	Biotechnology	321.88M
ADD	Color Star Technology Co., Ltd.	Entertainment	13.50M
ADEA	Adeia Inc.	Software - Application	1.24B
ADI	Analog Devices, Inc.	Semiconductors	112.60B
ADIL	Adial Pharmaceuticals, Inc.	Biotechnology	4.04M
ADM	Archer-Daniels-Midland Company	Farm Products	30.99B
ADMA	ADMA Biologics, Inc.	Biotechnology	2.78B
ADN	Advent Technologies Holdings, Inc.	Utilities - Renewable	11.51M
ADNT	Adient plc	Auto Parts	2.28B
ADP	Automatic Data Processing, Inc.	Staffing & Employment Services	105.35B
ADPT	Adaptive Biotechnologies Corporation	Biotechnology	662.42M
ADRT	Ault Disruptive Technologies Corporation	Shell Companies	49.13M
ADSE	ADS-TEC Energy PLC	Electrical Equipment & Parts	626.24M
ADSK	Autodesk, Inc.	Software - Application	52.22B
ADT	ADT Inc.	Security & Protection Services	6.56B
ADTN	ADTRAN Holdings, Inc.	Communication Equipment	518.21M
ADTX	Aditxt, Inc.	Biotechnology	2.40M
ADUS	Addus HomeCare Corporation	Medical Care Facilities	2.18B
ADV	Advantage Solutions Inc.	Advertising Agencies	1.27B
ADVM	Adverum Biotechnologies, Inc.	Biotechnology	150.49M
ADXN	Addex Therapeutics Ltd	Biotechnology	12.91M
AE	Adams Resources & Energy, Inc.	Oil & Gas Refining & Marketing	68.80M
AEAE	AltEnergy Acquisition Corp.	Shell Companies	70.30M
AEE	Ameren Corporation	Utilities - Regulated Electric	21.11B
AEG	Aegon N.V.	Insurance - Diversified	10.35B
AEHL	Antelope Enterprise Holdings Limited	Building Products & Equipment	41.49M
AEHR	Aehr Test Systems	Semiconductor Equipment & Materials	530.30M
AEI	Alset EHome International Inc.	Real Estate - Development	10.99M
AEIS	Advanced Energy Industries, Inc.	Electrical Equipment & Parts	4.04B
AEM	Agnico Eagle Mines Limited	Gold	37.18B
AEMD	Aethlon Medical, Inc.	Medical Devices	5.14M
AENT	Alliance Entertainment Holding Corporation	Entertainment	99.33M
AEO	American Eagle Outfitters, Inc.	Apparel Retail	4.36B
AEON	AEON Biopharma, Inc.	Biotechnology	73.91M
AEP	American Electric Power Company, Inc.	Utilities - Regulated Electric	51.09B
AER	AerCap Holdings N.V.	Rental & Leasing Services	19.65B
AERT	Aeries Technology, Inc	Consulting Services	95.30M
AES	The AES Corporation	Utilities - Diversified	12.43B
AESI	Atlas Energy Solutions Inc.	Oil & Gas Equipment & Services	2.27B
AEVA	Aeva Technologies, Inc.	Software - Infrastructure	182.85M
AEYE	AudioEye, Inc.	Software - Application	288.97M
AEZS	Aeterna Zentaris Inc.	Biotechnology	16.41M
AFAR	Aura FAT Projects Acquisition Corp	Shell Companies	67.53M
AFBI	Affinity Bancshares, Inc.	Banks - Regional	139.37M
AFCG	AFC Gamma, Inc.	REIT - Specialty	184.76M
AFG	American Financial Group, Inc.	Insurance - Property & Casualty	10.96B
AFJK	Aimei Health Technology Co., Ltd Ordinary Share	Shell Companies	93.78M
AFL	Aflac Incorporated	Insurance - Life	54.29B
AFMD	Affimed N.V.	Biotechnology	80.74M
AFRI	Forafric Global PLC	Farm Products	306.56M
AFRM	Affirm Holdings, Inc.	Software - Infrastructure	8.48B
AFYA	Afya Limited	Education & Training Services	1.52B
AG	First Majestic Silver Corp.	Silver	1.74B
AGAE	Allied Gaming & Entertainment Inc.	Entertainment	63.04M
AGBA	AGBA Acquisition Limited	Asset Management	183.10M
AGCO	AGCO Corporation	Farm & Heavy Construction Machinery	7.24B
AGEN	Agenus Inc.	Biotechnology	132.63M
AGFY	Agrify Corporation	Farm & Heavy Construction Machinery	3.97M
AGI	Alamos Gold Inc.	Gold	7.02B
AGIO	Agios Pharmaceuticals, Inc.	Biotechnology	2.66B
AGL	agilon health, inc.	Medical Care Facilities	2.99B
AGM	Federal Agricultural Mortgage Corporation	Credit Services	2.21B
AGM.A	Federal Agricultural Mortgage Corporation	Credit Services	2.29B
AGMH	AGM Group Holdings Inc.	Computer Hardware	18.55M
AGNC	AGNC Investment Corp.	REIT - Mortgage	7.79B
AGO	Assured Guaranty Ltd.	Insurance - Specialty	4.45B
AGR	Avangrid, Inc.	Utilities - Regulated Electric	13.75B
AGRI	AgriFORCE Growing Systems Ltd.	Farm Products	4.56M
AGRO	Adecoagro S.A.	Farm Products	984.60M
AGS	PlayAGS, Inc.	Gambling	460.14M
AGX	Argan, Inc.	Engineering & Construction	1.03B
AGYS	Agilysys, Inc.	Software - Application	3.03B
AHCO	AdaptHealth Corp.	Medical Devices	1.53B
AHG	Akso Health Group	Medical Distribution	21.04M
AHH	Armada Hoffler Properties, Inc.	REIT - Diversified	803.54M
AHI	Advanced Human Imaging Limited	Software - Application	13.11M
AHR	American Healthcare REIT, Inc.	REIT - Healthcare Facilities	771.27M
AHT	Ashford Hospitality Trust, Inc.	REIT - Hotel & Motel	43.96M
AI	C3.ai, Inc.	Software - Application	3.23B
AIEV	Thunder Power Holdings, Inc.	Shell Companies	3.93M
AIG	American International Group, Inc.	Insurance - Diversified	52.82B
AIHS	Senmiao Technology Limited	Credit Services	10.23M
AILE	iLearningEngines Inc.	Software - Infrastructure	1.12B
AIM	AIM ImmunoTech Inc.	Biotechnology	20.57M
AIMAU	Aimfinity Investment Corp. I	Shell Companies	96.61M
AIMD	Ainos, Inc.	Medical Devices	4.98M
AIN	Albany International Corp.	Textile Manufacturing	2.88B
AIOT	PowerFleet, Inc.	Software - Infrastructure	484.15M
AIP	Arteris, Inc.	Semiconductors	310.53M
AIR	AAR Corp.	Aerospace & Defense	2.31B
AIRE	reAlpha Tech Corp.	Real Estate Services	66.04M
AIRG	Airgain, Inc.	Communication Equipment	80.83M
AIRI	Air Industries Group	Aerospace & Defense	12.33M
AIRJ	Montana Technologies Corporation	Building Products & Equipment	557.68M
AIRS	AirSculpt Technologies, Inc.	Medical Care Facilities	268.85M
AIRT	Air T, Inc.	Conglomerates	68.34M
AISP	Airship AI Holdings, Inc.	Software - Infrastructure	88.06M
AIT	Applied Industrial Technologies, Inc.	Industrial Distribution	8.34B
AITR	AI TRANSPORTATION ACQUISITION CORP	Shell Companies	81.36M
AIU	Meta Data Limited	Education & Training Services	35.47M
AIV	Apartment Investment and Management Company	REIT - Residential	1.30B
AIXI	Xiao-I Corporation	Software - Application	46.65M
AIZ	Assurant, Inc.	Insurance - Specialty	9.15B
AJG	Arthur J. Gallagher & Co.	Insurance Brokers	61.89B
AJX	Great Ajax Corp.	REIT - Mortgage	154.60M
AKA	a.k.a. Brands Holding Corp.	Apparel Retail	167.34M
AKAM	Akamai Technologies, Inc.	Software - Infrastructure	14.83B
AKAN	Akanda Corp.	Drug Manufacturers - Specialty & Generic	2.84M
AKBA	Akebia Therapeutics, Inc.	Biotechnology	290.29M
AKO.A	Embotelladora Andina S.A.	Beverages - Non-Alcoholic	2.64B
AKO.B	Embotelladora Andina S.A.	Beverages - Non-Alcoholic	3.01B
AKR	Acadia Realty Trust	REIT - Retail	2.17B
AKRO	Akero Therapeutics, Inc.	Biotechnology	1.85B
AKTS	Akoustis Technologies, Inc.	Communication Equipment	13.06M
AKTX	Akari Therapeutics, Plc	Biotechnology	30.90M
AKYA	Akoya Biosciences, Inc.	Medical Instruments & Supplies	119.02M
AL	Air Lease Corporation	Rental & Leasing Services	5.46B
ALAB	Astera Labs, Inc.	Semiconductors	6.59B
ALAR	Alarum Technologies Ltd.	Software - Infrastructure	170.47M
ALB	Albemarle Corporation	Specialty Chemicals	10.69B
ALBT	Avalon GloboCare Corp.	Real Estate Services	3.66M
ALC	Alcon Inc.	Medical Instruments & Supplies	46.06B
ALCE	Alternus Clean Energy Inc	Utilities - Renewable	25.04M
ALCO	Alico, Inc.	Farm Products	218.81M
ALCY	Alchemy Investments Acquisition Corp 1	Shell Companies	161.68M
ALDX	Aldeyra Therapeutics, Inc.	Biotechnology	232.90M
ALE	ALLETE, Inc.	Utilities - Diversified	3.73B
ALEC	Alector, Inc.	Biotechnology	614.93M
ALEX	Alexander & Baldwin, Inc.	REIT - Retail	1.43B
ALF	Centurion Acquisition Corp.	Shell Companies	3.61B
ALG	Alamo Group Inc.	Farm & Heavy Construction Machinery	2.32B
ALGM	Allegro MicroSystems, Inc.	Semiconductors	4.40B
ALGN	Align Technology, Inc.	Medical Devices	17.21B
ALGS	Aligos Therapeutics, Inc.	Biotechnology	39.22M
ALGT	Allegiant Travel Company	Airlines	999.22M
ALHC	Alignment Healthcare, Inc.	Healthcare Plans	1.70B
ALIM	Alimera Sciences, Inc.	Drug Manufacturers - Specialty & Generic	292.15M
ALIT	Alight, Inc.	Software - Application	4.13B
ALK	Alaska Air Group, Inc.	Airlines	4.95B
ALKS	Alkermes plc	Drug Manufacturers - Specialty & Generic	4.54B
ALKT	Alkami Technology, Inc.	Software - Application	3.20B
ALL	The Allstate Corporation	Insurance - Property & Casualty	45.76B
ALLE	Allegion plc	Security & Protection Services	12.06B
ALLG	Allego N.V.	Specialty Retail	459.36M
ALLK	Allakos Inc.	Biotechnology	80.31M
ALLO	Allogene Therapeutics, Inc.	Biotechnology	607.37M
ALLR	Allarity Therapeutics, Inc.	Biotechnology	4.81M
ALLT	Allot Ltd.	Software - Infrastructure	110.71M
ALLY	Ally Financial Inc.	Credit Services	13.50B
ALMS	Alumis Inc.	Biotechnology	676.41M
ALNT	Allient Inc.	Electronic Components	475.26M
ALNY	Alnylam Pharmaceuticals, Inc.	Biotechnology	29.49B
ALOT	AstroNova, Inc.	Computer Hardware	116.46M
ALPP	Alpine 4 Holdings, Inc.	Conglomerates	10.67M
ALRM	Alarm.com Holdings, Inc.	Software - Application	3.56B
ALRN	Aileron Therapeutics, Inc.	Biotechnology	49.71M
ALRS	Alerus Financial Corporation	Banks - Regional	440.55M
ALSA	Alpha Star Acquisition Corporation	Shell Companies	66.86M
ALSN	Allison Transmission Holdings, Inc.	Auto Parts	7.70B
ALT	Altimmune, Inc.	Biotechnology	439.24M
ALTG	Alta Equipment Group Inc.	Rental & Leasing Services	352.69M
ALTI	AlTi Global, Inc.	Asset Management	574.84M
ALTM	Arcadium Lithium plc	Specialty Chemicals	3.39B
ALTO	Alto Ingredients, Inc.	Specialty Chemicals	119.16M
ALTR	Altair Engineering Inc.	Software - Infrastructure	7.23B
ALTS	ALT5 Sigma Corporation	Waste Management	26.90M
ALUR	Allurion Technologies Inc.	Medical Devices	52.96M
ALV	Autoliv, Inc.	Auto Parts	7.94B
ALVO	Alvotech	Drug Manufacturers - Specialty & Generic	3.54B
ALVR	AlloVir, Inc.	Biotechnology	86.19M
ALX	Alexander's, Inc.	REIT - Retail	1.23B
ALXO	ALX Oncology Holdings Inc.	Biotechnology	278.74M
ALZN	Alzamend Neuro, Inc.	Biotechnology	3.15M
AM	Antero Midstream Corporation	Oil & Gas Midstream	6.99B
AMAL	Amalgamated Financial Corp.	Banks - Regional	975.85M
AMAT	Applied Materials, Inc.	Semiconductor Equipment & Materials	165.23B
AMBA	Ambarella, Inc.	Semiconductor Equipment & Materials	2.09B
AMBC	Ambac Financial Group, Inc.	Insurance - Specialty	585.21M
AMBI	Ambipar Emergency Response	Waste Management	256.09M
AMBO	Ambow Education Holding Ltd.	Education & Training Services	3.65M
AMBP	Ardagh Metal Packaging S.A.	Packaging & Containers	2.18B
AMC	AMC Entertainment Holdings, Inc.	Entertainment	1.89B
AMCR	Amcor plc	Packaging & Containers	15.13B
AMCX	AMC Networks Inc.	Entertainment	486.24M
AMD	Advanced Micro Devices, Inc.	Semiconductors	220.39B
AME	AMETEK, Inc.	Specialty Industrial Machinery	39.79B
AMED	Amedisys, Inc.	Medical Care Facilities	3.21B
AMG	Affiliated Managers Group, Inc.	Asset Management	5.81B
AMGN	Amgen Inc.	Drug Manufacturers - General	178.91B
AMH	American Homes 4 Rent	REIT - Residential	13.13B
AMIX	Autonomix Medical, Inc.	Medical Devices	20.35M
AMK	AssetMark Financial Holdings, Inc.	Asset Management	2.57B
AMKR	Amkor Technology, Inc.	Semiconductor Equipment & Materials	7.66B
AMLI	American Lithium Corp.	Other Industrial Metals & Mining	98.14M
AMLX	Amylyx Pharmaceuticals, Inc.	Biotechnology	128.87M
AMN	AMN Healthcare Services, Inc.	Medical Care Facilities	2.58B
AMP	Ameriprise Financial, Inc.	Asset Management	42.98B
AMPG	AmpliTech Group, Inc.	Communication Equipment	11.18M
AMPH	Amphastar Pharmaceuticals, Inc.	Drug Manufacturers - Specialty & Generic	2.10B
AMPL	Amplitude, Inc.	Software - Application	1.04B
AMPS	Altus Power, Inc.	Utilities - Renewable	651.49M
AMPX	Amprius Technologies, Inc.	Electrical Equipment & Parts	127.29M
AMPY	Amplify Energy Corp.	Oil & Gas Exploration & Production	291.74M
AMR	Alpha Metallurgical Resources, Inc.	Coking Coal	3.78B
AMRC	Ameresco, Inc.	Engineering & Construction	1.61B
AMRK	A-Mark Precious Metals, Inc.	Capital Markets	860.84M
AMRN	Amarin Corporation plc	Drug Manufacturers - General	320.21M
AMRX	Amneal Pharmaceuticals, Inc.	Drug Manufacturers - Specialty & Generic	2.23B
AMS	American Shared Hospital Services	Medical Care Facilities	19.46M
AMSC	American Superconductor Corporation	Specialty Industrial Machinery	864.28M
AMSF	AMERISAFE, Inc.	Insurance - Specialty	882.13M
AMST	Amesite Inc.	Software - Application	6.58M
AMSWA	American Software, Inc.	Software - Application	353.11M
AMT	American Tower Corporation	REIT - Specialty	102.94B
AMTB	Amerant Bancorp Inc.	Banks - Regional	759.62M
AMTD	AMTD IDEA Group	Asset Management	1.05B
AMTX	Aemetis, Inc.	Oil & Gas Refining & Marketing	150.51M
AMWD	American Woodmark Corporation	Furnishings, Fixtures & Appliances	1.60B
AMWL	American Well Corporation	Health Information Services	126.08M
AMX	América Móvil, SAB de CV	Telecom Services	51.54B
AMZN	Amazon.com, Inc.	Internet Retail	1,885.62B
AN	AutoNation, Inc.	Auto & Truck Dealerships	7.15B
ANAB	AnaptysBio, Inc.	Biotechnology	968.17M
ANDE	The Andersons, Inc.	Food Distribution	1.88B
ANEB	Anebulo Pharmaceuticals, Inc.	Biotechnology	57.05M
ANET	Arista Networks, Inc.	Computer Hardware	97.95B
ANF	Abercrombie & Fitch Co.	Apparel Retail	7.62B
ANGH	Anghami Inc.	Entertainment	28.52M
ANGI	Angi Inc.	Internet Content & Information	1.11B
ANGO	AngioDynamics, Inc.	Medical Instruments & Supplies	320.80M
ANIK	Anika Therapeutics, Inc.	Medical Instruments & Supplies	405.46M
ANIP	ANI Pharmaceuticals, Inc.	Drug Manufacturers - Specialty & Generic	1.35B
ANIX	Anixa Biosciences, Inc.	Biotechnology	99.54M
ANL	Adlai Nortye Ltd.	Biotechnology	364.21M
ANNX	Annexon, Inc.	Biotechnology	653.04M
ANRO	Alto Neuroscience, Inc.	Biotechnology	361.59M
ANSC	Agriculture & Natural Solutions Acquisition Corporation	Shell Companies	444.40M
ANSS	ANSYS, Inc.	Software - Application	26.75B
ANTE	AirNet Technology Inc.	Advertising Agencies	6.22M
ANTX	AN2 Therapeutics, Inc.	Biotechnology	76.66M
ANVS	Annovis Bio, Inc.	Biotechnology	109.52M
ANY	Sphere 3D Corp.	Software - Application	21.17M
AOGO	Arogo Capital Acquisition Corp.	Shell Companies	47.68M
AOMR	Angel Oak Mortgage, Inc.	REIT - Mortgage	307.23M
AON	Aon plc	Insurance Brokers	71.19B
AORT	Artivion, Inc.	Medical Devices	1.13B
AOS	A. O. Smith Corporation	Specialty Industrial Machinery	12.47B
AOSL	Alpha and Omega Semiconductor Limited	Semiconductors	1.19B
AOUT	American Outdoor Brands, Inc.	Leisure	127.01M
AP	Ampco-Pittsburgh Corporation	Metal Fabrication	31.95M
APA	APA Corporation	Oil & Gas Exploration & Production	11.46B
APAM	Artisan Partners Asset Management Inc.	Asset Management	3.04B
APCX	AppTech Payments Corp.	Software - Infrastructure	23.44M
APD	Air Products and Chemicals, Inc.	Specialty Chemicals	59.03B
APDN	Applied DNA Sciences, Inc.	Diagnostics & Research	3.54M
APEI	American Public Education, Inc.	Education & Training Services	350.10M
APG	APi Group Corporation	Engineering & Construction	10.21B
APGE	Apogee Therapeutics, Inc.	Biotechnology	2.84B
APH	Amphenol Corporation	Electronic Components	73.79B
API	Agora, Inc.	Software - Application	228.93M
APLD	Applied Digital Corporation	Information Technology Services	597.93M
APLE	Apple Hospitality REIT, Inc.	REIT - Hotel & Motel	3.66B
APLM	Apollomics, Inc.	Biotechnology	21.65M
APLS	Apellis Pharmaceuticals, Inc.	Biotechnology	4.70B
APLT	Applied Therapeutics, Inc.	Biotechnology	565.62M
APM	Aptorum Group Limited	Biotechnology	17.46M
APO	Apollo Global Management, Inc.	Asset Management	70.00B
APOG	Apogee Enterprises, Inc.	Building Products & Equipment	1.49B
APP	AppLovin Corporation	Software - Application	24.66B
APPF	AppFolio, Inc.	Software - Application	8.19B
APPN	Appian Corporation	Software - Infrastructure	2.68B
APPS	Digital Turbine, Inc.	Software - Application	235.45M
APRE	Aprea Therapeutics, Inc.	Biotechnology	20.69M
APT	Alpha Pro Tech, Ltd.	Building Products & Equipment	67.85M
APTO	Aptose Biosciences Inc.	Biotechnology	10.41M
APTV	Aptiv PLC	Auto Parts	18.56B
APVO	Aptevo Therapeutics Inc.	Biotechnology	3.12M
APWC	Asia Pacific Wire & Cable Corporation Limited	Electrical Equipment & Parts	32.99M
APXI	APx Acquisition Corp. I	Shell Companies	115.06M
APYX	Apyx Medical Corporation	Medical Devices	46.74M
AQB	AquaBounty Technologies, Inc.	Farm Products	5.90M
AQMS	Aqua Metals, Inc.	Waste Management	41.56M
AQN	Algonquin Power & Utilities Corp.	Utilities - Renewable	4.78B
AQST	Aquestive Therapeutics, Inc.	Drug Manufacturers - Specialty & Generic	340.03M
AQU	Aquaron Acquisition Corp.	Shell Companies	26.54M
AR	Antero Resources Corporation	Oil & Gas Exploration & Production	8.98B
ARAY	Accuray Incorporated	Medical Devices	185.09M
ARBB	ARB IOT Group Limited	Information Technology Services	10.45M
ARBE	Arbe Robotics Ltd.	Software - Infrastructure	170.52M
ARBK	Argo Blockchain plc	Capital Markets	92.98M
ARC	ARC Document Solutions, Inc.	Specialty Business Services	133.91M
ARCB	ArcBest Corporation	Trucking	2.89B
ARCC	Ares Capital Corporation	Asset Management	12.85B
ARCH	Arch Resources, Inc.	Coking Coal	2.55B
ARCO	Arcos Dorados Holdings Inc.	Restaurants	2.02B
ARCT	Arcturus Therapeutics Holdings Inc.	Biotechnology	622.66M
ARDT	Ardent Health Partners, Inc.	Medical Care Facilities	2.48B
ARDX	Ardelyx, Inc.	Biotechnology	1.27B
ARE	Alexandria Real Estate Equities, Inc.	REIT - Office	20.61B
AREB	American Rebel Holdings, Inc.	Footwear & Accessories	3.68M
AREC	American Resources Corporation	Coking Coal	51.98M
AREN	The Arena Group Holdings, Inc.	Internet Content & Information	26.34M
ARES	Ares Management Corporation	Asset Management	29.25B
ARGX	argenx SE	Biotechnology	30.13B
ARHS	Arhaus, Inc.	Home Improvement Retail	2.13B
ARI	Apollo Commercial Real Estate Finance, Inc.	REIT - Mortgage	1.55B
ARIS	Aris Water Solutions, Inc.	Utilities - Regulated Water	515.34M
ARKO	Arko Corp.	Specialty Retail	748.86M
ARKR	Ark Restaurants Corp.	Restaurants	48.15M
ARL	American Realty Investors, Inc.	Real Estate Services	356.80M
ARLO	Arlo Technologies, Inc.	Building Products & Equipment	1.47B
ARLP	Alliance Resource Partners, L.P.	Thermal Coal	3.11B
ARM	Arm Holdings plc	Semiconductors	138.71B
ARMK	Aramark	Specialty Business Services	8.96B
ARMN	Aris Mining Corporation	Gold	704.04M
ARMP	Armata Pharmaceuticals, Inc.	Biotechnology	108.46M
AROC	Archrock, Inc.	Oil & Gas Equipment & Services	3.63B
AROW	Arrow Financial Corporation	Banks - Regional	527.67M
ARQ	Arq, Inc.	Pollution & Treatment Controls	236.06M
ARQQ	Arqit Quantum Inc.	Software - Infrastructure	59.95M
ARQT	Arcutis Biotherapeutics, Inc.	Biotechnology	1.09B
ARR	ARMOUR Residential REIT, Inc.	REIT - Mortgage	1.00B
ARRY	Array Technologies, Inc.	Solar	1.58B
ARTL	Artelo Biosciences, Inc.	Biotechnology	4.29M
ARTNA	Artesian Resources Corporation	Utilities - Regulated Water	401.79M
ARTV	Artiva Biotherapeutics, Inc.	Biotechnology	268.39M
ARTW	Art's-Way Manufacturing Co., Inc.	Farm & Heavy Construction Machinery	7.74M
ARVN	Arvinas, Inc.	Biotechnology	1.86B
ARW	Arrow Electronics, Inc.	Electronics & Computer Distribution	6.63B
ARWR	Arrowhead Pharmaceuticals, Inc.	Biotechnology	3.54B
ARYD	ARYA Sciences Acquisition Corp IV	Shell Companies	69.90M
AS	Amer Sports, Inc.	Leisure	5.72B
ASA	ASA Gold and Precious Metals Limited	Asset Management	360.91M
ASAI	Sendas Distribuidora S.A.	Grocery Stores	2.30B
ASAN	Asana, Inc.	Software - Application	3.43B
ASB	Associated Banc-Corp	Banks - Regional	3.48B
ASC	Ardmore Shipping Corporation	Marine Shipping	870.05M
ASCB	A SPAC II Acquisition Corporation	Shell Companies	81.97M
ASGN	ASGN Incorporated	Information Technology Services	4.38B
ASH	Ashland Inc.	Specialty Chemicals	4.80B
ASIX	AdvanSix Inc.	Chemicals	740.74M
ASLE	AerSale Corporation	Airports & Air Services	356.22M
ASM	Avino Silver & Gold Mines Ltd.	Other Precious Metals & Mining	137.06M
ASMB	Assembly Biosciences, Inc.	Biotechnology	90.43M
ASML	ASML Holding N.V.	Semiconductor Equipment & Materials	340.46B
ASND	Ascendis Pharma A/S	Biotechnology	7.47B
ASNS	Actelis Networks, Inc.	Communication Equipment	8.55M
ASO	Academy Sports and Outdoors, Inc.	Specialty Retail	3.88B
ASPI	ASP Isotopes Inc.	Chemicals	163.18M
ASPN	Aspen Aerogels, Inc.	Building Products & Equipment	1.57B
ASPS	Altisource Portfolio Solutions S.A.	Real Estate Services	37.14M
ASR	Grupo Aeroportuario del Sureste, S. A. B. de C. V.	Airports & Air Services	9.07B
ASRT	Assertio Holdings, Inc.	Drug Manufacturers - Specialty & Generic	134.12M
ASRV	AmeriServ Financial, Inc.	Banks - Regional	42.12M
ASST	Asset Entities Inc.	Internet Content & Information	12.25M
ASTC	Astrotech Corporation	Aerospace & Defense	14.45M
ASTE	Astec Industries, Inc.	Farm & Heavy Construction Machinery	788.25M
ASTH	Astrana Health, Inc.	Medical Care Facilities	2.68B
ASTI	Ascent Solar Technologies, Inc.	Solar	7.35M
ASTL	Algoma Steel Group Inc.	Steel	891.12M
ASTS	AST SpaceMobile, Inc.	Communication Equipment	4.77B
ASUR	Asure Software, Inc.	Software - Application	265.87M
ASX	ASE Technology Holding Co., Ltd.	Semiconductors	21.05B
ASXC	Asensus Surgical, Inc.	Medical Devices	92.01M
ASYS	Amtech Systems, Inc.	Semiconductor Equipment & Materials	82.13M
ATAI	Atai Life Sciences N.V.	Biotechnology	256.13M
ATAT	Atour Lifestyle Holdings Limited	Lodging	2.26B
ATCH	AtlasClear Holdings Inc.	Software - Infrastructure	5.54M
ATEC	Alphatec Holdings, Inc.	Medical Devices	1.40B
ATEK	Athena Technology Acquisition Corp. II	Shell Companies	136.94M
ATEN	A10 Networks, Inc.	Software - Infrastructure	1.06B
ATER	Aterian, Inc.	Furnishings, Fixtures & Appliances	25.31M
ATEX	Anterix Inc.	Telecom Services	744.81M
ATGE	Adtalem Global Education Inc.	Education & Training Services	3.00B
ATGL	Alpha Technology Group Limited	Software - Infrastructure	53.27M
ATHA	Athira Pharma, Inc.	Biotechnology	126.10M
ATHE	Alterity Therapeutics Limited	Biotechnology	13.60M
ATHM	Autohome Inc.	Internet Content & Information	2.98B
ATI	ATI Inc.	Metal Fabrication	8.24B
ATIF	ATIF Holdings Limited	Capital Markets	10.13M
ATIP	ATI Physical Therapy, Inc.	Medical Care Facilities	27.87M
ATKR	Atkore Inc.	Electrical Equipment & Parts	4.92B
ATLC	Atlanticus Holdings Corporation	Credit Services	522.16M
ATLO	Ames National Corporation	Banks - Regional	188.21M
ATLX	Atlas Lithium Corporation	Other Precious Metals & Mining	164.88M
ATMC	AlphaTime Acquisition Corp	Shell Companies	76.43M
ATMU	Atmus Filtration Technologies Inc.	Pollution & Treatment Controls	2.55B
ATMV	AlphaVest Acquisition Corp	Shell Companies	77.84M
ATNF	180 Life Sciences Corp.	Biotechnology	2.31M
ATNI	ATN International, Inc.	Telecom Services	426.43M
ATNM	Actinium Pharmaceuticals, Inc.	Biotechnology	209.23M
ATO	Atmos Energy Corporation	Utilities - Regulated Gas	19.33B
ATOM	Atomera Incorporated	Semiconductor Equipment & Materials	83.62M
ATOS	Atossa Therapeutics, Inc.	Biotechnology	167.89M
ATPC	Agape ATP Corporation	Packaged Foods	13.14M
ATR	AptarGroup, Inc.	Medical Instruments & Supplies	9.74B
ATRA	Atara Biotherapeutics, Inc.	Biotechnology	49.39M
ATRC	AtriCure, Inc.	Medical Instruments & Supplies	1.07B
ATRI	Atrion Corporation	Medical Instruments & Supplies	806.28M
ATRO	Astronics Corporation	Aerospace & Defense	774.19M
ATS	ATS Corporation	Specialty Industrial Machinery	2.95B
ATSG	Air Transport Services Group, Inc.	Airlines	1.06B
ATUS	Altice USA, Inc.	Telecom Services	913.02M
ATXG	Addentax Group Corp.	Integrated Freight & Logistics	4.20M
ATXI	Avenue Therapeutics, Inc.	Biotechnology	2.56M
ATXS	Astria Therapeutics, Inc.	Biotechnology	630.95M
ATYR	aTyr Pharma, Inc.	Biotechnology	140.81M
AU	AngloGold Ashanti Limited	Gold	11.40B
AUB	Atlantic Union Bankshares Corporation	Banks - Regional	3.74B
AUBN	Auburn National Bancorporation, Inc.	Banks - Regional	65.00M
AUDC	AudioCodes Ltd.	Communication Equipment	327.12M
AUGX	Augmedix, Inc.	Health Information Services	111.77M
AUID	authID Inc.	Software - Infrastructure	99.38M
AULT	Ault Alliance, Inc.	Aerospace & Defense	9.32M
AUMN	Golden Minerals Company	Other Precious Metals & Mining	5.78M
AUNA	Auna SA	Medical Care Facilities	270.00M
AUPH	Aurinia Pharmaceuticals Inc.	Biotechnology	817.35M
AUR	Aurora Innovation, Inc.	Information Technology Services	6.34B
AURA	Aura Biosciences, Inc.	Biotechnology	486.52M
AUST	Austin Gold Corp.	Gold	12.74M
AUTL	Autolus Therapeutics plc	Biotechnology	1.18B
AUUD	Auddia Inc.	Software - Application	3.38M
AVA	Avista Corporation	Utilities - Diversified	3.07B
AVAH	Aveanna Healthcare Holdings Inc.	Medical Care Facilities	811.84M
AVAL	Grupo Aval Acciones y Valores S.A.	Banks - Regional	2.47B
AVAV	AeroVironment, Inc.	Aerospace & Defense	4.85B
AVB	AvalonBay Communities, Inc.	REIT - Residential	29.18B
AVBP	ArriVent BioPharma, Inc.	Biotechnology	739.88M
AVD	American Vanguard Corporation	Agricultural Inputs	258.58M
AVDL	Avadel Pharmaceuticals plc	Drug Manufacturers - Specialty & Generic	1.58B
AVDX	AvidXchange Holdings, Inc.	Software - Infrastructure	2.61B
AVGO	Broadcom Inc.	Semiconductors	679.26B
AVGR	Avinger, Inc.	Medical Instruments & Supplies	2.53M
AVIR	Atea Pharmaceuticals, Inc.	Biotechnology	319.21M
AVNS	Avanos Medical, Inc.	Medical Devices	1.06B
AVNT	Avient Corporation	Specialty Chemicals	4.13B
AVNW	Aviat Networks, Inc.	Communication Equipment	375.59M
AVO	Mission Produce, Inc.	Food Distribution	792.06M
AVPT	AvePoint, Inc.	Software - Infrastructure	2.01B
AVT	Avnet, Inc.	Electronics & Computer Distribution	4.82B
AVTE	Aerovate Therapeutics, Inc.	Biotechnology	53.32M
AVTR	Avantor, Inc.	Specialty Chemicals	18.33B
AVTX	Avalo Therapeutics, Inc.	Biotechnology	11.28M
AVXL	Anavex Life Sciences Corp.	Biotechnology	534.93M
AVY	Avery Dennison Corporation	Packaging & Containers	17.28B
AWH	Aspira Women's Health Inc.	Diagnostics & Research	19.66M
AWI	Armstrong World Industries, Inc.	Building Products & Equipment	5.60B
AWK	American Water Works Company, Inc.	Utilities - Regulated Water	27.90B
AWR	American States Water Company	Utilities - Regulated Water	3.05B
AWRE	Aware, Inc.	Software - Application	42.17M
AWX	Avalon Holdings Corporation	Waste Management	8.31M
AX	Axos Financial, Inc.	Banks - Regional	4.42B
AXDX	Accelerate Diagnostics, Inc.	Medical Devices	28.45M
AXGN	AxoGen, Inc.	Medical Devices	386.79M
AXIL	AXIL Brands, Inc.	Consumer Electronics	39.98M
AXL	American Axle & Manufacturing Holdings, Inc.	Auto Parts	832.86M
AXNX	Axonics, Inc.	Medical Devices	3.50B
AXON	Axon Enterprise, Inc.	Aerospace & Defense	23.11B
AXP	American Express Company	Credit Services	178.92B
AXR	AMREP Corporation	Real Estate - Development	133.52M
AXS	AXIS Capital Holdings Limited	Insurance - Specialty	6.32B
AXSM	Axsome Therapeutics, Inc.	Biotechnology	4.00B
AXTA	Axalta Coating Systems Ltd.	Specialty Chemicals	7.75B
AXTI	AXT, Inc.	Semiconductor Equipment & Materials	156.28M
AY	Atlantica Sustainable Infrastructure plc	Utilities - Renewable	2.56B
AYI	Acuity Brands, Inc.	Electrical Equipment & Parts	7.68B
AYRO	Ayro, Inc.	Auto Manufacturers	3.94M
AYTU	Aytu BioPharma, Inc.	Drug Manufacturers - Specialty & Generic	16.05M
AZ	A2Z Smart Technologies Corp.	Aerospace & Defense	28.02M
AZEK	The AZEK Company Inc.	Building Products & Equipment	6.57B
AZN	AstraZeneca PLC	Drug Manufacturers - General	241.32B
AZO	AutoZone, Inc.	Specialty Retail	52.35B
AZPN	Aspen Technology, Inc.	Software - Application	12.04B
AZTA	Azenta, Inc.	Medical Instruments & Supplies	3.33B
AZTR	Azitra, Inc.	Biotechnology	739.41K
AZUL	Azul S.A.	Airlines	473.53M
AZZ	AZZ Inc.	Specialty Business Services	2.40B
B	Barnes Group Inc.	Specialty Industrial Machinery	2.02B
BA	The Boeing Company	Aerospace & Defense	115.33B
BABA	Alibaba Group Holding Limited	Internet Retail	167.16B
BAC	Bank of America Corporation	Banks - Diversified	322.90B
BACA	Berenson Acquisition Corp. I	Shell Companies	84.04M
BACK	IMAC Holdings, Inc.	Medical Care Facilities	1.95M
BAER	Bridger Aerospace Group Holdings, Inc.	Security & Protection Services	174.89M
BAFN	BayFirst Financial Corp.	Banks - Regional	53.75M
BAH	Booz Allen Hamilton Holding Corporation	Consulting Services	18.12B
BAK	Braskem S.A.	Chemicals	2.53B
BALL	Ball Corporation	Packaging & Containers	19.55B
BALY	Bally's Corporation	Resorts & Casinos	695.94M
BAM	Brookfield Asset Management Inc.	Asset Management	18.13B
BANC	Banc of California, Inc.	Banks - Regional	2.33B
BAND	Bandwidth Inc.	Software - Infrastructure	615.51M
BANF	BancFirst Corporation	Banks - Regional	3.58B
BANL	CBL International Limited	Oil & Gas Midstream	20.42M
BANR	Banner Corporation	Banks - Regional	2.06B
BANX	ArrowMark Financial Corp.	Asset Management	135.94M
BAOS	Baosheng Media Group Holdings Limited	Advertising Agencies	3.76M
BAP	Credicorp Ltd.	Banks - Regional	13.68B
BARK	BARK, Inc.	Specialty Retail	263.92M
BASE	Couchbase, Inc.	Software - Infrastructure	978.02M
BATL	Battalion Oil Corporation	Oil & Gas Exploration & Production	58.75M
BATRA	Atlanta Braves Holdings Inc	Entertainment	2.68B
BATRK	Atlanta Braves Holdings Inc	Entertainment	2.68B
BAX	Baxter International Inc.	Medical Instruments & Supplies	18.34B
BAYA	Bayview Acquisition Corp	Shell Companies	79.64M
BB	BlackBerry Limited	Software - Infrastructure	1.41B
BBAI	BigBear.ai Holdings, Inc.	Information Technology Services	341.50M
BBAR	BBVA Argentina	Banks - Regional	2.40B
BBCP	Concrete Pumping Holdings, Inc.	Engineering & Construction	368.01M
BBD	Banco Bradesco S.A.	Banks - Regional	22.47B
BBDC	Barings BDC, Inc.	Asset Management	1.07B
BBDO	Banco Bradesco S.A.	Banks - Regional	21.98B
BBGI	Beasley Broadcast Group, Inc.	Broadcasting	19.23M
BBIO	BridgeBio Pharma, Inc.	Biotechnology	4.90B
BBLG	Bone Biologics Corporation	Medical Devices	1.96M
BBSI	Barrett Business Services, Inc.	Staffing & Employment Services	944.87M
BBU	Brookfield Business Partners L.P.	Conglomerates	1.49B
BBUC	Brookfield Business Corporation	Asset Management	1.62B
BBVA	Banco Bilbao Vizcaya Argentaria, S.A.	Banks - Diversified	63.15B
BBW	Build-A-Bear Workshop, Inc.	Specialty Retail	371.50M
BBWI	Bath & Body Works, Inc.	Specialty Retail	8.09B
BBY	Best Buy Co., Inc.	Specialty Retail	18.31B
BC	Brunswick Corporation	Recreational Vehicles	5.59B
BCAB	BioAtla, Inc.	Biotechnology	78.43M
BCAL	Southern California Bancorp	Banks - Regional	285.89M
BCAN	Femto Technologies Inc.	Software - Application	6.41M
BCBP	BCB Bancorp, Inc.	Banks - Regional	214.17M
BCC	Boise Cascade Company	Building Materials	5.56B
BCDA	BioCardia, Inc.	Biotechnology	5.52M
BCE	BCE Inc.	Telecom Services	30.66B
BCG	Binah Capital Group, Inc.	Asset Management	77.86M
BCH	Banco de Chile	Banks - Regional	11.86B
BCLI	Brainstorm Cell Therapeutics Inc.	Biotechnology	26.71M
BCML	BayCom Corp	Banks - Regional	270.41M
BCO	The Brink's Company	Security & Protection Services	4.96B
BCOV	Brightcove Inc.	Software - Application	107.89M
BCOW	1895 Bancorp of Wisconsin, Inc.	Banks - Regional	51.38M
BCPC	Balchem Corporation	Specialty Chemicals	5.77B
BCRX	BioCryst Pharmaceuticals, Inc.	Biotechnology	1.52B
BCS	Barclays PLC	Banks - Diversified	44.15B
BCSA	Blockchain Coinvestors Acquisition Corp. I	Shell Companies	144.23M
BCSF	Bain Capital Specialty Finance, Inc.	Asset Management	1.09B
BCTX	BriaCell Therapeutics Corp.	Biotechnology	13.34M
BCYC	Bicycle Therapeutics plc	Biotechnology	1.02B
BDC	Belden Inc.	Communication Equipment	3.65B
BDL	Flanigan's Enterprises, Inc.	Restaurants	49.29M
BDN	Brandywine Realty Trust	REIT - Office	863.06M
BDRX	Biodexa Pharmaceuticals Plc	Biotechnology	163.19K
BDSX	Biodesix, Inc.	Diagnostics & Research	196.69M
BDTX	Black Diamond Therapeutics, Inc.	Biotechnology	331.33M
BDX	Becton, Dickinson and Company	Medical Instruments & Supplies	69.30B
BE	Bloom Energy Corporation	Electrical Equipment & Parts	3.01B
BEAM	Beam Therapeutics Inc.	Biotechnology	2.64B
BEAT	HeartBeam, Inc.	Health Information Services	63.69M
BECN	Beacon Roofing Supply, Inc.	Industrial Distribution	6.41B
BEDU	Bright Scholar Education Holdings Limited	Education & Training Services	53.21M
BEEM	Beam Global	Solar	87.56M
BEEP	Mobile Infrastructure Corporation	Infrastructure Operations	91.46M
BEKE	KE Holdings Inc.	Real Estate Services	15.81B
BELFA	Bel Fuse Inc.	Electronic Components	954.02M
BELFB	Bel Fuse Inc.	Electronic Components	937.09M
BEN	Franklin Resources, Inc.	Asset Management	12.02B
BENF	Beneficient	Asset Management	13.88M
BEP	Brookfield Renewable Partners L.P.	Utilities - Renewable	15.63B
BEPC	Brookfield Renewable Corporation	Utilities - Renewable	4.98B
BERY	Berry Global Group, Inc.	Packaging & Containers	7.44B
BEST	BEST Inc.	Trucking	51.98M
BETR	Better Home & Finance Holding Company	Mortgage Finance	401.27M
BF.A	Brown-Forman Corporation	Beverages - Wineries & Distilleries	21.12B
BF.B	Brown-Forman Corporation	Beverages - Wineries & Distilleries	20.97B
BFAC	Battery Future Acquisition Corp.	Shell Companies	136.50M
BFAM	Bright Horizons Family Solutions Inc.	Personal Services	6.99B
BFC	Bank First Corporation	Banks - Regional	943.92M
BFH	Bread Financial Holdings, Inc.	Credit Services	2.69B
BFI	BurgerFi International, Inc.	Restaurants	15.44M
BFIN	BankFinancial Corporation	Banks - Regional	147.04M
BFLY	Butterfly Network, Inc.	Medical Devices	229.67M
BFRG	Bullfrog AI Holdings, Inc.	Health Information Services	23.46M
BFRI	Biofrontera Inc.	Drug Manufacturers - Specialty & Generic	6.01M
BFS	Saul Centers, Inc.	REIT - Retail	948.96M
BFST	Business First Bancshares, Inc.	Banks - Regional	646.86M
BG	Bunge Limited	Farm Products	16.07B
BGC	BGC Group, Inc	Capital Markets	4.45B
BGFV	Big 5 Sporting Goods Corporation	Specialty Retail	62.56M
BGI	Birks Group Inc.	Luxury Goods	48.49M
BGLC	BioNexus Gene Lab Corp.	Specialty Chemicals	8.57M
BGNE	BeiGene, Ltd.	Biotechnology	17.37B
BGS	B&G Foods, Inc.	Packaged Foods	679.49M
BGSF	BGSF, Inc.	Staffing & Employment Services	90.61M
BGXX	Bright Green Corporation	Drug Manufacturers - Specialty & Generic	44.54M
BH	Biglari Holdings Inc.	Restaurants	610.65M
BH.A	Biglari Holdings Inc.	Restaurants	614.94M
BHAC	Focus Impact BH3 Acquisition Co.	Shell Companies	91.91M
BHAT	Blue Hat Interactive Entertainment Technology	Electronic Gaming & Multimedia	56.10M
BHB	Bar Harbor Bankshares	Banks - Regional	486.07M
BHC	Bausch Health Companies Inc.	Drug Manufacturers - Specialty & Generic	2.18B
BHE	Benchmark Electronics, Inc.	Electronic Components	1.47B
BHF	Brighthouse Financial, Inc.	Insurance - Life	3.15B
BHIL	Benson Hill, Inc.	Agricultural Inputs	39.80M
BHLB	Berkshire Hills Bancorp, Inc.	Banks - Regional	1.20B
BHM	Bluerock Homes Trust, Inc.	REIT - Residential	73.82M
BHP	BHP Group Limited	Other Industrial Metals & Mining	136.65B
BHR	Braemar Hotels & Resorts Inc.	REIT - Hotel & Motel	248.29M
BHRB	Burke & Herbert Bank & Trust Company	Banks - Regional	1.01B
BHVN	Biohaven Pharmaceutical Holding Company Ltd.	Biotechnology	3.43B
BIAF	bioAffinity Technologies, Inc.	Diagnostics & Research	29.49M
BIDU	Baidu, Inc.	Internet Content & Information	31.62B
BIG	Big Lots, Inc.	Discount Stores	30.72M
BIGC	BigCommerce Holdings, Inc.	Software - Application	623.61M
BIIB	Biogen Inc.	Drug Manufacturers - General	31.05B
BILI	Bilibili Inc.	Electronic Gaming & Multimedia	6.08B
BILL	BILL Holdings Inc	Software - Application	5.56B
BIMI	BIMI International Medical Inc.	Pharmaceutical Retailers	4.48M
BIO	Bio-Rad Laboratories, Inc.	Medical Devices	9.53B
BIO.B	Bio-Rad Laboratories, Inc.	Medical Devices	8.34B
BIOR	Biora Therapeutics, Inc.	Biotechnology	24.50M
BIOX	Bioceres Crop Solutions Corp.	Agricultural Inputs	679.80M
BIP	Brookfield Infrastructure Partners L.P.	Utilities - Diversified	14.29B
BIPC	Brookfield Infrastructure Corporation	Utilities - Regulated Gas	5.09B
BIRD	Allbirds, Inc.	Apparel Retail	97.76M
BIRK	Birkenstock Holding plc	Footwear & Accessories	10.98B
BITF	Bitfarms Ltd.	Capital Markets	1.01B
BIVI	BioVie Inc.	Biotechnology	24.22M
BJ	BJ's Wholesale Club Holdings, Inc.	Discount Stores	11.76B
BJDX	Bluejay Diagnostics, Inc.	Medical Devices	291.00K
BJRI	BJ's Restaurants, Inc.	Restaurants	735.16M
BK	The Bank of New York Mellon Corporation	Asset Management	48.87B
BKD	Brookdale Senior Living Inc.	Medical Care Facilities	1.52B
BKE	The Buckle, Inc.	Apparel Retail	2.14B
BKH	Black Hills Corporation	Utilities - Regulated Gas	4.03B
BKHA	Black Hawk Acquisition Corporation	Shell Companies	90.63M
BKKT	Bakkt Holdings, Inc.	Software - Infrastructure	105.07M
BKNG	Booking Holdings Inc.	Travel Services	125.87B
BKR	Baker Hughes Company	Oil & Gas Equipment & Services	38.41B
BKSY	BlackSky Technology Inc.	Scientific & Technical Instruments	162.79M
BKTI	BK Technologies Corporation	Communication Equipment	44.74M
BKU	BankUnited, Inc.	Banks - Regional	2.88B
BKYI	BIO-key International, Inc.	Security & Protection Services	2.63M
BL	BlackLine, Inc.	Software - Application	2.94B
BLAC	Bellevue Life Sciences Acquisition Corp.	Shell Companies	60.90M
BLBD	Blue Bird Corporation	Auto Manufacturers	1.65B
BLBX	Blackboxstocks Inc.	Software - Application	8.71M
BLCO	Bausch + Lomb Corporation	Medical Instruments & Supplies	5.92B
BLD	TopBuild Corp.	Engineering & Construction	15.01B
BLDE	Blade Air Mobility, Inc.	Airports & Air Services	262.20M
BLDP	Ballard Power Systems Inc.	Specialty Industrial Machinery	657.15M
BLDR	Builders FirstSource, Inc.	Building Products & Equipment	20.25B
BLEU	bleuacacia ltd	Shell Companies	83.49M
BLFS	BioLife Solutions, Inc.	Medical Instruments & Supplies	1.10B
BLFY	Blue Foundry Bancorp	Banks - Regional	269.57M
BLIN	Bridgeline Digital, Inc.	Software - Infrastructure	9.83M
BLK	BlackRock, Inc.	Asset Management	128.84B
BLKB	Blackbaud, Inc.	Software - Application	4.15B
BLMN	Bloomin' Brands, Inc.	Restaurants	1.80B
BLMZ	BloomZ Inc.	Electronic Gaming & Multimedia	21.45M
BLND	Blend Labs, Inc.	Software - Application	655.81M
BLNK	Blink Charging Co.	Engineering & Construction	322.89M
BLRX	BioLineRx Ltd.	Biotechnology	61.19M
BLTE	Belite Bio, Inc	Biotechnology	1.44B
BLUE	bluebird bio, Inc.	Biotechnology	216.83M
BLX	Banco Latinoamericano de Comercio Exterior, S. A.	Banks - Regional	1.12B
BLZE	Backblaze, Inc.	Software - Infrastructure	258.96M
BMA	Banco Macro S.A.	Banks - Regional	4.35B
BMBL	Bumble Inc.	Software - Application	1.16B
BMEA	Biomea Fusion, Inc.	Biotechnology	194.10M
BMI	Badger Meter, Inc.	Scientific & Technical Instruments	5.93B
BMO	Bank of Montreal	Banks - Diversified	60.18B
BMR	Beamr Imaging Ltd.	Software - Application	68.26M
BMRA	Biomerica, Inc.	Medical Devices	5.72M
BMRC	Bank of Marin Bancorp	Banks - Regional	332.88M
BMRN	BioMarin Pharmaceutical Inc.	Biotechnology	15.93B
BMTX	BM Technologies, Inc.	Software - Application	33.17M
BMY	Bristol-Myers Squibb Company	Drug Manufacturers - General	99.53B
BN	Brookfield Corporation	Asset Management	78.65B
BNAI	Brand Engagement Network, Inc.	Software - Infrastructure	88.49M
BNED	Barnes & Noble Education, Inc.	Specialty Retail	261.56M
BNGO	Bionano Genomics, Inc.	Medical Instruments & Supplies	49.90M
BNIX	Bannix Acquisition Corp.	Shell Companies	44.90M
BNL	Broadstone Net Lease, Inc.	REIT - Diversified	3.37B
BNOX	Bionomics Limited	Biotechnology	7.75M
BNR	Burning Rock Biotech Limited	Diagnostics & Research	74.96M
BNRE	Brookfield Reinsurance Ltd.	Insurance - Reinsurance	5.70B
BNRE.A	Brookfield Reinsurance Ltd.	Insurance - Reinsurance	4.40B
BNRG	Brenmiller Energy Ltd	Utilities - Renewable	1.99M
BNS	The Bank of Nova Scotia	Banks - Diversified	57.52B
BNTC	Benitec Biopharma Inc.	Biotechnology	79.72M
BNTX	BioNTech SE	Biotechnology	20.54B
BNZI	Banzai International, Inc.	Software - Application	3.98M
BOC	Boston Omaha Corporation	Conglomerates	447.89M
BOCN	Blue Ocean Acquisition Corp.	Shell Companies	74.02M
BODI	The Beachbody Company, Inc.	Internet Content & Information	52.66M
BOF	BranchOut Food Inc.	Packaged Foods	4.87M
BOH	Bank of Hawaii Corporation	Banks - Regional	2.72B
BOKF	BOK Financial Corporation	Banks - Regional	6.74B
BOLD	Boundless Bio, Inc.	Biotechnology	83.45M
BOLT	Bolt Biotherapeutics, Inc.	Biotechnology	28.29M
BON	Bon Natural Life Limited	Packaged Foods	2.94M
BOOM	DMC Global Inc.	Oil & Gas Equipment & Services	277.75M
BOOT	Boot Barn Holdings, Inc.	Apparel Retail	3.98B
BORR	Borr Drilling Limited	Oil & Gas Drilling	1.65B
BOSC	B.O.S. Better Online Solutions Ltd.	Communication Equipment	17.30M
BOTJ	Bank of the James Financial Group, Inc.	Banks - Regional	61.34M
BOW	Bowhead Specialty Holdings Inc.	Insurance - Property & Casualty	864.85M
BOWL	Bowlero Corp.	Leisure	1.86B
BOWN	Bowen Acquisition Corp	Shell Companies	97.16M
BOX	Box, Inc.	Software - Infrastructure	4.08B
BOXL	Boxlight Corporation	Communication Equipment	6.12M
BP	BP p.l.c.	Oil & Gas Integrated	95.67B
BPMC	Blueprint Medicines Corporation	Biotechnology	6.72B
BPOP	Popular, Inc.	Banks - Regional	7.48B
BPRN	Princeton Bancorp Inc	Banks - Regional	239.54M
BPT	BP Prudhoe Bay Royalty Trust	Oil & Gas Midstream	34.67M
BPTH	Bio-Path Holdings, Inc.	Biotechnology	3.37M
BQ	Boqii Holding Limited	Specialty Retail	2.10M
BR	Broadridge Financial Solutions, Inc.	Information Technology Services	25.36B
BRAC	Broad Capital Acquisition Corp.	Shell Companies	34.25M
BRAG	Bragg Gaming Group Inc.	Gambling	134.43M
BRBR	BellRing Brands, Inc.	Packaged Foods	6.66B
BRBS	Blue Ridge Bankshares, Inc.	Banks - Regional	204.34M
BRC	Brady Corporation	Security & Protection Services	3.39B
BRCC	BRC Inc.	Packaged Foods	1.21B
BRDG	Bridge Investment Group Holdings Inc.	Asset Management	2.08B
BREA	Brera Holdings PLC	Entertainment	7.14M
BRFH	Barfresh Food Group, Inc.	Beverages - Non-Alcoholic	54.91M
BRFS	BRF S.A.	Packaged Foods	6.35B
BRID	Bridgford Foods Corporation	Packaged Foods	84.87M
BRK.A	Berkshire Hathaway Inc.	Insurance - Diversified	950.24B
BRK.B	Berkshire Hathaway Inc.	Insurance - Diversified	950.64B
BRKH	Burtech Acquisition Corp.	Shell Companies	169.75M
BRKL	Brookline Bancorp, Inc.	Banks - Regional	947.17M
BRKR	Bruker Corporation	Medical Devices	10.17B
BRLS	Borealis Foods Inc.	Packaged Foods	186.00M
BRLT	Brilliant Earth Group, Inc.	Luxury Goods	252.48M
BRN	Barnwell Industries, Inc.	Oil & Gas Exploration & Production	23.37M
BRNS	Barinthus Biotherapeutics plc	Biotechnology	58.82M
BRO	Brown & Brown, Inc.	Insurance Brokers	28.34B
BROG	Brooge Energy Limited	Oil & Gas Midstream	82.75M
BROS	Dutch Bros Inc.	Restaurants	5.87B
BRSP	BrightSpire Capital, Inc.	REIT - Mortgage	819.75M
BRT	BRT Apartments Corp.	REIT - Residential	346.53M
BRTX	BioRestorative Therapies, Inc.	Biotechnology	10.83M
BRX	Brixmor Property Group Inc.	REIT - Retail	7.80B
BRY	Berry Corporation	Oil & Gas Exploration & Production	514.34M
BRZE	Braze, Inc.	Software - Application	4.32B
BSAC	Banco Santander-Chile	Banks - Regional	9.28B
BSBK	Bogota Financial Corp.	Banks - Regional	96.43M
BSBR	Banco Santander (Brasil) S.A.	Banks - Regional	37.95B
BSET	Bassett Furniture Industries, Incorporated	Furnishings, Fixtures & Appliances	117.55M
BSFC	Blue Star Foods Corp.	Packaged Foods	4.57M
BSIG	BrightSphere Investment Group Inc.	Asset Management	986.20M
BSM	Black Stone Minerals, L.P.	Oil & Gas Exploration & Production	3.17B
BSRR	Sierra Bancorp	Banks - Regional	424.52M
BSVN	Bank7 Corp.	Banks - Regional	375.00M
BSX	Boston Scientific Corporation	Medical Devices	108.64B
BSY	Bentley Systems, Incorporated	Software - Application	14.41B
BTAI	BioXcel Therapeutics, Inc.	Biotechnology	42.03M
BTBD	BT Brands, Inc.	Restaurants	8.62M
BTBT	Bit Digital, Inc.	Capital Markets	426.54M
BTCM	BIT Mining Limited	Information Technology Services	31.34M
BTCS	BTCS Inc.	Capital Markets	24.17M
BTCT	BTC Digital Ltd.	Computer Hardware	4.88M
BTCY	Biotricity, Inc.	Medical Devices	14.76M
BTDR	Bitdeer Technologies Group	Software - Application	1.29B
BTE	Baytex Energy Corp.	Oil & Gas Exploration & Production	2.86B
BTG	B2Gold Corp.	Gold	3.83B
BTI	British American Tobacco p.l.c.	Tobacco	78.62B
BTM	Bitcoin Depot Inc.	Capital Markets	99.81M
BTMD	biote Corp.	Medical Care Facilities	485.13M
BTOC	Armlogi Holding Corp.	Integrated Freight & Logistics	200.51M
BTOG	Bit Origin Limited	Capital Markets	9.63M
BTSG	BrightSpring Health Services, Inc.	Health Information Services	2.14B
BTTR	Better Choice Company Inc.	Packaged Foods	2.57M
BTU	Peabody Energy Corporation	Thermal Coal	2.74B
BUD	Anheuser-Busch InBev SA/NV	Beverages - Brewers	123.36B
BUJA	Bukit Jalil Global Acquisition 1 Ltd	Shell Companies	83.28M
BUR	Burford Capital Limited	Asset Management	3.01B
BURL	Burlington Stores, Inc.	Apparel Retail	16.25B
BUSE	First Busey Corporation	Banks - Regional	1.57B
BV	BrightView Holdings, Inc.	Specialty Business Services	1.32B
BVN	Compania de Minas Buenaventura S.A.	Other Precious Metals & Mining	3.93B
BVS	Bioventus Inc.	Medical Devices	461.47M
BW	Babcock & Wilcox Enterprises, Inc.	Specialty Industrial Machinery	136.97M
BWA	BorgWarner Inc.	Auto Parts	7.35B
BWAY	BrainsWay Ltd.	Medical Devices	124.67M
BWB	Bridgewater Bancshares, Inc.	Banks - Regional	381.87M
BWEN	Broadwind, Inc.	Specialty Industrial Machinery	67.37M
BWFG	Bankwell Financial Group, Inc.	Banks - Regional	213.18M
BWIN	The Baldwin Insurance Group, Inc.	Insurance Brokers	2.91B
BWLP	BW LPG Limited	Marine Shipping	2.14B
BWMN	Bowman Consulting Group Ltd.	Engineering & Construction	601.01M
BWMX	Betterware de México, S.A.P.I. de C.V.	Specialty Retail	537.17M
BWXT	BWX Technologies, Inc.	Aerospace & Defense	9.00B
BX	Blackstone Inc.	Asset Management	171.15B
BXC	BlueLinx Holdings Inc.	Industrial Distribution	1.07B
BXMT	Blackstone Mortgage Trust, Inc.	REIT - Mortgage	3.11B
BXP	BXP Inc.	REIT - Office	11.27B
BY	Byline Bancorp, Inc.	Banks - Regional	1.24B
BYD	Boyd Gaming Corporation	Resorts & Casinos	5.79B
BYFC	Broadway Financial Corporation	Banks - Regional	48.76M
BYND	Beyond Meat, Inc.	Packaged Foods	388.66M
BYNO	byNordic Acquisition Corporation	Shell Companies	116.43M
BYON	Beyond, Inc.	Internet Retail	591.09M
BYRN	Byrna Technologies Inc.	Aerospace & Defense	208.98M
BYSI	BeyondSpring Inc.	Biotechnology	77.78M
BYU	BAIYU Holdings, Inc.	Shell Companies	24.32M
BZ	Kanzhun Limited	Internet Content & Information	6.05B
BZFD	BuzzFeed, Inc.	Internet Content & Information	97.97M
BZH	Beazer Homes USA, Inc.	Residential Construction	1.07B
BZUN	Baozun Inc.	Internet Retail	105.48M
C	Citigroup Inc.	Banks - Diversified	125.43B
CAAP	Corporación América Airports S.A.	Airports & Air Services	2.56B
CAAS	China Automotive Systems, Inc.	Auto Parts	120.44M
CABA	Cabaletta Bio, Inc.	Biotechnology	336.00M
CABO	Cable One, Inc.	Telecom Services	2.27B
CAC	Camden National Corporation	Banks - Regional	615.38M
CACC	Credit Acceptance Corporation	Credit Services	7.05B
CACI	CACI International Inc	Information Technology Services	10.15B
CACO	Caravelle International Group	Marine Shipping	25.33M
CADE	Cadence Bank	Banks - Regional	6.08B
CADL	Candel Therapeutics, Inc.	Biotechnology	177.05M
CAE	CAE Inc.	Aerospace & Defense	5.69B
CAG	Conagra Brands, Inc.	Packaged Foods	14.58B
CAH	Cardinal Health, Inc.	Medical Distribution	24.31B
CAKE	The Cheesecake Factory Incorporated	Restaurants	1.98B
CAL	Caleres, Inc.	Apparel Retail	1.33B
CALB	California BanCorp	Banks - Regional	207.11M
CALC	CalciMedica, Inc.	Biotechnology	54.29M
CALM	Cal-Maine Foods, Inc.	Farm Products	3.53B
CALT	Calliditas Therapeutics AB (publ)	Biotechnology	1.02B
CALX	Calix, Inc.	Software - Infrastructure	2.65B
CAMT	Camtek Ltd.	Semiconductor Equipment & Materials	4.39B
CAN	Canaan Inc.	Computer Hardware	281.18M
CANF	Can-Fite BioPharma Ltd.	Biotechnology	21.10M
CANG	Cango Inc.	Auto & Truck Dealerships	200.82M
CAPL	CrossAmerica Partners LP	Oil & Gas Refining & Marketing	761.30M
CAPR	Capricor Therapeutics, Inc.	Biotechnology	131.12M
CAPT	Captivision Inc.	Building Materials	60.82M
CAR	Avis Budget Group, Inc.	Rental & Leasing Services	3.50B
CARA	Cara Therapeutics, Inc.	Biotechnology	19.14M
CARE	Carter Bankshares, Inc.	Banks - Regional	374.00M
CARG	CarGurus, Inc.	Auto & Truck Dealerships	2.59B
CARM	Carisma Therapeutics, Inc.	Biotechnology	45.29M
CARR	Carrier Global Corporation	Building Products & Equipment	60.85B
CARS	Cars.com Inc.	Auto & Truck Dealerships	1.33B
CART	Maplebear Inc.	Internet Retail	9.04B
CARV	Carver Bancorp, Inc.	Banks - Regional	9.83M
CASH	Pathward Financial, Inc.	Banks - Regional	1.72B
CASI	CASI Pharmaceuticals, Inc.	Biotechnology	92.07M
CASS	Cass Information Systems, Inc.	Specialty Business Services	570.44M
CASY	Casey's General Stores, Inc.	Specialty Retail	14.62B
CAT	Caterpillar Inc.	Farm & Heavy Construction Machinery	167.26B
CATO	The Cato Corporation	Apparel Retail	96.40M
CATX	Perspective Therapeutics, Inc.	Medical Devices	842.88M
CATY	Cathay General Bancorp	Banks - Regional	3.23B
CAUD	Collective Audience, Inc.	Software - Application	7.30M
CAVA	CAVA Group, Inc.	Restaurants	9.27B
CB	Chubb Limited	Insurance - Property & Casualty	112.42B
CBAN	Colony Bankcorp, Inc.	Banks - Regional	276.02M
CBAT	CBAK Energy Technology, Inc.	Electrical Equipment & Parts	116.93M
CBFV	CB Financial Services, Inc.	Banks - Regional	125.99M
CBL	CBL & Associates Properties, Inc.	REIT - Retail	830.28M
CBNK	Capital Bancorp, Inc.	Banks - Regional	346.82M
CBOE	Cboe Global Markets, Inc.	Financial Data & Stock Exchanges	19.61B
CBRE	CBRE Group, Inc.	Real Estate Services	34.00B
CBRG	Chain Bridge I	Shell Companies	75.59M
CBRL	Cracker Barrel Old Country Store, Inc.	Restaurants	1.02B
CBSH	Commerce Bancshares, Inc.	Banks - Regional	8.41B
CBT	Cabot Corporation	Specialty Chemicals	5.48B
CBU	Community Bank System, Inc.	Banks - Regional	3.25B
CBUS	Cibus, Inc.	Biotechnology	252.19M
CBZ	CBIZ, Inc.	Specialty Business Services	4.30B
CC	The Chemours Company	Specialty Chemicals	3.52B
CCAP	Crescent Capital BDC, Inc.	Asset Management	700.46M
CCB	Coastal Financial Corporation	Banks - Regional	711.90M
CCBG	Capital City Bank Group, Inc.	Banks - Regional	600.58M
CCCC	C4 Therapeutics, Inc.	Biotechnology	429.69M
CCCS	CCC Intelligent Solutions Holdings Inc.	Software - Infrastructure	6.84B
CCEL	Cryo-Cell International, Inc.	Medical Care Facilities	59.01M
CCEP	Coca-Cola Europacific Partners PLC	Beverages - Non-Alcoholic	33.68B
CCG	Cheche Group Inc.	Internet Content & Information	64.60M
CCI	Crown Castle Inc.	REIT - Specialty	47.30B
CCIX	Churchill Capital Corp IX	Shell Companies	367.36M
CCJ	Cameco Corporation	Uranium	19.22B
CCK	Crown Holdings, Inc.	Packaging & Containers	10.51B
CCL	Carnival Corporation & plc	Travel Services	21.58B
CCLD	CareCloud, Inc.	Health Information Services	35.52M
CCM	Concord Medical Services Holdings Limited	Medical Care Facilities	26.36M
CCNE	CNB Financial Corporation	Banks - Regional	541.05M
CCO	Clear Channel Outdoor Holdings, Inc.	Advertising Agencies	803.92M
CCOI	Cogent Communications Holdings, Inc.	Telecom Services	3.33B
CCRD	CoreCard Corporation	Software - Application	98.91M
CCRN	Cross Country Healthcare, Inc.	Medical Care Facilities	607.16M
CCS	Century Communities, Inc.	Residential Construction	3.25B
CCSI	Consensus Cloud Solutions, Inc.	Software - Infrastructure	417.85M
CCTG	CCSC Technology International Holdings Limited	Electrical Equipment & Parts	15.98M
CCTS	Cactus Acquisition Corp. 1 Limited	Shell Companies	57.96M
CCU	Compania Cervecerias Unidas S.A.	Beverages - Brewers	2.03B
CDAQ	Compass Digital Acquisition Corp.	Shell Companies	113.14M
CDE	Coeur Mining, Inc.	Gold	2.51B
CDIO	Cardio Diagnostics Holdings, Inc.	Biotechnology	9.89M
CDLR	Cadeler A/S	Engineering & Construction	2.25B
CDLX	Cardlytics, Inc.	Advertising Agencies	401.97M
CDMO	Avid Bioservices, Inc.	Biotechnology	652.34M
CDNA	CareDx, Inc	Diagnostics & Research	966.68M
CDNS	Cadence Design Systems, Inc.	Software - Application	69.38B
CDP	COPT Defense Properties	REIT - Office	3.23B
CDRE	Cadre Holdings, Inc.	Aerospace & Defense	1.48B
CDRO	Codere Online Luxembourg, S.A.	Gambling	356.27M
CDT	Conduit Pharmaceuticals Inc.	Biotechnology	16.80M
CDTG	CDT Environmental Technology Investment Holdings Limited ordinary shares	Waste Management	32.04M
CDTX	Cidara Therapeutics, Inc.	Biotechnology	91.50M
CDW	CDW Corporation	Information Technology Services	31.06B
CDXC	ChromaDex Corporation	Packaged Foods	217.99M
CDXS	Codexis, Inc.	Biotechnology	254.01M
CDZI	Cadiz Inc.	Utilities - Regulated Water	232.50M
CE	Celanese Corporation	Chemicals	15.11B
CEAD	CEA Industries Inc.	Farm & Heavy Construction Machinery	4.82M
CECO	CECO Environmental Corp.	Pollution & Treatment Controls	974.70M
CEG	Constellation Energy Corporation	Utilities - Renewable	52.85B
CEI	Camber Energy, Inc.	Specialty Industrial Machinery	21.45M
AUTL	Autolus Therapeutics plc	Biotechnology	1.18B
AUUD	Auddia Inc.	Software - Application	3.38M
AVA	Avista Corporation	Utilities - Diversified	3.07B
AVAH	Aveanna Healthcare Holdings Inc.	Medical Care Facilities	811.84M
AVAL	Grupo Aval Acciones y Valores S.A.	Banks - Regional	2.47B
AVAV	AeroVironment, Inc.	Aerospace & Defense	4.85B
AVB	AvalonBay Communities, Inc.	REIT - Residential	29.18B
AVBP	ArriVent BioPharma, Inc.	Biotechnology	739.88M
AVD	American Vanguard Corporation	Agricultural Inputs	258.58M
AVDL	Avadel Pharmaceuticals plc	Drug Manufacturers - Specialty & Generic	1.58B
AVDX	AvidXchange Holdings, Inc.	Software - Infrastructure	2.61B
AVGO	Broadcom Inc.	Semiconductors	679.26B
AVGR	Avinger, Inc.	Medical Instruments & Supplies	2.53M
AVIR	Atea Pharmaceuticals, Inc.	Biotechnology	319.21M
AVNS	Avanos Medical, Inc.	Medical Devices	1.06B
AVNT	Avient Corporation	Specialty Chemicals	4.13B
AVNW	Aviat Networks, Inc.	Communication Equipment	375.59M
AVO	Mission Produce, Inc.	Food Distribution	792.06M
AVPT	AvePoint, Inc.	Software - Infrastructure	2.01B
AVT	Avnet, Inc.	Electronics & Computer Distribution	4.82B
AVTE	Aerovate Therapeutics, Inc.	Biotechnology	53.32M
AVTR	Avantor, Inc.	Specialty Chemicals	18.33B
AVTX	Avalo Therapeutics, Inc.	Biotechnology	11.28M
AVXL	Anavex Life Sciences Corp.	Biotechnology	534.93M
AVY	Avery Dennison Corporation	Packaging & Containers	17.28B
AWH	Aspira Women's Health Inc.	Diagnostics & Research	19.66M
AWI	Armstrong World Industries, Inc.	Building Products & Equipment	5.60B
AWK	American Water Works Company, Inc.	Utilities - Regulated Water	27.90B
AWR	American States Water Company	Utilities - Regulated Water	3.05B
AWRE	Aware, Inc.	Software - Application	42.17M
AWX	Avalon Holdings Corporation	Waste Management	8.31M
AX	Axos Financial, Inc.	Banks - Regional	4.42B
AXDX	Accelerate Diagnostics, Inc.	Medical Devices	28.45M
AXGN	AxoGen, Inc.	Medical Devices	386.79M
AXIL	AXIL Brands, Inc.	Consumer Electronics	39.98M
AXL	American Axle & Manufacturing Holdings, Inc.	Auto Parts	832.86M
AXNX	Axonics, Inc.	Medical Devices	3.50B
AXON	Axon Enterprise, Inc.	Aerospace & Defense	23.11B
AXP	American Express Company	Credit Services	178.92B
AXR	AMREP Corporation	Real Estate - Development	133.52M
AXS	AXIS Capital Holdings Limited	Insurance - Specialty	6.32B
AXSM	Axsome Therapeutics, Inc.	Biotechnology	4.00B
AXTA	Axalta Coating Systems Ltd.	Specialty Chemicals	7.75B
AXTI	AXT, Inc.	Semiconductor Equipment & Materials	156.28M
AY	Atlantica Sustainable Infrastructure plc	Utilities - Renewable	2.56B
AYI	Acuity Brands, Inc.	Electrical Equipment & Parts	7.68B
AYRO	Ayro, Inc.	Auto Manufacturers	3.94M
AYTU	Aytu BioPharma, Inc.	Drug Manufacturers - Specialty & Generic	16.05M
AZ	A2Z Smart Technologies Corp.	Aerospace & Defense	28.02M
AZEK	The AZEK Company Inc.	Building Products & Equipment	6.57B
AZN	AstraZeneca PLC	Drug Manufacturers - General	241.32B
AZO	AutoZone, Inc.	Specialty Retail	52.35B
AZPN	Aspen Technology, Inc.	Software - Application	12.04B
AZTA	Azenta, Inc.	Medical Instruments & Supplies	3.33B
AZTR	Azitra, Inc.	Biotechnology	739.41K
AZUL	Azul S.A.	Airlines	473.53M
AZZ	AZZ Inc.	Specialty Business Services	2.40B
B	Barnes Group Inc.	Specialty Industrial Machinery	2.02B
BA	The Boeing Company	Aerospace & Defense	115.33B
BABA	Alibaba Group Holding Limited	Internet Retail	167.16B
BAC	Bank of America Corporation	Banks - Diversified	322.90B
BACA	Berenson Acquisition Corp. I	Shell Companies	84.04M
BACK	IMAC Holdings, Inc.	Medical Care Facilities	1.95M
BAER	Bridger Aerospace Group Holdings, Inc.	Security & Protection Services	174.89M
BAFN	BayFirst Financial Corp.	Banks - Regional	53.75M
BAH	Booz Allen Hamilton Holding Corporation	Consulting Services	18.12B
BAK	Braskem S.A.	Chemicals	2.53B
BALL	Ball Corporation	Packaging & Containers	19.55B
BALY	Bally's Corporation	Resorts & Casinos	695.94M
BAM	Brookfield Asset Management Inc.	Asset Management	18.13B
BANC	Banc of California, Inc.	Banks - Regional	2.33B
BAND	Bandwidth Inc.	Software - Infrastructure	615.51M
BANF	BancFirst Corporation	Banks - Regional	3.58B
BANL	CBL International Limited	Oil & Gas Midstream	20.42M
BANR	Banner Corporation	Banks - Regional	2.06B
BANX	ArrowMark Financial Corp.	Asset Management	135.94M
BAOS	Baosheng Media Group Holdings Limited	Advertising Agencies	3.76M
BAP	Credicorp Ltd.	Banks - Regional	13.68B
BARK	BARK, Inc.	Specialty Retail	263.92M
BASE	Couchbase, Inc.	Software - Infrastructure	978.02M
BATL	Battalion Oil Corporation	Oil & Gas Exploration & Production	58.75M
BATRA	Atlanta Braves Holdings Inc	Entertainment	2.68B
BATRK	Atlanta Braves Holdings Inc	Entertainment	2.68B
BAX	Baxter International Inc.	Medical Instruments & Supplies	18.34B
BAYA	Bayview Acquisition Corp	Shell Companies	79.64M
BB	BlackBerry Limited	Software - Infrastructure	1.41B
BBAI	BigBear.ai Holdings, Inc.	Information Technology Services	341.50M
BBAR	BBVA Argentina	Banks - Regional	2.40B
BBCP	Concrete Pumping Holdings, Inc.	Engineering & Construction	368.01M
BBD	Banco Bradesco S.A.	Banks - Regional	22.47B
BBDC	Barings BDC, Inc.	Asset Management	1.07B
BBDO	Banco Bradesco S.A.	Banks - Regional	21.98B
BBGI	Beasley Broadcast Group, Inc.	Broadcasting	19.23M
BBIO	BridgeBio Pharma, Inc.	Biotechnology	4.90B
BBLG	Bone Biologics Corporation	Medical Devices	1.96M
BBSI	Barrett Business Services, Inc.	Staffing & Employment Services	944.87M
BBU	Brookfield Business Partners L.P.	Conglomerates	1.49B
BBUC	Brookfield Business Corporation	Asset Management	1.62B
BBVA	Banco Bilbao Vizcaya Argentaria, S.A.	Banks - Diversified	63.15B
BBW	Build-A-Bear Workshop, Inc.	Specialty Retail	371.50M
BBWI	Bath & Body Works, Inc.	Specialty Retail	8.09B
BBY	Best Buy Co., Inc.	Specialty Retail	18.31B
BC	Brunswick Corporation	Recreational Vehicles	5.59B
BCAB	BioAtla, Inc.	Biotechnology	78.43M
BCAL	Southern California Bancorp	Banks - Regional	285.89M
BCAN	Femto Technologies Inc.	Software - Application	6.41M
BCBP	BCB Bancorp, Inc.	Banks - Regional	214.17M
BCC	Boise Cascade Company	Building Materials	5.56B
BCDA	BioCardia, Inc.	Biotechnology	5.52M
BCE	BCE Inc.	Telecom Services	30.66B
BCG	Binah Capital Group, Inc.	Asset Management	77.86M
BCH	Banco de Chile	Banks - Regional	11.86B
BCLI	Brainstorm Cell Therapeutics Inc.	Biotechnology	26.71M
BCML	BayCom Corp	Banks - Regional	270.41M
BCO	The Brink's Company	Security & Protection Services	4.96B
BCOV	Brightcove Inc.	Software - Application	107.89M
BCOW	1895 Bancorp of Wisconsin, Inc.	Banks - Regional	51.38M
BCPC	Balchem Corporation	Specialty Chemicals	5.77B
BCRX	BioCryst Pharmaceuticals, Inc.	Biotechnology	1.52B
BCS	Barclays PLC	Banks - Diversified	44.15B
BCSA	Blockchain Coinvestors Acquisition Corp. I	Shell Companies	144.23M
BCSF	Bain Capital Specialty Finance, Inc.	Asset Management	1.09B
BCTX	BriaCell Therapeutics Corp.	Biotechnology	13.34M
BCYC	Bicycle Therapeutics plc	Biotechnology	1.02B
BDC	Belden Inc.	Communication Equipment	3.65B
BDL	Flanigan's Enterprises, Inc.	Restaurants	49.29M
BDN	Brandywine Realty Trust	REIT - Office	863.06M
BDRX	Biodexa Pharmaceuticals Plc	Biotechnology	163.19K
BDSX	Biodesix, Inc.	Diagnostics & Research	196.69M
BDTX	Black Diamond Therapeutics, Inc.	Biotechnology	331.33M
BDX	Becton, Dickinson and Company	Medical Instruments & Supplies	69.30B
BE	Bloom Energy Corporation	Electrical Equipment & Parts	3.01B
BEAM	Beam Therapeutics Inc.	Biotechnology	2.64B
BEAT	HeartBeam, Inc.	Health Information Services	63.69M
BECN	Beacon Roofing Supply, Inc.	Industrial Distribution	6.41B
BEDU	Bright Scholar Education Holdings Limited	Education & Training Services	53.21M
BEEM	Beam Global	Solar	87.56M
BEEP	Mobile Infrastructure Corporation	Infrastructure Operations	91.46M
BEKE	KE Holdings Inc.	Real Estate Services	15.81B
BELFA	Bel Fuse Inc.	Electronic Components	954.02M
BELFB	Bel Fuse Inc.	Electronic Components	937.09M
BEN	Franklin Resources, Inc.	Asset Management	12.02B
BENF	Beneficient	Asset Management	13.88M
BEP	Brookfield Renewable Partners L.P.	Utilities - Renewable	15.63B
BEPC	Brookfield Renewable Corporation	Utilities - Renewable	4.98B
BERY	Berry Global Group, Inc.	Packaging & Containers	7.44B
BEST	BEST Inc.	Trucking	51.98M
BETR	Better Home & Finance Holding Company	Mortgage Finance	401.27M
BF.A	Brown-Forman Corporation	Beverages - Wineries & Distilleries	21.12B
BF.B	Brown-Forman Corporation	Beverages - Wineries & Distilleries	20.97B
BFAC	Battery Future Acquisition Corp.	Shell Companies	136.50M
BFAM	Bright Horizons Family Solutions Inc.	Personal Services	6.99B
BFC	Bank First Corporation	Banks - Regional	943.92M
BFH	Bread Financial Holdings, Inc.	Credit Services	2.69B
BFI	BurgerFi International, Inc.	Restaurants	15.44M
BFIN	BankFinancial Corporation	Banks - Regional	147.04M
BFLY	Butterfly Network, Inc.	Medical Devices	229.67M
BFRG	Bullfrog AI Holdings, Inc.	Health Information Services	23.46M
BFRI	Biofrontera Inc.	Drug Manufacturers - Specialty & Generic	6.01M
BFS	Saul Centers, Inc.	REIT - Retail	948.96M
BFST	Business First Bancshares, Inc.	Banks - Regional	646.86M
BG	Bunge Limited	Farm Products	16.07B
BGC	BGC Group, Inc	Capital Markets	4.45B
BGFV	Big 5 Sporting Goods Corporation	Specialty Retail	62.56M
BGI	Birks Group Inc.	Luxury Goods	48.49M
BGLC	BioNexus Gene Lab Corp.	Specialty Chemicals	8.57M
BGNE	BeiGene, Ltd.	Biotechnology	17.37B
BGS	B&G Foods, Inc.	Packaged Foods	679.49M
BGSF	BGSF, Inc.	Staffing & Employment Services	90.61M
BGXX	Bright Green Corporation	Drug Manufacturers - Specialty & Generic	44.54M
BH	Biglari Holdings Inc.	Restaurants	610.65M
BH.A	Biglari Holdings Inc.	Restaurants	614.94M
BHAC	Focus Impact BH3 Acquisition Co.	Shell Companies	91.91M
BHAT	Blue Hat Interactive Entertainment Technology	Electronic Gaming & Multimedia	56.10M
BHB	Bar Harbor Bankshares	Banks - Regional	486.07M
BHC	Bausch Health Companies Inc.	Drug Manufacturers - Specialty & Generic	2.18B
BHE	Benchmark Electronics, Inc.	Electronic Components	1.47B
BHF	Brighthouse Financial, Inc.	Insurance - Life	3.15B
BHIL	Benson Hill, Inc.	Agricultural Inputs	39.80M
BHLB	Berkshire Hills Bancorp, Inc.	Banks - Regional	1.20B
BHM	Bluerock Homes Trust, Inc.	REIT - Residential	73.82M
BHP	BHP Group Limited	Other Industrial Metals & Mining	136.65B
BHR	Braemar Hotels & Resorts Inc.	REIT - Hotel & Motel	248.29M
BHRB	Burke & Herbert Bank & Trust Company	Banks - Regional	1.01B
BHVN	Biohaven Pharmaceutical Holding Company Ltd.	Biotechnology	3.43B
BIAF	bioAffinity Technologies, Inc.	Diagnostics & Research	29.49M
BIDU	Baidu, Inc.	Internet Content & Information	31.62B
BIG	Big Lots, Inc.	Discount Stores	30.72M
BIGC	BigCommerce Holdings, Inc.	Software - Application	623.61M
BIIB	Biogen Inc.	Drug Manufacturers - General	31.05B
BILI	Bilibili Inc.	Electronic Gaming & Multimedia	6.08B
BILL	BILL Holdings Inc	Software - Application	5.56B
BIMI	BIMI International Medical Inc.	Pharmaceutical Retailers	4.48M
BIO	Bio-Rad Laboratories, Inc.	Medical Devices	9.53B
BIO.B	Bio-Rad Laboratories, Inc.	Medical Devices	8.34B
BIOR	Biora Therapeutics, Inc.	Biotechnology	24.50M
BIOX	Bioceres Crop Solutions Corp.	Agricultural Inputs	679.80M
BIP	Brookfield Infrastructure Partners L.P.	Utilities - Diversified	14.29B
BIPC	Brookfield Infrastructure Corporation	Utilities - Regulated Gas	5.09B
BIRD	Allbirds, Inc.	Apparel Retail	97.76M
BIRK	Birkenstock Holding plc	Footwear & Accessories	10.98B
BITF	Bitfarms Ltd.	Capital Markets	1.01B
BIVI	BioVie Inc.	Biotechnology	24.22M
BJ	BJ's Wholesale Club Holdings, Inc.	Discount Stores	11.76B
BJDX	Bluejay Diagnostics, Inc.	Medical Devices	291.00K
BJRI	BJ's Restaurants, Inc.	Restaurants	735.16M
BK	The Bank of New York Mellon Corporation	Asset Management	48.87B
BKD	Brookdale Senior Living Inc.	Medical Care Facilities	1.52B
BKE	The Buckle, Inc.	Apparel Retail	2.14B
BKH	Black Hills Corporation	Utilities - Regulated Gas	4.03B
BKHA	Black Hawk Acquisition Corporation	Shell Companies	90.63M
BKKT	Bakkt Holdings, Inc.	Software - Infrastructure	105.07M
BKNG	Booking Holdings Inc.	Travel Services	125.87B
BKR	Baker Hughes Company	Oil & Gas Equipment & Services	38.41B
BKSY	BlackSky Technology Inc.	Scientific & Technical Instruments	162.79M
BKTI	BK Technologies Corporation	Communication Equipment	44.74M
BKU	BankUnited, Inc.	Banks - Regional	2.88B
BKYI	BIO-key International, Inc.	Security & Protection Services	2.63M
BL	BlackLine, Inc.	Software - Application	2.94B
BLAC	Bellevue Life Sciences Acquisition Corp.	Shell Companies	60.90M
BLBD	Blue Bird Corporation	Auto Manufacturers	1.65B
BLBX	Blackboxstocks Inc.	Software - Application	8.71M
BLCO	Bausch + Lomb Corporation	Medical Instruments & Supplies	5.92B
BLD	TopBuild Corp.	Engineering & Construction	15.01B
BLDE	Blade Air Mobility, Inc.	Airports & Air Services	262.20M
BLDP	Ballard Power Systems Inc.	Specialty Industrial Machinery	657.15M
BLDR	Builders FirstSource, Inc.	Building Products & Equipment	20.25B
BLEU	bleuacacia ltd	Shell Companies	83.49M
BLFS	BioLife Solutions, Inc.	Medical Instruments & Supplies	1.10B
BLFY	Blue Foundry Bancorp	Banks - Regional	269.57M
BLIN	Bridgeline Digital, Inc.	Software - Infrastructure	9.83M
BLK	BlackRock, Inc.	Asset Management	128.84B
BLKB	Blackbaud, Inc.	Software - Application	4.15B
BLMN	Bloomin' Brands, Inc.	Restaurants	1.80B
BLMZ	BloomZ Inc.	Electronic Gaming & Multimedia	21.45M
BLND	Blend Labs, Inc.	Software - Application	655.81M
BLNK	Blink Charging Co.	Engineering & Construction	322.89M
BLRX	BioLineRx Ltd.	Biotechnology	61.19M
BLTE	Belite Bio, Inc	Biotechnology	1.44B
BLUE	bluebird bio, Inc.	Biotechnology	216.83M
BLX	Banco Latinoamericano de Comercio Exterior, S. A.	Banks - Regional	1.12B
BLZE	Backblaze, Inc.	Software - Infrastructure	258.96M
BMA	Banco Macro S.A.	Banks - Regional	4.35B
BMBL	Bumble Inc.	Software - Application	1.16B
BMEA	Biomea Fusion, Inc.	Biotechnology	194.10M
BMI	Badger Meter, Inc.	Scientific & Technical Instruments	5.93B
BMO	Bank of Montreal	Banks - Diversified	60.18B
BMR	Beamr Imaging Ltd.	Software - Application	68.26M
BMRA	Biomerica, Inc.	Medical Devices	5.72M
BMRC	Bank of Marin Bancorp	Banks - Regional	332.88M
BMRN	BioMarin Pharmaceutical Inc.	Biotechnology	15.93B
BMTX	BM Technologies, Inc.	Software - Application	33.17M
BMY	Bristol-Myers Squibb Company	Drug Manufacturers - General	99.53B
BN	Brookfield Corporation	Asset Management	78.65B
BNAI	Brand Engagement Network, Inc.	Software - Infrastructure	88.49M
BNED	Barnes & Noble Education, Inc.	Specialty Retail	261.56M
BNGO	Bionano Genomics, Inc.	Medical Instruments & Supplies	49.90M
BNIX	Bannix Acquisition Corp.	Shell Companies	44.90M
BNL	Broadstone Net Lease, Inc.	REIT - Diversified	3.37B
BNOX	Bionomics Limited	Biotechnology	7.75M
BNR	Burning Rock Biotech Limited	Diagnostics & Research	74.96M
BNRE	Brookfield Reinsurance Ltd.	Insurance - Reinsurance	5.70B
BNRE.A	Brookfield Reinsurance Ltd.	Insurance - Reinsurance	4.40B
BNRG	Brenmiller Energy Ltd	Utilities - Renewable	1.99M
BNS	The Bank of Nova Scotia	Banks - Diversified	57.52B
BNTC	Benitec Biopharma Inc.	Biotechnology	79.72M
BNTX	BioNTech SE	Biotechnology	20.54B
BNZI	Banzai International, Inc.	Software - Application	3.98M
BOC	Boston Omaha Corporation	Conglomerates	447.89M
BOCN	Blue Ocean Acquisition Corp.	Shell Companies	74.02M
BODI	The Beachbody Company, Inc.	Internet Content & Information	52.66M
BOF	BranchOut Food Inc.	Packaged Foods	4.87M
BOH	Bank of Hawaii Corporation	Banks - Regional	2.72B
BOKF	BOK Financial Corporation	Banks - Regional	6.74B
BOLD	Boundless Bio, Inc.	Biotechnology	83.45M
BOLT	Bolt Biotherapeutics, Inc.	Biotechnology	28.29M
BON	Bon Natural Life Limited	Packaged Foods	2.94M
BOOM	DMC Global Inc.	Oil & Gas Equipment & Services	277.75M
BOOT	Boot Barn Holdings, Inc.	Apparel Retail	3.98B
BORR	Borr Drilling Limited	Oil & Gas Drilling	1.65B
BOSC	B.O.S. Better Online Solutions Ltd.	Communication Equipment	17.30M
BOTJ	Bank of the James Financial Group, Inc.	Banks - Regional	61.34M
BOW	Bowhead Specialty Holdings Inc.	Insurance - Property & Casualty	864.85M
BOWL	Bowlero Corp.	Leisure	1.86B
BOWN	Bowen Acquisition Corp	Shell Companies	97.16M
BOX	Box, Inc.	Software - Infrastructure	4.08B
BOXL	Boxlight Corporation	Communication Equipment	6.12M
BP	BP p.l.c.	Oil & Gas Integrated	95.67B
BPMC	Blueprint Medicines Corporation	Biotechnology	6.72B
BPOP	Popular, Inc.	Banks - Regional	7.48B
BPRN	Princeton Bancorp Inc	Banks - Regional	239.54M
BPT	BP Prudhoe Bay Royalty Trust	Oil & Gas Midstream	34.67M
BPTH	Bio-Path Holdings, Inc.	Biotechnology	3.37M
BQ	Boqii Holding Limited	Specialty Retail	2.10M
BR	Broadridge Financial Solutions, Inc.	Information Technology Services	25.36B
BRAC	Broad Capital Acquisition Corp.	Shell Companies	34.25M
BRAG	Bragg Gaming Group Inc.	Gambling	134.43M
BRBR	BellRing Brands, Inc.	Packaged Foods	6.66B
BRBS	Blue Ridge Bankshares, Inc.	Banks - Regional	204.34M
BRC	Brady Corporation	Security & Protection Services	3.39B
BRCC	BRC Inc.	Packaged Foods	1.21B
BRDG	Bridge Investment Group Holdings Inc.	Asset Management	2.08B
BREA	Brera Holdings PLC	Entertainment	7.14M
BRFH	Barfresh Food Group, Inc.	Beverages - Non-Alcoholic	54.91M
BRFS	BRF S.A.	Packaged Foods	6.35B
BRID	Bridgford Foods Corporation	Packaged Foods	84.87M
BRK.A	Berkshire Hathaway Inc.	Insurance - Diversified	950.24B
BRK.B	Berkshire Hathaway Inc.	Insurance - Diversified	950.64B
BRKH	Burtech Acquisition Corp.	Shell Companies	169.75M
BRKL	Brookline Bancorp, Inc.	Banks - Regional	947.17M
BRKR	Bruker Corporation	Medical Devices	10.17B
BRLS	Borealis Foods Inc.	Packaged Foods	186.00M
BRLT	Brilliant Earth Group, Inc.	Luxury Goods	252.48M
BRN	Barnwell Industries, Inc.	Oil & Gas Exploration & Production	23.37M
BRNS	Barinthus Biotherapeutics plc	Biotechnology	58.82M
BRO	Brown & Brown, Inc.	Insurance Brokers	28.34B
BROG	Brooge Energy Limited	Oil & Gas Midstream	82.75M
BROS	Dutch Bros Inc.	Restaurants	5.87B
BRSP	BrightSpire Capital, Inc.	REIT - Mortgage	819.75M
BRT	BRT Apartments Corp.	REIT - Residential	346.53M
BRTX	BioRestorative Therapies, Inc.	Biotechnology	10.83M
BRX	Brixmor Property Group Inc.	REIT - Retail	7.80B
BRY	Berry Corporation	Oil & Gas Exploration & Production	514.34M
BRZE	Braze, Inc.	Software - Application	4.32B
BSAC	Banco Santander-Chile	Banks - Regional	9.28B
BSBK	Bogota Financial Corp.	Banks - Regional	96.43M
BSBR	Banco Santander (Brasil) S.A.	Banks - Regional	37.95B
BSET	Bassett Furniture Industries, Incorporated	Furnishings, Fixtures & Appliances	117.55M
BSFC	Blue Star Foods Corp.	Packaged Foods	4.57M
BSIG	BrightSphere Investment Group Inc.	Asset Management	986.20M
BSM	Black Stone Minerals, L.P.	Oil & Gas Exploration & Production	3.17B
BSRR	Sierra Bancorp	Banks - Regional	424.52M
BSVN	Bank7 Corp.	Banks - Regional	375.00M
BSX	Boston Scientific Corporation	Medical Devices	108.64B
BSY	Bentley Systems, Incorporated	Software - Application	14.41B
BTAI	BioXcel Therapeutics, Inc.	Biotechnology	42.03M
BTBD	BT Brands, Inc.	Restaurants	8.62M
BTBT	Bit Digital, Inc.	Capital Markets	426.54M
BTCM	BIT Mining Limited	Information Technology Services	31.34M
BTCS	BTCS Inc.	Capital Markets	24.17M
BTCT	BTC Digital Ltd.	Computer Hardware	4.88M
BTCY	Biotricity, Inc.	Medical Devices	14.76M
BTDR	Bitdeer Technologies Group	Software - Application	1.29B
BTE	Baytex Energy Corp.	Oil & Gas Exploration & Production	2.86B
BTG	B2Gold Corp.	Gold	3.83B
BTI	British American Tobacco p.l.c.	Tobacco	78.62B
BTM	Bitcoin Depot Inc.	Capital Markets	99.81M
BTMD	biote Corp.	Medical Care Facilities	485.13M
BTOC	Armlogi Holding Corp.	Integrated Freight & Logistics	200.51M
BTOG	Bit Origin Limited	Capital Markets	9.63M
BTSG	BrightSpring Health Services, Inc.	Health Information Services	2.14B
BTTR	Better Choice Company Inc.	Packaged Foods	2.57M
BTU	Peabody Energy Corporation	Thermal Coal	2.74B
BUD	Anheuser-Busch InBev SA/NV	Beverages - Brewers	123.36B
BUJA	Bukit Jalil Global Acquisition 1 Ltd	Shell Companies	83.28M
BUR	Burford Capital Limited	Asset Management	3.01B
BURL	Burlington Stores, Inc.	Apparel Retail	16.25B
BUSE	First Busey Corporation	Banks - Regional	1.57B
BV	BrightView Holdings, Inc.	Specialty Business Services	1.32B
BVN	Compania de Minas Buenaventura S.A.	Other Precious Metals & Mining	3.93B
BVS	Bioventus Inc.	Medical Devices	461.47M
BW	Babcock & Wilcox Enterprises, Inc.	Specialty Industrial Machinery	136.97M
BWA	BorgWarner Inc.	Auto Parts	7.35B
BWAY	BrainsWay Ltd.	Medical Devices	124.67M
BWB	Bridgewater Bancshares, Inc.	Banks - Regional	381.87M
BWEN	Broadwind, Inc.	Specialty Industrial Machinery	67.37M
BWFG	Bankwell Financial Group, Inc.	Banks - Regional	213.18M
BWIN	The Baldwin Insurance Group, Inc.	Insurance Brokers	2.91B
BWLP	BW LPG Limited	Marine Shipping	2.14B
BWMN	Bowman Consulting Group Ltd.	Engineering & Construction	601.01M
BWMX	Betterware de México, S.A.P.I. de C.V.	Specialty Retail	537.17M
BWXT	BWX Technologies, Inc.	Aerospace & Defense	9.00B
BX	Blackstone Inc.	Asset Management	171.15B
BXC	BlueLinx Holdings Inc.	Industrial Distribution	1.07B
BXMT	Blackstone Mortgage Trust, Inc.	REIT - Mortgage	3.11B
BXP	BXP Inc.	REIT - Office	11.27B
BY	Byline Bancorp, Inc.	Banks - Regional	1.24B
BYD	Boyd Gaming Corporation	Resorts & Casinos	5.79B
BYFC	Broadway Financial Corporation	Banks - Regional	48.76M
BYND	Beyond Meat, Inc.	Packaged Foods	388.66M
BYNO	byNordic Acquisition Corporation	Shell Companies	116.43M
BYON	Beyond, Inc.	Internet Retail	591.09M
BYRN	Byrna Technologies Inc.	Aerospace & Defense	208.98M
BYSI	BeyondSpring Inc.	Biotechnology	77.78M
BYU	BAIYU Holdings, Inc.	Shell Companies	24.32M
BZ	Kanzhun Limited	Internet Content & Information	6.05B
BZFD	BuzzFeed, Inc.	Internet Content & Information	97.97M
BZH	Beazer Homes USA, Inc.	Residential Construction	1.07B
BZUN	Baozun Inc.	Internet Retail	105.48M
C	Citigroup Inc.	Banks - Diversified	125.43B
CAAP	Corporación América Airports S.A.	Airports & Air Services	2.56B
CAAS	China Automotive Systems, Inc.	Auto Parts	120.44M
CABA	Cabaletta Bio, Inc.	Biotechnology	336.00M
CABO	Cable One, Inc.	Telecom Services	2.27B
CAC	Camden National Corporation	Banks - Regional	615.38M
CACC	Credit Acceptance Corporation	Credit Services	7.05B
CACI	CACI International Inc	Information Technology Services	10.15B
CACO	Caravelle International Group	Marine Shipping	25.33M
CADE	Cadence Bank	Banks - Regional	6.08B
CADL	Candel Therapeutics, Inc.	Biotechnology	177.05M
CAE	CAE Inc.	Aerospace & Defense	5.69B
CAG	Conagra Brands, Inc.	Packaged Foods	14.58B
CAH	Cardinal Health, Inc.	Medical Distribution	24.31B
CAKE	The Cheesecake Factory Incorporated	Restaurants	1.98B
CAL	Caleres, Inc.	Apparel Retail	1.33B
CALB	California BanCorp	Banks - Regional	207.11M
CALC	CalciMedica, Inc.	Biotechnology	54.29M
CALM	Cal-Maine Foods, Inc.	Farm Products	3.53B
CALT	Calliditas Therapeutics AB (publ)	Biotechnology	1.02B
CALX	Calix, Inc.	Software - Infrastructure	2.65B
CAMT	Camtek Ltd.	Semiconductor Equipment & Materials	4.39B
CAN	Canaan Inc.	Computer Hardware	281.18M
CANF	Can-Fite BioPharma Ltd.	Biotechnology	21.10M
CANG	Cango Inc.	Auto & Truck Dealerships	200.82M
CAPL	CrossAmerica Partners LP	Oil & Gas Refining & Marketing	761.30M
CAPR	Capricor Therapeutics, Inc.	Biotechnology	131.12M
CAPT	Captivision Inc.	Building Materials	60.82M
CAR	Avis Budget Group, Inc.	Rental & Leasing Services	3.50B
CARA	Cara Therapeutics, Inc.	Biotechnology	19.14M
CARE	Carter Bankshares, Inc.	Banks - Regional	374.00M
CARG	CarGurus, Inc.	Auto & Truck Dealerships	2.59B
CARM	Carisma Therapeutics, Inc.	Biotechnology	45.29M
CARR	Carrier Global Corporation	Building Products & Equipment	60.85B
CARS	Cars.com Inc.	Auto & Truck Dealerships	1.33B
CART	Maplebear Inc.	Internet Retail	9.04B
CARV	Carver Bancorp, Inc.	Banks - Regional	9.83M
CASH	Pathward Financial, Inc.	Banks - Regional	1.72B
CASI	CASI Pharmaceuticals, Inc.	Biotechnology	92.07M
CASS	Cass Information Systems, Inc.	Specialty Business Services	570.44M
CASY	Casey's General Stores, Inc.	Specialty Retail	14.62B
CAT	Caterpillar Inc.	Farm & Heavy Construction Machinery	167.26B
CATO	The Cato Corporation	Apparel Retail	96.40M
CATX	Perspective Therapeutics, Inc.	Medical Devices	842.88M
CATY	Cathay General Bancorp	Banks - Regional	3.23B
CAUD	Collective Audience, Inc.	Software - Application	7.30M
CAVA	CAVA Group, Inc.	Restaurants	9.27B
CB	Chubb Limited	Insurance - Property & Casualty	112.42B
CBAN	Colony Bankcorp, Inc.	Banks - Regional	276.02M
CBAT	CBAK Energy Technology, Inc.	Electrical Equipment & Parts	116.93M
CBFV	CB Financial Services, Inc.	Banks - Regional	125.99M
CBL	CBL & Associates Properties, Inc.	REIT - Retail	830.28M
CBNK	Capital Bancorp, Inc.	Banks - Regional	346.82M
CBOE	Cboe Global Markets, Inc.	Financial Data & Stock Exchanges	19.61B
CBRE	CBRE Group, Inc.	Real Estate Services	34.00B
CBRG	Chain Bridge I	Shell Companies	75.59M
CBRL	Cracker Barrel Old Country Store, Inc.	Restaurants	1.02B
CBSH	Commerce Bancshares, Inc.	Banks - Regional	8.41B
CBT	Cabot Corporation	Specialty Chemicals	5.48B
CBU	Community Bank System, Inc.	Banks - Regional	3.25B
CBUS	Cibus, Inc.	Biotechnology	252.19M
CBZ	CBIZ, Inc.	Specialty Business Services	4.30B
CC	The Chemours Company	Specialty Chemicals	3.52B
CCAP	Crescent Capital BDC, Inc.	Asset Management	700.46M
CCB	Coastal Financial Corporation	Banks - Regional	711.90M
CCBG	Capital City Bank Group, Inc.	Banks - Regional	600.58M
CCCC	C4 Therapeutics, Inc.	Biotechnology	429.69M
CCCS	CCC Intelligent Solutions Holdings Inc.	Software - Infrastructure	6.84B
CCEL	Cryo-Cell International, Inc.	Medical Care Facilities	59.01M
CCEP	Coca-Cola Europacific Partners PLC	Beverages - Non-Alcoholic	33.68B
CCG	Cheche Group Inc.	Internet Content & Information	64.60M
CCI	Crown Castle Inc.	REIT - Specialty	47.30B
CCIX	Churchill Capital Corp IX	Shell Companies	367.36M
CCJ	Cameco Corporation	Uranium	19.22B
CCK	Crown Holdings, Inc.	Packaging & Containers	10.51B
CCL	Carnival Corporation & plc	Travel Services	21.58B
CCLD	CareCloud, Inc.	Health Information Services	35.52M
CCM	Concord Medical Services Holdings Limited	Medical Care Facilities	26.36M
CCNE	CNB Financial Corporation	Banks - Regional	541.05M
CCO	Clear Channel Outdoor Holdings, Inc.	Advertising Agencies	803.92M
CCOI	Cogent Communications Holdings, Inc.	Telecom Services	3.33B
CCRD	CoreCard Corporation	Software - Application	98.91M
CCRN	Cross Country Healthcare, Inc.	Medical Care Facilities	607.16M
CCS	Century Communities, Inc.	Residential Construction	3.25B
CCSI	Consensus Cloud Solutions, Inc.	Software - Infrastructure	417.85M
CCTG	CCSC Technology International Holdings Limited	Electrical Equipment & Parts	15.98M
CCTS	Cactus Acquisition Corp. 1 Limited	Shell Companies	57.96M
CCU	Compania Cervecerias Unidas S.A.	Beverages - Brewers	2.03B
CDAQ	Compass Digital Acquisition Corp.	Shell Companies	113.14M
CDE	Coeur Mining, Inc.	Gold	2.51B
CDIO	Cardio Diagnostics Holdings, Inc.	Biotechnology	9.89M
CDLR	Cadeler A/S	Engineering & Construction	2.25B
CDLX	Cardlytics, Inc.	Advertising Agencies	401.97M
CDMO	Avid Bioservices, Inc.	Biotechnology	652.34M
CDNA	CareDx, Inc	Diagnostics & Research	966.68M
CDNS	Cadence Design Systems, Inc.	Software - Application	69.38B
CDP	COPT Defense Properties	REIT - Office	3.23B
CDRE	Cadre Holdings, Inc.	Aerospace & Defense	1.48B
CDRO	Codere Online Luxembourg, S.A.	Gambling	356.27M
CDT	Conduit Pharmaceuticals Inc.	Biotechnology	16.80M
CDTG	CDT Environmental Technology Investment Holdings Limited ordinary shares	Waste Management	32.04M
CDTX	Cidara Therapeutics, Inc.	Biotechnology	91.50M
CDW	CDW Corporation	Information Technology Services	31.06B
CDXC	ChromaDex Corporation	Packaged Foods	217.99M
CDXS	Codexis, Inc.	Biotechnology	254.01M
CDZI	Cadiz Inc.	Utilities - Regulated Water	232.50M
CE	Celanese Corporation	Chemicals	15.11B
CEAD	CEA Industries Inc.	Farm & Heavy Construction Machinery	4.82M
CECO	CECO Environmental Corp.	Pollution & Treatment Controls	974.70M
CEG	Constellation Energy Corporation	Utilities - Renewable	52.85B
CEI	Camber Energy, Inc.	Specialty Industrial Machinery	21.45M
FTK	Flotek Industries, Inc.	Oil & Gas Equipment & Services	131.97M
FTLF	FitLife Brands, Inc.	Packaged Foods	148.75M
FTNT	Fortinet, Inc.	Software - Infrastructure	43.66B
FTRE	Fortrea Holdings Inc.	Biotechnology	2.46B
FTS	Fortis Inc.	Utilities - Regulated Electric	20.43B
FTV	Fortive Corporation	Scientific & Technical Instruments	24.88B
FUBO	fuboTV Inc.	Broadcasting	424.33M
FUFU	BitFuFu Inc.	Capital Markets	117.75M
FUL	H.B. Fuller Company	Specialty Chemicals	4.68B
FULC	Fulcrum Therapeutics, Inc.	Biotechnology	525.82M
FULT	Fulton Financial Corporation	Banks - Regional	3.58B
FUN	Six Flags Entertainment Corp.	Leisure	4.74B
FUNC	First United Corporation	Banks - Regional	186.85M
FURY	Fury Gold Mines Limited	Other Industrial Metals & Mining	58.27M
FUSB	First US Bancshares, Inc.	Banks - Regional	58.88M
FUTU	Futu Holdings Limited	Capital Markets	2.68B
FVCB	FVCBankcorp, Inc.	Banks - Regional	223.91M
FVRR	Fiverr International Ltd.	Internet Content & Information	843.51M
FWONA	Formula One Group - Series A	Entertainment	29.73B
FWONK	Formula One Group - Series C	Entertainment	29.84B
FWRD	Forward Air Corporation	Integrated Freight & Logistics	650.25M
FWRG	First Watch Restaurant Group, Inc.	Restaurants	944.53M
FXNC	First National Corporation	Banks - Regional	108.60M
FYBR	Frontier Communications Parent, Inc.	Telecom Services	7.14B
G	Genpact Limited	Information Technology Services	6.30B
GABC	German American Bancorp, Inc.	Banks - Regional	1.20B
GAIA	Gaia, Inc.	Entertainment	118.87M
GAIN	Gladstone Investment Corporation	Asset Management	518.04M
GALT	Galectin Therapeutics Inc.	Biotechnology	153.51M
GAMB	Gambling.com Group Limited	Gambling	349.66M
GAMC	Golden Arrow Merger Corp.	Shell Companies	83.88M
GAME	GameSquare Holdings Inc	Electronic Gaming & Multimedia	14.16M
GAN	GAN Limited	Gambling	70.35M
GANX	Gain Therapeutics, Inc.	Biotechnology	19.90M
GAQ	Generation Asia I Acquisition Limited	Shell Companies	87.81M
GASS	StealthGas Inc.	Marine Shipping	239.96M
GATE	Marblegate Acquisition Corp.	Shell Companies	127.52M
GATO	Gatos Silver, Inc.	Other Precious Metals & Mining	835.71M
GATX	GATX Corporation	Rental & Leasing Services	4.93B
GAU	Galiano Gold Inc.	Gold	440.91M
GAUZ	Gauzy Ltd.	Tools & Accessories	190.54M
GB	Global Blue Group Holding AG	Software - Infrastructure	900.74M
GBBK	Global Blockchain Acquisition Corp.	Shell Companies	60.65M
GBCI	Glacier Bancorp, Inc.	Banks - Regional	5.07B
GBDC	Golub Capital BDC, Inc.	Asset Management	4.07B
GBIO	Generation Bio Co.	Biotechnology	206.90M
GBLI	Global Indemnity Group, LLC	Insurance - Property & Casualty	425.00M
GBNY	Generations Bancorp NY, Inc.	Banks - Regional	23.68M
GBR	New Concept Energy, Inc.	Real Estate Services	6.95M
GBTG	Global Business Travel Group, Inc.	Software - Application	3.19B
GBX	The Greenbrier Companies, Inc.	Railroads	1.59B
GCBC	Greene County Bancorp, Inc.	Banks - Regional	608.71M
GCI	Gannett Co., Inc.	Publishing	705.28M
GCMG	GCM Grosvenor Inc	Asset Management	2.11B
GCO	Genesco Inc.	Apparel Retail	359.77M
GCT	GigaCloud Technology Inc.	Software - Infrastructure	1.17B
GCTK	GlucoTrack, Inc.	Medical Instruments & Supplies	7.34M
GCTS	GCT Semiconductor Holding, Inc.	Semiconductors	213.39M
GD	General Dynamics Corporation	Aerospace & Defense	80.24B
GDC	GD Culture Group Limited	Electronic Gaming & Multimedia	11.59M
GDDY	GoDaddy Inc.	Software - Infrastructure	20.29B
GDEN	Golden Entertainment, Inc.	Resorts & Casinos	945.32M
GDEV	GDEV Inc.	Electronic Gaming & Multimedia	470.77M
GDHG	Golden Heaven Group Holdings Ltd.	Leisure	7.46M
GDOT	Green Dot Corporation	Credit Services	510.28M
GDRX	GoodRx Holdings, Inc.	Health Information Services	3.24B
GDS	GDS Holdings Limited	Information Technology Services	1.99B
GDST	Goldenstone Acquisition Limited	Shell Companies	39.24M
GDTC	CytoMed Therapeutics Limited	Biotechnology	20.84M
GDYN	Grid Dynamics Holdings, Inc.	Information Technology Services	984.06M
GE	GE Aerospace	Aerospace & Defense	183.54B
GECC	Great Elm Capital Corp.	Asset Management	112.75M
GEF	Greif, Inc.	Packaging & Containers	3.18B
GEF.B	Greif, Inc.	Packaging & Containers	3.20B
GEG	Great Elm Group, Inc.	Asset Management	57.85M
GEHC	GE HealthCare Technologies Inc.	Health Information Services	37.31B
GEL	Genesis Energy, L.P.	Oil & Gas Midstream	1.72B
GEN	Gen Digital Inc.	Software - Infrastructure	16.23B
GENC	Gencor Industries, Inc.	Farm & Heavy Construction Machinery	343.14M
GENE	Genetic Technologies Limited	Diagnostics & Research	3.98M
GENI	Genius Sports Limited	Internet Content & Information	1.38B
GENK	GEN Restaurant Group, Inc.	Restaurants	37.00M
GEO	The GEO Group, Inc.	Security & Protection Services	1.96B
GEOS	Geospace Technologies Corporation	Oil & Gas Equipment & Services	115.78M
GERN	Geron Corporation	Biotechnology	2.78B
GES	Guess', Inc.	Apparel Retail	1.27B
GETY	Getty Images Holdings, Inc.	Internet Content & Information	1.50B
GEV	GE Vernova Inc.	Utilities - Renewable	45.02B
GEVO	Gevo, Inc.	Specialty Chemicals	140.51M
GFAI	Guardforce AI Co., Limited	Security & Protection Services	19.96M
GFF	Griffon Corporation	Conglomerates	3.67B
GFI	Gold Fields Limited	Gold	14.62B
GFL	GFL Environmental Inc.	Waste Management	14.07B
GFR	Greenfire Resources Ltd	Oil & Gas Exploration & Production	476.27M
GFS	GLOBALFOUNDRIES Inc.	Semiconductors	27.64B
GGAL	Grupo Financiero Galicia S.A.	Banks - Regional	5.69B
GGB	Gerdau S.A.	Steel	6.53B
GGG	Graco Inc.	Specialty Industrial Machinery	14.23B
GGR	Gogoro Inc.	Auto Manufacturers	410.32M
GH	Guardant Health, Inc.	Diagnostics & Research	4.44B
GHC	Graham Holdings Company	Education & Training Services	3.62B
GHG	GreenTree Hospitality Group Ltd.	Lodging	247.29M
GHI	Greystone Housing Impact Investors LP	Mortgage Finance	344.44M
GHIX	Gores Holdings IX, Inc.	Shell Companies	203.23M
GHLD	Guild Holdings Company	Mortgage Finance	869.25M
GHM	Graham Corporation	Specialty Industrial Machinery	350.79M
GHRS	GH Research PLC	Biotechnology	631.10M
GHSI	Guardion Health Sciences, Inc.	Drug Manufacturers - Specialty & Generic	12.14M
GIB	CGI Inc.	Information Technology Services	24.87B
GIC	Global Industrial Company	Industrial Distribution	1.36B
GIFI	Gulf Island Fabrication, Inc.	Metal Fabrication	102.09M
GIGM	GigaMedia Limited	Electronic Gaming & Multimedia	14.15M
GIII	G-III Apparel Group, Ltd.	Apparel Manufacturing	1.22B
GIL	Gildan Activewear Inc.	Apparel Manufacturing	6.78B
GILD	Gilead Sciences, Inc.	Drug Manufacturers - General	96.85B
GILT	Gilat Satellite Networks Ltd.	Communication Equipment	256.29M
GIPR	Generation Income Properties, Inc.	REIT - Diversified	15.89M
GIS	General Mills, Inc.	Packaged Foods	37.78B
GKOS	Glaukos Corporation	Medical Devices	5.92B
GL	Globe Life Inc.	Insurance - Life	8.40B
GLAC	Global Lights Acquisition Corp	Shell Companies	92.89M
GLAD	Gladstone Capital Corporation	Asset Management	521.78M
GLBE	Global-e Online Ltd.	Internet Retail	5.64B
GLBS	Globus Maritime Limited	Marine Shipping	36.43M
GLBZ	Glen Burnie Bancorp	Banks - Regional	13.79M
GLDD	Great Lakes Dredge & Dock Corporation	Engineering & Construction	608.44M
GLDG	GoldMining Inc.	Gold	162.06M
GLLI	Globalink Investment Inc.	Shell Companies	67.34M
GLMD	Galmed Pharmaceuticals Ltd.	Biotechnology	1.89M
GLNG	Golar LNG Limited	Oil & Gas Midstream	3.63B
GLOB	Globant S.A.	Information Technology Services	8.39B
GLP	Global Partners LP	Oil & Gas Midstream	1.35B
GLPG	Galapagos NV	Biotechnology	1.82B
GLPI	Gaming and Leisure Properties, Inc.	REIT - Specialty	13.81B
GLRE	Greenlight Capital Re, Ltd.	Insurance - Reinsurance	480.37M
GLSI	Greenwich LifeSciences, Inc.	Biotechnology	201.19M
GLST	Global Star Acquisition, Inc.	Shell Companies	82.75M
GLT	Glatfelter Corporation	Paper & Paper Products	68.11M
GLTO	Galecto, Inc.	Biotechnology	15.61M
GLUE	Monte Rosa Therapeutics, Inc.	Biotechnology	272.73M
GLW	Corning Incorporated	Electronic Components	33.41B
GLYC	GlycoMimetics, Inc.	Biotechnology	14.24M
GM	General Motors Company	Auto Manufacturers	50.27B
GMAB	Genmab A/S	Biotechnology	18.38B
GME	GameStop Corp.	Specialty Retail	9.76B
GMED	Globus Medical, Inc.	Medical Devices	9.65B
GMGI	Golden Matrix Group, Inc.	Electronic Gaming & Multimedia	286.30M
GMM	Global Mofy Metaverse Limited	Information Technology Services	26.28M
GMRE	Global Medical REIT Inc.	REIT - Healthcare Facilities	623.41M
GMS	GMS Inc.	Building Products & Equipment	3.77B
GNE	Genie Energy Ltd.	Utilities - Regulated Electric	450.09M
GNFT	Genfit S.A.	Biotechnology	219.03M
GNK	Genco Shipping & Trading Limited	Marine Shipping	825.54M
GNL	Global Net Lease, Inc.	REIT - Diversified	2.03B
GNLN	Greenlane Holdings, Inc.	Tobacco	1.63M
GNLX	Genelux Corporation	Biotechnology	71.45M
GNPX	Genprex, Inc.	Biotechnology	3.80M
GNRC	Generac Holdings Inc.	Specialty Industrial Machinery	9.40B
GNS	Genius Group Limited	Education & Training Services	37.43M
GNSS	Genasys Inc.	Scientific & Technical Instruments	110.60M
GNTA	Genenta Science S.p.A.	Biotechnology	78.41M
GNTX	Gentex Corporation	Auto Parts	7.17B
GNTY	Guaranty Bancshares, Inc.	Banks - Regional	383.17M
GNW	Genworth Financial, Inc.	Insurance - Life	2.98B
GO	Grocery Outlet Holding Corp.	Grocery Stores	2.08B
GOCO	GoHealth, Inc.	Insurance Brokers	130.25M
GODN	Golden Star Acquisition Corporation	Shell Companies	79.81M
GOEV	Canoo Inc.	Auto Manufacturers	144.45M
GOGL	Golden Ocean Group Limited	Marine Shipping	2.45B
GOGO	Gogo Inc.	Telecom Services	1.13B
GOLD	Barrick Gold Corporation	Gold	31.64B
GOLF	Acushnet Holdings Corp.	Leisure	4.56B
GOOD	Gladstone Commercial Corporation	REIT - Diversified	602.62M
GOOG	Alphabet Inc.	Internet Content & Information	2,091.72B
GOOGL	Alphabet Inc.	Internet Content & Information	2,092.07B
GOOS	Canada Goose Holdings Inc.	Apparel Manufacturing	1.09B
GORO	Gold Resource Corporation	Gold	38.22M
GORV	Lazydays Holdings, Inc.	Auto & Truck Dealerships	45.60M
GOSS	Gossamer Bio, Inc.	Biotechnology	223.96M
GOTU	Gaotu Techedu Inc.	Education & Training Services	1.24B
GOVX	GeoVax Labs, Inc.	Biotechnology	10.53M
GP	GreenPower Motor Company Inc.	Farm & Heavy Construction Machinery	28.09M
GPAK	Gamer Pakistan Inc.	Specialty Business Services	4.01M
GPAT	GP-Act III Acquisition Corp.	Shell Companies	360.63M
GPC	Genuine Parts Company	Auto Parts	20.25B
GPCR	Structure Therapeutics Inc.	Biotechnology	2.11B
GPI	Group 1 Automotive, Inc.	Auto & Truck Dealerships	4.57B
GPK	Graphic Packaging Holding Company	Packaging & Containers	8.94B
GPMT	Granite Point Mortgage Trust Inc.	REIT - Mortgage	154.89M
GPN	Global Payments Inc.	Specialty Business Services	25.97B
GPOR	Gulfport Energy Corporation	Oil & Gas Exploration & Production	2.70B
GPRE	Green Plains Inc.	Chemicals	1.15B
GPRK	GeoPark Limited	Oil & Gas Exploration & Production	496.30M
GPRO	GoPro, Inc.	Consumer Electronics	235.51M
GPS	The Gap, Inc.	Apparel Retail	8.41B
GRAB	Grab Holdings Limited	Software - Application	12.60B
GRAF	Graf Global Corp.	Shell Companies	434.32M
GRAL	GRAIL, LLC	Diagnostics & Research	483.92M
GRBK	Green Brick Partners, Inc.	Residential Construction	3.35B
GRC	The Gorman-Rupp Company	Specialty Industrial Machinery	1.07B
GRDI	GRIID Infrastructure Inc.	Capital Markets	76.98M
GREE	Greenidge Generation Holdings Inc.	Capital Markets	26.44M
GRFS	Grifols, S.A.	Drug Manufacturers - General	6.10B
GRFX	Graphex Group Limited	Other Industrial Metals & Mining	12.50M
GRI	GRI Bio, Inc.	Biotechnology	758.59K
GRIN	Grindrod Shipping Holdings Ltd.	Marine Shipping	278.73M
GRMN	Garmin Ltd.	Scientific & Technical Instruments	34.26B
GRND	Grindr Inc.	Software - Application	2.00B
GRNQ	Greenpro Capital Corp.	Consulting Services	7.67M
GRNT	Granite Ridge Resources, Inc	Oil & Gas Exploration & Production	875.33M
GROM	Grom Social Enterprises, Inc.	Internet Content & Information	2.46M
GROV	Grove Collaborative Holdings, Inc.	Household & Personal Products	52.31M
GROW	U.S. Global Investors, Inc.	Asset Management	37.15M
GROY	Gold Royalty Corp.	Gold	229.09M
GRPN	Groupon, Inc.	Internet Content & Information	621.19M
GRRR	Gorilla Technology Group Inc.	Software - Infrastructure	29.89M
GRTS	Gritstone bio, Inc.	Biotechnology	68.69M
GRVY	Gravity Co., Ltd.	Electronic Gaming & Multimedia	536.33M
GRWG	GrowGeneration Corp.	Specialty Retail	140.54M
GRYP	Gryphon Digital Mining, Inc.	Capital Markets	36.98M
GS	The Goldman Sachs Group, Inc.	Capital Markets	164.07B
GSAT	Globalstar, Inc.	Telecom Services	2.22B
GSBC	Great Southern Bancorp, Inc.	Banks - Regional	746.34M
GSBD	Goldman Sachs BDC, Inc.	Asset Management	1.68B
GSHD	Goosehead Insurance, Inc	Insurance - Diversified	2.15B
GSIT	GSI Technology, Inc.	Semiconductors	72.01M
GSIW	Garden Stage Limited	Capital Markets	110.96M
GSK	GSK plc	Drug Manufacturers - General	80.81B
GSL	Global Ship Lease, Inc.	Rental & Leasing Services	906.01M
GSM	Ferroglobe PLC	Other Industrial Metals & Mining	989.21M
GSUN	Golden Sun Education Group Limited	Education & Training Services	43.40M
GT	The Goodyear Tire & Rubber Company	Auto Parts	3.30B
GTAC	Global Technology Acquisition Corp. I	Shell Companies	80.12M
GTBP	GT Biopharma, Inc.	Biotechnology	5.77M
GTE	Gran Tierra Energy Inc.	Oil & Gas Exploration & Production	273.22M
GTEC	Greenland Technologies Holding Corporation	Specialty Industrial Machinery	21.48M
GTES	Gates Industrial Corporation plc	Specialty Industrial Machinery	4.64B
GTHX	G1 Therapeutics, Inc.	Biotechnology	208.86M
GTI	Graphjet Technology Sdn. Bhd.	Other Industrial Metals & Mining	453.42M
GTIM	Good Times Restaurants Inc.	Restaurants	29.60M
GTLB	GitLab Inc.	Software - Infrastructure	8.01B
GTLS	Chart Industries, Inc.	Specialty Industrial Machinery	6.83B
GTN	Gray Television, Inc.	Broadcasting	658.49M
GTN.A	Gray Television, Inc.	Broadcasting	653.12M
GTX	Garrett Motion Inc.	Auto Parts	1.96B
GTY	Getty Realty Corp.	REIT - Retail	1.62B
GURE	Gulf Resources, Inc.	Chemicals	10.95M
GUTS	Fractyl Health, Inc.	Biotechnology	181.53M
GV	Visionary Holdings Inc.	Education & Training Services	8.42M
GVA	Granite Construction Incorporated	Engineering & Construction	3.00B
GVH	Globavend Holdings Limited	Integrated Freight & Logistics	9.79M
GVP	GSE Systems, Inc.	Software - Application	10.59M
GWAV	Greenwave Technology Solutions, Inc.	Waste Management	16.45M
GWH	ESS Tech, Inc.	Electrical Equipment & Parts	128.79M
GWRE	Guidewire Software, Inc.	Software - Application	12.26B
GWRS	Global Water Resources, Inc.	Utilities - Regulated Water	310.90M
GWW	W.W. Grainger, Inc.	Industrial Distribution	47.24B
GXAI	Gaxos.ai Inc.	Electronic Gaming & Multimedia	2.41M
GXO	GXO Logistics, Inc.	Integrated Freight & Logistics	6.60B
GYRE	Gyre Therapeutics, Inc.	Biotechnology	1.16B
GYRO	Gyrodyne, LLC	Real Estate Services	17.90M
H	Hyatt Hotels Corporation	Lodging	15.31B
HA	Hawaiian Holdings, Inc.	Airlines	652.26M
HAE	Haemonetics Corporation	Medical Instruments & Supplies	4.56B
HAFC	Hanmi Financial Corporation	Banks - Regional	613.52M
HAFN	Hafnia Limited	Marine Shipping	3.99B
HAIA	Healthcare AI Acquisition Corp.	Shell Companies	60.64M
HAIN	The Hain Celestial Group, Inc.	Packaged Foods	669.34M
HAL	Halliburton Company	Oil & Gas Equipment & Services	30.22B
HALO	Halozyme Therapeutics, Inc.	Biotechnology	7.03B
HAO	Haoxi Health Technology Limited	Advertising Agencies	122.10M
HAS	Hasbro, Inc.	Leisure	9.04B
HASI	HA Sustainable Infrastructure Capital Inc.	Real Estate Services	3.75B
HAYN	Haynes International, Inc.	Metal Fabrication	763.27M
HAYW	Hayward Holdings, Inc.	Electrical Equipment & Parts	3.16B
HBAN	Huntington Bancshares Incorporated	Banks - Regional	21.96B
HBB	Hamilton Beach Brands Holding Company	Furnishings, Fixtures & Appliances	273.87M
HBCP	Home Bancorp, Inc.	Banks - Regional	353.93M
HBI	Hanesbrands Inc.	Apparel Manufacturing	2.14B
HBIO	Harvard Bioscience, Inc.	Medical Instruments & Supplies	141.15M
HBM	Hudbay Minerals Inc.	Copper	3.10B
HBNC	Horizon Bancorp, Inc.	Banks - Regional	710.71M
HBT	HBT Financial, Inc.	Banks - Regional	737.35M
HCA	HCA Healthcare, Inc.	Medical Care Facilities	94.83B
HCAT	Health Catalyst, Inc.	Health Information Services	447.48M
HCC	Warrior Met Coal, Inc.	Coking Coal	3.51B
HCI	HCI Group, Inc.	Insurance - Property & Casualty	984.78M
HCKT	The Hackett Group, Inc.	Information Technology Services	740.33M
HCM	HUTCHMED (China) Limited	Drug Manufacturers - Specialty & Generic	3.13B
HCP	HashiCorp, Inc.	Software - Infrastructure	7.02B
HCSG	Healthcare Services Group, Inc.	Medical Care Facilities	836.26M
HCTI	Healthcare Triangle, Inc.	Health Information Services	4.01M
HCVI	Hennessy Capital Investment Corp. VI	Shell Companies	176.15M
HCWB	HCW Biologics Inc.	Biotechnology	22.69M
HD	The Home Depot, Inc.	Home Improvement Retail	357.36B
HDB	HDFC Bank Limited	Banks - Regional	145.69B
HDL	Super Hi International Holding Ltd.	Restaurants	985.20M
HDSN	Hudson Technologies, Inc.	Specialty Chemicals	402.32M
HE	Hawaiian Electric Industries, Inc.	Utilities - Regulated Electric	1.85B
HEAR	Turtle Beach Corporation	Consumer Electronics	308.85M
HEES	H&E Equipment Services, Inc.	Rental & Leasing Services	1.86B
HEI	HEICO Corporation	Aerospace & Defense	28.57B
HEI.A	HEICO Corporation	Aerospace & Defense	28.49B
HELE	Helen of Troy Limited	Household & Personal Products	1.39B
HEPA	Hepion Pharmaceuticals, Inc.	Biotechnology	4.66M
HEPS	D-Market Elektronik Hizmetler ve Ticaret A.S.	Internet Retail	1.02B
HES	Hess Corporation	Oil & Gas Exploration & Production	46.45B
HESM	Hess Midstream LP	Oil & Gas Midstream	8.40B
HFBL	Home Federal Bancorp, Inc. of Louisiana	Banks - Regional	38.73M
HFFG	HF Foods Group Inc.	Food Distribution	198.87M
HFWA	Heritage Financial Corporation	Banks - Regional	802.03M
HG	Hamilton Insurance Group, Ltd.	Insurance - Reinsurance	1.93B
HGBL	Heritage Global Inc.	Capital Markets	89.06M
HGTY	Hagerty, Inc.	Insurance - Property & Casualty	941.88M
HGV	Hilton Grand Vacations Inc.	Resorts & Casinos	4.50B
HHGC	HHG Capital Corporation	Shell Companies	58.79M
HHH	Howard Hughes Holdings Inc.	Real Estate - Diversified	3.65B
HHS	Harte Hanks, Inc.	Conglomerates	60.82M
HI	Hillenbrand, Inc.	Specialty Industrial Machinery	3.00B
HIFS	Hingham Institution for Savings	Banks - Regional	529.74M
HIG	The Hartford Financial Services Group, Inc.	Insurance - Property & Casualty	32.80B
HIHO	Highway Holdings Limited	Metal Fabrication	8.23M
HII	Huntington Ingalls Industries, Inc.	Aerospace & Defense	10.95B
HIMS	Hims & Hers Health, Inc.	Household & Personal Products	4.45B
HIMX	Himax Technologies, Inc.	Semiconductors	1.19B
HIPO	Hippo Holdings Inc.	Insurance - Specialty	467.83M
HITI	High Tide Inc.	Pharmaceutical Retailers	148.01M
HIVE	HIVE Blockchain Technologies Ltd.	Capital Markets	378.12M
HIW	Highwoods Properties, Inc.	REIT - Office	3.22B
HKD	AMTD Digital Inc.	Software - Application	648.63M
HKIT	Hitek Global Inc.	Software - Application	20.58M
HL	Hecla Mining Company	Other Precious Metals & Mining	3.52B
HLF	Herbalife Nutrition Ltd.	Packaged Foods	1.22B
HLI	Houlihan Lokey, Inc.	Capital Markets	10.30B
HLIO	Helios Technologies, Inc.	Specialty Industrial Machinery	1.50B
HLIT	Harmonic Inc.	Communication Equipment	1.60B
HLLY	Holley Inc.	Auto Parts	456.36M
HLMN	Hillman Solutions Corp.	Tools & Accessories	1.97B
HLN	Haleon plc	Drug Manufacturers - Specialty & Generic	41.48B
HLNE	Hamilton Lane Incorporated	Asset Management	7.72B
HLP	Hongli Group Inc.	Steel	16.96M
HLT	Hilton Worldwide Holdings Inc.	Lodging	55.04B
HLVX	HilleVax, Inc.	Biotechnology	94.72M
HLX	Helix Energy Solutions Group, Inc.	Oil & Gas Equipment & Services	1.73B
HLXB	Helix Acquisition Corp. II	Shell Companies	236.67M
HMC	Honda Motor Co., Ltd.	Auto Manufacturers	50.75B
HMN	Horace Mann Educators Corporation	Insurance - Property & Casualty	1.42B
HMNF	HMN Financial, Inc.	Banks - Regional	118.32M
HMST	HomeStreet, Inc.	Banks - Regional	264.01M
HMY	Harmony Gold Mining Company Limited	Gold	5.69B
HNI	HNI Corporation	Business Equipment & Supplies	2.58B
HNNA	Hennessy Advisors, Inc.	Asset Management	62.73M
HNRA	HNR Acquisition Corp	Shell Companies	14.17M
HNRG	Hallador Energy Company	Thermal Coal	278.63M
HNST	The Honest Company, Inc.	Household & Personal Products	357.56M
HNVR	Hanover Bancorp, Inc.	Banks - Regional	127.66M
HOFT	Hooker Furnishings Corporation	Furnishings, Fixtures & Appliances	161.30M
HOFV	Hall of Fame Resort & Entertainment Company	Entertainment	18.94M
HOG	Harley-Davidson, Inc.	Recreational Vehicles	5.15B
HOLO	MicroCloud Hologram Inc.	Electronic Components	34.69M
HOLX	Hologic, Inc.	Medical Instruments & Supplies	19.04B
HOMB	Home Bancshares, Inc. (Conway, AR)	Banks - Regional	5.77B
HON	Honeywell International Inc.	Conglomerates	131.34B
HONE	HarborOne Bancorp, Inc.	Banks - Regional	601.33M
HOOD	Robinhood Markets, Inc.	Capital Markets	18.33B
HOOK	HOOKIPA Pharma Inc.	Biotechnology	55.37M
HOPE	Hope Bancorp, Inc.	Banks - Regional	1.60B
HOTH	Hoth Therapeutics, Inc.	Biotechnology	3.75M
HOUR	Hour Loop, Inc.	Internet Retail	34.76M
HOUS	Anywhere Real Estate Inc.	Real Estate Services	519.98M
HOV	Hovnanian Enterprises, Inc.	Residential Construction	1.23B
HOVR	New Horizon Aircraft Ltd.	Aerospace & Defense	13.08M
HOWL	Werewolf Therapeutics, Inc.	Biotechnology	113.42M
HP	Helmerich & Payne, Inc.	Oil & Gas Drilling	3.80B
HPCO	Hempacco Co., Inc.	Tobacco	2.80M
HPE	Hewlett Packard Enterprise Company	Communication Equipment	24.93B
HPH	Highest Performances Holdings Inc.	Asset Management	1.35B
HPK	HighPeak Energy, Inc.	Oil & Gas Exploration & Production	2.07B
HPP	Hudson Pacific Properties, Inc.	REIT - Office	825.70M
HPQ	HP Inc.	Computer Hardware	35.03B
HQI	HireQuest, Inc.	Staffing & Employment Services	188.72M
HQY	HealthEquity, Inc.	Health Information Services	6.84B
HR	Healthcare Realty Trust Incorporated	REIT - Healthcare Facilities	6.68B
HRB	H&R Block, Inc.	Personal Services	8.10B
HRI	Herc Holdings Inc.	Rental & Leasing Services	4.32B
HRL	Hormel Foods Corporation	Packaged Foods	17.44B
HRMY	Harmony Biosciences Holdings, Inc.	Biotechnology	1.92B
HROW	Harrow Health, Inc.	Drug Manufacturers - Specialty & Generic	850.40M
HRTG	Heritage Insurance Holdings, Inc.	Insurance - Property & Casualty	242.03M
HRTX	Heron Therapeutics, Inc.	Biotechnology	438.26M
HRYU	Hanryu Holdings, Inc.	Internet Content & Information	13.52M
HRZN	Horizon Technology Finance Corporation	Asset Management	455.21M
HSAI	Hesai Group	Auto Parts	550.62M
HSBC	HSBC Holdings plc	Banks - Diversified	161.53B
HSCS	Heart Test Laboratories, Inc.	Medical Devices	2.61M
HSDT	Helius Medical Technologies, Inc.	Medical Devices	2.07M
HSHP	Himalaya Shipping Ltd.	Marine Shipping	349.01M
HSIC	Henry Schein, Inc.	Medical Distribution	9.21B
HSII	Heidrick & Struggles International, Inc.	Staffing & Employment Services	811.86M
HSON	Hudson Global, Inc.	Staffing & Employment Services	50.49M
HSPO	Horizon Space Acquisition I Corp.	Shell Companies	86.86M
HST	Host Hotels & Resorts, Inc.	REIT - Hotel & Motel	12.51B
HSTM	HealthStream, Inc.	Health Information Services	890.35M
HSY	The Hershey Company	Confectioners	39.08B
HTBI	HomeTrust Bancshares, Inc.	Banks - Regional	605.16M
HTBK	Heritage Commerce Corp	Banks - Regional	645.02M
HTCR	HeartCore Enterprises, Inc.	Software - Application	14.60M
HTGC	Hercules Capital, Inc.	Asset Management	3.49B
HTH	Hilltop Holdings Inc.	Banks - Regional	2.18B
HTHT	H World Group Limited	Lodging	10.15B
HTLD	Heartland Express, Inc.	Trucking	1.05B
HTLF	Heartland Financial USA, Inc.	Banks - Regional	2.28B
HTOO	Fusion Fuel Green PLC	Utilities - Renewable	13.92M
HTZ	Hertz Global Holdings, Inc.	Rental & Leasing Services	1.15B
HUBB	Hubbell Incorporated	Electrical Equipment & Parts	20.06B
HUBC	HUB Cyber Security (Israel) Ltd.	Software - Infrastructure	7.35M
HUBG	Hub Group, Inc.	Integrated Freight & Logistics	2.85B
HUBS	HubSpot, Inc.	Software - Application	24.80B
HUDA	Hudson Acquisition I Corp.	Shell Companies	27.37M
HUDI	Huadi International Group Co., Ltd.	Steel	35.65M
HUGE	FSD Pharma Inc.	Drug Manufacturers - Specialty & Generic	4.47M
HUIZ	Huize Holding Limited	Insurance Brokers	46.74M
HUM	Humana Inc.	Healthcare Plans	48.79B
HUMA	Humacyte, Inc.	Biotechnology	953.86M
HUN	Huntsman Corporation	Chemicals	4.08B
HURC	Hurco Companies, Inc.	Specialty Industrial Machinery	116.80M
HURN	Huron Consulting Group Inc.	Consulting Services	2.04B
HUSA	Houston American Energy Corp.	Oil & Gas Exploration & Production	13.74M
HUT	Hut 8 Mining Corp.	Capital Markets	1.31B
HUYA	HUYA Inc.	Entertainment	980.09M
HVT	Haverty Furniture Companies, Inc.	Home Improvement Retail	460.18M
HVT.A	Haverty Furniture Companies, Inc.	Home Improvement Retail	447.72M
HWBK	Hawthorn Bancshares, Inc.	Banks - Regional	147.74M
HWC	Hancock Whitney Corporation	Banks - Regional	4.82B
HWH	HWH International Inc.	Leisure	13.79M
HWKN	Hawkins, Inc.	Specialty Chemicals	2.15B
HWM	Howmet Aerospace Inc.	Aerospace & Defense	38.41B
HXL	Hexcel Corporation	Aerospace & Defense	5.31B
HY	Hyster-Yale Materials Handling, Inc.	Farm & Heavy Construction Machinery	1.41B
HYAC	Haymaker Acquisition Corp. III	Shell Companies	312.61M
HYFM	Hydrofarm Holdings Group, Inc.	Farm & Heavy Construction Machinery	28.97M
HYLN	Hyliion Holdings Corp.	Auto Parts	389.84M
HYMC	Hycroft Mining Holding Corporation	Gold	58.90M
HYPR	Hyperfine, Inc.	Medical Devices	82.09M
HYZN	Hyzon Motors Inc.	Auto Parts	35.01M
HZO	MarineMax, Inc.	Specialty Retail	823.32M
IAC	IAC Inc.	Internet Content & Information	4.48B
IAG	IAMGOLD Corporation	Gold	1.97B
IART	Integra LifeSciences Holdings Corporation	Medical Devices	1.96B
IAS	Integral Ad Science Holding Corp.	Advertising Agencies	1.69B
IAUX	i-80 Gold Corp.	Gold	400.29M
IBAC	IB Acquisition Corp.	Shell Companies	157.65M
IBCP	Independent Bank Corporation	Banks - Regional	719.98M
IBEX	IBEX Limited	Information Technology Services	303.15M
IBIO	iBio, Inc.	Biotechnology	17.94M
IBKR	Interactive Brokers Group, Inc.	Capital Markets	12.98B
IBM	International Business Machines Corporation	Information Technology Services	174.57B
IBN	ICICI Bank Limited	Banks - Regional	101.63B
IBOC	International Bancshares Corporation	Banks - Regional	4.23B
IBP	Installed Building Products, Inc.	Residential Construction	7.51B
IBRX	ImmunityBio, Inc.	Biotechnology	3.65B
IBTA	Ibotta, Inc.	Software - Application	2.08B
IBTX	Independent Bank Group, Inc.	Banks - Regional	2.43B
ICAD	iCAD, Inc.	Medical Devices	37.10M
ICCC	ImmuCell Corporation	Biotechnology	32.58M
ICCH	ICC Holdings, Inc.	Insurance - Specialty	70.40M
ICCM	IceCure Medical Ltd	Medical Devices	34.27M
ICCT	iCoreConnect Inc.	Health Information Services	6.77M
ICD	Independence Contract Drilling, Inc.	Oil & Gas Drilling	21.76M
ICE	Intercontinental Exchange, Inc.	Financial Data & Stock Exchanges	87.04B
ICFI	ICF International, Inc.	Consulting Services	2.76B
ICG	Intchains Group Limited	Semiconductors	426.22M
ICHR	Ichor Holdings, Ltd.	Semiconductor Equipment & Materials	1.09B
ICL	ICL Group Ltd	Agricultural Inputs	5.50B
ICLK	iClick Interactive Asia Group Limited	Advertising Agencies	27.66M
ICLR	ICON PLC	Diagnostics & Research	27.28B
ICMB	Investcorp Credit Management BDC, Inc.	Asset Management	48.48M
ICON	Icon Energy Corp.	Marine Shipping	5.13M
ICU	SeaStar Medical Holding Corporation	Biotechnology	35.02M
ICUI	ICU Medical, Inc.	Medical Instruments & Supplies	3.09B
IDA	IDACORP, Inc.	Utilities - Regulated Electric	5.23B
IDAI	T Stamp Inc.	Software - Application	4.47M
IDCC	InterDigital, Inc.	Software - Application	3.06B
IDN	Intellicheck, Inc.	Software - Application	58.99M
IDR	Idaho Strategic Resources, Inc.	Gold	138.80M
IDT	IDT Corporation	Telecom Services	956.79M
IDXX	IDEXX Laboratories, Inc.	Diagnostics & Research	39.15B
IDYA	IDEAYA Biosciences, Inc.	Biotechnology	3.58B
IE	Ivanhoe Electric Inc.	Copper	1.12B
IEP	Icahn Enterprises L.P.	Oil & Gas Refining & Marketing	7.82B
IESC	IES Holdings, Inc.	Engineering & Construction	2.84B
IEX	IDEX Corporation	Specialty Industrial Machinery	15.57B
IFBD	Infobird Co., Ltd	Software - Application	4.81M
IFF	International Flavors & Fragrances Inc.	Specialty Chemicals	25.65B
IFIN	InFinT Acquisition Corporation	Shell Companies	124.32M
IFRX	InflaRx N.V.	Biotechnology	88.91M
IFS	Intercorp Financial Services Inc.	Banks - Regional	2.58B
IGC	IGC Pharma Inc	Biotechnology	34.83M
IGIC	International General Insurance Holdings Ltd.	Insurance - Diversified	807.22M
IGMS	IGM Biosciences, Inc.	Biotechnology	643.09M
IGT	International Game Technology PLC	Gambling	4.52B
IGTA	Inception Growth Acquisition Limited	Shell Companies	63.60M
IH	iHuman Inc.	Education & Training Services	84.24M
IHG	InterContinental Hotels Group PLC	Lodging	16.68B
IHRT	iHeartMedia, Inc.	Broadcasting	203.70M
IHS	IHS Holding Limited	Telecom Services	959.25M
IHT	InnSuites Hospitality Trust	REIT - Hotel & Motel	14.17M
III	Information Services Group, Inc.	Information Technology Services	171.79M
IIIN	Insteel Industries, Inc.	Metal Fabrication	665.21M
IIIV	i3 Verticals, Inc.	Software - Infrastructure	584.33M
IINN	Inspira Technologies Oxy B.H.N. Ltd.	Medical Devices	20.93M
IIPR	Innovative Industrial Properties, Inc.	REIT - Industrial	3.49B
IKNA	Ikena Oncology, Inc.	Biotechnology	81.07M
IKT	Inhibikase Therapeutics, Inc.	Biotechnology	10.90M
ILAG	Intelligent Living Application Group Inc.	Building Products & Equipment	15.30M
ILMN	Illumina, Inc.	Diagnostics & Research	19.51B
ILPT	Industrial Logistics Properties Trust	REIT - Industrial	336.73M
IMAB	I-Mab	Biotechnology	104.02M
IMAQ	International Media Acquisition Corp.	Shell Companies	86.58M
IMAX	IMAX Corporation	Entertainment	1.08B
IMCC	IM Cannabis Corp.	Drug Manufacturers - Specialty & Generic	5.94M
IMCR	Immunocore Holdings plc	Biotechnology	1.97B
IMKTA	Ingles Markets, Incorporated	Grocery Stores	1.50B
IMMP	Immutep Limited	Biotechnology	270.94M
IMMR	Immersion Corporation	Software - Application	391.18M
IMMX	Immix Biopharma, Inc.	Biotechnology	58.90M
IMNM	Immunome, Inc.	Biotechnology	915.13M
IMNN	Imunon, Inc.	Biotechnology	28.11M
IMO	Imperial Oil Limited	Oil & Gas Integrated	37.13B
IMOS	ChipMOS TECHNOLOGIES INC.	Semiconductors	862.87M
IMPP	Imperial Petroleum Inc.	Oil & Gas Midstream	114.57M
IMRN	Immuron Limited	Biotechnology	16.56M
IMRX	Immuneering Corporation	Biotechnology	33.80M
IMTE	Integrated Media Technology Limited	Electronic Components	3.76M
IMTX	Immatics N.V.	Biotechnology	1.23B
IMUX	Immunic, Inc.	Biotechnology	126.11M
IMVT	Immunovant, Inc.	Biotechnology	4.14B
IMXI	International Money Express, Inc.	Software - Infrastructure	707.63M
INAB	IN8bio, Inc.	Biotechnology	37.06M
INAQ	Insight Acquisition Corp.	Shell Companies	79.74M
INBK	First Internet Bancorp	Banks - Regional	328.92M
INBS	Intelligent Bio Solutions Inc.	Medical Devices	4.09M
INBX	Inhibrx, Inc.	Biotechnology	196.11M
INCR	InterCure Ltd.	Drug Manufacturers - Specialty & Generic	99.65M
INCY	Incyte Corporation	Biotechnology	13.00B
INDB	Independent Bank Corp.	Banks - Regional	2.70B
INDI	indie Semiconductor, Inc.	Semiconductor Equipment & Materials	1.01B
INDO	Indonesia Energy Corporation Limited	Oil & Gas Exploration & Production	22.75M
INDP	Indaptus Therapeutics, Inc.	Biotechnology	17.25M
INDV	Indivior PLC	Drug Manufacturers - Specialty & Generic	1.75B
INFA	Informatica Inc.	Software - Infrastructure	8.28B
INFN	Infinera Corporation	Communication Equipment	1.40B
INFU	InfuSystem Holdings, Inc.	Medical Instruments & Supplies	142.04M
INFY	Infosys Limited	Information Technology Services	93.73B
ING	ING Groep N.V.	Banks - Diversified	59.99B
INGN	Inogen, Inc.	Medical Devices	218.56M
INGR	Ingredion Incorporated	Packaged Foods	8.11B
INHD	Inno Holdings Inc.	Steel	15.02M
INKT	MiNK Therapeutics, Inc.	Biotechnology	32.09M
INLX	Intellinetics, Inc.	Software - Application	32.10M
INM	InMed Pharmaceuticals Inc.	Biotechnology	2.01M
INMB	INmune Bio, Inc.	Biotechnology	159.64M
INMD	InMode Ltd.	Medical Devices	1.54B
INN	Summit Hotel Properties, Inc.	REIT - Hotel & Motel	679.45M
INNV	InnovAge Holding Corp.	Medical Care Facilities	856.72M
INO	Inovio Pharmaceuticals, Inc.	Biotechnology	268.31M
INOD	Innodata Inc.	Information Technology Services	537.68M
INSE	Inspired Entertainment, Inc.	Gambling	240.47M
INSG	Inseego Corp.	Communication Equipment	109.50M
INSM	Insmed Incorporated	Biotechnology	11.99B
INSP	Inspire Medical Systems, Inc.	Medical Devices	4.13B
INST	Instructure Holdings, Inc.	Software - Application	3.40B
INSW	International Seaways, Inc.	Oil & Gas Midstream	2.76B
INTA	Intapp, Inc.	Software - Application	2.69B
INTC	Intel Corporation	Semiconductors	129.09B
INTE	Integral Acquisition Corporation 1	Shell Companies	45.01M
INTG	The InterGroup Corporation	Lodging	44.29M
INTJ	Intelligent Group Limited	Consulting Services	13.13M
INTR	Inter & Co, Inc.	Banks - Regional	2.68B
INTS	Intensity Therapeutics, Inc.	Biotechnology	65.55M
INTT	inTEST Corporation	Semiconductor Equipment & Materials	134.26M
INTU	Intuit Inc.	Software - Application	177.46B
INTZ	Intrusion Inc.	Software - Infrastructure	6.89M
INUV	Inuvo, Inc.	Software - Application	42.12M
INVA	Innoviva, Inc.	Biotechnology	1.18B
INVE	Identiv, Inc.	Computer Hardware	93.76M
INVH	Invitation Homes Inc.	REIT - Residential	21.16B
INVO	INVO Bioscience, Inc.	Medical Devices	3.62M
INVZ	Innoviz Technologies Ltd.	Auto Parts	130.75M
INZY	Inozyme Pharma, Inc.	Biotechnology	353.19M
IOBT	IO Biotech, Inc.	Biotechnology	85.97M
IONQ	IonQ, Inc.	Computer Hardware	1.64B
IONR	ioneer Ltd	Other Industrial Metals & Mining	212.19M
IONS	Ionis Pharmaceuticals, Inc.	Biotechnology	7.31B
IOR	Income Opportunity Realty Investors, Inc.	Mortgage Finance	65.25M
IOSP	Innospec Inc.	Specialty Chemicals	3.24B
IOT	Samsara Inc.	Software - Infrastructure	20.28B
IOVA	Iovance Biotherapeutics, Inc.	Biotechnology	2.51B
IP	International Paper Company	Packaging & Containers	16.09B
IPA	ImmunoPrecise Antibodies Ltd.	Biotechnology	21.84M
IPAR	Inter Parfums, Inc.	Household & Personal Products	4.44B
IPDN	Professional Diversity Network, Inc.	Staffing & Employment Services	5.72M
IPG	The Interpublic Group of Companies, Inc.	Advertising Agencies	11.88B
IPGP	IPG Photonics Corporation	Semiconductor Equipment & Materials	3.81B
IPHA	Innate Pharma S.A.	Biotechnology	174.04M
IPI	Intrepid Potash, Inc.	Agricultural Inputs	343.67M
IPSC	Century Therapeutics, Inc.	Biotechnology	186.75M
IPW	iPower Inc.	Internet Retail	47.98M
IPWR	Ideal Power Inc.	Electrical Equipment & Parts	56.94M
IPX	IperionX Limited	Other Industrial Metals & Mining	371.88M
IPXX	Inflection Point Acquisition Corp. II	Shell Companies	333.13M
IQ	iQIYI, Inc.	Entertainment	3.10B
IQV	IQVIA Holdings Inc.	Diagnostics & Research	44.15B
IR	Ingersoll Rand Inc.	Specialty Industrial Machinery	39.83B
IRAA	Iris Acquisition Corp	Shell Companies	79.27M
IRBT	iRobot Corporation	Furnishings, Fixtures & Appliances	324.53M
IRDM	Iridium Communications Inc.	Telecom Services	3.39B
IREN	Iris Energy Limited	Capital Markets	1.69B
IRIX	IRIDEX Corporation	Medical Devices	32.31M
IRM	Iron Mountain Incorporated	REIT - Specialty	29.55B
IRMD	IRadimed Corporation	Medical Devices	586.99M
IROH	Iron Horse Acquisitions Corp.	Shell Companies	89.56M
IRON	Disc Medicine, Inc.	Biotechnology	1.29B
IROQ	IF Bancorp, Inc.	Banks - Regional	57.66M
IRS	IRSA Inversiones y Representaciones SA	Real Estate Services	966.37M
IRT	Independence Realty Trust, Inc.	REIT - Residential	4.20B
IRTC	iRhythm Technologies, Inc.	Medical Devices	2.75B
IRWD	Ironwood Pharmaceuticals, Inc.	Drug Manufacturers - Specialty & Generic	1.10B
ISDR	Issuer Direct Corporation	Software - Application	36.27M
ISPC	iSpecimen Inc.	Diagnostics & Research	3.60M
ISPO	Inspirato Incorporated	Travel Services	32.06M
ISPR	Ispire Technology Inc.	Tobacco	423.62M
ISRG	Intuitive Surgical, Inc.	Medical Instruments & Supplies	155.82B
ISRL	Israel Acquisitions Corp	Shell Companies	141.98M
ISSC	Innovative Solutions and Support, Inc.	Aerospace & Defense	106.89M
ISTR	Investar Holding Corporation	Banks - Regional	184.64M
IT	Gartner, Inc.	Information Technology Services	39.06B
ITCI	Intra-Cellular Therapies, Inc.	Drug Manufacturers - Specialty & Generic	8.13B
ITGR	Integer Holdings Corporation	Medical Devices	4.13B
ITI	Iteris, Inc.	Communication Equipment	205.85M
ITIC	Investors Title Company	Insurance - Specialty	385.25M
ITOS	iTeos Therapeutics, Inc.	Biotechnology	624.20M
ITP	IT Tech Packaging, Inc.	Paper & Paper Products	2.44M
ITRG	Integra Resources Corp.	Other Precious Metals & Mining	80.32M
ITRI	Itron, Inc.	Scientific & Technical Instruments	4.69B
ITRM	Iterum Therapeutics plc	Biotechnology	20.23M
ITRN	Ituran Location and Control Ltd.	Scientific & Technical Instruments	534.28M
ITT	ITT Inc.	Specialty Industrial Machinery	11.55B
ITUB	Itaú Unibanco Holding S.A.	Banks - Regional	59.50B
ITW	Illinois Tool Works Inc.	Specialty Industrial Machinery	73.31B
IVA	Inventiva S.A.	Biotechnology	134.34M
IVAC	Intevac, Inc.	Specialty Industrial Machinery	101.82M
IVCA	Investcorp India Acquisition Corp	Shell Companies	185.18M
IVCB	Investcorp Europe Acquisition Corp I	Shell Companies	204.96M
IVCP	Swiftmerge Acquisition Corp.	Shell Companies	74.90M
IVDA	Iveda Solutions, Inc.	Security & Protection Services	7.49M
IVP	Inspire Veterinary Partners, Inc.	Personal Services	6.78M
IVR	Invesco Mortgage Capital Inc.	REIT - Mortgage	446.51M
IVT	InvenTrust Properties Corp.	REIT - Retail	1.85B
IVVD	Invivyd, Inc.	Biotechnology	139.00M
IVZ	Invesco Ltd.	Asset Management	7.76B
IX	ORIX Corporation	Financial Conglomerates	26.97B
IXAQ	IX Acquisition Corp.	Shell Companies	98.43M
IXHL	Incannex Healthcare Limited	Drug Manufacturers - Specialty & Generic	33.52M
IZEA	IZEA Worldwide, Inc.	Internet Content & Information	37.42M
IZM	ICZOOM Group Inc.	Electronics & Computer Distribution	22.19M
J	Jacobs Engineering Group Inc.	Engineering & Construction	18.39B
JACK	Jack in the Box Inc.	Restaurants	1.16B
JAGX	Jaguar Health, Inc.	Biotechnology	5.99M
JAKK	JAKKS Pacific, Inc.	Leisure	221.63M
JAMF	Jamf Holding Corp.	Software - Application	2.34B
JANX	Janux Therapeutics, Inc.	Biotechnology	2.17B
JAZZ	Jazz Pharmaceuticals plc	Biotechnology	7.05B
JBGS	JBG SMITH Properties	REIT - Office	1.51B
JBHT	J.B. Hunt Transport Services, Inc.	Integrated Freight & Logistics	17.87B
JBI	Janus International Group, Inc.	Building Products & Equipment	2.18B
JBL	Jabil Inc.	Electronic Components	12.44B
JBLU	JetBlue Airways Corporation	Airlines	2.34B
JBSS	Sanfilippo (John B.) & Son, Inc	Packaged Foods	1.19B
JBT	John Bean Technologies Corporation	Specialty Industrial Machinery	3.08B
JCI	Johnson Controls International plc	Building Products & Equipment	46.80B
JCSE	JE Cleantech Holdings Limited	Specialty Industrial Machinery	6.08M
JCTCF	Jewett-Cameron Trading Company Ltd.	Lumber & Wood Production	15.50M
JD	JD.com, Inc.	Internet Retail	35.85B
JDZG	Jiade Limited	Information Technology Services	14.05M
JEF	Jefferies Financial Group Inc.	Capital Markets	11.89B
JELD	JELD-WEN Holding, Inc.	Building Products & Equipment	1.45B
JEWL	Adamas One Corp.	Luxury Goods	11.06M
JFBR	Jeffs' Brands Ltd	Internet Retail	2.24M
JFIN	Jiayin Group Inc.	Internet Content & Information	292.21M
JFU	9F Inc.	Information Technology Services	23.78M
JG	Aurora Mobile Limited	Software - Infrastructure	17.40M
JHG	Janus Henderson Group plc	Asset Management	5.87B
JHX	James Hardie Industries plc	Building Materials	15.33B
JILL	J.Jill, Inc.	Apparel Retail	403.20M
JJSF	J&J Snack Foods Corp.	Packaged Foods	3.24B
JKHY	Jack Henry & Associates, Inc.	Information Technology Services	12.50B
JKS	JinkoSolar Holding Co., Ltd.	Solar	1.05B
JL	J-Long Group Limited	Apparel Manufacturing	14.92M
JLL	Jones Lang LaSalle Incorporated	Real Estate Services	11.86B
JMIA	Jumia Technologies AG	Internet Retail	1.23B
JMSB	John Marshall Bancorp, Inc.	Banks - Regional	272.37M
JNJ	Johnson & Johnson	Drug Manufacturers - General	386.83B
JNPR	Juniper Networks, Inc.	Communication Equipment	12.31B
JNVR	Janover Inc.	Software - Infrastructure	7.25M
JOB	GEE Group, Inc.	Staffing & Employment Services	35.45M
JOBY	Joby Aviation, Inc.	Airports & Air Services	4.33B
JOE	The St. Joe Company	Real Estate - Diversified	3.66B
JOUT	Johnson Outdoors Inc.	Leisure	430.80M
JPM	JPMorgan Chase & Co.	Banks - Diversified	615.23B
JRSH	Jerash Holdings (US), Inc.	Apparel Manufacturing	37.41M
JRVR	James River Group Holdings, Ltd.	Insurance - Specialty	329.46M
JSPR	Jasper Therapeutics, Inc.	Biotechnology	269.73M
JTAI	Jet.AI Inc.	Software - Application	5.18M
JUNE	Junee Limited	Engineering & Construction	64.66M
JVA	Coffee Holding Co., Inc.	Packaged Foods	13.93M
JVSA	JVSPAC Acquisition Corp.	Shell Companies	78.48M
JWEL	Jowell Global Ltd.	Internet Retail	3.06M
JWN	Nordstrom, Inc.	Department Stores	3.66B
JWSM	Jaws Mustang Acquisition Corporation	Shell Companies	299.32M
JXJT	JX Luxventure Limited	Apparel Manufacturing	9.93M
JXN	Jackson Financial Inc.	Insurance - Life	6.74B
JYD	Jayud Global Logistics Limited	Integrated Freight & Logistics	14.26M
JYNT	The Joint Corp.	Medical Care Facilities	213.75M
JZ	Jianzhi Education Technology Group Company Limited	Education & Training Services	16.15M
JZXN	Jiuzi Holdings, Inc.	Auto & Truck Dealerships	21.02M
K	Kellanova Co	Packaged Foods	19.64B
KA	Kineta, Inc.	Biotechnology	7.97M
KACL	Kairous Acquisition Corp. Limited	Shell Companies	44.39M
KAI	Kadant Inc.	Specialty Industrial Machinery	4.19B
KALA	Kala Pharmaceuticals, Inc.	Biotechnology	30.72M
KALU	Kaiser Aluminum Corporation	Aluminum	1.26B
KALV	KalVista Pharmaceuticals, Inc.	Biotechnology	604.71M
KAR	Openlane Inc.	Auto & Truck Dealerships	1.93B
KARO	Karooooo Ltd.	Software - Application	1.08B
KAVL	Kaival Brands Innovations Group, Inc.	Tobacco	7.33M
KB	KB Financial Group Inc.	Banks - Regional	24.83B
KBDC	Kayne Anderson BDC, Inc.	null	1.15B
KBH	KB Home	Residential Construction	6.40B
KBR	KBR, Inc.	Engineering & Construction	8.81B
KC	Kingsoft Cloud Holdings Limited	Software - Application	624.26M
KCGI	Kensington Capital Acquisition Corp. V	Shell Companies	127.36M
KD	Kyndryl Holdings, Inc.	Information Technology Services	6.21B
KDLY	Kindly MD, Inc.	Medical Care Facilities	9.27M
KDP	Keurig Dr Pepper Inc.	Beverages - Non-Alcoholic	46.24B
KE	Kimball Electronics, Inc.	Electrical Equipment & Parts	583.51M
KELYA	Kelly Services, Inc.	Staffing & Employment Services	832.69M
KELYB	Kelly Services, Inc.	Staffing & Employment Services	813.19M
KEN	Kenon Holdings Ltd.	Utilities - Independent Power Producers	1.25B
KEP	Korea Electric Power Corporation	Utilities - Regulated Electric	9.19B
KEQU	Kewaunee Scientific Corporation	Furnishings, Fixtures & Appliances	153.02M
KEX	Kirby Corporation	Marine Shipping	7.03B
KEY	KeyCorp	Banks - Regional	15.40B
KEYS	Keysight Technologies, Inc.	Scientific & Technical Instruments	23.78B
KFFB	Kentucky First Federal Bancorp	Banks - Regional	27.94M
KFRC	Kforce Inc.	Staffing & Employment Services	1.33B
KFS	Kingsway Financial Services Inc.	Auto & Truck Dealerships	242.36M
KFY	Korn Ferry	Staffing & Employment Services	3.77B
KGC	Kinross Gold Corporation	Gold	10.67B
KGEI	Kolibri Global Energy Inc.	Oil & Gas Exploration & Production	116.50M
KGS	Kodiak Gas Services, Inc.	Oil & Gas Equipment & Services	2.37B
KHC	The Kraft Heinz Company	Packaged Foods	41.03B
KIDS	OrthoPediatrics Corp.	Medical Devices	774.20M
KIM	Kimco Realty Corporation	REIT - Retail	14.68B
KIND	Nextdoor Holdings, Inc.	Internet Content & Information	1.11B
KINS	Kingstone Companies, Inc.	Insurance - Property & Casualty	84.64M
KIRK	Kirkland's, Inc.	Home Improvement Retail	23.46M
KITT	Nauticus Robotics, Inc.	Aerospace & Defense	12.87M
KKR	KKR & Co. Inc.	Asset Management	106.04B
KLAC	KLA Corporation	Semiconductor Equipment & Materials	103.17B
KLG	WK Kellogg Co	Packaged Foods	1.50B
KLIC	Kulicke and Soffa Industries, Inc.	Semiconductor Equipment & Materials	2.49B
KLTR	Kaltura, Inc.	Software - Application	193.19M
KLXE	KLX Energy Services Holdings, Inc.	Oil & Gas Equipment & Services	109.58M
KMB	Kimberly-Clark Corporation	Household & Personal Products	45.98B
KMDA	Kamada Ltd.	Drug Manufacturers - Specialty & Generic	334.79M
KMI	Kinder Morgan, Inc.	Oil & Gas Midstream	47.65B
KMPR	Kemper Corporation	Insurance - Property & Casualty	4.21B
KMT	Kennametal Inc.	Tools & Accessories	2.05B
KMX	CarMax, Inc.	Auto & Truck Dealerships	12.97B
KN	Knowles Corporation	Communication Equipment	1.62B
KNDI	Kandi Technologies Group, Inc.	Auto Parts	165.14M
KNF	Knife River Corporation	Building Materials	4.57B
KNOP	KNOT Offshore Partners LP	Marine Shipping	249.21M
KNSA	Kiniksa Pharmaceuticals, Ltd.	Biotechnology	1.86B
KNSL	Kinsale Capital Group, Inc.	Insurance - Property & Casualty	10.65B
KNTK	Kinetik Holdings Inc.	Oil & Gas Midstream	2.47B
KNW	Know Labs, Inc.	Scientific & Technical Instruments	28.83M
KNX	Knight-Swift Transportation Holdings Inc.	Trucking	8.74B
KO	The Coca-Cola Company	Beverages - Non-Alcoholic	290.72B
KOD	Kodiak Sciences Inc.	Biotechnology	149.72M
KODK	Eastman Kodak Company	Specialty Business Services	448.16M
KOF	Coca-Cola FEMSA, SAB de CV	Beverages - Non-Alcoholic	4.68B
KOP	Koppers Holdings Inc.	Specialty Chemicals	837.83M
KOPN	Kopin Corporation	Electronic Components	117.26M
KORE	KORE Group Holdings, Inc.	Telecom Services	50.10M
KOS	Kosmos Energy Ltd.	Oil & Gas Exploration & Production	2.58B
KOSS	Koss Corporation	Consumer Electronics	82.18M
KPLT	Katapult Holdings, Inc.	Software - Infrastructure	84.49M
KPRX	Kiora Pharmaceuticals, Inc.	Biotechnology	13.25M
KPTI	Karyopharm Therapeutics Inc.	Biotechnology	133.34M
KR	The Kroger Co.	Grocery Stores	39.43B
KRC	Kilroy Realty Corporation	REIT - Office	4.28B
KREF	KKR Real Estate Finance Trust Inc.	REIT - Mortgage	802.88M
KRG	Kite Realty Group Trust	REIT - Retail	5.48B
KRKR	36Kr Holdings Inc.	Internet Content & Information	10.31M
KRMD	KORU Medical Systems, Inc.	Medical Instruments & Supplies	107.55M
KRNL	Kernel Group Holdings, Inc.	Shell Companies	86.48M
KRNT	Kornit Digital Ltd.	Specialty Industrial Machinery	739.90M
KRNY	Kearny Financial Corp.	Banks - Regional	454.60M
KRO	Kronos Worldwide, Inc.	Specialty Chemicals	1.37B
KRON	Kronos Bio, Inc.	Biotechnology	76.92M
KROS	Keros Therapeutics, Inc.	Biotechnology	1.88B
KRP	Kimbell Royalty Partners, LP	Oil & Gas Exploration & Production	1.92B
KRRO	Korro Bio, Inc.	Biotechnology	435.09M
KRT	Karat Packaging Inc.	Packaging & Containers	584.87M
KRUS	Kura Sushi USA, Inc.	Restaurants	633.77M
KRYS	Krystal Biotech, Inc.	Biotechnology	5.82B
KSCP	Knightscope, Inc.	Security & Protection Services	31.15M
KSPI	Kaspi.kz JSC	Software - Infrastructure	24.95B
KSS	Kohl's Corporation	Department Stores	2.34B
KT	KT Corporation	Telecom Services	6.93B
KTB	Kontoor Brands, Inc.	Apparel Manufacturing	3.87B
KTCC	Key Tronic Corporation	Computer Hardware	41.97M
KTOS	Kratos Defense & Security Solutions, Inc.	Aerospace & Defense	3.35B
KTRA	Kintara Therapeutics, Inc.	Biotechnology	11.89M
KTTA	Pasithea Therapeutics Corp.	Biotechnology	5.29M
KUKE	Kuke Music Holding Limited	Entertainment	40.84M
KULR	KULR Technology Group, Inc.	Electronic Components	52.72M
KURA	Kura Oncology, Inc.	Biotechnology	1.59B
KVAC	Keen Vision Acquisition Corporation	Shell Companies	207.22M
KVHI	KVH Industries, Inc.	Communication Equipment	90.30M
KVUE	Kenvue Inc.	Household & Personal Products	35.60B
KVYO	Klaviyo, Inc.	Software - Infrastructure	6.72B
KW	Kennedy-Wilson Holdings, Inc.	Real Estate Services	1.43B
KWE	KWESST Micro Systems Inc.	Aerospace & Defense	3.21M
KWR	Quaker Chemical Corporation	Specialty Chemicals	3.25B
KXIN	Kaixin Auto Holdings	Auto & Truck Dealerships	5.59M
KYMR	Kymera Therapeutics, Inc.	Biotechnology	2.63B
KYTX	Kyverna Therapeutics, Inc.	Biotechnology	383.29M
KZIA	Kazia Therapeutics Limited	Biotechnology	8.64M
KZR	Kezar Life Sciences, Inc.	Biotechnology	47.32M
L	Loews Corporation	Insurance - Property & Casualty	17.88B
LAAC	Lithium Americas (Argentina) Corp.	Other Industrial Metals & Mining	484.41M
LAB	Standard BioTools Inc.	Medical Devices	831.60M
LAC	Lithium Americas Corp.	Other Industrial Metals & Mining	566.38M
LAD	Lithia Motors, Inc.	Auto & Truck Dealerships	7.28B
LADR	Ladder Capital Corp	REIT - Mortgage	1.58B
LAES	SEALSQ Corp	Semiconductors	20.46M
LAKE	Lakeland Industries, Inc.	Apparel Manufacturing	181.42M
LAMR	Lamar Advertising Company	REIT - Specialty	12.19B
LANC	Lancaster Colony Corporation	Packaged Foods	5.25B
LAND	Gladstone Land Corporation	REIT - Specialty	532.20M
LANV	Lanvin Group Holdings Limited	Luxury Goods	214.63M
LARK	Landmark Bancorp, Inc.	Banks - Regional	109.75M
LASE	Laser Photonics Corporation	Specialty Industrial Machinery	19.88M
LASR	nLIGHT, Inc.	Semiconductors	564.12M
LATG	Chenghe Acquisition I Co.	Shell Companies	82.35M
LAUR	Laureate Education, Inc.	Education & Training Services	2.39B
LAW	CS Disco, Inc.	Software - Application	360.46M
LAZ	Lazard Ltd	Capital Markets	4.37B
LAZR	Luminar Technologies, Inc.	Auto Parts	730.60M
LB	LandBridge Company LLC	Apparel Retail	550.39M
LBPH	Longboard Pharmaceuticals, Inc.	Biotechnology	1.31B
LBRDA	Liberty Broadband Corporation	Telecom Services	9.60B
LBRDK	Liberty Broadband Corporation	Telecom Services	9.61B
LBRT	Liberty Energy Inc.	Oil & Gas Equipment & Services	3.86B
LBTYA	Liberty Global plc	Telecom Services	7.36B
LBTYB	Liberty Global plc	Telecom Services	7.16B
LBTYK	Liberty Global plc	Telecom Services	7.40B
LC	LendingClub Corporation	Credit Services	1.22B
LCFY	Locafy Limited	Internet Content & Information	6.07M
LCID	Lucid Group, Inc.	Auto Manufacturers	7.86B
LCII	LCI Industries	Recreational Vehicles	2.94B
LCNB	LCNB Corp.	Banks - Regional	209.32M
LCTX	Lineage Cell Therapeutics, Inc.	Biotechnology	190.71M
LCUT	Lifetime Brands, Inc.	Furnishings, Fixtures & Appliances	185.86M
LCW	Learn CW Investment Corporation	Shell Companies	165.67M
LDI	loanDepot, Inc.	Mortgage Finance	640.71M
LDOS	Leidos Holdings, Inc.	Information Technology Services	20.10B
LDTC	LeddarTech Holdings Inc.	Software - Application	18.63M
LDWY	Lendway, Inc.	Advertising Agencies	7.86M
LE	Lands' End, Inc.	Apparel Retail	556.52M
LEA	Lear Corporation	Auto Parts	6.80B
LECO	Lincoln Electric Holdings, Inc.	Tools & Accessories	11.88B
LEDS	SemiLEDs Corporation	Semiconductors	10.36M
LEE	Lee Enterprises, Incorporated	Publishing	62.07M
LEG	Leggett & Platt, Incorporated	Furnishings, Fixtures & Appliances	1.79B
LEGH	Legacy Housing Corporation	Residential Construction	682.44M
LEGN	Legend Biotech Corporation	Biotechnology	10.29B
LEGT	Legato Merger Corp. III	Shell Companies	262.40M
LEN	Lennar Corporation	Residential Construction	48.95B
LEN.B	Lennar Corporation	Residential Construction	48.71B
LENZ	LENZ Therapeutics, Inc.	Biotechnology	620.49M
LESL	Leslie's, Inc.	Specialty Retail	557.92M
LEU	Centrus Energy Corp.	Uranium	642.05M
LEV	The Lion Electric Company	Farm & Heavy Construction Machinery	192.29M
LEVI	Levi Strauss & Co.	Apparel Manufacturing	7.24B
LEXX	Lexaria Bioscience Corp.	Biotechnology	54.55M
LFCR	Lifecore Biomedical, Inc.	Drug Manufacturers - Specialty & Generic	200.56M
LFLY	Leafly Holdings, Inc.	Pharmaceutical Retailers	5.45M
LFMD	LifeMD, Inc.	Health Information Services	281.23M
LFST	LifeStance Health Group, Inc.	Medical Care Facilities	2.12B
LFT	Lument Finance Trust, Inc.	REIT - Mortgage	137.44M
LFUS	Littelfuse, Inc.	Electronic Components	6.37B
LFVN	LifeVantage Corporation	Packaged Foods	106.81M
LFWD	ReWalk Robotics Ltd.	Medical Devices	39.31M
LGCB	Linkage Global Inc	Internet Retail	59.56M
LGCL	Lucas GC Limited	Software - Application	192.73M
LGF.A	Lions Gate Entertainment Corp.	Entertainment	1.91B
LGF.B	Lions Gate Entertainment Corp.	Entertainment	1.87B
LGHL	Lion Group Holding Ltd.	Capital Markets	1.33M
LGIH	LGI Homes, Inc.	Residential Construction	2.66B
LGL	The LGL Group, Inc.	Electronic Components	29.01M
LGMK	LogicMark, Inc.	Health Information Services	1.20M
LGND	Ligand Pharmaceuticals Incorporated	Biotechnology	1.94B
LGO	Largo Inc.	Other Industrial Metals & Mining	129.43M
LGVN	Longeveron Inc.	Biotechnology	47.96M
LH	Labcorp Holdings Inc.	Diagnostics & Research	17.91B
LHX	L3Harris Technologies, Inc.	Aerospace & Defense	42.41B
LI	Li Auto Inc.	Auto Manufacturers	18.47B
LICN	Lichen China Limited	Specialty Business Services	80.40M
LICY	Li-Cycle Holdings Corp.	Waste Management	78.12M
LIDR	AEye, Inc.	Software - Infrastructure	11.89M
LIF	Life360, Inc.	Software - Application	2.34B
LIFW	MSP Recovery, Inc.	Health Information Services	52.40M
LII	Lennox International Inc.	Building Products & Equipment	20.38B
LILA	Liberty Latin America Ltd.	Telecom Services	2.06B
LILAK	Liberty Latin America Ltd.	Telecom Services	2.06B
LILM	Lilium N.V.	Aerospace & Defense	512.63M
LIN	Linde plc	Specialty Chemicals	218.01B
LINC	Lincoln Educational Services Corporation	Education & Training Services	437.07M
LIND	Lindblad Expeditions Holdings, Inc.	Travel Services	478.59M
LINE	Lineage, Inc.	REIT - Industrial	20.33B
LINK	Interlink Electronics, Inc.	Electronic Components	40.43M
LION	Lionsgate Studios Corp.	Shell Companies	2.13B
LIPO	Lipella Pharmaceuticals Inc.	Biotechnology	6.31M
LIQT	LiqTech International, Inc.	Pollution & Treatment Controls	13.55M
LITB	LightInTheBox Holding Co., Ltd.	Internet Retail	63.08M
LITE	Lumentum Holdings Inc.	Communication Equipment	3.37B
LITM	Snow Lake Resources Ltd.	Other Industrial Metals & Mining	13.98M
LIVE	Live Ventures Incorporated	Home Improvement Retail	58.38M
LIVN	LivaNova PLC	Medical Devices	2.79B
LIXT	Lixte Biotechnology Holdings, Inc.	Biotechnology	4.95M
LKCO	Luokung Technology Corp.	Software - Application	8.95M
LKFN	Lakeland Financial Corporation	Banks - Regional	1.77B
LKQ	LKQ Corporation	Auto Parts	10.70B
LL	LL Flooring Holdings, Inc.	Home Improvement Retail	27.56M
LLAP	Terran Orbital Corporation	Aerospace & Defense	147.02M
LLY	Eli Lilly and Company	Drug Manufacturers - General	746.38B
LLYVA	Liberty Live Group - Series A	Entertainment	3.38B
LLYVK	Liberty Live Group - Series C	Entertainment	3.45B
LMAT	LeMaitre Vascular, Inc.	Medical Instruments & Supplies	1.96B
LMB	Limbach Holdings, Inc.	Building Products & Equipment	660.47M
LMFA	LM Funding America, Inc.	Credit Services	8.79M
LMND	Lemonade, Inc.	Insurance - Property & Casualty	1.59B
LMNR	Limoneira Company	Farm Products	396.42M
LMT	Lockheed Martin Corporation	Aerospace & Defense	126.93B
LNC	Lincoln National Corporation	Insurance - Life	5.70B
LND	BrasilAgro - Companhia Brasileira de Propriedades Agrícolas	Farm Products	460.21M
LNG	Cheniere Energy, Inc.	Oil & Gas Midstream	41.22B
LNKB	LINKBANCORP, Inc.	Banks - Regional	258.51M
LNN	Lindsay Corporation	Farm & Heavy Construction Machinery	1.36B
LNSR	LENSAR, Inc.	Medical Devices	57.92M
LNT	Alliant Energy Corporation	Utilities - Regulated Electric	14.35B
LNTH	Lantheus Holdings, Inc.	Drug Manufacturers - Specialty & Generic	7.52B
LNW	Light & Wonder, Inc.	Gambling	9.44B
LNZA	LanzaTech Global, Inc.	Waste Management	388.55M
LOAN	Manhattan Bridge Capital, Inc.	REIT - Mortgage	62.23M
LOAR	Loar Holdings Inc.	Aerospace & Defense	5.35B
LOB	Live Oak Bancshares, Inc.	Banks - Regional	2.01B
LOBO	LOBO EV TECHNOLOGIES LTD.	Auto Manufacturers	21.19M
LOCL	Local Bounti Corporation	Farm Products	23.94M
LOCO	El Pollo Loco Holdings, Inc.	Restaurants	369.48M
LODE	Comstock Inc.	Other Precious Metals & Mining	24.56M
LOGC	ContextLogic Inc	Internet Retail	140.10M
LOGI	Logitech International S.A.	Computer Hardware	13.59B
LOMA	Loma Negra Compañía Industrial Argentina SA	Building Materials	1.10B
LOOP	Loop Industries, Inc.	Specialty Chemicals	83.19M
LOPE	Grand Canyon Education, Inc.	Education & Training Services	4.61B
LOT	Lotus Technology Inc.	Auto Manufacturers	4.04B
LOVE	The Lovesac Company	Furnishings, Fixtures & Appliances	423.13M
LOW	Lowe's Companies, Inc.	Home Improvement Retail	136.58B
LPA	Logistic Properties of the Americas	Real Estate - Development	516.87M
LPAA	Launch One Acquisition Corp.	Shell Companies	249.25M
LPCN	Lipocine Inc.	Biotechnology	26.63M
LPG	Dorian LPG Ltd.	Oil & Gas Midstream	1.69B
LPL	LG Display Co., Ltd.	Consumer Electronics	4.03B
LPLA	LPL Financial Holdings Inc.	Capital Markets	16.19B
LPRO	Open Lending Corporation	Credit Services	744.19M
LPSN	LivePerson, Inc.	Software - Application	116.97M
LPTH	LightPath Technologies, Inc.	Electronic Components	52.78M
LPTV	Loop Media, Inc.	Broadcasting	10.05M
LPTX	Leap Therapeutics, Inc.	Biotechnology	81.89M
LPX	Louisiana-Pacific Corporation	Building Products & Equipment	7.04B
LQDA	Liquidia Corporation	Biotechnology	876.85M
LQDT	Liquidity Services, Inc.	Internet Retail	678.08M
LQR	LQR House Inc.	Beverages - Wineries & Distilleries	3.71M
LRCX	Lam Research Corporation	Semiconductor Equipment & Materials	113.77B
LRE	Lead Real Estate Co., Ltd	Real Estate - Development	28.65M
FTK	Flotek Industries, Inc.	Oil & Gas Equipment & Services	131.97M
FTLF	FitLife Brands, Inc.	Packaged Foods	148.75M
FTNT	Fortinet, Inc.	Software - Infrastructure	43.66B
FTRE	Fortrea Holdings Inc.	Biotechnology	2.46B
FTS	Fortis Inc.	Utilities - Regulated Electric	20.43B
FTV	Fortive Corporation	Scientific & Technical Instruments	24.88B
FUBO	fuboTV Inc.	Broadcasting	424.33M
FUFU	BitFuFu Inc.	Capital Markets	117.75M
FUL	H.B. Fuller Company	Specialty Chemicals	4.68B
FULC	Fulcrum Therapeutics, Inc.	Biotechnology	525.82M
FULT	Fulton Financial Corporation	Banks - Regional	3.58B
FUN	Six Flags Entertainment Corp.	Leisure	4.74B
FUNC	First United Corporation	Banks - Regional	186.85M
FURY	Fury Gold Mines Limited	Other Industrial Metals & Mining	58.27M
FUSB	First US Bancshares, Inc.	Banks - Regional	58.88M
FUTU	Futu Holdings Limited	Capital Markets	2.68B
FVCB	FVCBankcorp, Inc.	Banks - Regional	223.91M
FVRR	Fiverr International Ltd.	Internet Content & Information	843.51M
FWONA	Formula One Group - Series A	Entertainment	29.73B
FWONK	Formula One Group - Series C	Entertainment	29.84B
FWRD	Forward Air Corporation	Integrated Freight & Logistics	650.25M
FWRG	First Watch Restaurant Group, Inc.	Restaurants	944.53M
FXNC	First National Corporation	Banks - Regional	108.60M
FYBR	Frontier Communications Parent, Inc.	Telecom Services	7.14B
G	Genpact Limited	Information Technology Services	6.30B
GABC	German American Bancorp, Inc.	Banks - Regional	1.20B
GAIA	Gaia, Inc.	Entertainment	118.87M
GAIN	Gladstone Investment Corporation	Asset Management	518.04M
GALT	Galectin Therapeutics Inc.	Biotechnology	153.51M
GAMB	Gambling.com Group Limited	Gambling	349.66M
GAMC	Golden Arrow Merger Corp.	Shell Companies	83.88M
GAME	GameSquare Holdings Inc	Electronic Gaming & Multimedia	14.16M
GAN	GAN Limited	Gambling	70.35M
GANX	Gain Therapeutics, Inc.	Biotechnology	19.90M
GAQ	Generation Asia I Acquisition Limited	Shell Companies	87.81M
GASS	StealthGas Inc.	Marine Shipping	239.96M
GATE	Marblegate Acquisition Corp.	Shell Companies	127.52M
GATO	Gatos Silver, Inc.	Other Precious Metals & Mining	835.71M
GATX	GATX Corporation	Rental & Leasing Services	4.93B
GAU	Galiano Gold Inc.	Gold	440.91M
GAUZ	Gauzy Ltd.	Tools & Accessories	190.54M
GB	Global Blue Group Holding AG	Software - Infrastructure	900.74M
GBBK	Global Blockchain Acquisition Corp.	Shell Companies	60.65M
GBCI	Glacier Bancorp, Inc.	Banks - Regional	5.07B
GBDC	Golub Capital BDC, Inc.	Asset Management	4.07B
GBIO	Generation Bio Co.	Biotechnology	206.90M
GBLI	Global Indemnity Group, LLC	Insurance - Property & Casualty	425.00M
GBNY	Generations Bancorp NY, Inc.	Banks - Regional	23.68M
GBR	New Concept Energy, Inc.	Real Estate Services	6.95M
GBTG	Global Business Travel Group, Inc.	Software - Application	3.19B
GBX	The Greenbrier Companies, Inc.	Railroads	1.59B
GCBC	Greene County Bancorp, Inc.	Banks - Regional	608.71M
GCI	Gannett Co., Inc.	Publishing	705.28M
GCMG	GCM Grosvenor Inc	Asset Management	2.11B
GCO	Genesco Inc.	Apparel Retail	359.77M
GCT	GigaCloud Technology Inc.	Software - Infrastructure	1.17B
GCTK	GlucoTrack, Inc.	Medical Instruments & Supplies	7.34M
GCTS	GCT Semiconductor Holding, Inc.	Semiconductors	213.39M
GD	General Dynamics Corporation	Aerospace & Defense	80.24B
GDC	GD Culture Group Limited	Electronic Gaming & Multimedia	11.59M
GDDY	GoDaddy Inc.	Software - Infrastructure	20.29B
GDEN	Golden Entertainment, Inc.	Resorts & Casinos	945.32M
GDEV	GDEV Inc.	Electronic Gaming & Multimedia	470.77M
GDHG	Golden Heaven Group Holdings Ltd.	Leisure	7.46M
GDOT	Green Dot Corporation	Credit Services	510.28M
GDRX	GoodRx Holdings, Inc.	Health Information Services	3.24B
GDS	GDS Holdings Limited	Information Technology Services	1.99B
GDST	Goldenstone Acquisition Limited	Shell Companies	39.24M
GDTC	CytoMed Therapeutics Limited	Biotechnology	20.84M
GDYN	Grid Dynamics Holdings, Inc.	Information Technology Services	984.06M
GE	GE Aerospace	Aerospace & Defense	183.54B
GECC	Great Elm Capital Corp.	Asset Management	112.75M
GEF	Greif, Inc.	Packaging & Containers	3.18B
GEF.B	Greif, Inc.	Packaging & Containers	3.20B
GEG	Great Elm Group, Inc.	Asset Management	57.85M
GEHC	GE HealthCare Technologies Inc.	Health Information Services	37.31B
GEL	Genesis Energy, L.P.	Oil & Gas Midstream	1.72B
GEN	Gen Digital Inc.	Software - Infrastructure	16.23B
GENC	Gencor Industries, Inc.	Farm & Heavy Construction Machinery	343.14M
GENE	Genetic Technologies Limited	Diagnostics & Research	3.98M
GENI	Genius Sports Limited	Internet Content & Information	1.38B
GENK	GEN Restaurant Group, Inc.	Restaurants	37.00M
GEO	The GEO Group, Inc.	Security & Protection Services	1.96B
GEOS	Geospace Technologies Corporation	Oil & Gas Equipment & Services	115.78M
GERN	Geron Corporation	Biotechnology	2.78B
GES	Guess', Inc.	Apparel Retail	1.27B
GETY	Getty Images Holdings, Inc.	Internet Content & Information	1.50B
GEV	GE Vernova Inc.	Utilities - Renewable	45.02B
GEVO	Gevo, Inc.	Specialty Chemicals	140.51M
GFAI	Guardforce AI Co., Limited	Security & Protection Services	19.96M
GFF	Griffon Corporation	Conglomerates	3.67B
GFI	Gold Fields Limited	Gold	14.62B
GFL	GFL Environmental Inc.	Waste Management	14.07B
GFR	Greenfire Resources Ltd	Oil & Gas Exploration & Production	476.27M
GFS	GLOBALFOUNDRIES Inc.	Semiconductors	27.64B
GGAL	Grupo Financiero Galicia S.A.	Banks - Regional	5.69B
GGB	Gerdau S.A.	Steel	6.53B
GGG	Graco Inc.	Specialty Industrial Machinery	14.23B
GGR	Gogoro Inc.	Auto Manufacturers	410.32M
GH	Guardant Health, Inc.	Diagnostics & Research	4.44B
GHC	Graham Holdings Company	Education & Training Services	3.62B
GHG	GreenTree Hospitality Group Ltd.	Lodging	247.29M
GHI	Greystone Housing Impact Investors LP	Mortgage Finance	344.44M
GHIX	Gores Holdings IX, Inc.	Shell Companies	203.23M
GHLD	Guild Holdings Company	Mortgage Finance	869.25M
GHM	Graham Corporation	Specialty Industrial Machinery	350.79M
GHRS	GH Research PLC	Biotechnology	631.10M
GHSI	Guardion Health Sciences, Inc.	Drug Manufacturers - Specialty & Generic	12.14M
GIB	CGI Inc.	Information Technology Services	24.87B
GIC	Global Industrial Company	Industrial Distribution	1.36B
GIFI	Gulf Island Fabrication, Inc.	Metal Fabrication	102.09M
GIGM	GigaMedia Limited	Electronic Gaming & Multimedia	14.15M
GIII	G-III Apparel Group, Ltd.	Apparel Manufacturing	1.22B
GIL	Gildan Activewear Inc.	Apparel Manufacturing	6.78B
GILD	Gilead Sciences, Inc.	Drug Manufacturers - General	96.85B
GILT	Gilat Satellite Networks Ltd.	Communication Equipment	256.29M
GIPR	Generation Income Properties, Inc.	REIT - Diversified	15.89M
GIS	General Mills, Inc.	Packaged Foods	37.78B
GKOS	Glaukos Corporation	Medical Devices	5.92B
GL	Globe Life Inc.	Insurance - Life	8.40B
GLAC	Global Lights Acquisition Corp	Shell Companies	92.89M
GLAD	Gladstone Capital Corporation	Asset Management	521.78M
GLBE	Global-e Online Ltd.	Internet Retail	5.64B
GLBS	Globus Maritime Limited	Marine Shipping	36.43M
GLBZ	Glen Burnie Bancorp	Banks - Regional	13.79M
GLDD	Great Lakes Dredge & Dock Corporation	Engineering & Construction	608.44M
GLDG	GoldMining Inc.	Gold	162.06M
GLLI	Globalink Investment Inc.	Shell Companies	67.34M
GLMD	Galmed Pharmaceuticals Ltd.	Biotechnology	1.89M
GLNG	Golar LNG Limited	Oil & Gas Midstream	3.63B
GLOB	Globant S.A.	Information Technology Services	8.39B
GLP	Global Partners LP	Oil & Gas Midstream	1.35B
GLPG	Galapagos NV	Biotechnology	1.82B
GLPI	Gaming and Leisure Properties, Inc.	REIT - Specialty	13.81B
GLRE	Greenlight Capital Re, Ltd.	Insurance - Reinsurance	480.37M
GLSI	Greenwich LifeSciences, Inc.	Biotechnology	201.19M
GLST	Global Star Acquisition, Inc.	Shell Companies	82.75M
GLT	Glatfelter Corporation	Paper & Paper Products	68.11M
GLTO	Galecto, Inc.	Biotechnology	15.61M
GLUE	Monte Rosa Therapeutics, Inc.	Biotechnology	272.73M
GLW	Corning Incorporated	Electronic Components	33.41B
GLYC	GlycoMimetics, Inc.	Biotechnology	14.24M
GM	General Motors Company	Auto Manufacturers	50.27B
GMAB	Genmab A/S	Biotechnology	18.38B
GME	GameStop Corp.	Specialty Retail	9.76B
GMED	Globus Medical, Inc.	Medical Devices	9.65B
GMGI	Golden Matrix Group, Inc.	Electronic Gaming & Multimedia	286.30M
GMM	Global Mofy Metaverse Limited	Information Technology Services	26.28M
GMRE	Global Medical REIT Inc.	REIT - Healthcare Facilities	623.41M
GMS	GMS Inc.	Building Products & Equipment	3.77B
GNE	Genie Energy Ltd.	Utilities - Regulated Electric	450.09M
GNFT	Genfit S.A.	Biotechnology	219.03M
GNK	Genco Shipping & Trading Limited	Marine Shipping	825.54M
GNL	Global Net Lease, Inc.	REIT - Diversified	2.03B
GNLN	Greenlane Holdings, Inc.	Tobacco	1.63M
GNLX	Genelux Corporation	Biotechnology	71.45M
GNPX	Genprex, Inc.	Biotechnology	3.80M
GNRC	Generac Holdings Inc.	Specialty Industrial Machinery	9.40B
GNS	Genius Group Limited	Education & Training Services	37.43M
GNSS	Genasys Inc.	Scientific & Technical Instruments	110.60M
GNTA	Genenta Science S.p.A.	Biotechnology	78.41M
GNTX	Gentex Corporation	Auto Parts	7.17B
GNTY	Guaranty Bancshares, Inc.	Banks - Regional	383.17M
GNW	Genworth Financial, Inc.	Insurance - Life	2.98B
GO	Grocery Outlet Holding Corp.	Grocery Stores	2.08B
GOCO	GoHealth, Inc.	Insurance Brokers	130.25M
GODN	Golden Star Acquisition Corporation	Shell Companies	79.81M
GOEV	Canoo Inc.	Auto Manufacturers	144.45M
GOGL	Golden Ocean Group Limited	Marine Shipping	2.45B
GOGO	Gogo Inc.	Telecom Services	1.13B
GOLD	Barrick Gold Corporation	Gold	31.64B
GOLF	Acushnet Holdings Corp.	Leisure	4.56B
GOOD	Gladstone Commercial Corporation	REIT - Diversified	602.62M
GOOG	Alphabet Inc.	Internet Content & Information	2,091.72B
GOOGL	Alphabet Inc.	Internet Content & Information	2,092.07B
GOOS	Canada Goose Holdings Inc.	Apparel Manufacturing	1.09B
GORO	Gold Resource Corporation	Gold	38.22M
GORV	Lazydays Holdings, Inc.	Auto & Truck Dealerships	45.60M
GOSS	Gossamer Bio, Inc.	Biotechnology	223.96M
GOTU	Gaotu Techedu Inc.	Education & Training Services	1.24B
GOVX	GeoVax Labs, Inc.	Biotechnology	10.53M
GP	GreenPower Motor Company Inc.	Farm & Heavy Construction Machinery	28.09M
GPAK	Gamer Pakistan Inc.	Specialty Business Services	4.01M
GPAT	GP-Act III Acquisition Corp.	Shell Companies	360.63M
GPC	Genuine Parts Company	Auto Parts	20.25B
GPCR	Structure Therapeutics Inc.	Biotechnology	2.11B
GPI	Group 1 Automotive, Inc.	Auto & Truck Dealerships	4.57B
GPK	Graphic Packaging Holding Company	Packaging & Containers	8.94B
GPMT	Granite Point Mortgage Trust Inc.	REIT - Mortgage	154.89M
GPN	Global Payments Inc.	Specialty Business Services	25.97B
GPOR	Gulfport Energy Corporation	Oil & Gas Exploration & Production	2.70B
GPRE	Green Plains Inc.	Chemicals	1.15B
GPRK	GeoPark Limited	Oil & Gas Exploration & Production	496.30M
GPRO	GoPro, Inc.	Consumer Electronics	235.51M
GPS	The Gap, Inc.	Apparel Retail	8.41B
GRAB	Grab Holdings Limited	Software - Application	12.60B
GRAF	Graf Global Corp.	Shell Companies	434.32M
GRAL	GRAIL, LLC	Diagnostics & Research	483.92M
GRBK	Green Brick Partners, Inc.	Residential Construction	3.35B
GRC	The Gorman-Rupp Company	Specialty Industrial Machinery	1.07B
GRDI	GRIID Infrastructure Inc.	Capital Markets	76.98M
GREE	Greenidge Generation Holdings Inc.	Capital Markets	26.44M
GRFS	Grifols, S.A.	Drug Manufacturers - General	6.10B
GRFX	Graphex Group Limited	Other Industrial Metals & Mining	12.50M
GRI	GRI Bio, Inc.	Biotechnology	758.59K
GRIN	Grindrod Shipping Holdings Ltd.	Marine Shipping	278.73M
GRMN	Garmin Ltd.	Scientific & Technical Instruments	34.26B
GRND	Grindr Inc.	Software - Application	2.00B
GRNQ	Greenpro Capital Corp.	Consulting Services	7.67M
GRNT	Granite Ridge Resources, Inc	Oil & Gas Exploration & Production	875.33M
GROM	Grom Social Enterprises, Inc.	Internet Content & Information	2.46M
GROV	Grove Collaborative Holdings, Inc.	Household & Personal Products	52.31M
GROW	U.S. Global Investors, Inc.	Asset Management	37.15M
GROY	Gold Royalty Corp.	Gold	229.09M
GRPN	Groupon, Inc.	Internet Content & Information	621.19M
GRRR	Gorilla Technology Group Inc.	Software - Infrastructure	29.89M
GRTS	Gritstone bio, Inc.	Biotechnology	68.69M
GRVY	Gravity Co., Ltd.	Electronic Gaming & Multimedia	536.33M
GRWG	GrowGeneration Corp.	Specialty Retail	140.54M
GRYP	Gryphon Digital Mining, Inc.	Capital Markets	36.98M
GS	The Goldman Sachs Group, Inc.	Capital Markets	164.07B
GSAT	Globalstar, Inc.	Telecom Services	2.22B
GSBC	Great Southern Bancorp, Inc.	Banks - Regional	746.34M
GSBD	Goldman Sachs BDC, Inc.	Asset Management	1.68B
GSHD	Goosehead Insurance, Inc	Insurance - Diversified	2.15B
GSIT	GSI Technology, Inc.	Semiconductors	72.01M
GSIW	Garden Stage Limited	Capital Markets	110.96M
GSK	GSK plc	Drug Manufacturers - General	80.81B
GSL	Global Ship Lease, Inc.	Rental & Leasing Services	906.01M
GSM	Ferroglobe PLC	Other Industrial Metals & Mining	989.21M
GSUN	Golden Sun Education Group Limited	Education & Training Services	43.40M
GT	The Goodyear Tire & Rubber Company	Auto Parts	3.30B
GTAC	Global Technology Acquisition Corp. I	Shell Companies	80.12M
GTBP	GT Biopharma, Inc.	Biotechnology	5.77M
GTE	Gran Tierra Energy Inc.	Oil & Gas Exploration & Production	273.22M
GTEC	Greenland Technologies Holding Corporation	Specialty Industrial Machinery	21.48M
GTES	Gates Industrial Corporation plc	Specialty Industrial Machinery	4.64B
GTHX	G1 Therapeutics, Inc.	Biotechnology	208.86M
GTI	Graphjet Technology Sdn. Bhd.	Other Industrial Metals & Mining	453.42M
GTIM	Good Times Restaurants Inc.	Restaurants	29.60M
GTLB	GitLab Inc.	Software - Infrastructure	8.01B
GTLS	Chart Industries, Inc.	Specialty Industrial Machinery	6.83B
GTN	Gray Television, Inc.	Broadcasting	658.49M
GTN.A	Gray Television, Inc.	Broadcasting	653.12M
GTX	Garrett Motion Inc.	Auto Parts	1.96B
GTY	Getty Realty Corp.	REIT - Retail	1.62B
GURE	Gulf Resources, Inc.	Chemicals	10.95M
GUTS	Fractyl Health, Inc.	Biotechnology	181.53M
GV	Visionary Holdings Inc.	Education & Training Services	8.42M
GVA	Granite Construction Incorporated	Engineering & Construction	3.00B
GVH	Globavend Holdings Limited	Integrated Freight & Logistics	9.79M
GVP	GSE Systems, Inc.	Software - Application	10.59M
GWAV	Greenwave Technology Solutions, Inc.	Waste Management	16.45M
GWH	ESS Tech, Inc.	Electrical Equipment & Parts	128.79M
GWRE	Guidewire Software, Inc.	Software - Application	12.26B
GWRS	Global Water Resources, Inc.	Utilities - Regulated Water	310.90M
GWW	W.W. Grainger, Inc.	Industrial Distribution	47.24B
GXAI	Gaxos.ai Inc.	Electronic Gaming & Multimedia	2.41M
GXO	GXO Logistics, Inc.	Integrated Freight & Logistics	6.60B
GYRE	Gyre Therapeutics, Inc.	Biotechnology	1.16B
GYRO	Gyrodyne, LLC	Real Estate Services	17.90M
H	Hyatt Hotels Corporation	Lodging	15.31B
HA	Hawaiian Holdings, Inc.	Airlines	652.26M
HAE	Haemonetics Corporation	Medical Instruments & Supplies	4.56B
HAFC	Hanmi Financial Corporation	Banks - Regional	613.52M
HAFN	Hafnia Limited	Marine Shipping	3.99B
HAIA	Healthcare AI Acquisition Corp.	Shell Companies	60.64M
HAIN	The Hain Celestial Group, Inc.	Packaged Foods	669.34M
HAL	Halliburton Company	Oil & Gas Equipment & Services	30.22B
HALO	Halozyme Therapeutics, Inc.	Biotechnology	7.03B
HAO	Haoxi Health Technology Limited	Advertising Agencies	122.10M
HAS	Hasbro, Inc.	Leisure	9.04B
HASI	HA Sustainable Infrastructure Capital Inc.	Real Estate Services	3.75B
HAYN	Haynes International, Inc.	Metal Fabrication	763.27M
HAYW	Hayward Holdings, Inc.	Electrical Equipment & Parts	3.16B
HBAN	Huntington Bancshares Incorporated	Banks - Regional	21.96B
HBB	Hamilton Beach Brands Holding Company	Furnishings, Fixtures & Appliances	273.87M
HBCP	Home Bancorp, Inc.	Banks - Regional	353.93M
HBI	Hanesbrands Inc.	Apparel Manufacturing	2.14B
HBIO	Harvard Bioscience, Inc.	Medical Instruments & Supplies	141.15M
HBM	Hudbay Minerals Inc.	Copper	3.10B
HBNC	Horizon Bancorp, Inc.	Banks - Regional	710.71M
HBT	HBT Financial, Inc.	Banks - Regional	737.35M
HCA	HCA Healthcare, Inc.	Medical Care Facilities	94.83B
HCAT	Health Catalyst, Inc.	Health Information Services	447.48M
HCC	Warrior Met Coal, Inc.	Coking Coal	3.51B
HCI	HCI Group, Inc.	Insurance - Property & Casualty	984.78M
HCKT	The Hackett Group, Inc.	Information Technology Services	740.33M
HCM	HUTCHMED (China) Limited	Drug Manufacturers - Specialty & Generic	3.13B
HCP	HashiCorp, Inc.	Software - Infrastructure	7.02B
HCSG	Healthcare Services Group, Inc.	Medical Care Facilities	836.26M
HCTI	Healthcare Triangle, Inc.	Health Information Services	4.01M
HCVI	Hennessy Capital Investment Corp. VI	Shell Companies	176.15M
HCWB	HCW Biologics Inc.	Biotechnology	22.69M
HD	The Home Depot, Inc.	Home Improvement Retail	357.36B
HDB	HDFC Bank Limited	Banks - Regional	145.69B
HDL	Super Hi International Holding Ltd.	Restaurants	985.20M
HDSN	Hudson Technologies, Inc.	Specialty Chemicals	402.32M
HE	Hawaiian Electric Industries, Inc.	Utilities - Regulated Electric	1.85B
HEAR	Turtle Beach Corporation	Consumer Electronics	308.85M
HEES	H&E Equipment Services, Inc.	Rental & Leasing Services	1.86B
HEI	HEICO Corporation	Aerospace & Defense	28.57B
HEI.A	HEICO Corporation	Aerospace & Defense	28.49B
HELE	Helen of Troy Limited	Household & Personal Products	1.39B
HEPA	Hepion Pharmaceuticals, Inc.	Biotechnology	4.66M
HEPS	D-Market Elektronik Hizmetler ve Ticaret A.S.	Internet Retail	1.02B
HES	Hess Corporation	Oil & Gas Exploration & Production	46.45B
HESM	Hess Midstream LP	Oil & Gas Midstream	8.40B
HFBL	Home Federal Bancorp, Inc. of Louisiana	Banks - Regional	38.73M
HFFG	HF Foods Group Inc.	Food Distribution	198.87M
HFWA	Heritage Financial Corporation	Banks - Regional	802.03M
HG	Hamilton Insurance Group, Ltd.	Insurance - Reinsurance	1.93B
HGBL	Heritage Global Inc.	Capital Markets	89.06M
HGTY	Hagerty, Inc.	Insurance - Property & Casualty	941.88M
HGV	Hilton Grand Vacations Inc.	Resorts & Casinos	4.50B
HHGC	HHG Capital Corporation	Shell Companies	58.79M
HHH	Howard Hughes Holdings Inc.	Real Estate - Diversified	3.65B
HHS	Harte Hanks, Inc.	Conglomerates	60.82M
HI	Hillenbrand, Inc.	Specialty Industrial Machinery	3.00B
HIFS	Hingham Institution for Savings	Banks - Regional	529.74M
HIG	The Hartford Financial Services Group, Inc.	Insurance - Property & Casualty	32.80B
HIHO	Highway Holdings Limited	Metal Fabrication	8.23M
HII	Huntington Ingalls Industries, Inc.	Aerospace & Defense	10.95B
HIMS	Hims & Hers Health, Inc.	Household & Personal Products	4.45B
HIMX	Himax Technologies, Inc.	Semiconductors	1.19B
HIPO	Hippo Holdings Inc.	Insurance - Specialty	467.83M
HITI	High Tide Inc.	Pharmaceutical Retailers	148.01M
HIVE	HIVE Blockchain Technologies Ltd.	Capital Markets	378.12M
HIW	Highwoods Properties, Inc.	REIT - Office	3.22B
HKD	AMTD Digital Inc.	Software - Application	648.63M
HKIT	Hitek Global Inc.	Software - Application	20.58M
HL	Hecla Mining Company	Other Precious Metals & Mining	3.52B
HLF	Herbalife Nutrition Ltd.	Packaged Foods	1.22B
HLI	Houlihan Lokey, Inc.	Capital Markets	10.30B
HLIO	Helios Technologies, Inc.	Specialty Industrial Machinery	1.50B
HLIT	Harmonic Inc.	Communication Equipment	1.60B
HLLY	Holley Inc.	Auto Parts	456.36M
HLMN	Hillman Solutions Corp.	Tools & Accessories	1.97B
HLN	Haleon plc	Drug Manufacturers - Specialty & Generic	41.48B
HLNE	Hamilton Lane Incorporated	Asset Management	7.72B
HLP	Hongli Group Inc.	Steel	16.96M
HLT	Hilton Worldwide Holdings Inc.	Lodging	55.04B
HLVX	HilleVax, Inc.	Biotechnology	94.72M
HLX	Helix Energy Solutions Group, Inc.	Oil & Gas Equipment & Services	1.73B
HLXB	Helix Acquisition Corp. II	Shell Companies	236.67M
HMC	Honda Motor Co., Ltd.	Auto Manufacturers	50.75B
HMN	Horace Mann Educators Corporation	Insurance - Property & Casualty	1.42B
HMNF	HMN Financial, Inc.	Banks - Regional	118.32M
HMST	HomeStreet, Inc.	Banks - Regional	264.01M
HMY	Harmony Gold Mining Company Limited	Gold	5.69B
HNI	HNI Corporation	Business Equipment & Supplies	2.58B
HNNA	Hennessy Advisors, Inc.	Asset Management	62.73M
HNRA	HNR Acquisition Corp	Shell Companies	14.17M
HNRG	Hallador Energy Company	Thermal Coal	278.63M
HNST	The Honest Company, Inc.	Household & Personal Products	357.56M
HNVR	Hanover Bancorp, Inc.	Banks - Regional	127.66M
HOFT	Hooker Furnishings Corporation	Furnishings, Fixtures & Appliances	161.30M
HOFV	Hall of Fame Resort & Entertainment Company	Entertainment	18.94M
HOG	Harley-Davidson, Inc.	Recreational Vehicles	5.15B
HOLO	MicroCloud Hologram Inc.	Electronic Components	34.69M
HOLX	Hologic, Inc.	Medical Instruments & Supplies	19.04B
HOMB	Home Bancshares, Inc. (Conway, AR)	Banks - Regional	5.77B
HON	Honeywell International Inc.	Conglomerates	131.34B
HONE	HarborOne Bancorp, Inc.	Banks - Regional	601.33M
HOOD	Robinhood Markets, Inc.	Capital Markets	18.33B
HOOK	HOOKIPA Pharma Inc.	Biotechnology	55.37M
HOPE	Hope Bancorp, Inc.	Banks - Regional	1.60B
HOTH	Hoth Therapeutics, Inc.	Biotechnology	3.75M
HOUR	Hour Loop, Inc.	Internet Retail	34.76M
HOUS	Anywhere Real Estate Inc.	Real Estate Services	519.98M
HOV	Hovnanian Enterprises, Inc.	Residential Construction	1.23B
HOVR	New Horizon Aircraft Ltd.	Aerospace & Defense	13.08M
HOWL	Werewolf Therapeutics, Inc.	Biotechnology	113.42M
HP	Helmerich & Payne, Inc.	Oil & Gas Drilling	3.80B
HPCO	Hempacco Co., Inc.	Tobacco	2.80M
HPE	Hewlett Packard Enterprise Company	Communication Equipment	24.93B
HPH	Highest Performances Holdings Inc.	Asset Management	1.35B
HPK	HighPeak Energy, Inc.	Oil & Gas Exploration & Production	2.07B
HPP	Hudson Pacific Properties, Inc.	REIT - Office	825.70M
HPQ	HP Inc.	Computer Hardware	35.03B
HQI	HireQuest, Inc.	Staffing & Employment Services	188.72M
HQY	HealthEquity, Inc.	Health Information Services	6.84B
HR	Healthcare Realty Trust Incorporated	REIT - Healthcare Facilities	6.68B
HRB	H&R Block, Inc.	Personal Services	8.10B
HRI	Herc Holdings Inc.	Rental & Leasing Services	4.32B
HRL	Hormel Foods Corporation	Packaged Foods	17.44B
HRMY	Harmony Biosciences Holdings, Inc.	Biotechnology	1.92B
HROW	Harrow Health, Inc.	Drug Manufacturers - Specialty & Generic	850.40M
HRTG	Heritage Insurance Holdings, Inc.	Insurance - Property & Casualty	242.03M
HRTX	Heron Therapeutics, Inc.	Biotechnology	438.26M
HRYU	Hanryu Holdings, Inc.	Internet Content & Information	13.52M
HRZN	Horizon Technology Finance Corporation	Asset Management	455.21M
HSAI	Hesai Group	Auto Parts	550.62M
HSBC	HSBC Holdings plc	Banks - Diversified	161.53B
HSCS	Heart Test Laboratories, Inc.	Medical Devices	2.61M
HSDT	Helius Medical Technologies, Inc.	Medical Devices	2.07M
HSHP	Himalaya Shipping Ltd.	Marine Shipping	349.01M
HSIC	Henry Schein, Inc.	Medical Distribution	9.21B
HSII	Heidrick & Struggles International, Inc.	Staffing & Employment Services	811.86M
HSON	Hudson Global, Inc.	Staffing & Employment Services	50.49M
HSPO	Horizon Space Acquisition I Corp.	Shell Companies	86.86M
HST	Host Hotels & Resorts, Inc.	REIT - Hotel & Motel	12.51B
HSTM	HealthStream, Inc.	Health Information Services	890.35M
HSY	The Hershey Company	Confectioners	39.08B
HTBI	HomeTrust Bancshares, Inc.	Banks - Regional	605.16M
HTBK	Heritage Commerce Corp	Banks - Regional	645.02M
HTCR	HeartCore Enterprises, Inc.	Software - Application	14.60M
HTGC	Hercules Capital, Inc.	Asset Management	3.49B
HTH	Hilltop Holdings Inc.	Banks - Regional	2.18B
HTHT	H World Group Limited	Lodging	10.15B
HTLD	Heartland Express, Inc.	Trucking	1.05B
HTLF	Heartland Financial USA, Inc.	Banks - Regional	2.28B
HTOO	Fusion Fuel Green PLC	Utilities - Renewable	13.92M
HTZ	Hertz Global Holdings, Inc.	Rental & Leasing Services	1.15B
HUBB	Hubbell Incorporated	Electrical Equipment & Parts	20.06B
HUBC	HUB Cyber Security (Israel) Ltd.	Software - Infrastructure	7.35M
HUBG	Hub Group, Inc.	Integrated Freight & Logistics	2.85B
HUBS	HubSpot, Inc.	Software - Application	24.80B
HUDA	Hudson Acquisition I Corp.	Shell Companies	27.37M
HUDI	Huadi International Group Co., Ltd.	Steel	35.65M
HUGE	FSD Pharma Inc.	Drug Manufacturers - Specialty & Generic	4.47M
HUIZ	Huize Holding Limited	Insurance Brokers	46.74M
HUM	Humana Inc.	Healthcare Plans	48.79B
HUMA	Humacyte, Inc.	Biotechnology	953.86M
HUN	Huntsman Corporation	Chemicals	4.08B
HURC	Hurco Companies, Inc.	Specialty Industrial Machinery	116.80M
HURN	Huron Consulting Group Inc.	Consulting Services	2.04B
HUSA	Houston American Energy Corp.	Oil & Gas Exploration & Production	13.74M
HUT	Hut 8 Mining Corp.	Capital Markets	1.31B
HUYA	HUYA Inc.	Entertainment	980.09M
HVT	Haverty Furniture Companies, Inc.	Home Improvement Retail	460.18M
HVT.A	Haverty Furniture Companies, Inc.	Home Improvement Retail	447.72M
HWBK	Hawthorn Bancshares, Inc.	Banks - Regional	147.74M
HWC	Hancock Whitney Corporation	Banks - Regional	4.82B
HWH	HWH International Inc.	Leisure	13.79M
HWKN	Hawkins, Inc.	Specialty Chemicals	2.15B
HWM	Howmet Aerospace Inc.	Aerospace & Defense	38.41B
HXL	Hexcel Corporation	Aerospace & Defense	5.31B
HY	Hyster-Yale Materials Handling, Inc.	Farm & Heavy Construction Machinery	1.41B
HYAC	Haymaker Acquisition Corp. III	Shell Companies	312.61M
HYFM	Hydrofarm Holdings Group, Inc.	Farm & Heavy Construction Machinery	28.97M
HYLN	Hyliion Holdings Corp.	Auto Parts	389.84M
HYMC	Hycroft Mining Holding Corporation	Gold	58.90M
HYPR	Hyperfine, Inc.	Medical Devices	82.09M
HYZN	Hyzon Motors Inc.	Auto Parts	35.01M
HZO	MarineMax, Inc.	Specialty Retail	823.32M
IAC	IAC Inc.	Internet Content & Information	4.48B
IAG	IAMGOLD Corporation	Gold	1.97B
IART	Integra LifeSciences Holdings Corporation	Medical Devices	1.96B
IAS	Integral Ad Science Holding Corp.	Advertising Agencies	1.69B
IAUX	i-80 Gold Corp.	Gold	400.29M
IBAC	IB Acquisition Corp.	Shell Companies	157.65M
IBCP	Independent Bank Corporation	Banks - Regional	719.98M
IBEX	IBEX Limited	Information Technology Services	303.15M
IBIO	iBio, Inc.	Biotechnology	17.94M
IBKR	Interactive Brokers Group, Inc.	Capital Markets	12.98B
IBM	International Business Machines Corporation	Information Technology Services	174.57B
IBN	ICICI Bank Limited	Banks - Regional	101.63B
IBOC	International Bancshares Corporation	Banks - Regional	4.23B
IBP	Installed Building Products, Inc.	Residential Construction	7.51B
IBRX	ImmunityBio, Inc.	Biotechnology	3.65B
IBTA	Ibotta, Inc.	Software - Application	2.08B
IBTX	Independent Bank Group, Inc.	Banks - Regional	2.43B
ICAD	iCAD, Inc.	Medical Devices	37.10M
ICCC	ImmuCell Corporation	Biotechnology	32.58M
ICCH	ICC Holdings, Inc.	Insurance - Specialty	70.40M
ICCM	IceCure Medical Ltd	Medical Devices	34.27M
ICCT	iCoreConnect Inc.	Health Information Services	6.77M
ICD	Independence Contract Drilling, Inc.	Oil & Gas Drilling	21.76M
ICE	Intercontinental Exchange, Inc.	Financial Data & Stock Exchanges	87.04B
ICFI	ICF International, Inc.	Consulting Services	2.76B
ICG	Intchains Group Limited	Semiconductors	426.22M
ICHR	Ichor Holdings, Ltd.	Semiconductor Equipment & Materials	1.09B
ICL	ICL Group Ltd	Agricultural Inputs	5.50B
ICLK	iClick Interactive Asia Group Limited	Advertising Agencies	27.66M
ICLR	ICON PLC	Diagnostics & Research	27.28B
ICMB	Investcorp Credit Management BDC, Inc.	Asset Management	48.48M
ICON	Icon Energy Corp.	Marine Shipping	5.13M
ICU	SeaStar Medical Holding Corporation	Biotechnology	35.02M
ICUI	ICU Medical, Inc.	Medical Instruments & Supplies	3.09B
IDA	IDACORP, Inc.	Utilities - Regulated Electric	5.23B
IDAI	T Stamp Inc.	Software - Application	4.47M
IDCC	InterDigital, Inc.	Software - Application	3.06B
IDN	Intellicheck, Inc.	Software - Application	58.99M
IDR	Idaho Strategic Resources, Inc.	Gold	138.80M
IDT	IDT Corporation	Telecom Services	956.79M
IDXX	IDEXX Laboratories, Inc.	Diagnostics & Research	39.15B
IDYA	IDEAYA Biosciences, Inc.	Biotechnology	3.58B
IE	Ivanhoe Electric Inc.	Copper	1.12B
IEP	Icahn Enterprises L.P.	Oil & Gas Refining & Marketing	7.82B
IESC	IES Holdings, Inc.	Engineering & Construction	2.84B
IEX	IDEX Corporation	Specialty Industrial Machinery	15.57B
IFBD	Infobird Co., Ltd	Software - Application	4.81M
IFF	International Flavors & Fragrances Inc.	Specialty Chemicals	25.65B
IFIN	InFinT Acquisition Corporation	Shell Companies	124.32M
IFRX	InflaRx N.V.	Biotechnology	88.91M
IFS	Intercorp Financial Services Inc.	Banks - Regional	2.58B
IGC	IGC Pharma Inc	Biotechnology	34.83M
IGIC	International General Insurance Holdings Ltd.	Insurance - Diversified	807.22M
IGMS	IGM Biosciences, Inc.	Biotechnology	643.09M
IGT	International Game Technology PLC	Gambling	4.52B
IGTA	Inception Growth Acquisition Limited	Shell Companies	63.60M
IH	iHuman Inc.	Education & Training Services	84.24M
IHG	InterContinental Hotels Group PLC	Lodging	16.68B
IHRT	iHeartMedia, Inc.	Broadcasting	203.70M
IHS	IHS Holding Limited	Telecom Services	959.25M
IHT	InnSuites Hospitality Trust	REIT - Hotel & Motel	14.17M
III	Information Services Group, Inc.	Information Technology Services	171.79M
IIIN	Insteel Industries, Inc.	Metal Fabrication	665.21M
IIIV	i3 Verticals, Inc.	Software - Infrastructure	584.33M
IINN	Inspira Technologies Oxy B.H.N. Ltd.	Medical Devices	20.93M
IIPR	Innovative Industrial Properties, Inc.	REIT - Industrial	3.49B
IKNA	Ikena Oncology, Inc.	Biotechnology	81.07M
IKT	Inhibikase Therapeutics, Inc.	Biotechnology	10.90M
ILAG	Intelligent Living Application Group Inc.	Building Products & Equipment	15.30M
ILMN	Illumina, Inc.	Diagnostics & Research	19.51B
ILPT	Industrial Logistics Properties Trust	REIT - Industrial	336.73M
IMAB	I-Mab	Biotechnology	104.02M
IMAQ	International Media Acquisition Corp.	Shell Companies	86.58M
IMAX	IMAX Corporation	Entertainment	1.08B
IMCC	IM Cannabis Corp.	Drug Manufacturers - Specialty & Generic	5.94M
IMCR	Immunocore Holdings plc	Biotechnology	1.97B
IMKTA	Ingles Markets, Incorporated	Grocery Stores	1.50B
IMMP	Immutep Limited	Biotechnology	270.94M
IMMR	Immersion Corporation	Software - Application	391.18M
IMMX	Immix Biopharma, Inc.	Biotechnology	58.90M
IMNM	Immunome, Inc.	Biotechnology	915.13M
IMNN	Imunon, Inc.	Biotechnology	28.11M
IMO	Imperial Oil Limited	Oil & Gas Integrated	37.13B
IMOS	ChipMOS TECHNOLOGIES INC.	Semiconductors	862.87M
IMPP	Imperial Petroleum Inc.	Oil & Gas Midstream	114.57M
IMRN	Immuron Limited	Biotechnology	16.56M
IMRX	Immuneering Corporation	Biotechnology	33.80M
IMTE	Integrated Media Technology Limited	Electronic Components	3.76M
IMTX	Immatics N.V.	Biotechnology	1.23B
IMUX	Immunic, Inc.	Biotechnology	126.11M
IMVT	Immunovant, Inc.	Biotechnology	4.14B
IMXI	International Money Express, Inc.	Software - Infrastructure	707.63M
INAB	IN8bio, Inc.	Biotechnology	37.06M
INAQ	Insight Acquisition Corp.	Shell Companies	79.74M
INBK	First Internet Bancorp	Banks - Regional	328.92M
INBS	Intelligent Bio Solutions Inc.	Medical Devices	4.09M
INBX	Inhibrx, Inc.	Biotechnology	196.11M
INCR	InterCure Ltd.	Drug Manufacturers - Specialty & Generic	99.65M
INCY	Incyte Corporation	Biotechnology	13.00B
INDB	Independent Bank Corp.	Banks - Regional	2.70B
INDI	indie Semiconductor, Inc.	Semiconductor Equipment & Materials	1.01B
INDO	Indonesia Energy Corporation Limited	Oil & Gas Exploration & Production	22.75M
INDP	Indaptus Therapeutics, Inc.	Biotechnology	17.25M
INDV	Indivior PLC	Drug Manufacturers - Specialty & Generic	1.75B
INFA	Informatica Inc.	Software - Infrastructure	8.28B
INFN	Infinera Corporation	Communication Equipment	1.40B
INFU	InfuSystem Holdings, Inc.	Medical Instruments & Supplies	142.04M
INFY	Infosys Limited	Information Technology Services	93.73B
ING	ING Groep N.V.	Banks - Diversified	59.99B
INGN	Inogen, Inc.	Medical Devices	218.56M
INGR	Ingredion Incorporated	Packaged Foods	8.11B
INHD	Inno Holdings Inc.	Steel	15.02M
INKT	MiNK Therapeutics, Inc.	Biotechnology	32.09M
INLX	Intellinetics, Inc.	Software - Application	32.10M
INM	InMed Pharmaceuticals Inc.	Biotechnology	2.01M
INMB	INmune Bio, Inc.	Biotechnology	159.64M
INMD	InMode Ltd.	Medical Devices	1.54B
INN	Summit Hotel Properties, Inc.	REIT - Hotel & Motel	679.45M
INNV	InnovAge Holding Corp.	Medical Care Facilities	856.72M
INO	Inovio Pharmaceuticals, Inc.	Biotechnology	268.31M
INOD	Innodata Inc.	Information Technology Services	537.68M
INSE	Inspired Entertainment, Inc.	Gambling	240.47M
INSG	Inseego Corp.	Communication Equipment	109.50M
INSM	Insmed Incorporated	Biotechnology	11.99B
INSP	Inspire Medical Systems, Inc.	Medical Devices	4.13B
INST	Instructure Holdings, Inc.	Software - Application	3.40B
INSW	International Seaways, Inc.	Oil & Gas Midstream	2.76B
INTA	Intapp, Inc.	Software - Application	2.69B
INTC	Intel Corporation	Semiconductors	129.09B
INTE	Integral Acquisition Corporation 1	Shell Companies	45.01M
INTG	The InterGroup Corporation	Lodging	44.29M
INTJ	Intelligent Group Limited	Consulting Services	13.13M
INTR	Inter & Co, Inc.	Banks - Regional	2.68B
INTS	Intensity Therapeutics, Inc.	Biotechnology	65.55M
INTT	inTEST Corporation	Semiconductor Equipment & Materials	134.26M
INTU	Intuit Inc.	Software - Application	177.46B
INTZ	Intrusion Inc.	Software - Infrastructure	6.89M
INUV	Inuvo, Inc.	Software - Application	42.12M
INVA	Innoviva, Inc.	Biotechnology	1.18B
INVE	Identiv, Inc.	Computer Hardware	93.76M
INVH	Invitation Homes Inc.	REIT - Residential	21.16B
INVO	INVO Bioscience, Inc.	Medical Devices	3.62M
INVZ	Innoviz Technologies Ltd.	Auto Parts	130.75M
INZY	Inozyme Pharma, Inc.	Biotechnology	353.19M
IOBT	IO Biotech, Inc.	Biotechnology	85.97M
IONQ	IonQ, Inc.	Computer Hardware	1.64B
IONR	ioneer Ltd	Other Industrial Metals & Mining	212.19M
IONS	Ionis Pharmaceuticals, Inc.	Biotechnology	7.31B
IOR	Income Opportunity Realty Investors, Inc.	Mortgage Finance	65.25M
IOSP	Innospec Inc.	Specialty Chemicals	3.24B
IOT	Samsara Inc.	Software - Infrastructure	20.28B
IOVA	Iovance Biotherapeutics, Inc.	Biotechnology	2.51B
IP	International Paper Company	Packaging & Containers	16.09B
IPA	ImmunoPrecise Antibodies Ltd.	Biotechnology	21.84M
IPAR	Inter Parfums, Inc.	Household & Personal Products	4.44B
IPDN	Professional Diversity Network, Inc.	Staffing & Employment Services	5.72M
IPG	The Interpublic Group of Companies, Inc.	Advertising Agencies	11.88B
IPGP	IPG Photonics Corporation	Semiconductor Equipment & Materials	3.81B
IPHA	Innate Pharma S.A.	Biotechnology	174.04M
IPI	Intrepid Potash, Inc.	Agricultural Inputs	343.67M
IPSC	Century Therapeutics, Inc.	Biotechnology	186.75M
IPW	iPower Inc.	Internet Retail	47.98M
IPWR	Ideal Power Inc.	Electrical Equipment & Parts	56.94M
IPX	IperionX Limited	Other Industrial Metals & Mining	371.88M
IPXX	Inflection Point Acquisition Corp. II	Shell Companies	333.13M
IQ	iQIYI, Inc.	Entertainment	3.10B
IQV	IQVIA Holdings Inc.	Diagnostics & Research	44.15B
IR	Ingersoll Rand Inc.	Specialty Industrial Machinery	39.83B
IRAA	Iris Acquisition Corp	Shell Companies	79.27M
IRBT	iRobot Corporation	Furnishings, Fixtures & Appliances	324.53M
IRDM	Iridium Communications Inc.	Telecom Services	3.39B
IREN	Iris Energy Limited	Capital Markets	1.69B
IRIX	IRIDEX Corporation	Medical Devices	32.31M
IRM	Iron Mountain Incorporated	REIT - Specialty	29.55B
IRMD	IRadimed Corporation	Medical Devices	586.99M
IROH	Iron Horse Acquisitions Corp.	Shell Companies	89.56M
IRON	Disc Medicine, Inc.	Biotechnology	1.29B
IROQ	IF Bancorp, Inc.	Banks - Regional	57.66M
IRS	IRSA Inversiones y Representaciones SA	Real Estate Services	966.37M
IRT	Independence Realty Trust, Inc.	REIT - Residential	4.20B
IRTC	iRhythm Technologies, Inc.	Medical Devices	2.75B
IRWD	Ironwood Pharmaceuticals, Inc.	Drug Manufacturers - Specialty & Generic	1.10B
ISDR	Issuer Direct Corporation	Software - Application	36.27M
ISPC	iSpecimen Inc.	Diagnostics & Research	3.60M
ISPO	Inspirato Incorporated	Travel Services	32.06M
ISPR	Ispire Technology Inc.	Tobacco	423.62M
ISRG	Intuitive Surgical, Inc.	Medical Instruments & Supplies	155.82B
ISRL	Israel Acquisitions Corp	Shell Companies	141.98M
ISSC	Innovative Solutions and Support, Inc.	Aerospace & Defense	106.89M
ISTR	Investar Holding Corporation	Banks - Regional	184.64M
IT	Gartner, Inc.	Information Technology Services	39.06B
ITCI	Intra-Cellular Therapies, Inc.	Drug Manufacturers - Specialty & Generic	8.13B
ITGR	Integer Holdings Corporation	Medical Devices	4.13B
ITI	Iteris, Inc.	Communication Equipment	205.85M
ITIC	Investors Title Company	Insurance - Specialty	385.25M
ITOS	iTeos Therapeutics, Inc.	Biotechnology	624.20M
ITP	IT Tech Packaging, Inc.	Paper & Paper Products	2.44M
ITRG	Integra Resources Corp.	Other Precious Metals & Mining	80.32M
ITRI	Itron, Inc.	Scientific & Technical Instruments	4.69B
ITRM	Iterum Therapeutics plc	Biotechnology	20.23M
ITRN	Ituran Location and Control Ltd.	Scientific & Technical Instruments	534.28M
ITT	ITT Inc.	Specialty Industrial Machinery	11.55B
ITUB	Itaú Unibanco Holding S.A.	Banks - Regional	59.50B
ITW	Illinois Tool Works Inc.	Specialty Industrial Machinery	73.31B
IVA	Inventiva S.A.	Biotechnology	134.34M
IVAC	Intevac, Inc.	Specialty Industrial Machinery	101.82M
IVCA	Investcorp India Acquisition Corp	Shell Companies	185.18M
IVCB	Investcorp Europe Acquisition Corp I	Shell Companies	204.96M
IVCP	Swiftmerge Acquisition Corp.	Shell Companies	74.90M
IVDA	Iveda Solutions, Inc.	Security & Protection Services	7.49M
IVP	Inspire Veterinary Partners, Inc.	Personal Services	6.78M
IVR	Invesco Mortgage Capital Inc.	REIT - Mortgage	446.51M
IVT	InvenTrust Properties Corp.	REIT - Retail	1.85B
IVVD	Invivyd, Inc.	Biotechnology	139.00M
IVZ	Invesco Ltd.	Asset Management	7.76B
IX	ORIX Corporation	Financial Conglomerates	26.97B
IXAQ	IX Acquisition Corp.	Shell Companies	98.43M
IXHL	Incannex Healthcare Limited	Drug Manufacturers - Specialty & Generic	33.52M
IZEA	IZEA Worldwide, Inc.	Internet Content & Information	37.42M
IZM	ICZOOM Group Inc.	Electronics & Computer Distribution	22.19M
J	Jacobs Engineering Group Inc.	Engineering & Construction	18.39B
JACK	Jack in the Box Inc.	Restaurants	1.16B
JAGX	Jaguar Health, Inc.	Biotechnology	5.99M
JAKK	JAKKS Pacific, Inc.	Leisure	221.63M
JAMF	Jamf Holding Corp.	Software - Application	2.34B
JANX	Janux Therapeutics, Inc.	Biotechnology	2.17B
JAZZ	Jazz Pharmaceuticals plc	Biotechnology	7.05B
JBGS	JBG SMITH Properties	REIT - Office	1.51B
JBHT	J.B. Hunt Transport Services, Inc.	Integrated Freight & Logistics	17.87B
JBI	Janus International Group, Inc.	Building Products & Equipment	2.18B
JBL	Jabil Inc.	Electronic Components	12.44B
JBLU	JetBlue Airways Corporation	Airlines	2.34B
JBSS	Sanfilippo (John B.) & Son, Inc	Packaged Foods	1.19B
JBT	John Bean Technologies Corporation	Specialty Industrial Machinery	3.08B
JCI	Johnson Controls International plc	Building Products & Equipment	46.80B
JCSE	JE Cleantech Holdings Limited	Specialty Industrial Machinery	6.08M
JCTCF	Jewett-Cameron Trading Company Ltd.	Lumber & Wood Production	15.50M
JD	JD.com, Inc.	Internet Retail	35.85B
JDZG	Jiade Limited	Information Technology Services	14.05M
JEF	Jefferies Financial Group Inc.	Capital Markets	11.89B
JELD	JELD-WEN Holding, Inc.	Building Products & Equipment	1.45B
JEWL	Adamas One Corp.	Luxury Goods	11.06M
JFBR	Jeffs' Brands Ltd	Internet Retail	2.24M
JFIN	Jiayin Group Inc.	Internet Content & Information	292.21M
JFU	9F Inc.	Information Technology Services	23.78M
JG	Aurora Mobile Limited	Software - Infrastructure	17.40M
JHG	Janus Henderson Group plc	Asset Management	5.87B
JHX	James Hardie Industries plc	Building Materials	15.33B
JILL	J.Jill, Inc.	Apparel Retail	403.20M
JJSF	J&J Snack Foods Corp.	Packaged Foods	3.24B
JKHY	Jack Henry & Associates, Inc.	Information Technology Services	12.50B
JKS	JinkoSolar Holding Co., Ltd.	Solar	1.05B
JL	J-Long Group Limited	Apparel Manufacturing	14.92M
JLL	Jones Lang LaSalle Incorporated	Real Estate Services	11.86B
JMIA	Jumia Technologies AG	Internet Retail	1.23B
JMSB	John Marshall Bancorp, Inc.	Banks - Regional	272.37M
JNJ	Johnson & Johnson	Drug Manufacturers - General	386.83B
JNPR	Juniper Networks, Inc.	Communication Equipment	12.31B
JNVR	Janover Inc.	Software - Infrastructure	7.25M
JOB	GEE Group, Inc.	Staffing & Employment Services	35.45M
JOBY	Joby Aviation, Inc.	Airports & Air Services	4.33B
JOE	The St. Joe Company	Real Estate - Diversified	3.66B
JOUT	Johnson Outdoors Inc.	Leisure	430.80M
JPM	JPMorgan Chase & Co.	Banks - Diversified	615.23B
JRSH	Jerash Holdings (US), Inc.	Apparel Manufacturing	37.41M
JRVR	James River Group Holdings, Ltd.	Insurance - Specialty	329.46M
JSPR	Jasper Therapeutics, Inc.	Biotechnology	269.73M
JTAI	Jet.AI Inc.	Software - Application	5.18M
JUNE	Junee Limited	Engineering & Construction	64.66M
JVA	Coffee Holding Co., Inc.	Packaged Foods	13.93M
JVSA	JVSPAC Acquisition Corp.	Shell Companies	78.48M
JWEL	Jowell Global Ltd.	Internet Retail	3.06M
JWN	Nordstrom, Inc.	Department Stores	3.66B
JWSM	Jaws Mustang Acquisition Corporation	Shell Companies	299.32M
JXJT	JX Luxventure Limited	Apparel Manufacturing	9.93M
JXN	Jackson Financial Inc.	Insurance - Life	6.74B
JYD	Jayud Global Logistics Limited	Integrated Freight & Logistics	14.26M
JYNT	The Joint Corp.	Medical Care Facilities	213.75M
JZ	Jianzhi Education Technology Group Company Limited	Education & Training Services	16.15M
JZXN	Jiuzi Holdings, Inc.	Auto & Truck Dealerships	21.02M
K	Kellanova Co	Packaged Foods	19.64B
KA	Kineta, Inc.	Biotechnology	7.97M
KACL	Kairous Acquisition Corp. Limited	Shell Companies	44.39M
KAI	Kadant Inc.	Specialty Industrial Machinery	4.19B
KALA	Kala Pharmaceuticals, Inc.	Biotechnology	30.72M
KALU	Kaiser Aluminum Corporation	Aluminum	1.26B
KALV	KalVista Pharmaceuticals, Inc.	Biotechnology	604.71M
KAR	Openlane Inc.	Auto & Truck Dealerships	1.93B
KARO	Karooooo Ltd.	Software - Application	1.08B
KAVL	Kaival Brands Innovations Group, Inc.	Tobacco	7.33M
KB	KB Financial Group Inc.	Banks - Regional	24.83B
KBDC	Kayne Anderson BDC, Inc.	null	1.15B
KBH	KB Home	Residential Construction	6.40B
KBR	KBR, Inc.	Engineering & Construction	8.81B
KC	Kingsoft Cloud Holdings Limited	Software - Application	624.26M
KCGI	Kensington Capital Acquisition Corp. V	Shell Companies	127.36M
KD	Kyndryl Holdings, Inc.	Information Technology Services	6.21B
KDLY	Kindly MD, Inc.	Medical Care Facilities	9.27M
KDP	Keurig Dr Pepper Inc.	Beverages - Non-Alcoholic	46.24B
KE	Kimball Electronics, Inc.	Electrical Equipment & Parts	583.51M
KELYA	Kelly Services, Inc.	Staffing & Employment Services	832.69M
KELYB	Kelly Services, Inc.	Staffing & Employment Services	813.19M
KEN	Kenon Holdings Ltd.	Utilities - Independent Power Producers	1.25B
KEP	Korea Electric Power Corporation	Utilities - Regulated Electric	9.19B
KEQU	Kewaunee Scientific Corporation	Furnishings, Fixtures & Appliances	153.02M
KEX	Kirby Corporation	Marine Shipping	7.03B
KEY	KeyCorp	Banks - Regional	15.40B
KEYS	Keysight Technologies, Inc.	Scientific & Technical Instruments	23.78B
KFFB	Kentucky First Federal Bancorp	Banks - Regional	27.94M
KFRC	Kforce Inc.	Staffing & Employment Services	1.33B
KFS	Kingsway Financial Services Inc.	Auto & Truck Dealerships	242.36M
KFY	Korn Ferry	Staffing & Employment Services	3.77B
KGC	Kinross Gold Corporation	Gold	10.67B
KGEI	Kolibri Global Energy Inc.	Oil & Gas Exploration & Production	116.50M
KGS	Kodiak Gas Services, Inc.	Oil & Gas Equipment & Services	2.37B
KHC	The Kraft Heinz Company	Packaged Foods	41.03B
KIDS	OrthoPediatrics Corp.	Medical Devices	774.20M
KIM	Kimco Realty Corporation	REIT - Retail	14.68B
KIND	Nextdoor Holdings, Inc.	Internet Content & Information	1.11B
KINS	Kingstone Companies, Inc.	Insurance - Property & Casualty	84.64M
KIRK	Kirkland's, Inc.	Home Improvement Retail	23.46M
KITT	Nauticus Robotics, Inc.	Aerospace & Defense	12.87M
KKR	KKR & Co. Inc.	Asset Management	106.04B
KLAC	KLA Corporation	Semiconductor Equipment & Materials	103.17B
KLG	WK Kellogg Co	Packaged Foods	1.50B
KLIC	Kulicke and Soffa Industries, Inc.	Semiconductor Equipment & Materials	2.49B
KLTR	Kaltura, Inc.	Software - Application	193.19M
KLXE	KLX Energy Services Holdings, Inc.	Oil & Gas Equipment & Services	109.58M
KMB	Kimberly-Clark Corporation	Household & Personal Products	45.98B
KMDA	Kamada Ltd.	Drug Manufacturers - Specialty & Generic	334.79M
KMI	Kinder Morgan, Inc.	Oil & Gas Midstream	47.65B
KMPR	Kemper Corporation	Insurance - Property & Casualty	4.21B
KMT	Kennametal Inc.	Tools & Accessories	2.05B
KMX	CarMax, Inc.	Auto & Truck Dealerships	12.97B
KN	Knowles Corporation	Communication Equipment	1.62B
KNDI	Kandi Technologies Group, Inc.	Auto Parts	165.14M
KNF	Knife River Corporation	Building Materials	4.57B
KNOP	KNOT Offshore Partners LP	Marine Shipping	249.21M
KNSA	Kiniksa Pharmaceuticals, Ltd.	Biotechnology	1.86B
KNSL	Kinsale Capital Group, Inc.	Insurance - Property & Casualty	10.65B
KNTK	Kinetik Holdings Inc.	Oil & Gas Midstream	2.47B
KNW	Know Labs, Inc.	Scientific & Technical Instruments	28.83M
KNX	Knight-Swift Transportation Holdings Inc.	Trucking	8.74B
KO	The Coca-Cola Company	Beverages - Non-Alcoholic	290.72B
KOD	Kodiak Sciences Inc.	Biotechnology	149.72M
KODK	Eastman Kodak Company	Specialty Business Services	448.16M
KOF	Coca-Cola FEMSA, SAB de CV	Beverages - Non-Alcoholic	4.68B
KOP	Koppers Holdings Inc.	Specialty Chemicals	837.83M
KOPN	Kopin Corporation	Electronic Components	117.26M
KORE	KORE Group Holdings, Inc.	Telecom Services	50.10M
KOS	Kosmos Energy Ltd.	Oil & Gas Exploration & Production	2.58B
KOSS	Koss Corporation	Consumer Electronics	82.18M
KPLT	Katapult Holdings, Inc.	Software - Infrastructure	84.49M
KPRX	Kiora Pharmaceuticals, Inc.	Biotechnology	13.25M
KPTI	Karyopharm Therapeutics Inc.	Biotechnology	133.34M
KR	The Kroger Co.	Grocery Stores	39.43B
KRC	Kilroy Realty Corporation	REIT - Office	4.28B
KREF	KKR Real Estate Finance Trust Inc.	REIT - Mortgage	802.88M
KRG	Kite Realty Group Trust	REIT - Retail	5.48B
KRKR	36Kr Holdings Inc.	Internet Content & Information	10.31M
KRMD	KORU Medical Systems, Inc.	Medical Instruments & Supplies	107.55M
KRNL	Kernel Group Holdings, Inc.	Shell Companies	86.48M
KRNT	Kornit Digital Ltd.	Specialty Industrial Machinery	739.90M
KRNY	Kearny Financial Corp.	Banks - Regional	454.60M
KRO	Kronos Worldwide, Inc.	Specialty Chemicals	1.37B
KRON	Kronos Bio, Inc.	Biotechnology	76.92M
KROS	Keros Therapeutics, Inc.	Biotechnology	1.88B
KRP	Kimbell Royalty Partners, LP	Oil & Gas Exploration & Production	1.92B
KRRO	Korro Bio, Inc.	Biotechnology	435.09M
KRT	Karat Packaging Inc.	Packaging & Containers	584.87M
KRUS	Kura Sushi USA, Inc.	Restaurants	633.77M
KRYS	Krystal Biotech, Inc.	Biotechnology	5.82B
KSCP	Knightscope, Inc.	Security & Protection Services	31.15M
KSPI	Kaspi.kz JSC	Software - Infrastructure	24.95B
KSS	Kohl's Corporation	Department Stores	2.34B
KT	KT Corporation	Telecom Services	6.93B
KTB	Kontoor Brands, Inc.	Apparel Manufacturing	3.87B
KTCC	Key Tronic Corporation	Computer Hardware	41.97M
KTOS	Kratos Defense & Security Solutions, Inc.	Aerospace & Defense	3.35B
KTRA	Kintara Therapeutics, Inc.	Biotechnology	11.89M
KTTA	Pasithea Therapeutics Corp.	Biotechnology	5.29M
KUKE	Kuke Music Holding Limited	Entertainment	40.84M
KULR	KULR Technology Group, Inc.	Electronic Components	52.72M
KURA	Kura Oncology, Inc.	Biotechnology	1.59B
KVAC	Keen Vision Acquisition Corporation	Shell Companies	207.22M
KVHI	KVH Industries, Inc.	Communication Equipment	90.30M
KVUE	Kenvue Inc.	Household & Personal Products	35.60B
KVYO	Klaviyo, Inc.	Software - Infrastructure	6.72B
KW	Kennedy-Wilson Holdings, Inc.	Real Estate Services	1.43B
KWE	KWESST Micro Systems Inc.	Aerospace & Defense	3.21M
KWR	Quaker Chemical Corporation	Specialty Chemicals	3.25B
KXIN	Kaixin Auto Holdings	Auto & Truck Dealerships	5.59M
KYMR	Kymera Therapeutics, Inc.	Biotechnology	2.63B
KYTX	Kyverna Therapeutics, Inc.	Biotechnology	383.29M
KZIA	Kazia Therapeutics Limited	Biotechnology	8.64M
KZR	Kezar Life Sciences, Inc.	Biotechnology	47.32M
L	Loews Corporation	Insurance - Property & Casualty	17.88B
LAAC	Lithium Americas (Argentina) Corp.	Other Industrial Metals & Mining	484.41M
LAB	Standard BioTools Inc.	Medical Devices	831.60M
LAC	Lithium Americas Corp.	Other Industrial Metals & Mining	566.38M
LAD	Lithia Motors, Inc.	Auto & Truck Dealerships	7.28B
LADR	Ladder Capital Corp	REIT - Mortgage	1.58B
LAES	SEALSQ Corp	Semiconductors	20.46M
LAKE	Lakeland Industries, Inc.	Apparel Manufacturing	181.42M
LAMR	Lamar Advertising Company	REIT - Specialty	12.19B
LANC	Lancaster Colony Corporation	Packaged Foods	5.25B
LAND	Gladstone Land Corporation	REIT - Specialty	532.20M
LANV	Lanvin Group Holdings Limited	Luxury Goods	214.63M
LARK	Landmark Bancorp, Inc.	Banks - Regional	109.75M
LASE	Laser Photonics Corporation	Specialty Industrial Machinery	19.88M
LASR	nLIGHT, Inc.	Semiconductors	564.12M
LATG	Chenghe Acquisition I Co.	Shell Companies	82.35M
LAUR	Laureate Education, Inc.	Education & Training Services	2.39B
LAW	CS Disco, Inc.	Software - Application	360.46M
LAZ	Lazard Ltd	Capital Markets	4.37B
LAZR	Luminar Technologies, Inc.	Auto Parts	730.60M
LB	LandBridge Company LLC	Apparel Retail	550.39M
LBPH	Longboard Pharmaceuticals, Inc.	Biotechnology	1.31B
LBRDA	Liberty Broadband Corporation	Telecom Services	9.60B
LBRDK	Liberty Broadband Corporation	Telecom Services	9.61B
LBRT	Liberty Energy Inc.	Oil & Gas Equipment & Services	3.86B
LBTYA	Liberty Global plc	Telecom Services	7.36B
LBTYB	Liberty Global plc	Telecom Services	7.16B
LBTYK	Liberty Global plc	Telecom Services	7.40B
LC	LendingClub Corporation	Credit Services	1.22B
LCFY	Locafy Limited	Internet Content & Information	6.07M
LCID	Lucid Group, Inc.	Auto Manufacturers	7.86B
LCII	LCI Industries	Recreational Vehicles	2.94B
LCNB	LCNB Corp.	Banks - Regional	209.32M
LCTX	Lineage Cell Therapeutics, Inc.	Biotechnology	190.71M
LCUT	Lifetime Brands, Inc.	Furnishings, Fixtures & Appliances	185.86M
LCW	Learn CW Investment Corporation	Shell Companies	165.67M
LDI	loanDepot, Inc.	Mortgage Finance	640.71M
LDOS	Leidos Holdings, Inc.	Information Technology Services	20.10B
LDTC	LeddarTech Holdings Inc.	Software - Application	18.63M
LDWY	Lendway, Inc.	Advertising Agencies	7.86M
LE	Lands' End, Inc.	Apparel Retail	556.52M
LEA	Lear Corporation	Auto Parts	6.80B
LECO	Lincoln Electric Holdings, Inc.	Tools & Accessories	11.88B
LEDS	SemiLEDs Corporation	Semiconductors	10.36M
LEE	Lee Enterprises, Incorporated	Publishing	62.07M
LEG	Leggett & Platt, Incorporated	Furnishings, Fixtures & Appliances	1.79B
LEGH	Legacy Housing Corporation	Residential Construction	682.44M
LEGN	Legend Biotech Corporation	Biotechnology	10.29B
LEGT	Legato Merger Corp. III	Shell Companies	262.40M
LEN	Lennar Corporation	Residential Construction	48.95B
LEN.B	Lennar Corporation	Residential Construction	48.71B
LENZ	LENZ Therapeutics, Inc.	Biotechnology	620.49M
LESL	Leslie's, Inc.	Specialty Retail	557.92M
LEU	Centrus Energy Corp.	Uranium	642.05M
LEV	The Lion Electric Company	Farm & Heavy Construction Machinery	192.29M
LEVI	Levi Strauss & Co.	Apparel Manufacturing	7.24B
LEXX	Lexaria Bioscience Corp.	Biotechnology	54.55M
LFCR	Lifecore Biomedical, Inc.	Drug Manufacturers - Specialty & Generic	200.56M
LFLY	Leafly Holdings, Inc.	Pharmaceutical Retailers	5.45M
LFMD	LifeMD, Inc.	Health Information Services	281.23M
LFST	LifeStance Health Group, Inc.	Medical Care Facilities	2.12B
LFT	Lument Finance Trust, Inc.	REIT - Mortgage	137.44M
LFUS	Littelfuse, Inc.	Electronic Components	6.37B
LFVN	LifeVantage Corporation	Packaged Foods	106.81M
LFWD	ReWalk Robotics Ltd.	Medical Devices	39.31M
LGCB	Linkage Global Inc	Internet Retail	59.56M
LGCL	Lucas GC Limited	Software - Application	192.73M
LGF.A	Lions Gate Entertainment Corp.	Entertainment	1.91B
LGF.B	Lions Gate Entertainment Corp.	Entertainment	1.87B
LGHL	Lion Group Holding Ltd.	Capital Markets	1.33M
LGIH	LGI Homes, Inc.	Residential Construction	2.66B
LGL	The LGL Group, Inc.	Electronic Components	29.01M
LGMK	LogicMark, Inc.	Health Information Services	1.20M
LGND	Ligand Pharmaceuticals Incorporated	Biotechnology	1.94B
LGO	Largo Inc.	Other Industrial Metals & Mining	129.43M
LGVN	Longeveron Inc.	Biotechnology	47.96M
LH	Labcorp Holdings Inc.	Diagnostics & Research	17.91B
LHX	L3Harris Technologies, Inc.	Aerospace & Defense	42.41B
LI	Li Auto Inc.	Auto Manufacturers	18.47B
LICN	Lichen China Limited	Specialty Business Services	80.40M
LICY	Li-Cycle Holdings Corp.	Waste Management	78.12M
LIDR	AEye, Inc.	Software - Infrastructure	11.89M
LIF	Life360, Inc.	Software - Application	2.34B
LIFW	MSP Recovery, Inc.	Health Information Services	52.40M
LII	Lennox International Inc.	Building Products & Equipment	20.38B
LILA	Liberty Latin America Ltd.	Telecom Services	2.06B
LILAK	Liberty Latin America Ltd.	Telecom Services	2.06B
LILM	Lilium N.V.	Aerospace & Defense	512.63M
LIN	Linde plc	Specialty Chemicals	218.01B
LINC	Lincoln Educational Services Corporation	Education & Training Services	437.07M
LIND	Lindblad Expeditions Holdings, Inc.	Travel Services	478.59M
LINE	Lineage, Inc.	REIT - Industrial	20.33B
LINK	Interlink Electronics, Inc.	Electronic Components	40.43M
LION	Lionsgate Studios Corp.	Shell Companies	2.13B
LIPO	Lipella Pharmaceuticals Inc.	Biotechnology	6.31M
LIQT	LiqTech International, Inc.	Pollution & Treatment Controls	13.55M
LITB	LightInTheBox Holding Co., Ltd.	Internet Retail	63.08M
LITE	Lumentum Holdings Inc.	Communication Equipment	3.37B
LITM	Snow Lake Resources Ltd.	Other Industrial Metals & Mining	13.98M
LIVE	Live Ventures Incorporated	Home Improvement Retail	58.38M
LIVN	LivaNova PLC	Medical Devices	2.79B
LIXT	Lixte Biotechnology Holdings, Inc.	Biotechnology	4.95M
LKCO	Luokung Technology Corp.	Software - Application	8.95M
LKFN	Lakeland Financial Corporation	Banks - Regional	1.77B
LKQ	LKQ Corporation	Auto Parts	10.70B
LL	LL Flooring Holdings, Inc.	Home Improvement Retail	27.56M
LLAP	Terran Orbital Corporation	Aerospace & Defense	147.02M
LLY	Eli Lilly and Company	Drug Manufacturers - General	746.38B
LLYVA	Liberty Live Group - Series A	Entertainment	3.38B
LLYVK	Liberty Live Group - Series C	Entertainment	3.45B
LMAT	LeMaitre Vascular, Inc.	Medical Instruments & Supplies	1.96B
LMB	Limbach Holdings, Inc.	Building Products & Equipment	660.47M
LMFA	LM Funding America, Inc.	Credit Services	8.79M
LMND	Lemonade, Inc.	Insurance - Property & Casualty	1.59B
LMNR	Limoneira Company	Farm Products	396.42M
LMT	Lockheed Martin Corporation	Aerospace & Defense	126.93B
LNC	Lincoln National Corporation	Insurance - Life	5.70B
LND	BrasilAgro - Companhia Brasileira de Propriedades Agrícolas	Farm Products	460.21M
LNG	Cheniere Energy, Inc.	Oil & Gas Midstream	41.22B
LNKB	LINKBANCORP, Inc.	Banks - Regional	258.51M
LNN	Lindsay Corporation	Farm & Heavy Construction Machinery	1.36B
LNSR	LENSAR, Inc.	Medical Devices	57.92M
LNT	Alliant Energy Corporation	Utilities - Regulated Electric	14.35B
LNTH	Lantheus Holdings, Inc.	Drug Manufacturers - Specialty & Generic	7.52B
LNW	Light & Wonder, Inc.	Gambling	9.44B
LNZA	LanzaTech Global, Inc.	Waste Management	388.55M
LOAN	Manhattan Bridge Capital, Inc.	REIT - Mortgage	62.23M
LOAR	Loar Holdings Inc.	Aerospace & Defense	5.35B
LOB	Live Oak Bancshares, Inc.	Banks - Regional	2.01B
LOBO	LOBO EV TECHNOLOGIES LTD.	Auto Manufacturers	21.19M
LOCL	Local Bounti Corporation	Farm Products	23.94M
LOCO	El Pollo Loco Holdings, Inc.	Restaurants	369.48M
LODE	Comstock Inc.	Other Precious Metals & Mining	24.56M
LOGC	ContextLogic Inc	Internet Retail	140.10M
LOGI	Logitech International S.A.	Computer Hardware	13.59B
LOMA	Loma Negra Compañía Industrial Argentina SA	Building Materials	1.10B
LOOP	Loop Industries, Inc.	Specialty Chemicals	83.19M
LOPE	Grand Canyon Education, Inc.	Education & Training Services	4.61B
LOT	Lotus Technology Inc.	Auto Manufacturers	4.04B
LOVE	The Lovesac Company	Furnishings, Fixtures & Appliances	423.13M
LOW	Lowe's Companies, Inc.	Home Improvement Retail	136.58B
LPA	Logistic Properties of the Americas	Real Estate - Development	516.87M
LPAA	Launch One Acquisition Corp.	Shell Companies	249.25M
LPCN	Lipocine Inc.	Biotechnology	26.63M
LPG	Dorian LPG Ltd.	Oil & Gas Midstream	1.69B
LPL	LG Display Co., Ltd.	Consumer Electronics	4.03B
LPLA	LPL Financial Holdings Inc.	Capital Markets	16.19B
LPRO	Open Lending Corporation	Credit Services	744.19M
LPSN	LivePerson, Inc.	Software - Application	116.97M
LPTH	LightPath Technologies, Inc.	Electronic Components	52.78M
LPTV	Loop Media, Inc.	Broadcasting	10.05M
LPTX	Leap Therapeutics, Inc.	Biotechnology	81.89M
LPX	Louisiana-Pacific Corporation	Building Products & Equipment	7.04B
LQDA	Liquidia Corporation	Biotechnology	876.85M
LQDT	Liquidity Services, Inc.	Internet Retail	678.08M
LQR	LQR House Inc.	Beverages - Wineries & Distilleries	3.71M
LRCX	Lam Research Corporation	Semiconductor Equipment & Materials	113.77B
LRE	Lead Real Estate Co., Ltd	Real Estate - Development	28.65M
LRFC	Logan Ridge Finance Corporation	Asset Management	59.62M
LRHC	La Rosa Holding Corp.	Real Estate Services	16.66M
LRMR	Larimar Therapeutics, Inc.	Biotechnology	543.59M
LRN	Stride, Inc.	Education & Training Services	3.29B
LSAK	Lesaka Technologies, Inc.	Software - Infrastructure	309.43M
LSB	LakeShore Biopharma Co., Ltd	Biotechnology	88.59M
LSBK	Lake Shore Bancorp, Inc.	Banks - Regional	70.97M
LSCC	Lattice Semiconductor Corporation	Semiconductors	7.03B
LSEA	Landsea Homes Corporation	Real Estate - Development	440.66M
LSF	Laird Superfood, Inc.	Packaged Foods	40.09M
LSH	Lakeside Holding Limited	Integrated Freight & Logistics	18.85M
LSPD	Lightspeed Commerce Inc.	Software - Application	2.05B
LSTA	Lisata Therapeutics, Inc.	Biotechnology	27.83M
LSTR	Landstar System, Inc.	Integrated Freight & Logistics	6.93B
LSXMA	Liberty SiriusXM Group - Series A	Broadcasting	7.40B
LSXMB	Liberty SiriusXM Group - Series B	Broadcasting	7.58B
LSXMK	Liberty SiriusXM Group - Series C	Broadcasting	7.25B
LTBR	Lightbridge Corporation	Electrical Equipment & Parts	43.45M
LTC	LTC Properties, Inc.	REIT - Healthcare Facilities	1.56B
LTH	Life Time Group Holdings, Inc.	Leisure	4.08B
LTM	LATAM Airlines Group S.A.	Airlines	7.56B
LTRN	Lantern Pharma Inc.	Biotechnology	49.28M
LTRX	Lantronix, Inc.	Communication Equipment	146.56M
LTRY	Lottery.com Inc.	Gambling	4.78M
LU	Lufax Holding Ltd	Credit Services	1.53B
LUCD	Lucid Diagnostics Inc.	Medical Devices	44.66M
LUCY	Innovative Eyewear, Inc.	Medical Instruments & Supplies	6.28M
LULU	Lululemon Athletica Inc.	Apparel Retail	30.74B
LUMN	Lumen Technologies, Inc.	Telecom Services	2.47B
LUMO	Lumos Pharma, Inc.	Biotechnology	14.29M
LUNA	Luna Innovations Incorporated	Scientific & Technical Instruments	105.61M
LUNG	Pulmonx Corporation	Medical Devices	273.30M
LUNR	Intuitive Machines, Inc.	Aerospace & Defense	481.70M
LUV	Southwest Airlines Co.	Airlines	16.29B
LUXH	LuxUrban Hotels Inc.	Lodging	15.72M
LVLU	Lulu's Fashion Lounge Holdings, Inc.	Apparel Retail	66.95M
LVO	LiveOne, Inc.	Entertainment	160.81M
LVRO	Lavoro Limited	Agricultural Inputs	607.53M
LVS	Las Vegas Sands Corp.	Resorts & Casinos	29.65B
LVTX	LAVA Therapeutics N.V.	Biotechnology	52.06M
LVWR	LiveWire Group, Inc.	Auto Manufacturers	1.34B
LW	Lamb Weston Holdings, Inc.	Packaged Foods	8.38B
LWAY	Lifeway Foods, Inc.	Packaged Foods	173.55M
LWLG	Lightwave Logic, Inc.	Specialty Chemicals	404.72M
LX	LexinFintech Holdings Ltd.	Credit Services	290.96M
LXEH	Lixiang Education Holding Co., Ltd.	Education & Training Services	3.36M
LXEO	Lexeo Therapeutics, Inc.	Biotechnology	413.46M
LXFR	Luxfer Holdings PLC	Specialty Industrial Machinery	357.07M
LXP	LXP Industrial Trust	REIT - Industrial	3.05B
LXRX	Lexicon Pharmaceuticals, Inc.	Biotechnology	806.13M
LXU	LSB Industries, Inc.	Chemicals	626.01M
LYB	LyondellBasell Industries N.V.	Specialty Chemicals	31.88B
LYEL	Lyell Immunopharma, Inc.	Biotechnology	404.08M
LYFT	Lyft, Inc.	Software - Application	4.70B
LYG	Lloyds Banking Group plc	Banks - Regional	47.17B
LYRA	Lyra Therapeutics, Inc.	Biotechnology	18.48M
LYT	Lytus Technologies Holdings PTV. Ltd.	Software - Application	2.76M
LYTS	LSI Industries Inc.	Electronic Components	467.53M
LYV	Live Nation Entertainment, Inc.	Entertainment	21.68B
LZ	LegalZoom.com, Inc.	Specialty Business Services	1.23B
LZB	La-Z-Boy Incorporated	Furnishings, Fixtures & Appliances	1.85B
LZM	Lifezone Metals Limited	Other Industrial Metals & Mining	556.00M
M	Macy's, Inc.	Department Stores	4.77B
MA	Mastercard Incorporated	Credit Services	411.02B
MAA	Mid-America Apartment Communities, Inc.	REIT - Residential	16.45B
MAC	The Macerich Company	REIT - Retail	3.56B
MACA	Moringa Acquisition Corp	Shell Companies	45.74M
MACI	Melar Acquisition Corp. I	Shell Companies	220.11M
MAG	MAG Silver Corp.	Silver	1.37B
MAIA	MAIA Biotechnology, Inc.	Biotechnology	68.04M
MAIN	Main Street Capital Corporation	Asset Management	4.39B
MAMA	Mama's Creations, Inc.	Packaged Foods	271.28M
MAMO	Massimo Group	Recreational Vehicles	161.91M
MAN	ManpowerGroup Inc.	Staffing & Employment Services	3.65B
MANH	Manhattan Associates, Inc.	Software - Application	15.67B
MANU	Manchester United plc	Entertainment	2.82B
MAPS	WM Technology, Inc.	Software - Application	105.51M
MAQC	Maquia Capital Acquisition Corporation	Shell Companies	68.54M
MAR	Marriott International, Inc.	Lodging	68.56B
MARA	Marathon Digital Holdings, Inc.	Capital Markets	5.65B
MARPS	Marine Petroleum Trust	Oil & Gas Midstream	7.68M
MARX	Mars Acquisition Corp.	Shell Companies	48.72M
MAS	Masco Corporation	Building Products & Equipment	17.19B
MASI	Masimo Corporation	Medical Devices	5.63B
MASS	908 Devices Inc.	Medical Devices	187.94M
MAT	Mattel, Inc.	Leisure	6.64B
MATH	Metalpha Technology Holding Limited	Capital Markets	48.11M
MATV	Mativ Holdings, Inc.	Specialty Chemicals	1.01B
MATW	Matthews International Corporation	Conglomerates	877.54M
MATX	Matson, Inc.	Marine Shipping	4.51B
MAX	MediaAlpha, Inc.	Internet Content & Information	950.45M
MAXN	Maxeon Solar Technologies, Ltd.	Solar	10.28M
MAYS	J.W. Mays, Inc.	Real Estate Services	87.34M
MBC	MasterBrand, Inc.	Furnishings, Fixtures & Appliances	2.31B
MBCN	Middlefield Banc Corp.	Banks - Regional	206.92M
MBI	MBIA Inc.	Insurance - Specialty	224.57M
MBIN	Merchants Bancorp	Banks - Regional	2.03B
MBIO	Mustang Bio, Inc.	Biotechnology	11.32M
MBLY	Mobileye Global Inc.	Auto Parts	16.45B
MBOT	Microbot Medical Inc.	Medical Instruments & Supplies	16.05M
MBRX	Moleculin Biotech, Inc.	Biotechnology	7.37M
MBUU	Malibu Boats, Inc.	Recreational Vehicles	783.45M
MBWM	Mercantile Bank Corporation	Banks - Regional	794.43M
MC	Moelis & Company	Capital Markets	4.86B
MCAA	Mountain & Co. I Acquisition Corp.	Shell Companies	161.55M
MCAG	Mountain Crest Acquisition Corp. V	Shell Companies	33.95M
MCB	Metropolitan Bank Holding Corp.	Banks - Regional	588.52M
MCBC	Macatawa Bank Corporation	Banks - Regional	511.64M
MCBS	MetroCity Bankshares, Inc.	Banks - Regional	795.99M
MCD	McDonald's Corporation	Restaurants	190.75B
MCFT	MasterCraft Boat Holdings, Inc.	Recreational Vehicles	357.03M
MCHP	Microchip Technology Incorporated	Semiconductors	47.00B
MCHX	Marchex, Inc.	Advertising Agencies	70.32M
MCK	McKesson Corporation	Medical Distribution	79.27B
MCO	Moody's Corporation	Financial Data & Stock Exchanges	82.56B
MCRB	Seres Therapeutics, Inc.	Biotechnology	205.21M
MCRI	Monarch Casino & Resort, Inc.	Resorts & Casinos	1.46B
MCS	The Marcus Corporation	Entertainment	398.24M
MCVT	Mill City Ventures III, Ltd.	Credit Services	17.30M
MCW	Mister Car Wash, Inc.	Personal Services	2.44B
MCY	Mercury General Corporation	Insurance - Property & Casualty	3.29B
MD	Pediatrix Medical Group, Inc.	Medical Care Facilities	708.94M
MDAI	Spectral AI, Inc.	Medical Devices	29.26M
MDB	MongoDB, Inc.	Software - Infrastructure	17.76B
MDBH	MDB Capital Holdings, LLC Class A common	Capital Markets	109.04M
MDGL	Madrigal Pharmaceuticals, Inc.	Biotechnology	5.80B
MDIA	MediaCo Holding Inc.	Broadcasting	191.49M
MDJH	MDJM Ltd	Real Estate Services	16.23M
MDLZ	Mondelez International, Inc.	Confectioners	89.94B
MDRR	Medalist Diversified REIT, Inc.	REIT - Diversified	13.13M
MDT	Medtronic plc	Medical Devices	103.08B
MDU	MDU Resources Group, Inc.	Conglomerates	5.47B
MDV	Modiv Inc.	REIT - Diversified	140.09M
MDWD	MediWound Ltd.	Biotechnology	174.44M
MDXG	MiMedx Group, Inc.	Biotechnology	1.13B
MDXH	MDxHealth SA	Diagnostics & Research	71.49M
ME	23andMe Holding Co.	Diagnostics & Research	211.80M
MEC	Mayville Engineering Company, Inc.	Metal Fabrication	388.16M
MED	Medifast, Inc.	Personal Services	228.37M
MEDP	Medpace Holdings, Inc.	Diagnostics & Research	11.71B
MEDS	TRxADE HEALTH, Inc.	Pharmaceutical Retailers	12.88M
MEG	Montrose Environmental Group, Inc.	Waste Management	1.02B
MEGL	Magic Empire Global Limited	Capital Markets	10.55M
MEI	Methode Electronics, Inc.	Electronic Components	444.73M
MEIP	MEI Pharma, Inc.	Biotechnology	22.39M
MELI	MercadoLibre, Inc.	Internet Retail	82.07B
MEOH	Methanex Corporation	Chemicals	3.18B
MERC	Mercer International Inc.	Paper & Paper Products	515.41M
MESA	Mesa Air Group, Inc.	Airlines	64.65M
MESO	Mesoblast Limited	Biotechnology	804.69M
MET	MetLife, Inc.	Insurance - Life	54.67B
META	Meta Platforms, Inc.	Internet Content & Information	1,172.08B
METC	Ramaco Resources, Inc.	Coking Coal	681.85M
METCB	Ramaco Resources, Inc.	Coking Coal	701.09M
MFA	MFA Financial, Inc.	REIT - Mortgage	1.15B
MFC	Manulife Financial Corporation	Insurance - Life	47.20B
MFG	Mizuho Financial Group, Inc.	Banks - Regional	54.49B
MFH	Mercurity Fintech Holding Inc.	Capital Markets	120.42M
MFI	mF International Limited	Software - Application	10.14M
MFIC	MidCap Financial Investment Corporation	Asset Management	1.36B
MFIN	Medallion Financial Corp.	Credit Services	187.01M
MG	Mistras Group, Inc.	Security & Protection Services	310.13M
MGA	Magna International Inc.	Auto Parts	12.55B
MGEE	MGE Energy, Inc.	Utilities - Regulated Electric	3.16B
MGIC	Magic Software Enterprises Ltd.	Information Technology Services	527.08M
MGIH	Millennium Group International Holdings Limited	Packaging & Containers	16.31M
MGLD	The Marygold Companies, Inc.	Asset Management	46.35M
MGM	MGM Resorts International	Resorts & Casinos	13.44B
MGNI	Magnite, Inc.	Advertising Agencies	1.99B
MGNX	MacroGenics, Inc.	Biotechnology	331.96M
MGOL	MGO Global Inc.	Advertising Agencies	5.02M
MGPI	MGP Ingredients, Inc.	Beverages - Wineries & Distilleries	1.77B
MGRC	McGrath RentCorp	Rental & Leasing Services	2.72B
MGRM	Monogram Orthopaedics, Inc.	Medical Devices	76.32M
MGRX	Mangoceuticals, Inc.	Health Information Services	10.28M
MGTX	MeiraGTx Holdings plc	Biotechnology	314.46M
MGX	Metagenomi, Inc.	Biotechnology	154.54M
MGY	Magnolia Oil & Gas Corporation	Oil & Gas Exploration & Production	4.80B
MGYR	Magyar Bancorp, Inc.	Banks - Regional	82.53M
MHH	Mastech Digital, Inc.	Staffing & Employment Services	103.43M
MHK	Mohawk Industries, Inc.	Furnishings, Fixtures & Appliances	10.36B
MHLD	Maiden Holdings, Ltd.	Insurance - Reinsurance	197.40M
MHO	M/I Homes, Inc.	Residential Construction	4.53B
MHUA	Meihua International Medical Technologies Co., Ltd.	Medical Instruments & Supplies	26.11M
MI	NFT Limited	Internet Retail	3.39M
MICS	The Singing Machine Company, Inc.	Consumer Electronics	3.95M
MIDD	The Middleby Corporation	Specialty Industrial Machinery	7.08B
MIGI	Mawson Infrastructure Group, Inc.	Capital Markets	20.67M
MIND	MIND Technology, Inc.	Scientific & Technical Instruments	6.55M
MIR	Mirion Technologies, Inc.	Specialty Industrial Machinery	2.41B
MIRA	MIRA Pharmaceuticals, Inc.	Drug Manufacturers - General	34.88M
MIRM	Mirum Pharmaceuticals, Inc.	Biotechnology	1.92B
MIST	Milestone Pharmaceuticals Inc.	Biotechnology	78.81M
MITA	Coliseum Acquisition Corp.	Shell Companies	72.89M
MITK	Mitek Systems, Inc.	Software - Application	621.38M
MITQ	Moving iMage Technologies, Inc.	Communication Equipment	6.73M
MITT	AG Mortgage Investment Trust, Inc.	REIT - Mortgage	228.27M
MKC	McCormick & Company, Incorporated	Packaged Foods	20.52B
MKC.V	McCormick & Company, Incorporated	Packaged Foods	20.56B
MKFG	Markforged Holding Corporation	Computer Hardware	75.61M
MKL	Markel Corporation	Insurance - Property & Casualty	21.48B
MKSI	MKS Instruments, Inc.	Scientific & Technical Instruments	8.04B
MKTW	MarketWise, Inc.	Financial Data & Stock Exchanges	48.18M
MKTX	MarketAxess Holdings Inc.	Capital Markets	8.54B
ML	MoneyLion Inc.	Software - Application	705.21M
MLAB	Mesa Laboratories, Inc.	Scientific & Technical Instruments	594.28M
MLCO	Melco Resorts & Entertainment Limited	Resorts & Casinos	2.54B
MLEC	Moolec Science SA	Biotechnology	36.44M
MLGO	MicroAlgo Inc.	Software - Infrastructure	9.82M
MLI	Mueller Industries, Inc.	Metal Fabrication	7.89B
MLKN	MillerKnoll, Inc.	Furnishings, Fixtures & Appliances	2.13B
MLM	Martin Marietta Materials, Inc.	Building Materials	35.85B
MLNK	MeridianLink, Inc.	Software - Application	1.82B
MLP	Maui Land & Pineapple Company, Inc.	Real Estate Services	462.71M
MLR	Miller Industries, Inc.	Auto Parts	794.30M
MLSS	Milestone Scientific Inc.	Medical Instruments & Supplies	74.14M
MLTX	MoonLake Immunotherapeutics	Biotechnology	2.61B
MLYS	Mineralys Therapeutics, Inc.	Biotechnology	623.59M
MMA	Alta Global Group Limited	Leisure	26.07M
MMAT	Meta Materials Inc.	Electronic Components	15.06M
MMC	Marsh & McLennan Companies, Inc.	Insurance Brokers	108.95B
MMI	Marcus & Millichap, Inc.	Real Estate Services	1.53B
MMLP	Martin Midstream Partners L.P.	Oil & Gas Midstream	157.37M
MMM	3M Company	Conglomerates	70.16B
MMS	Maximus, Inc.	Specialty Business Services	5.68B
MMSI	Merit Medical Systems, Inc.	Medical Instruments & Supplies	4.94B
MMV	MultiMetaVerse Holdings Limited	Entertainment	21.75M
MMYT	MakeMyTrip Limited	Travel Services	10.11B
MNDO	MIND C.T.I. Ltd	Software - Application	38.15M
MNDR	Mobile-health Network Solutions	Health Information Services	36.42M
MNDY	monday.com Ltd.	Software - Application	11.43B
MNKD	MannKind Corporation	Biotechnology	1.56B
MNMD	Mind Medicine (MindMed) Inc.	Biotechnology	621.29M
MNOV	MediciNova, Inc.	Biotechnology	64.25M
MNPR	Monopar Therapeutics Inc.	Biotechnology	12.68M
MNR	Mach Natural Resources LP	Oil & Gas Exploration & Production	1.81B
MNRO	Monro, Inc.	Auto Parts	766.27M
MNSB	MainStreet Bancshares, Inc.	Banks - Regional	132.51M
MNSO	MINISO Group Holding Limited	Specialty Retail	4.97B
MNST	Monster Beverage Corporation	Beverages - Non-Alcoholic	53.69B
MNTK	Montauk Renewables, Inc.	Utilities - Diversified	817.64M
MNTN	Everest Consolidator Acquisition Corporation	Shell Companies	131.68M
MNTS	Momentus Inc.	Aerospace & Defense	9.50M
MNTX	Manitex International, Inc.	Farm & Heavy Construction Machinery	104.47M
MNY	MoneyHero Limited	Internet Content & Information	61.96M
MO	Altria Group, Inc.	Tobacco	87.21B
MOB	Mobilicom Ltd	Communication Equipment	5.55M
MOBX	Mobix Labs, Inc.	Semiconductors	35.07M
MOD	Modine Manufacturing Company	Auto Parts	5.30B
MODD	Modular Medical, Inc.	Medical Devices	49.13M
MODG	Topgolf Callaway Brands Corp.	Leisure	2.98B
MODV	ModivCare Inc.	Medical Care Facilities	327.06M
MOFG	MidWestOne Financial Group, Inc.	Banks - Regional	454.54M
MOG.A	Moog Inc.	Aerospace & Defense	6.24B
MOG.B	Moog Inc.	Aerospace & Defense	6.33B
MOGO	Mogo Inc.	Software - Infrastructure	34.57M
MOGU	MOGU Inc.	Internet Retail	17.39M
MOH	Molina Healthcare, Inc.	Healthcare Plans	20.25B
MOLN	Molecular Partners AG	Biotechnology	215.52M
MOMO	Hello Group Inc.	Internet Content & Information	1.26B
MOND	Mondee Holdings, Inc.	Travel Services	275.68M
MOR	MorphoSys AG	Biotechnology	2.80B
MORF	Morphic Holding, Inc.	Biotechnology	2.84B
MORN	Morningstar, Inc.	Financial Data & Stock Exchanges	13.80B
MOS	The Mosaic Company	Agricultural Inputs	9.45B
MOV	Movado Group, Inc.	Luxury Goods	405.59M
MOVE	Movano Inc.	Medical Devices	38.53M
MP	MP Materials Corp.	Other Industrial Metals & Mining	2.18B
MPAA	Motorcar Parts of America, Inc.	Auto Parts	119.98M
MPB	Mid Penn Bancorp, Inc.	Banks - Regional	485.99M
MPC	Marathon Petroleum Corporation	Oil & Gas Refining & Marketing	62.56B
MPLN	MultiPlan Corporation	Health Information Services	306.36M
MPLX	MPLX LP	Oil & Gas Midstream	43.84B
MPTI	M-tron Industries, Inc.	Electronic Components	93.33M
MPU	Mega Matrix Corp.	Entertainment	78.79M
MPW	Medical Properties Trust, Inc.	REIT - Healthcare Facilities	2.93B
MPWR	Monolithic Power Systems, Inc.	Semiconductors	38.80B
MPX	Marine Products Corporation	Recreational Vehicles	361.67M
MQ	Marqeta, Inc.	Software - Infrastructure	2.81B
MRAM	Everspin Technologies, Inc.	Semiconductors	130.20M
MRBK	Meridian Corporation	Banks - Regional	129.19M
MRC	MRC Global Inc.	Oil & Gas Equipment & Services	1.24B
MRCC	Monroe Capital Corporation	Asset Management	165.96M
MRCY	Mercury Systems, Inc.	Aerospace & Defense	2.03B
MRDB	MariaDB plc	Software - Infrastructure	37.43M
MREO	Mereo BioPharma Group plc	Biotechnology	565.29M
MRIN	Marin Software Incorporated	Software - Application	7.38M
MRK	Merck & Co., Inc.	Drug Manufacturers - General	292.77B
MRKR	Marker Therapeutics, Inc.	Biotechnology	44.34M
MRM	MEDIROM Healthcare Technologies Inc.	Personal Services	19.38M
MRNA	Moderna, Inc.	Biotechnology	45.98B
MRNO	Murano Global Investments PLC	Real Estate - Development	634.74M
MRNS	Marinus Pharmaceuticals, Inc.	Biotechnology	77.45M
MRO	Marathon Oil Corporation	Oil & Gas Exploration & Production	15.53B
MRSN	Mersana Therapeutics, Inc.	Biotechnology	243.50M
MRT	Marti Technologies, Inc.	Software - Application	92.92M
MRTN	Marten Transport, Ltd.	Trucking	1.53B
MRUS	Merus N.V.	Biotechnology	3.58B
MRVI	Maravai LifeSciences Holdings, Inc.	Biotechnology	1.24B
MRVL	Marvell Technology, Inc.	Semiconductors	54.63B
MRX	Marex Group plc	Capital Markets	1.54B
MS	Morgan Stanley	Capital Markets	168.15B
MSA	MSA Safety Incorporated	Security & Protection Services	7.37B
MSAI	MultiSensor AI Holdings, Inc.	Software - Infrastructure	38.44M
MSB	Mesabi Trust	Steel	223.70M
MSBI	Midland States Bancorp, Inc.	Banks - Regional	497.52M
MSC	Studio City International Holdings Limited	Resorts & Casinos	1.25B
MSCI	MSCI Inc.	Financial Data & Stock Exchanges	42.81B
MSDL	Morgan Stanley Direct Lending Fund	null	1.82B
MSEX	Middlesex Water Company	Utilities - Regulated Water	1.16B
MSFT	Microsoft Corporation	Software - Infrastructure	3,121.16B
MSGE	Madison Square Garden Entertainment Corp.	Leisure	1.89B
MSGM	Motorsport Games Inc.	Electronic Gaming & Multimedia	4.75M
MSGS	Madison Square Garden Sports Corp.	Entertainment	4.79B
MSI	Motorola Solutions, Inc.	Communication Equipment	66.10B
MSM	MSC Industrial Direct Co., Inc.	Industrial Distribution	4.96B
MSN	Emerson Radio Corp.	Consumer Electronics	10.10M
MSS	Maison Solutions Inc.	Grocery Stores	15.14M
MSSA	Metal Sky Star Acquisition Corporation	Shell Companies	72.72M
MSTR	MicroStrategy Incorporated	Software - Application	28.75B
MT	ArcelorMittal S.A.	Steel	18.32B
MTA	Metalla Royalty & Streaming Ltd.	Other Precious Metals & Mining	267.61M
MTAL	Metals Acquisition Corp	Shell Companies	946.43M
MTB	M&T Bank Corporation	Banks - Regional	29.08B
MTC	MMTec, Inc.	Software - Application	60.82M
MTCH	Match Group, Inc.	Internet Content & Information	8.93B
MTD	Mettler-Toledo International Inc.	Diagnostics & Research	31.84B
MTDR	Matador Resources Company	Oil & Gas Exploration & Production	7.49B
MTEK	Maris-Tech Ltd.	Electronic Components	13.24M
MTEM	Molecular Templates, Inc.	Biotechnology	9.68M
MTEN	Mingteng International Corporation Inc.	Manufacturing - Metal Fabrication	22.17M
MTEX	Mannatech, Incorporated	Food Distribution	13.93M
MTG	MGIC Investment Corporation	Insurance - Specialty	6.60B
MTH	Meritage Homes Corporation	Residential Construction	7.33B
MTLS	Materialise NV	Software - Application	331.96M
MTN	Vail Resorts, Inc.	Resorts & Casinos	6.89B
MTNB	Matinas BioPharma Holdings, Inc.	Biotechnology	41.76M
MTR	Mesa Royalty Trust	Oil & Gas Exploration & Production	15.52M
MTRN	Materion Corporation	Other Industrial Metals & Mining	2.49B
MTRX	Matrix Service Company	Engineering & Construction	279.64M
MTSI	MACOM Technology Solutions Holdings, Inc.	Semiconductors	6.92B
MTTR	Matterport, Inc.	Software - Application	1.40B
MTUS	Metallus Inc.	Steel	957.51M
MTW	The Manitowoc Company, Inc.	Farm & Heavy Construction Machinery	452.44M
MTX	Minerals Technologies Inc.	Specialty Chemicals	2.54B
MTZ	MasTec, Inc.	Engineering & Construction	8.43B
MU	Micron Technology, Inc.	Semiconductors	114.94B
MUFG	Mitsubishi UFJ Financial Group, Inc.	Banks - Diversified	128.46B
MULN	Mullen Automotive, Inc.	Auto Manufacturers	18.43M
MUR	Murphy Oil Corporation	Oil & Gas Exploration & Production	6.13B
MURA	Mural Oncology plc	Biotechnology	57.12M
MUSA	Murphy USA Inc.	Specialty Retail	10.48B
MUX	McEwen Mining Inc.	Other Precious Metals & Mining	455.19M
MVBF	MVB Financial Corp.	Banks - Regional	306.17M
MVIS	MicroVision, Inc.	Scientific & Technical Instruments	210.79M
MVST	Microvast Holdings, Inc.	Electrical Equipment & Parts	124.56M
MWA	Mueller Water Products, Inc.	Specialty Industrial Machinery	3.19B
MWG	Multi Ways Holdings Limited	Rental & Leasing Services	14.81M
MX	Magnachip Semiconductor Corporation	Semiconductors	188.47M
MXC	Mexco Energy Corporation	Oil & Gas Exploration & Production	21.79M
MXCT	MaxCyte, Inc.	Medical Devices	484.97M
MXL	MaxLinear, Inc.	Semiconductors	1.09B
MYE	Myers Industries, Inc.	Packaging & Containers	538.60M
MYFW	First Western Financial, Inc.	Banks - Regional	165.49M
MYGN	Myriad Genetics, Inc.	Diagnostics & Research	2.56B
MYNA	Mynaric AG	Communication Equipment	106.72M
MYND	Mynd.ai, Inc.	Education & Training Services	127.81M
MYNZ	Mainz Biomed B.V.	Diagnostics & Research	7.17M
MYO	Myomo, Inc.	Medical Devices	125.92M
MYPS	PLAYSTUDIOS, Inc.	Electronic Gaming & Multimedia	283.76M
MYRG	MYR Group Inc.	Engineering & Construction	2.36B
MYSZ	My Size, Inc.	Software - Application	2.29M
MYTE	MYT Netherlands Parent B.V.	Luxury Goods	355.58M
NA	Nano Labs Ltd	Semiconductors	28.30M
NAAS	NaaS Technology Inc.	Specialty Retail	64.51M
NABL	N-able, Inc.	Information Technology Services	2.54B
NAII	Natural Alternatives International, Inc.	Packaged Foods	36.03M
NAK	Northern Dynasty Minerals Ltd.	Other Industrial Metals & Mining	206.38M
NAMS	NewAmsterdam Pharma Company N.V.	Biotechnology	1.58B
NAOV	NanoVibronix, Inc.	Medical Devices	2.06M
NAPA	The Duckhorn Portfolio, Inc.	Beverages - Wineries & Distilleries	1.07B
NARI	Inari Medical, Inc.	Medical Devices	3.01B
NAT	Nordic American Tankers Limited	Marine Shipping	766.28M
NATH	Nathan's Famous, Inc.	Restaurants	298.18M
NATL	NCR Atleos Corporation	Software - Application	2.28B
NATR	Nature's Sunshine Products, Inc.	Packaged Foods	316.16M
NAUT	Nautilus Biotechnology, Inc.	Biotechnology	331.95M
NAVI	Navient Corporation	Credit Services	1.80B
NB	NioCorp Developments Ltd.	Other Industrial Metals & Mining	65.01M
NBBK	NB Bancorp, Inc.	Banks - Regional	807.57M
NBHC	National Bank Holdings Corporation	Banks - Regional	1.61B
NBIX	Neurocrine Biosciences, Inc.	Drug Manufacturers - Specialty & Generic	14.38B
NBN	Northeast Bank	Banks - Regional	573.32M
NBR	Nabors Industries Ltd.	Oil & Gas Drilling	921.78M
NBST	Newbury Street Acquisition Corporation	Shell Companies	53.70M
NBTB	NBT Bancorp Inc.	Banks - Regional	2.32B
NBTX	Nanobiotix S.A.	Biotechnology	247.33M
NBY	NovaBay Pharmaceuticals, Inc.	Biotechnology	839.97K
NC	NACCO Industries, Inc.	Thermal Coal	223.64M
NCDL	Nuveen Churchill Direct Lending Corp.	Asset Management	964.81M
NCI	Neo-Concept International Group Holdings Limited	Apparel Manufacturing	10.77M
NCL	Northann Corp.	Furnishings, Fixtures & Appliances	5.57M
NCLH	Norwegian Cruise Line Holdings Ltd.	Travel Services	7.97B
NCMI	National CineMedia, Inc.	Advertising Agencies	565.44M
NCNA	NuCana plc	Biotechnology	8.61M
NCNC	noco-noco Inc.	Auto Parts	20.15M
NCNO	nCino, Inc.	Software - Application	3.77B
NCPL	Netcapital Inc.	Capital Markets	2.97M
NCRA	Nocera, Inc.	Packaged Foods	13.42M
NCSM	NCS Multistage Holdings, Inc.	Oil & Gas Equipment & Services	43.80M
NCTY	The9 Limited	Capital Markets	63.17M
NDAQ	Nasdaq, Inc.	Financial Data & Stock Exchanges	40.23B
NDLS	Noodles & Company	Restaurants	80.26M
NDRA	ENDRA Life Sciences Inc.	Diagnostics & Research	6.48M
NDSN	Nordson Corporation	Specialty Industrial Machinery	14.11B
NE	Noble Corporation	Oil & Gas Drilling	6.52B
NECB	Northeast Community Bancorp, Inc.	Banks - Regional	310.41M
NEE	NextEra Energy, Inc.	Utilities - Regulated Electric	151.50B
NEGG	Newegg Commerce, Inc.	Internet Retail	334.50M
NEM	Newmont Corporation	Gold	53.98B
NEN	New England Realty Associates LP	Real Estate Services	248.14M
NEO	NeoGenomics, Inc.	Diagnostics & Research	2.27B
NEOG	Neogen Corporation	Diagnostics & Research	3.73B
NEON	Neonode Inc.	Electronic Components	44.71M
NEOV	NeoVolta Inc.	Electrical Equipment & Parts	92.40M
NEP	NextEra Energy Partners, LP	Utilities - Renewable	2.47B
NEPH	Nephros, Inc.	Medical Instruments & Supplies	23.51M
NERV	Minerva Neurosciences, Inc.	Biotechnology	21.05M
NET	Cloudflare, Inc.	Software - Infrastructure	25.95B
NETD	Nabors Energy Transition Corp. II	Shell Companies	404.13M
NEU	NewMarket Corporation	Specialty Chemicals	5.41B
NEUE	NeueHealth, Inc.	Healthcare Plans	54.04M
NEWP	New Pacific Metals Corp.	Other Precious Metals & Mining	257.10M
NEWT	Newtek Business Services Corp.	Banks - Regional	333.41M
NEXA	Nexa Resources S.A.	Other Industrial Metals & Mining	947.60M
NEXN	Nexxen International Ltd.	Advertising Agencies	460.66M
NEXT	NextDecade Corporation	Oil & Gas Exploration & Production	2.04B
NFBK	Northfield Bancorp, Inc. (Staten Island, NY)	Banks - Regional	562.95M
NFE	New Fortress Energy Inc.	Utilities - Regulated Gas	3.95B
NFG	National Fuel Gas Company	Oil & Gas Integrated	5.36B
NFGC	New Found Gold Corp.	Gold	519.06M
NFLX	Netflix, Inc.	Entertainment	267.38B
NG	NovaGold Resources Inc.	Gold	1.58B
NGD	New Gold Inc.	Gold	1.60B
NGG	National Grid plc	Utilities - Regulated Electric	62.42B
NGL	NGL Energy Partners LP	Oil & Gas Midstream	613.54M
NGNE	Neurogene Inc.	Biotechnology	515.97M
NGS	Natural Gas Services Group, Inc.	Oil & Gas Equipment & Services	247.50M
NGVC	Natural Grocers by Vitamin Cottage, Inc.	Grocery Stores	599.88M
NGVT	Ingevity Corporation	Specialty Chemicals	1.67B
NHC	National HealthCare Corporation	Medical Care Facilities	2.12B
NHI	National Health Investors, Inc.	REIT - Healthcare Facilities	3.25B
NHTC	Natural Health Trends Corp.	Internet Retail	83.73M
NI	NiSource Inc.	Utilities - Regulated Gas	14.03B
NIC	Nicolet Bankshares, Inc.	Banks - Regional	1.53B
NICE	NICE Ltd.	Software - Application	11.42B
NICK	Nicholas Financial, Inc.	Credit Services	47.23M
NINE	Nine Energy Service, Inc.	Oil & Gas Equipment & Services	65.77M
NIO	NIO Inc.	Auto Manufacturers	8.39B
NIPG	NIP Group Inc.	Entertainment	690.05M
NISN	Nisun International Enterprise Development Group Co., Ltd	Credit Services	46.04M
NITO	N2OFF, Inc.	Agricultural Inputs	1.65M
NIU	Niu Technologies	Auto Manufacturers	153.52M
NIVF	NewGenIvf Group Limited	Medical - Healthcare Plans	9.34M
NJR	New Jersey Resources Corporation	Utilities - Regulated Gas	4.63B
NKE	NIKE, Inc.	Footwear & Accessories	110.88B
NKGN	NKGen Biotech, Inc.	Biotechnology	27.96M
NKLA	Nikola Corporation	Farm & Heavy Construction Machinery	414.65M
NKSH	National Bankshares, Inc.	Banks - Regional	179.41M
NKTR	Nektar Therapeutics	Biotechnology	249.35M
NKTX	Nkarta, Inc.	Biotechnology	455.22M
NL	NL Industries, Inc.	Security & Protection Services	293.51M
NLOP	Net Lease Office Properties	REIT - Office	434.83M
NLSP	NLS Pharmaceutics AG	Biotechnology	10.41M
NLY	Annaly Capital Management, Inc.	REIT - Mortgage	10.08B
NMFC	New Mountain Finance Corporation	Asset Management	1.34B
NMG	Nouveau Monde Graphite Inc.	Other Industrial Metals & Mining	180.08M
NMHI	Nature's Miracle Holding Inc.	Specialty Industrial Machinery	5.10M
NMIH	NMI Holdings, Inc.	Insurance - Specialty	3.17B
NMM	Navios Maritime Partners L.P.	Marine Shipping	1.38B
NMR	Nomura Holdings, Inc.	Capital Markets	17.68B
NMRA	Neumora Therapeutics, Inc.	Biotechnology	2.01B
NMRK	Newmark Group, Inc.	Real Estate Services	2.19B
NMTC	NeuroOne Medical Technologies Corporation	Medical Devices	21.38M
NN	NextNav Inc.	Software - Infrastructure	981.91M
NNAG	99 Acquisition Group Inc.	Shell Companies	105.58M
NNBR	NN, Inc.	Conglomerates	186.02M
NNDM	Nano Dimension Ltd.	Computer Hardware	577.19M
NNE	Nano Nuclear Energy Inc.	Specialty Industrial Machinery	394.73M
NNI	Nelnet, Inc.	Credit Services	4.11B
NNN	NNN REIT Inc	REIT - Retail	8.41B
NNOX	Nano-X Imaging Ltd.	Medical Devices	497.48M
NNVC	NanoViricides, Inc.	Biotechnology	23.86M
NOA	North American Construction Group Ltd.	Oil & Gas Equipment & Services	519.88M
NOAH	Noah Holdings Limited	Asset Management	503.97M
NOC	Northrop Grumman Corporation	Aerospace & Defense	70.73B
NODK	NI Holdings, Inc.	Insurance - Property & Casualty	328.01M
NOG	Northern Oil and Gas, Inc.	Oil & Gas Exploration & Production	4.13B
NOK	Nokia Oyj	Communication Equipment	21.58B
NOMD	Nomad Foods Limited	Packaged Foods	2.96B
NOTE	FiscalNote Holdings, Inc.	Information Technology Services	215.01M
NOTV	Inotiv, Inc.	Diagnostics & Research	48.31M
NOV	NOV Inc.	Oil & Gas Equipment & Services	8.05B
NOVA	Sunnova Energy International Inc.	Solar	862.29M
NOVT	Novanta Inc.	Scientific & Technical Instruments	6.50B
NOVV	Nova Vision Acquisition Corporation	Shell Companies	40.09M
NOW	ServiceNow, Inc.	Software - Application	163.00B
NPAB	New Providence Acquisition Corp. II	Shell Companies	95.04M
NPCE	NeuroPace, Inc.	Medical Devices	211.73M
NPK	National Presto Industries, Inc.	Aerospace & Defense	547.37M
NPO	EnPro Industries, Inc.	Specialty Industrial Machinery	3.57B
NPWR	NET Power Inc.	Specialty Industrial Machinery	661.96M
NR	Newpark Resources, Inc.	Oil & Gas Equipment & Services	692.69M
NRBO	NeuroBo Pharmaceuticals, Inc.	Biotechnology	34.82M
NRC	National Research Corporation	Health Information Services	581.77M
NRDS	NerdWallet, Inc.	Internet Content & Information	1.23B
NRDY	Nerdy, Inc.	Software - Application	311.83M
NREF	NexPoint Real Estate Finance, Inc.	REIT - Mortgage	246.47M
NRG	NRG Energy, Inc.	Utilities - Independent Power Producers	15.31B
NRGV	Energy Vault Holdings, Inc.	Utilities - Renewable	165.22M
NRIM	Northrim BanCorp, Inc.	Banks - Regional	379.47M
NRIX	Nurix Therapeutics, Inc.	Biotechnology	1.36B
NRP	Natural Resource Partners L.P.	Thermal Coal	1.16B
NRSN	NeuroSense Therapeutics Ltd.	Biotechnology	14.07M
NRT	North European Oil Royalty Trust	Oil & Gas Exploration & Production	59.74M
NRXP	NRx Pharmaceuticals, Inc.	Biotechnology	24.61M
NRXS	NeurAxis, Inc.	Biotechnology	21.61M
NSA	National Storage Affiliates Trust	REIT - Industrial	5.04B
NSC	Norfolk Southern Corporation	Railroads	55.95B
NSIT	Insight Enterprises, Inc.	Electronics & Computer Distribution	7.24B
NSP	Insperity, Inc.	Staffing & Employment Services	3.89B
NSPR	InspireMD, Inc.	Medical Devices	80.16M
NSSC	Napco Security Technologies, Inc.	Security & Protection Services	1.99B
NSTS	NSTS Bancorp, Inc.	Banks - Regional	54.54M
NSYS	Nortech Systems Incorporated	Medical Devices	40.50M
NTAP	NetApp, Inc.	Computer Hardware	25.34B
NTB	The Bank of N.T. Butterfield & Son Limited	Banks - Diversified	1.82B
NTBL	Notable Labs, Ltd.	Biotechnology	6.09M
NTCT	NetScout Systems, Inc.	Software - Infrastructure	1.43B
NTES	NetEase, Inc.	Electronic Gaming & Multimedia	56.87B
NTGR	NETGEAR, Inc.	Communication Equipment	465.43M
NTIC	Northern Technologies International Corporation	Specialty Chemicals	123.21M
NTIP	Network-1 Technologies, Inc.	Specialty Business Services	37.30M
NTLA	Intellia Therapeutics, Inc.	Biotechnology	2.56B
NTNX	Nutanix, Inc.	Software - Infrastructure	12.06B
NTR	Nutrien Ltd.	Agricultural Inputs	25.04B
NTRA	Natera, Inc.	Diagnostics & Research	12.01B
NTRB	Nutriband Inc.	Biotechnology	83.32M
NTRP	NextTrip, Inc.	Travel Services	4.33M
NTRS	Northern Trust Corporation	Asset Management	18.31B
NTST	NETSTREIT Corp.	REIT - Retail	1.23B
NTWK	NetSol Technologies, Inc.	Software - Application	33.08M
NTZ	Natuzzi S.p.A.	Furnishings, Fixtures & Appliances	50.34M
NU	Nu Holdings Ltd.	Banks - Regional	57.99B
NUE	Nucor Corporation	Steel	38.39B
NUKK	Nukkleus Inc.	Software - Application	4.17M
NURO	NeuroMetrix, Inc.	Medical Devices	7.24M
NUS	Nu Skin Enterprises, Inc.	Household & Personal Products	536.90M
NUTX	Nutex Health, Inc.	Health Information Services	42.59M
NUVB	Nuvation Bio Inc.	Biotechnology	877.99M
NUVL	Nuvalent, Inc.	Biotechnology	5.06B
NUVO	Holdco Nuvo Group D.G Ltd.	Medical Devices	25.94M
NUWE	Nuwellis, Inc.	Medical Devices	1.42M
NUZE	NuZee, Inc.	Packaged Foods	8.99M
NVA	Nova Minerals Limited	Other Industrial Metals & Mining	1.23B
NVAC	NorthView Acquisition Corporation	Shell Companies	69.31M
NVAX	Novavax, Inc.	Biotechnology	1.70B
NVCR	NovoCure Limited	Medical Devices	2.53B
NVCT	Nuvectis Pharma, Inc.	Biotechnology	123.35M
NVDA	NVIDIA Corporation	Semiconductors	2,573.41B
NVEC	NVE Corporation	Semiconductors	398.78M
NVEE	NV5 Global, Inc.	Engineering & Construction	1.66B
NVEI	Nuvei Corporation	Software - Infrastructure	4.61B
NVFY	Nova LifeStyle, Inc.	Furnishings, Fixtures & Appliances	3.92M
NVGS	Navigator Holdings Ltd.	Oil & Gas Midstream	1.12B
NVMI	Nova Ltd.	Semiconductor Equipment & Materials	5.73B
NVNI	Nvni Group Limited	Software - Application	47.98M
NVNO	enVVeno Medical Corporation	Medical Devices	71.07M
NVO	Novo Nordisk A/S	Biotechnology	563.39B
NVOS	Novo Integrated Sciences, Inc.	Medical Care Facilities	11.95M
NVR	NVR, Inc.	Residential Construction	27.02B
NVRI	Enviri Corporation	Waste Management	881.94M
NVRO	Nevro Corp.	Medical Devices	354.62M
NVS	Novartis AG	Drug Manufacturers - General	217.62B
NVST	Envista Holdings Corporation	Medical Instruments & Supplies	2.87B
NVT	nVent Electric plc	Electrical Equipment & Parts	11.56B
NVTS	Navitas Semiconductor Corporation	Semiconductors	659.86M
NVVE	Nuvve Holding Corp.	Specialty Retail	3.74M
NVX	Novonix Limited	Electrical Equipment & Parts	221.73M
NWBI	Northwest Bancshares, Inc.	Banks - Regional	1.80B
NWE	NorthWestern Corporation	Utilities - Regulated Electric	3.27B
NWFL	Norwood Financial Corp.	Banks - Regional	223.11M
NWG	NatWest Group plc	Banks - Regional	39.49B
NWGL	Nature Wood Group Limited	Lumber & Wood Production	298.55M
NWL	Newell Brands Inc.	Household & Personal Products	3.54B
NWLI	National Western Life Group, Inc.	Insurance - Life	1.82B
NWN	Northwest Natural Holding Company	Utilities - Regulated Gas	1.55B
NWPX	Northwest Pipe Company	Metal Fabrication	369.95M
NWS	News Corporation	Entertainment	14.90B
NWSA	News Corporation	Entertainment	14.86B
NWTN	NWTN Inc.	Auto Manufacturers	271.90M
NX	Quanex Building Products Corporation	Building Products & Equipment	1.13B
NXE	NexGen Energy Ltd.	Uranium	3.45B
NXGL	NEXGEL, Inc.	Medical Instruments & Supplies	18.31M
NXL	Nexalin Technology, Inc.	Medical Devices	8.65M
NXPI	NXP Semiconductors N.V.	Semiconductors	64.52B
NXPL	NextPlat Corp	Software - Application	22.06M
NXRT	NexPoint Residential Trust, Inc.	REIT - Residential	1.12B
NXST	Nexstar Media Group, Inc.	Entertainment	5.97B
NXT	Nextracker Inc.	Solar	6.65B
NXTC	NextCure, Inc.	Biotechnology	45.04M
NXTT	Next Technology Holding Inc.	Software - Application	2.95M
NXU	Nxu, Inc.	Electrical Equipment & Parts	4.65M
NYAX	Nayax Ltd.	Information Technology Services	802.38M
NYC	American Strategic Investment Co	Real Estate Services	21.04M
NYCB	New York Community Bancorp, Inc.	Banks - Regional	3.71B
NYMT	New York Mortgage Trust, Inc.	REIT - Mortgage	597.54M
NYT	The New York Times Company	Publishing	8.67B
NYXH	Nyxoah S.A.	Medical Instruments & Supplies	283.13M
O	Realty Income Corporation	REIT - Retail	50.78B
OABI	OmniAb, Inc.	Biotechnology	553.42M
OAKU	Oak Woods Acquisition Corporation	Shell Companies	82.31M
OB	Outbrain Inc.	Internet Content & Information	234.93M
OBDC	Blue Owl Capital Corporation	Credit Services	6.09B
OBDE	Blue Owl Capital Corporation III	Asset Management	1.79B
OBE	Obsidian Energy Ltd.	Oil & Gas Exploration & Production	552.19M
OBIO	Orchestra BioMed Holdings, Inc.	Biotechnology	246.94M
OBK	Origin Bancorp, Inc.	Banks - Regional	1.08B
OBLG	Oblong, Inc.	Software - Application	4.85M
OBT	Orange County Bancorp, Inc.	Banks - Regional	333.39M
OC	Owens Corning	Building Products & Equipment	15.78B
OCC	Optical Cable Corporation	Communication Equipment	21.07M
OCEA	Ocean Biomedical, Inc.	Biotechnology	41.58M
OCFC	OceanFirst Financial Corp.	Banks - Regional	1.07B
OCFT	OneConnect Financial Technology Co., Ltd.	Software - Application	66.64M
OCG	Oriental Culture Holding LTD	Internet Retail	5.69M
OCGN	Ocugen, Inc.	Biotechnology	364.34M
OCS	Oculis Holding AG	Biotechnology	483.72M
OCSL	Oaktree Specialty Lending Corporation	Credit Services	1.48B
OCTO	Eightco Holdings Inc.	Packaging & Containers	3.19M
OCUL	Ocular Therapeutix, Inc.	Biotechnology	1.27B
OCUP	Ocuphire Pharma, Inc.	Biotechnology	52.89M
OCX	OncoCyte Corporation	Diagnostics & Research	43.84M
ODC	Oil-Dri Corporation of America	Specialty Chemicals	428.53M
ODD	Oddity Tech Ltd.	Software - Infrastructure	2.24B
ODFL	Old Dominion Freight Line, Inc.	Trucking	44.51B
ODP	The ODP Corporation	Specialty Retail	1.52B
ODV	Osisko Development Corp.	Gold	161.98M
OEC	Orion Engineered Carbons S.A.	Specialty Chemicals	1.40B
OESX	Orion Energy Systems, Inc.	Furnishings, Fixtures & Appliances	34.35M
OFG	OFG Bancorp	Banks - Regional	2.15B
OFIX	Orthofix Medical Inc.	Medical Devices	602.72M
OFLX	Omega Flex, Inc.	Specialty Industrial Machinery	532.58M
OFS	OFS Capital Corporation	Asset Management	114.96M
OGE	OGE Energy Corp.	Utilities - Regulated Electric	7.76B
OGEN	Oragenics, Inc.	Biotechnology	5.80M
OGI	OrganiGram Holdings Inc.	Drug Manufacturers - Specialty & Generic	169.51M
OGN	Organon & Co.	Drug Manufacturers - General	5.75B
OGS	ONE Gas, Inc.	Utilities - Regulated Gas	4.00B
OHI	Omega Healthcare Investors, Inc.	REIT - Healthcare Facilities	9.03B
OI	O-I Glass, Inc.	Packaging & Containers	1.81B
OII	Oceaneering International, Inc.	Oil & Gas Equipment & Services	2.96B
OIS	Oil States International, Inc.	Oil & Gas Equipment & Services	357.36M
OKE	ONEOK, Inc.	Oil & Gas Midstream	48.08B
OKLO	Oklo Inc.	Utilities - Regulated Electric	1.08B
OKTA	Okta, Inc.	Software - Infrastructure	14.90B
OKYO	OKYO Pharma Limited	Biotechnology	41.55M
OLB	The OLB Group, Inc.	Software - Infrastructure	4.80M
OLED	Universal Display Corporation	Electronic Components	10.30B
OLLI	Ollie's Bargain Outlet Holdings, Inc.	Discount Stores	6.06B
OLMA	Olema Pharmaceuticals, Inc.	Biotechnology	847.96M
OLN	Olin Corporation	Specialty Chemicals	5.36B
OLO	Olo Inc.	Software - Application	761.67M
OLP	One Liberty Properties, Inc.	REIT - Diversified	561.58M
OLPX	Olaplex Holdings, Inc.	Specialty Retail	1.33B
OM	Outset Medical, Inc.	Medical Devices	182.69M
OMAB	Grupo Aeroportuario del Centro Norte, SAB de CV	Airports & Air Services	3.31B
OMC	Omnicom Group Inc.	Advertising Agencies	19.02B
OMCL	Omnicell, Inc.	Health Information Services	1.33B
OMER	Omeros Corporation	Biotechnology	304.79M
OMEX	Odyssey Marine Exploration, Inc.	Other Industrial Metals & Mining	88.26M
OMF	OneMain Holdings, Inc.	Credit Services	6.35B
OMGA	Omega Therapeutics, Inc.	Biotechnology	101.49M
OMH	Ohmyhome Limited	Real Estate Services	12.07M
OMI	Owens & Minor, Inc.	Medical Distribution	1.19B
OMIC	Singular Genomics Systems, Inc.	Medical Instruments & Supplies	19.45M
ON	ON Semiconductor Corporation	Semiconductors	32.17B
ONB	Old National Bancorp	Banks - Regional	6.43B
ONCO	Onconetix, Inc.	Biotechnology	3.83M
ONCT	Oncternal Therapeutics, Inc.	Biotechnology	19.24M
ONCY	Oncolytics Biotech Inc.	Biotechnology	80.40M
ONDS	Ondas Holdings Inc.	Communication Equipment	63.94M
ONEW	OneWater Marine Inc.	Specialty Retail	379.43M
ONFO	Onfolio Holdings, Inc.	Internet Content & Information	4.49M
ONIT	Onity Group Inc.	Mortgage Finance	220.82M
ONL	Orion Office REIT Inc.	REIT - Office	226.79M
ONMD	OneMedNet Corporation	Health Information Services	34.34M
ONON	On Holding AG	Footwear & Accessories	12.41B
ONTF	ON24, Inc.	Software - Application	274.43M
ONTO	Onto Innovation Inc.	Semiconductor Equipment & Materials	8.88B
ONVO	Organovo Holdings, Inc.	Biotechnology	8.05M
ONYX	Onyx Acquisition Co. I	Shell Companies	89.39M
OOMA	Ooma, Inc.	Software - Application	267.83M
OP	OceanPal Inc.	Marine Shipping	13.49M
OPAD	Offerpad Solutions Inc.	Real Estate Services	120.40M
OPAL	OPAL Fuels Inc.	Utilities - Regulated Gas	116.10M
OPBK	OP Bancorp	Banks - Regional	190.62M
OPCH	Option Care Health, Inc.	Medical Care Facilities	5.47B
OPEN	Opendoor Technologies Inc.	Real Estate Services	1.61B
OPFI	OppFi Inc.	Credit Services	409.33M
OPGN	OpGen, Inc.	Medical Devices	4.07M
OPHC	OptimumBank Holdings, Inc.	Banks - Regional	43.07M
OPI	Office Properties Income Trust	REIT - Office	129.45M
OPK	OPKO Health, Inc.	Diagnostics & Research	1.00B
OPOF	Old Point Financial Corporation	Banks - Regional	90.60M
OPRA	Opera Limited	Internet Content & Information	1.08B
OPRT	Oportun Financial Corporation	Credit Services	111.04M
OPRX	OptimizeRx Corporation	Health Information Services	203.98M
OPT	Opthea Limited	Biotechnology	324.63M
OPTN	OptiNose, Inc.	Drug Manufacturers - Specialty & Generic	151.36M
OPTT	Ocean Power Technologies, Inc.	Specialty Industrial Machinery	21.56M
OPTX	Syntec Optics Holdings, Inc.	Electronic Components	57.67M
OPXS	Optex Systems Holdings, Inc	Aerospace & Defense	55.51M
OPY	Oppenheimer Holdings Inc.	Capital Markets	520.77M
OR	Osisko Gold Royalties Ltd	Gold	3.22B
ORA	Ormat Technologies, Inc.	Utilities - Renewable	4.61B
ORAN	Orange S.A.	Telecom Services	29.35B
ORC	Orchid Island Capital, Inc.	REIT - Mortgage	547.23M
ORCL	Oracle Corporation	Software - Infrastructure	374.98B
ORGN	Origin Materials, Inc.	Chemicals	133.05M
ORGO	Organogenesis Holdings Inc.	Drug Manufacturers - Specialty & Generic	407.00M
ORGS	Orgenesis Inc.	Biotechnology	29.27M
ORI	Old Republic International Corporation	Insurance - Diversified	9.38B
ORIC	ORIC Pharmaceuticals, Inc.	Biotechnology	743.33M
ORKT	Orangekloud Technology Inc.	Software - Application	122.65M
ORLA	Orla Mining Ltd.	Gold	1.19B
ORLY	O'Reilly Automotive, Inc.	Specialty Retail	66.64B
ORMP	Oramed Pharmaceuticals Inc.	Biotechnology	98.32M
ORN	Orion Group Holdings, Inc.	Engineering & Construction	272.70M
ORRF	Orrstown Financial Services, Inc.	Banks - Regional	676.17M
OS	OneStream, Inc.	Software - Application	6.39B
OSBC	Old Second Bancorp, Inc.	Banks - Regional	765.96M
OSCR	Oscar Health, Inc.	Healthcare Plans	3.46B
OSIS	OSI Systems, Inc.	Electronic Components	2.51B
OSK	Oshkosh Corporation	Farm & Heavy Construction Machinery	7.50B
OSPN	OneSpan Inc.	Software - Infrastructure	543.84M
OSS	One Stop Systems, Inc.	Computer Hardware	47.69M
OST	Ostin Technology Group Co., Ltd.	Electronic Components	4.93M
OSUR	OraSure Technologies, Inc.	Medical Instruments & Supplies	325.79M
OSW	OneSpaWorld Holdings Limited	Leisure	1.76B
OTEX	Open Text Corporation	Software - Application	8.54B
OTIS	Otis Worldwide Corporation	Specialty Industrial Machinery	37.26B
OTLK	Outlook Therapeutics, Inc.	Biotechnology	180.87M
OTLY	Oatly Group AB	Packaged Foods	574.25M
OTRK	Ontrak, Inc.	Health Information Services	12.14M
OTTR	Otter Tail Corporation	Utilities - Diversified	4.02B
OUST	Ouster, Inc.	Electronic Components	587.02M
OUT	Outfront Media Inc.	REIT - Specialty	2.63B
OVBC	Ohio Valley Banc Corp.	Banks - Regional	117.35M
OVID	Ovid Therapeutics Inc.	Biotechnology	73.43M
OVLY	Oak Valley Bancorp	Banks - Regional	227.38M
OVV	Ovintiv Inc.	Oil & Gas Exploration & Production	12.20B
OWL	Blue Owl Capital Inc.	Asset Management	27.36B
OWLT	Owlet, Inc.	Health Information Services	41.04M
OXBR	Oxbridge Re Holdings Limited	Insurance - Reinsurance	18.08M
OXM	Oxford Industries, Inc.	Apparel Manufacturing	1.65B
OXSQ	Oxford Square Capital Corp.	Asset Management	188.12M
OXY	Occidental Petroleum Corporation	Oil & Gas Exploration & Production	53.45B
OZ	Belpointe PREP, LLC	Real Estate - Development	258.61M
OZK	Bank OZK	Banks - Regional	5.29B
PAA	Plains All American Pipeline, L.P.	Oil & Gas Midstream	12.98B
PAAS	Pan American Silver Corp.	Gold	8.01B
PAC	Grupo Aeroportuario del Pacífico, SAB de CV	Airports & Air Services	8.12B
PACB	Pacific Biosciences of California, Inc.	Medical Devices	547.44M
PACK	Ranpak Holdings Corp.	Packaging & Containers	553.31M
PACS	PACS Group, Inc.	Medical Care Facilities	5.33B
PAG	Penske Automotive Group, Inc.	Auto & Truck Dealerships	10.91B
PAGP	Plains GP Holdings, L.P.	Oil & Gas Midstream	3.83B
PAGS	PagSeguro Digital Ltd.	Software - Infrastructure	4.19B
PAHC	Phibro Animal Health Corporation	Drug Manufacturers - Specialty & Generic	754.18M
PAL	Proficient Auto Logistics, Inc.	Integrated Freight & Logistics	523.62M
PALI	Palisade Bio, Inc.	Biotechnology	3.16M
PALT	Paltalk, Inc.	Software - Application	41.78M
PAM	Pampa Energía S.A.	Utilities - Independent Power Producers	3.49B
PANL	Pangaea Logistics Solutions, Ltd.	Marine Shipping	328.41M
PANW	Palo Alto Networks, Inc.	Software - Infrastructure	103.04B
PAPL	Pineapple Financial Inc.	Mortgage Finance	7.71M
PAR	PAR Technology Corporation	Software - Application	1.74B
PARA	Paramount Global	Entertainment	7.87B
PARAA	Paramount Global	Entertainment	7.89B
PARR	Par Pacific Holdings, Inc.	Oil & Gas Refining & Marketing	1.49B
PASG	Passage Bio, Inc.	Biotechnology	60.10M
PATH	UiPath Inc.	Software - Infrastructure	6.92B
PATK	Patrick Industries, Inc.	Furnishings, Fixtures & Appliances	2.83B
PAVM	PAVmed Inc.	Medical Devices	8.86M
PAVS	Paranovus Entertainment Technology Ltd.	Packaged Foods	7.41M
PAX	Patria Investments Limited	Asset Management	1.97B
PAY	Paymentus Holdings, Inc.	Software - Infrastructure	2.67B
PAYC	Paycom Software, Inc.	Software - Application	9.54B
PAYO	Payoneer Global Inc.	Software - Infrastructure	2.05B
PAYS	PaySign, Inc.	Software - Infrastructure	270.98M
PAYX	Paychex, Inc.	Staffing & Employment Services	46.21B
PB	Prosperity Bancshares, Inc.	Banks - Regional	6.97B
PBA	Pembina Pipeline Corporation	Oil & Gas Midstream	22.32B
PBBK	PB Bankshares, Inc.	Banks - Regional	40.26M
PBF	PBF Energy Inc.	Oil & Gas Refining & Marketing	4.77B
PBFS	Pioneer Bancorp, Inc.	Banks - Regional	289.13M
PBH	Prestige Consumer Healthcare Inc.	Drug Manufacturers - Specialty & Generic	3.52B
PBHC	Pathfinder Bancorp, Inc.	Banks - Regional	96.08M
PBI	Pitney Bowes Inc.	Integrated Freight & Logistics	1.18B
PBM	Psyence Biomedical Ltd.	Shell Companies	8.12M
PBPB	Potbelly Corporation	Restaurants	212.47M
PBR	Petróleo Brasileiro S.A. - Petrobras	Oil & Gas Integrated	88.46B
PBR.A	Petróleo Brasileiro S.A. - Petrobras	Oil & Gas Integrated	90.25B
PBT	Permian Basin Royalty Trust	Oil & Gas Midstream	512.93M
PBYI	Puma Biotechnology, Inc.	Biotechnology	178.00M
PCAR	PACCAR Inc	Farm & Heavy Construction Machinery	51.18B
PCB	PCB Bancorp	Banks - Regional	281.77M
PCG	PG&E Corporation	Utilities - Regulated Electric	39.27B
PCH	PotlatchDeltic Corporation	REIT - Specialty	3.53B
PCOR	Procore Technologies, Inc.	Software - Application	10.28B
PCRX	Pacira BioSciences, Inc.	Drug Manufacturers - Specialty & Generic	925.34M
PCSA	Processa Pharmaceuticals, Inc.	Biotechnology	6.43M
PCSC	Perceptive Capital Solutions Corp	Shell Companies	97.40M
PCT	PureCycle Technologies, Inc.	Pollution & Treatment Controls	1.26B
PCTY	Paylocity Holding Corporation	Software - Application	8.36B
PCVX	Vaxcyte, Inc.	Biotechnology	8.79B
PCYO	Pure Cycle Corporation	Utilities - Regulated Water	260.98M
PD	PagerDuty, Inc.	Software - Application	2.09B
PDCO	Patterson Companies, Inc.	Medical Distribution	2.32B
PDD	PDD Holdings Inc.	Internet Retail	165.02B
PDEX	Pro-Dex, Inc.	Medical Instruments & Supplies	68.89M
PDFS	PDF Solutions, Inc.	Software - Application	1.31B
PDLB	Ponce Financial Group, Inc.	Banks - Regional	237.64M
PDM	Piedmont Office Realty Trust, Inc.	REIT - Office	1.07B
PDS	Precision Drilling Corporation	Oil & Gas Drilling	1.03B
PDSB	PDS Biotechnology Corporation	Biotechnology	137.18M
PDYN	Palladyne AI Corp.	Software - Infrastructure	50.26M
PEB	Pebblebrook Hotel Trust	REIT - Hotel & Motel	1.66B
PEBK	Peoples Bancorp of North Carolina, Inc.	Banks - Regional	169.58M
PEBO	Peoples Bancorp Inc.	Banks - Regional	1.20B
PECO	Phillips Edison & Company, Inc.	REIT - Retail	4.34B
PED	PEDEVCO Corp.	Oil & Gas Exploration & Production	90.22M
PEG	Public Service Enterprise Group Incorporated	Utilities - Regulated Electric	38.67B
PEGA	Pegasystems Inc.	Software - Application	5.92B
PEGR	Project Energy Reimagined Acquisition Corp.	Shell Companies	128.90M
PEGY	Pineapple Energy Inc.	Solar	9.59M
PEN	Penumbra, Inc.	Medical Devices	6.69B
PENN	PENN Entertainment, Inc.	Resorts & Casinos	2.95B
PEP	PepsiCo, Inc.	Beverages - Non-Alcoholic	237.11B
PEPG	PepGen Inc.	Biotechnology	556.28M
PERF	Perfect Corp.	Software - Application	214.90M
PERI	Perion Network Ltd.	Internet Content & Information	404.08M
PESI	Perma-Fix Environmental Services, Inc.	Waste Management	194.83M
PET	Wag! Group Co.	Software - Application	54.27M
PETQ	PetIQ, Inc.	Drug Manufacturers - Specialty & Generic	636.46M
PETS	PetMed Express, Inc.	Pharmaceutical Retailers	83.05M
PETZ	TDH Holdings, Inc.	Restaurants	13.42M
PEV	Phoenix Motor Inc.	Auto Manufacturers	12.63M
PFBC	Preferred Bank	Banks - Regional	1.15B
PFC	Premier Financial Corp.	Banks - Regional	912.43M
PFE	Pfizer Inc.	Drug Manufacturers - General	173.09B
PFG	Principal Financial Group, Inc.	Asset Management	19.39B
PFGC	Performance Food Group Company	Food Distribution	10.65B
PFIE	Profire Energy, Inc.	Oil & Gas Equipment & Services	73.71M
PFIS	Peoples Financial Services Corp.	Banks - Regional	487.18M
PFLT	PennantPark Floating Rate Capital Ltd.	Asset Management	803.86M
PFMT	Performant Financial Corporation	Specialty Business Services	267.41M
PFS	Provident Financial Services, Inc.	Banks - Regional	2.45B
PFSI	PennyMac Financial Services, Inc.	Mortgage Finance	4.99B
PFTA	Perception Capital Corp. III	Shell Companies	114.27M
PFX	PhenixFIN Corporation	Asset Management	96.63M
PG	The Procter & Gamble Company	Household & Personal Products	379.19B
PGC	Peapack-Gladstone Financial Corporation	Banks - Regional	505.63M
PGEN	Precigen, Inc.	Biotechnology	387.46M
PGHL	Primega Group Holdings Limited	Waste Management	121.44M
PGNY	Progyny, Inc.	Health Information Services	2.79B
PGR	The Progressive Corporation	Insurance - Property & Casualty	126.52B
PGRE	Paramount Group, Inc.	REIT - Office	1.12B
PGRU	PropertyGuru Limited	Internet Content & Information	1.02B
PGY	Pagaya Technologies Ltd.	Software - Infrastructure	1.00B
PH	Parker-Hannifin Corporation	Specialty Industrial Machinery	70.37B
PHAR	Pharming Group N.V.	Biotechnology	590.85M
PHAT	Phathom Pharmaceuticals, Inc.	Biotechnology	666.13M
PHG	Koninklijke Philips N.V.	Medical Devices	26.59B
PHGE	BiomX Inc.	Biotechnology	13.31M
PHI	PLDT Inc.	Telecom Services	5.52B
PHIN	PHINIA Inc.	Auto Parts	1.86B
PHIO	Phio Pharmaceuticals Corp.	Biotechnology	1.68M
PHM	PulteGroup, Inc.	Residential Construction	27.57B
PHR	Phreesia, Inc.	Health Information Services	1.42B
PHUN	Phunware, Inc.	Software - Application	37.97M
PHVS	Pharvaris N.V.	Biotechnology	932.64M
PHX	PHX Minerals Inc.	Oil & Gas Exploration & Production	122.11M
PHYT	Pyrophyte Acquisition Corp.	Shell Companies	129.64M
PI	Impinj, Inc.	Communication Equipment	4.53B
PII	Polaris Inc.	Recreational Vehicles	4.60B
PIII	P3 Health Partners Inc.	Medical Care Facilities	222.50M
PIK	Kidpik Corp.	Internet Retail	5.27M
PINC	Premier, Inc.	Health Information Services	2.21B
PINE	Alpine Income Property Trust, Inc.	REIT - Retail	235.83M
PINS	Pinterest, Inc.	Internet Content & Information	25.58B
PIPR	Piper Sandler Companies	Capital Markets	4.93B
PIRS	Pieris Pharmaceuticals, Inc.	Biotechnology	20.20M
PIXY	ShiftPixy, Inc.	Staffing & Employment Services	10.61M
PJT	PJT Partners Inc.	Capital Markets	3.19B
PK	Park Hotels & Resorts Inc.	REIT - Hotel & Motel	3.20B
PKBK	Parke Bancorp, Inc.	Banks - Regional	231.90M
PKE	Park Aerospace Corp.	Aerospace & Defense	267.34M
PKG	Packaging Corporation of America	Packaging & Containers	17.89B
PKOH	Park-Ohio Holdings Corp.	Specialty Industrial Machinery	388.59M
PKST	Peakstone Realty Trust	REIT - Office	495.33M
PKX	POSCO Holdings Inc.	Steel	19.19B
PL	Planet Labs PBC	Aerospace & Defense	721.11M
PLAB	Photronics, Inc.	Semiconductor Equipment & Materials	1.57B
PLAG	Planet Green Holdings Corp.	Conglomerates	14.70M
PLAO	Patria Latin American Opportunity Acquisition Corp.	Shell Companies	263.42M
PLAY	Dave & Buster's Entertainment, Inc.	Entertainment	1.47B
PLBC	Plumas Bancorp	Banks - Regional	249.68M
PLBY	PLBY Group, Inc.	Leisure	61.16M
PLCE	The Children's Place, Inc.	Apparel Retail	104.33M
PLD	Prologis, Inc.	REIT - Industrial	115.48B
PLG	Platinum Group Metals Ltd.	Other Precious Metals & Mining	162.12M
PLL	Piedmont Lithium Inc.	Other Industrial Metals & Mining	186.33M
PLMI	Plum Acquisition Corp. I	Shell Companies	109.33M
PLMJ	Plum Acquisition Corp. III	Shell Companies	110.34M
PLMR	Palomar Holdings, Inc.	Insurance - Property & Casualty	2.27B
PLNT	Planet Fitness, Inc.	Leisure	6.48B
PLOW	Douglas Dynamics, Inc.	Auto Parts	704.60M
PLPC	Preformed Line Products Company	Electrical Equipment & Parts	639.94M
PLRX	Pliant Therapeutics, Inc.	Biotechnology	837.93M
PLSE	Pulse Biosciences, Inc.	Medical Instruments & Supplies	906.75M
PLTK	Playtika Holding Corp.	Electronic Gaming & Multimedia	2.82B
PLTR	Palantir Technologies Inc.	Software - Infrastructure	56.04B
PLUG	Plug Power Inc.	Electrical Equipment & Parts	1.91B
PLUR	Pluri Inc.	Biotechnology	31.74M
PLUS	ePlus inc.	Software - Application	2.39B
PLX	Protalix BioTherapeutics, Inc.	Biotechnology	81.75M
PLXS	Plexus Corp.	Electronic Components	3.43B
PLYA	Playa Hotels & Resorts N.V.	Resorts & Casinos	1.14B
PLYM	Plymouth Industrial REIT, Inc.	REIT - Industrial	1.10B
PM	Philip Morris International Inc.	Tobacco	178.07B
PMCB	PharmaCyte Biotech, Inc.	Biotechnology	16.96M
PMD	Psychemedics Corporation	Diagnostics & Research	12.73M
PMEC	Primech Holdings Ltd.	Specialty Business Services	19.64M
PMGM	Priveterra Acquisition Corp.	Shell Companies	97.48M
PMN	ProMIS Neurosciences, Inc.	Biotechnology	25.79M
PMNT	Perfect Moment Ltd.	Apparel Manufacturing	32.17M
PMT	PennyMac Mortgage Investment Trust	REIT - Mortgage	1.19B
PMTS	CPI Card Group Inc.	Credit Services	323.66M
PMVP	PMV Pharmaceuticals, Inc.	Biotechnology	86.17M
PNBK	Patriot National Bancorp, Inc.	Banks - Regional	6.92M
PNC	The PNC Financial Services Group, Inc.	Banks - Regional	72.36B
PNFP	Pinnacle Financial Partners, Inc.	Banks - Regional	7.44B
PNM	PNM Resources, Inc.	Utilities - Regulated Electric	3.74B
PNNT	PennantPark Investment Corporation	Asset Management	472.55M
PNR	Pentair plc	Specialty Industrial Machinery	14.55B
PNRG	PrimeEnergy Resources Corporation	Oil & Gas Exploration & Production	205.26M
PNST	Pinstripes Holdings Inc.	Restaurants	87.43M
PNTG	The Pennant Group, Inc.	Medical Care Facilities	895.36M
PNW	Pinnacle West Capital Corporation	Utilities - Regulated Electric	9.71B
POAI	Predictive Oncology Inc.	Medical Instruments & Supplies	4.88M
POCI	Precision Optics Corporation, Inc.	Medical Instruments & Supplies	37.48M
PODC	PodcastOne Inc	Internet Content & Information	35.21M
PODD	Insulet Corporation	Medical Devices	13.58B
POET	POET Technologies Inc.	Semiconductors	179.47M
POLA	Polar Power, Inc.	Electrical Equipment & Parts	7.38M
POOL	Pool Corporation	Industrial Distribution	14.22B
POR	Portland General Electric Company	Utilities - Regulated Electric	4.89B
POST	Post Holdings, Inc.	Packaged Foods	6.55B
POWI	Power Integrations, Inc.	Semiconductors	4.09B
POWL	Powell Industries, Inc.	Electrical Equipment & Parts	1.61B
POWW	AMMO, Inc.	Aerospace & Defense	221.08M
PPBI	Pacific Premier Bancorp, Inc.	Banks - Regional	2.57B
PPBT	Purple Biotech Ltd.	Biotechnology	12.59M
PPC	Pilgrim's Pride Corporation	Packaged Foods	9.89B
PPG	PPG Industries, Inc.	Specialty Chemicals	29.79B
PPIH	Perma-Pipe International Holdings, Inc.	Building Products & Equipment	75.45M
PPL	PPL Corporation	Utilities - Regulated Electric	22.09B
PPSI	Pioneer Power Solutions, Inc.	Electrical Equipment & Parts	47.27M
PPTA	Perpetua Resources Corp.	Other Precious Metals & Mining	413.08M
PPYA	Papaya Growth Opportunity Corp. I	Shell Companies	95.74M
PR	Permian Resources Corporation	Oil & Gas Exploration & Production	11.77B
PRA	ProAssurance Corporation	Insurance - Property & Casualty	623.37M
PRAA	PRA Group, Inc.	Credit Services	1.00B
PRAX	Praxis Precision Medicines, Inc.	Biotechnology	979.43M
PRCH	Porch Group, Inc.	Software - Application	194.90M
PRCT	PROCEPT BioRobotics Corporation	Medical Devices	3.20B
PRDO	Perdoceo Education Corporation	Education & Training Services	1.66B
PRE	Prenetics Global Limited	Diagnostics & Research	68.42M
PRFT	Perficient, Inc.	Information Technology Services	2.65B
PRFX	PainReform Ltd.	Drug Manufacturers - Specialty & Generic	1.42M
PRG	PROG Holdings, Inc.	Rental & Leasing Services	1.92B
PRGO	Perrigo Company plc	Drug Manufacturers - Specialty & Generic	3.82B
PRGS	Progress Software Corporation	Software - Infrastructure	2.51B
PRI	Primerica, Inc.	Insurance - Life	8.70B
PRIM	Primoris Services Corporation	Engineering & Construction	2.89B
PRK	Park National Corporation	Banks - Regional	2.91B
PRKS	United Parks & Resorts Inc.	Leisure	3.29B
PRLB	Proto Labs, Inc.	Metal Fabrication	864.80M
LRFC	Logan Ridge Finance Corporation	Asset Management	59.62M
LRHC	La Rosa Holding Corp.	Real Estate Services	16.66M
LRMR	Larimar Therapeutics, Inc.	Biotechnology	543.59M
LRN	Stride, Inc.	Education & Training Services	3.29B
LSAK	Lesaka Technologies, Inc.	Software - Infrastructure	309.43M
LSB	LakeShore Biopharma Co., Ltd	Biotechnology	88.59M
LSBK	Lake Shore Bancorp, Inc.	Banks - Regional	70.97M
LSCC	Lattice Semiconductor Corporation	Semiconductors	7.03B
LSEA	Landsea Homes Corporation	Real Estate - Development	440.66M
LSF	Laird Superfood, Inc.	Packaged Foods	40.09M
LSH	Lakeside Holding Limited	Integrated Freight & Logistics	18.85M
LSPD	Lightspeed Commerce Inc.	Software - Application	2.05B
LSTA	Lisata Therapeutics, Inc.	Biotechnology	27.83M
LSTR	Landstar System, Inc.	Integrated Freight & Logistics	6.93B
LSXMA	Liberty SiriusXM Group - Series A	Broadcasting	7.40B
LSXMB	Liberty SiriusXM Group - Series B	Broadcasting	7.58B
LSXMK	Liberty SiriusXM Group - Series C	Broadcasting	7.25B
LTBR	Lightbridge Corporation	Electrical Equipment & Parts	43.45M
LTC	LTC Properties, Inc.	REIT - Healthcare Facilities	1.56B
LTH	Life Time Group Holdings, Inc.	Leisure	4.08B
LTM	LATAM Airlines Group S.A.	Airlines	7.56B
LTRN	Lantern Pharma Inc.	Biotechnology	49.28M
LTRX	Lantronix, Inc.	Communication Equipment	146.56M
LTRY	Lottery.com Inc.	Gambling	4.78M
LU	Lufax Holding Ltd	Credit Services	1.53B
LUCD	Lucid Diagnostics Inc.	Medical Devices	44.66M
LUCY	Innovative Eyewear, Inc.	Medical Instruments & Supplies	6.28M
LULU	Lululemon Athletica Inc.	Apparel Retail	30.74B
LUMN	Lumen Technologies, Inc.	Telecom Services	2.47B
LUMO	Lumos Pharma, Inc.	Biotechnology	14.29M
LUNA	Luna Innovations Incorporated	Scientific & Technical Instruments	105.61M
LUNG	Pulmonx Corporation	Medical Devices	273.30M
LUNR	Intuitive Machines, Inc.	Aerospace & Defense	481.70M
LUV	Southwest Airlines Co.	Airlines	16.29B
LUXH	LuxUrban Hotels Inc.	Lodging	15.72M
LVLU	Lulu's Fashion Lounge Holdings, Inc.	Apparel Retail	66.95M
LVO	LiveOne, Inc.	Entertainment	160.81M
LVRO	Lavoro Limited	Agricultural Inputs	607.53M
LVS	Las Vegas Sands Corp.	Resorts & Casinos	29.65B
LVTX	LAVA Therapeutics N.V.	Biotechnology	52.06M
LVWR	LiveWire Group, Inc.	Auto Manufacturers	1.34B
LW	Lamb Weston Holdings, Inc.	Packaged Foods	8.38B
LWAY	Lifeway Foods, Inc.	Packaged Foods	173.55M
LWLG	Lightwave Logic, Inc.	Specialty Chemicals	404.72M
LX	LexinFintech Holdings Ltd.	Credit Services	290.96M
LXEH	Lixiang Education Holding Co., Ltd.	Education & Training Services	3.36M
LXEO	Lexeo Therapeutics, Inc.	Biotechnology	413.46M
LXFR	Luxfer Holdings PLC	Specialty Industrial Machinery	357.07M
LXP	LXP Industrial Trust	REIT - Industrial	3.05B
LXRX	Lexicon Pharmaceuticals, Inc.	Biotechnology	806.13M
LXU	LSB Industries, Inc.	Chemicals	626.01M
LYB	LyondellBasell Industries N.V.	Specialty Chemicals	31.88B
LYEL	Lyell Immunopharma, Inc.	Biotechnology	404.08M
LYFT	Lyft, Inc.	Software - Application	4.70B
LYG	Lloyds Banking Group plc	Banks - Regional	47.17B
LYRA	Lyra Therapeutics, Inc.	Biotechnology	18.48M
LYT	Lytus Technologies Holdings PTV. Ltd.	Software - Application	2.76M
LYTS	LSI Industries Inc.	Electronic Components	467.53M
LYV	Live Nation Entertainment, Inc.	Entertainment	21.68B
LZ	LegalZoom.com, Inc.	Specialty Business Services	1.23B
LZB	La-Z-Boy Incorporated	Furnishings, Fixtures & Appliances	1.85B
LZM	Lifezone Metals Limited	Other Industrial Metals & Mining	556.00M
M	Macy's, Inc.	Department Stores	4.77B
MA	Mastercard Incorporated	Credit Services	411.02B
MAA	Mid-America Apartment Communities, Inc.	REIT - Residential	16.45B
MAC	The Macerich Company	REIT - Retail	3.56B
MACA	Moringa Acquisition Corp	Shell Companies	45.74M
MACI	Melar Acquisition Corp. I	Shell Companies	220.11M
MAG	MAG Silver Corp.	Silver	1.37B
MAIA	MAIA Biotechnology, Inc.	Biotechnology	68.04M
MAIN	Main Street Capital Corporation	Asset Management	4.39B
MAMA	Mama's Creations, Inc.	Packaged Foods	271.28M
MAMO	Massimo Group	Recreational Vehicles	161.91M
MAN	ManpowerGroup Inc.	Staffing & Employment Services	3.65B
MANH	Manhattan Associates, Inc.	Software - Application	15.67B
MANU	Manchester United plc	Entertainment	2.82B
MAPS	WM Technology, Inc.	Software - Application	105.51M
MAQC	Maquia Capital Acquisition Corporation	Shell Companies	68.54M
MAR	Marriott International, Inc.	Lodging	68.56B
MARA	Marathon Digital Holdings, Inc.	Capital Markets	5.65B
MARPS	Marine Petroleum Trust	Oil & Gas Midstream	7.68M
MARX	Mars Acquisition Corp.	Shell Companies	48.72M
MAS	Masco Corporation	Building Products & Equipment	17.19B
MASI	Masimo Corporation	Medical Devices	5.63B
MASS	908 Devices Inc.	Medical Devices	187.94M
MAT	Mattel, Inc.	Leisure	6.64B
MATH	Metalpha Technology Holding Limited	Capital Markets	48.11M
MATV	Mativ Holdings, Inc.	Specialty Chemicals	1.01B
MATW	Matthews International Corporation	Conglomerates	877.54M
MATX	Matson, Inc.	Marine Shipping	4.51B
MAX	MediaAlpha, Inc.	Internet Content & Information	950.45M
MAXN	Maxeon Solar Technologies, Ltd.	Solar	10.28M
MAYS	J.W. Mays, Inc.	Real Estate Services	87.34M
MBC	MasterBrand, Inc.	Furnishings, Fixtures & Appliances	2.31B
MBCN	Middlefield Banc Corp.	Banks - Regional	206.92M
MBI	MBIA Inc.	Insurance - Specialty	224.57M
MBIN	Merchants Bancorp	Banks - Regional	2.03B
MBIO	Mustang Bio, Inc.	Biotechnology	11.32M
MBLY	Mobileye Global Inc.	Auto Parts	16.45B
MBOT	Microbot Medical Inc.	Medical Instruments & Supplies	16.05M
MBRX	Moleculin Biotech, Inc.	Biotechnology	7.37M
MBUU	Malibu Boats, Inc.	Recreational Vehicles	783.45M
MBWM	Mercantile Bank Corporation	Banks - Regional	794.43M
MC	Moelis & Company	Capital Markets	4.86B
MCAA	Mountain & Co. I Acquisition Corp.	Shell Companies	161.55M
MCAG	Mountain Crest Acquisition Corp. V	Shell Companies	33.95M
MCB	Metropolitan Bank Holding Corp.	Banks - Regional	588.52M
MCBC	Macatawa Bank Corporation	Banks - Regional	511.64M
MCBS	MetroCity Bankshares, Inc.	Banks - Regional	795.99M
MCD	McDonald's Corporation	Restaurants	190.75B
MCFT	MasterCraft Boat Holdings, Inc.	Recreational Vehicles	357.03M
MCHP	Microchip Technology Incorporated	Semiconductors	47.00B
MCHX	Marchex, Inc.	Advertising Agencies	70.32M
MCK	McKesson Corporation	Medical Distribution	79.27B
MCO	Moody's Corporation	Financial Data & Stock Exchanges	82.56B
MCRB	Seres Therapeutics, Inc.	Biotechnology	205.21M
MCRI	Monarch Casino & Resort, Inc.	Resorts & Casinos	1.46B
MCS	The Marcus Corporation	Entertainment	398.24M
MCVT	Mill City Ventures III, Ltd.	Credit Services	17.30M
MCW	Mister Car Wash, Inc.	Personal Services	2.44B
MCY	Mercury General Corporation	Insurance - Property & Casualty	3.29B
MD	Pediatrix Medical Group, Inc.	Medical Care Facilities	708.94M
MDAI	Spectral AI, Inc.	Medical Devices	29.26M
MDB	MongoDB, Inc.	Software - Infrastructure	17.76B
MDBH	MDB Capital Holdings, LLC Class A common	Capital Markets	109.04M
MDGL	Madrigal Pharmaceuticals, Inc.	Biotechnology	5.80B
MDIA	MediaCo Holding Inc.	Broadcasting	191.49M
MDJH	MDJM Ltd	Real Estate Services	16.23M
MDLZ	Mondelez International, Inc.	Confectioners	89.94B
MDRR	Medalist Diversified REIT, Inc.	REIT - Diversified	13.13M
MDT	Medtronic plc	Medical Devices	103.08B
MDU	MDU Resources Group, Inc.	Conglomerates	5.47B
MDV	Modiv Inc.	REIT - Diversified	140.09M
MDWD	MediWound Ltd.	Biotechnology	174.44M
MDXG	MiMedx Group, Inc.	Biotechnology	1.13B
MDXH	MDxHealth SA	Diagnostics & Research	71.49M
ME	23andMe Holding Co.	Diagnostics & Research	211.80M
MEC	Mayville Engineering Company, Inc.	Metal Fabrication	388.16M
MED	Medifast, Inc.	Personal Services	228.37M
MEDP	Medpace Holdings, Inc.	Diagnostics & Research	11.71B
MEDS	TRxADE HEALTH, Inc.	Pharmaceutical Retailers	12.88M
MEG	Montrose Environmental Group, Inc.	Waste Management	1.02B
MEGL	Magic Empire Global Limited	Capital Markets	10.55M
MEI	Methode Electronics, Inc.	Electronic Components	444.73M
MEIP	MEI Pharma, Inc.	Biotechnology	22.39M
MELI	MercadoLibre, Inc.	Internet Retail	82.07B
MEOH	Methanex Corporation	Chemicals	3.18B
MERC	Mercer International Inc.	Paper & Paper Products	515.41M
MESA	Mesa Air Group, Inc.	Airlines	64.65M
MESO	Mesoblast Limited	Biotechnology	804.69M
MET	MetLife, Inc.	Insurance - Life	54.67B
META	Meta Platforms, Inc.	Internet Content & Information	1,172.08B
METC	Ramaco Resources, Inc.	Coking Coal	681.85M
METCB	Ramaco Resources, Inc.	Coking Coal	701.09M
MFA	MFA Financial, Inc.	REIT - Mortgage	1.15B
MFC	Manulife Financial Corporation	Insurance - Life	47.20B
MFG	Mizuho Financial Group, Inc.	Banks - Regional	54.49B
MFH	Mercurity Fintech Holding Inc.	Capital Markets	120.42M
MFI	mF International Limited	Software - Application	10.14M
MFIC	MidCap Financial Investment Corporation	Asset Management	1.36B
MFIN	Medallion Financial Corp.	Credit Services	187.01M
MG	Mistras Group, Inc.	Security & Protection Services	310.13M
MGA	Magna International Inc.	Auto Parts	12.55B
MGEE	MGE Energy, Inc.	Utilities - Regulated Electric	3.16B
MGIC	Magic Software Enterprises Ltd.	Information Technology Services	527.08M
MGIH	Millennium Group International Holdings Limited	Packaging & Containers	16.31M
MGLD	The Marygold Companies, Inc.	Asset Management	46.35M
MGM	MGM Resorts International	Resorts & Casinos	13.44B
MGNI	Magnite, Inc.	Advertising Agencies	1.99B
MGNX	MacroGenics, Inc.	Biotechnology	331.96M
MGOL	MGO Global Inc.	Advertising Agencies	5.02M
MGPI	MGP Ingredients, Inc.	Beverages - Wineries & Distilleries	1.77B
MGRC	McGrath RentCorp	Rental & Leasing Services	2.72B
MGRM	Monogram Orthopaedics, Inc.	Medical Devices	76.32M
MGRX	Mangoceuticals, Inc.	Health Information Services	10.28M
MGTX	MeiraGTx Holdings plc	Biotechnology	314.46M
MGX	Metagenomi, Inc.	Biotechnology	154.54M
MGY	Magnolia Oil & Gas Corporation	Oil & Gas Exploration & Production	4.80B
MGYR	Magyar Bancorp, Inc.	Banks - Regional	82.53M
MHH	Mastech Digital, Inc.	Staffing & Employment Services	103.43M
MHK	Mohawk Industries, Inc.	Furnishings, Fixtures & Appliances	10.36B
MHLD	Maiden Holdings, Ltd.	Insurance - Reinsurance	197.40M
MHO	M/I Homes, Inc.	Residential Construction	4.53B
MHUA	Meihua International Medical Technologies Co., Ltd.	Medical Instruments & Supplies	26.11M
MI	NFT Limited	Internet Retail	3.39M
MICS	The Singing Machine Company, Inc.	Consumer Electronics	3.95M
MIDD	The Middleby Corporation	Specialty Industrial Machinery	7.08B
MIGI	Mawson Infrastructure Group, Inc.	Capital Markets	20.67M
MIND	MIND Technology, Inc.	Scientific & Technical Instruments	6.55M
MIR	Mirion Technologies, Inc.	Specialty Industrial Machinery	2.41B
MIRA	MIRA Pharmaceuticals, Inc.	Drug Manufacturers - General	34.88M
MIRM	Mirum Pharmaceuticals, Inc.	Biotechnology	1.92B
MIST	Milestone Pharmaceuticals Inc.	Biotechnology	78.81M
MITA	Coliseum Acquisition Corp.	Shell Companies	72.89M
MITK	Mitek Systems, Inc.	Software - Application	621.38M
MITQ	Moving iMage Technologies, Inc.	Communication Equipment	6.73M
MITT	AG Mortgage Investment Trust, Inc.	REIT - Mortgage	228.27M
MKC	McCormick & Company, Incorporated	Packaged Foods	20.52B
MKC.V	McCormick & Company, Incorporated	Packaged Foods	20.56B
MKFG	Markforged Holding Corporation	Computer Hardware	75.61M
MKL	Markel Corporation	Insurance - Property & Casualty	21.48B
MKSI	MKS Instruments, Inc.	Scientific & Technical Instruments	8.04B
MKTW	MarketWise, Inc.	Financial Data & Stock Exchanges	48.18M
MKTX	MarketAxess Holdings Inc.	Capital Markets	8.54B
ML	MoneyLion Inc.	Software - Application	705.21M
MLAB	Mesa Laboratories, Inc.	Scientific & Technical Instruments	594.28M
MLCO	Melco Resorts & Entertainment Limited	Resorts & Casinos	2.54B
MLEC	Moolec Science SA	Biotechnology	36.44M
MLGO	MicroAlgo Inc.	Software - Infrastructure	9.82M
MLI	Mueller Industries, Inc.	Metal Fabrication	7.89B
MLKN	MillerKnoll, Inc.	Furnishings, Fixtures & Appliances	2.13B
MLM	Martin Marietta Materials, Inc.	Building Materials	35.85B
MLNK	MeridianLink, Inc.	Software - Application	1.82B
MLP	Maui Land & Pineapple Company, Inc.	Real Estate Services	462.71M
MLR	Miller Industries, Inc.	Auto Parts	794.30M
MLSS	Milestone Scientific Inc.	Medical Instruments & Supplies	74.14M
MLTX	MoonLake Immunotherapeutics	Biotechnology	2.61B
MLYS	Mineralys Therapeutics, Inc.	Biotechnology	623.59M
MMA	Alta Global Group Limited	Leisure	26.07M
MMAT	Meta Materials Inc.	Electronic Components	15.06M
MMC	Marsh & McLennan Companies, Inc.	Insurance Brokers	108.95B
MMI	Marcus & Millichap, Inc.	Real Estate Services	1.53B
MMLP	Martin Midstream Partners L.P.	Oil & Gas Midstream	157.37M
MMM	3M Company	Conglomerates	70.16B
MMS	Maximus, Inc.	Specialty Business Services	5.68B
MMSI	Merit Medical Systems, Inc.	Medical Instruments & Supplies	4.94B
MMV	MultiMetaVerse Holdings Limited	Entertainment	21.75M
MMYT	MakeMyTrip Limited	Travel Services	10.11B
MNDO	MIND C.T.I. Ltd	Software - Application	38.15M
MNDR	Mobile-health Network Solutions	Health Information Services	36.42M
MNDY	monday.com Ltd.	Software - Application	11.43B
MNKD	MannKind Corporation	Biotechnology	1.56B
MNMD	Mind Medicine (MindMed) Inc.	Biotechnology	621.29M
MNOV	MediciNova, Inc.	Biotechnology	64.25M
MNPR	Monopar Therapeutics Inc.	Biotechnology	12.68M
MNR	Mach Natural Resources LP	Oil & Gas Exploration & Production	1.81B
MNRO	Monro, Inc.	Auto Parts	766.27M
MNSB	MainStreet Bancshares, Inc.	Banks - Regional	132.51M
MNSO	MINISO Group Holding Limited	Specialty Retail	4.97B
MNST	Monster Beverage Corporation	Beverages - Non-Alcoholic	53.69B
MNTK	Montauk Renewables, Inc.	Utilities - Diversified	817.64M
MNTN	Everest Consolidator Acquisition Corporation	Shell Companies	131.68M
MNTS	Momentus Inc.	Aerospace & Defense	9.50M
MNTX	Manitex International, Inc.	Farm & Heavy Construction Machinery	104.47M
MNY	MoneyHero Limited	Internet Content & Information	61.96M
MO	Altria Group, Inc.	Tobacco	87.21B
MOB	Mobilicom Ltd	Communication Equipment	5.55M
MOBX	Mobix Labs, Inc.	Semiconductors	35.07M
MOD	Modine Manufacturing Company	Auto Parts	5.30B
MODD	Modular Medical, Inc.	Medical Devices	49.13M
MODG	Topgolf Callaway Brands Corp.	Leisure	2.98B
MODV	ModivCare Inc.	Medical Care Facilities	327.06M
MOFG	MidWestOne Financial Group, Inc.	Banks - Regional	454.54M
MOG.A	Moog Inc.	Aerospace & Defense	6.24B
MOG.B	Moog Inc.	Aerospace & Defense	6.33B
MOGO	Mogo Inc.	Software - Infrastructure	34.57M
MOGU	MOGU Inc.	Internet Retail	17.39M
MOH	Molina Healthcare, Inc.	Healthcare Plans	20.25B
MOLN	Molecular Partners AG	Biotechnology	215.52M
MOMO	Hello Group Inc.	Internet Content & Information	1.26B
MOND	Mondee Holdings, Inc.	Travel Services	275.68M
MOR	MorphoSys AG	Biotechnology	2.80B
MORF	Morphic Holding, Inc.	Biotechnology	2.84B
MORN	Morningstar, Inc.	Financial Data & Stock Exchanges	13.80B
MOS	The Mosaic Company	Agricultural Inputs	9.45B
MOV	Movado Group, Inc.	Luxury Goods	405.59M
MOVE	Movano Inc.	Medical Devices	38.53M
MP	MP Materials Corp.	Other Industrial Metals & Mining	2.18B
MPAA	Motorcar Parts of America, Inc.	Auto Parts	119.98M
MPB	Mid Penn Bancorp, Inc.	Banks - Regional	485.99M
MPC	Marathon Petroleum Corporation	Oil & Gas Refining & Marketing	62.56B
MPLN	MultiPlan Corporation	Health Information Services	306.36M
MPLX	MPLX LP	Oil & Gas Midstream	43.84B
MPTI	M-tron Industries, Inc.	Electronic Components	93.33M
MPU	Mega Matrix Corp.	Entertainment	78.79M
MPW	Medical Properties Trust, Inc.	REIT - Healthcare Facilities	2.93B
MPWR	Monolithic Power Systems, Inc.	Semiconductors	38.80B
MPX	Marine Products Corporation	Recreational Vehicles	361.67M
MQ	Marqeta, Inc.	Software - Infrastructure	2.81B
MRAM	Everspin Technologies, Inc.	Semiconductors	130.20M
MRBK	Meridian Corporation	Banks - Regional	129.19M
MRC	MRC Global Inc.	Oil & Gas Equipment & Services	1.24B
MRCC	Monroe Capital Corporation	Asset Management	165.96M
MRCY	Mercury Systems, Inc.	Aerospace & Defense	2.03B
MRDB	MariaDB plc	Software - Infrastructure	37.43M
MREO	Mereo BioPharma Group plc	Biotechnology	565.29M
MRIN	Marin Software Incorporated	Software - Application	7.38M
MRK	Merck & Co., Inc.	Drug Manufacturers - General	292.77B
MRKR	Marker Therapeutics, Inc.	Biotechnology	44.34M
MRM	MEDIROM Healthcare Technologies Inc.	Personal Services	19.38M
MRNA	Moderna, Inc.	Biotechnology	45.98B
MRNO	Murano Global Investments PLC	Real Estate - Development	634.74M
MRNS	Marinus Pharmaceuticals, Inc.	Biotechnology	77.45M
MRO	Marathon Oil Corporation	Oil & Gas Exploration & Production	15.53B
MRSN	Mersana Therapeutics, Inc.	Biotechnology	243.50M
MRT	Marti Technologies, Inc.	Software - Application	92.92M
MRTN	Marten Transport, Ltd.	Trucking	1.53B
MRUS	Merus N.V.	Biotechnology	3.58B
MRVI	Maravai LifeSciences Holdings, Inc.	Biotechnology	1.24B
MRVL	Marvell Technology, Inc.	Semiconductors	54.63B
MRX	Marex Group plc	Capital Markets	1.54B
MS	Morgan Stanley	Capital Markets	168.15B
MSA	MSA Safety Incorporated	Security & Protection Services	7.37B
MSAI	MultiSensor AI Holdings, Inc.	Software - Infrastructure	38.44M
MSB	Mesabi Trust	Steel	223.70M
MSBI	Midland States Bancorp, Inc.	Banks - Regional	497.52M
MSC	Studio City International Holdings Limited	Resorts & Casinos	1.25B
MSCI	MSCI Inc.	Financial Data & Stock Exchanges	42.81B
MSDL	Morgan Stanley Direct Lending Fund	null	1.82B
MSEX	Middlesex Water Company	Utilities - Regulated Water	1.16B
MSFT	Microsoft Corporation	Software - Infrastructure	3,121.16B
MSGE	Madison Square Garden Entertainment Corp.	Leisure	1.89B
MSGM	Motorsport Games Inc.	Electronic Gaming & Multimedia	4.75M
MSGS	Madison Square Garden Sports Corp.	Entertainment	4.79B
MSI	Motorola Solutions, Inc.	Communication Equipment	66.10B
MSM	MSC Industrial Direct Co., Inc.	Industrial Distribution	4.96B
MSN	Emerson Radio Corp.	Consumer Electronics	10.10M
MSS	Maison Solutions Inc.	Grocery Stores	15.14M
MSSA	Metal Sky Star Acquisition Corporation	Shell Companies	72.72M
MSTR	MicroStrategy Incorporated	Software - Application	28.75B
MT	ArcelorMittal S.A.	Steel	18.32B
MTA	Metalla Royalty & Streaming Ltd.	Other Precious Metals & Mining	267.61M
MTAL	Metals Acquisition Corp	Shell Companies	946.43M
MTB	M&T Bank Corporation	Banks - Regional	29.08B
MTC	MMTec, Inc.	Software - Application	60.82M
MTCH	Match Group, Inc.	Internet Content & Information	8.93B
MTD	Mettler-Toledo International Inc.	Diagnostics & Research	31.84B
MTDR	Matador Resources Company	Oil & Gas Exploration & Production	7.49B
MTEK	Maris-Tech Ltd.	Electronic Components	13.24M
MTEM	Molecular Templates, Inc.	Biotechnology	9.68M
MTEN	Mingteng International Corporation Inc.	Manufacturing - Metal Fabrication	22.17M
MTEX	Mannatech, Incorporated	Food Distribution	13.93M
MTG	MGIC Investment Corporation	Insurance - Specialty	6.60B
MTH	Meritage Homes Corporation	Residential Construction	7.33B
MTLS	Materialise NV	Software - Application	331.96M
MTN	Vail Resorts, Inc.	Resorts & Casinos	6.89B
MTNB	Matinas BioPharma Holdings, Inc.	Biotechnology	41.76M
MTR	Mesa Royalty Trust	Oil & Gas Exploration & Production	15.52M
MTRN	Materion Corporation	Other Industrial Metals & Mining	2.49B
MTRX	Matrix Service Company	Engineering & Construction	279.64M
MTSI	MACOM Technology Solutions Holdings, Inc.	Semiconductors	6.92B
MTTR	Matterport, Inc.	Software - Application	1.40B
MTUS	Metallus Inc.	Steel	957.51M
MTW	The Manitowoc Company, Inc.	Farm & Heavy Construction Machinery	452.44M
MTX	Minerals Technologies Inc.	Specialty Chemicals	2.54B
MTZ	MasTec, Inc.	Engineering & Construction	8.43B
MU	Micron Technology, Inc.	Semiconductors	114.94B
MUFG	Mitsubishi UFJ Financial Group, Inc.	Banks - Diversified	128.46B
MULN	Mullen Automotive, Inc.	Auto Manufacturers	18.43M
MUR	Murphy Oil Corporation	Oil & Gas Exploration & Production	6.13B
MURA	Mural Oncology plc	Biotechnology	57.12M
MUSA	Murphy USA Inc.	Specialty Retail	10.48B
MUX	McEwen Mining Inc.	Other Precious Metals & Mining	455.19M
MVBF	MVB Financial Corp.	Banks - Regional	306.17M
MVIS	MicroVision, Inc.	Scientific & Technical Instruments	210.79M
MVST	Microvast Holdings, Inc.	Electrical Equipment & Parts	124.56M
MWA	Mueller Water Products, Inc.	Specialty Industrial Machinery	3.19B
MWG	Multi Ways Holdings Limited	Rental & Leasing Services	14.81M
MX	Magnachip Semiconductor Corporation	Semiconductors	188.47M
MXC	Mexco Energy Corporation	Oil & Gas Exploration & Production	21.79M
MXCT	MaxCyte, Inc.	Medical Devices	484.97M
MXL	MaxLinear, Inc.	Semiconductors	1.09B
MYE	Myers Industries, Inc.	Packaging & Containers	538.60M
MYFW	First Western Financial, Inc.	Banks - Regional	165.49M
MYGN	Myriad Genetics, Inc.	Diagnostics & Research	2.56B
MYNA	Mynaric AG	Communication Equipment	106.72M
MYND	Mynd.ai, Inc.	Education & Training Services	127.81M
MYNZ	Mainz Biomed B.V.	Diagnostics & Research	7.17M
MYO	Myomo, Inc.	Medical Devices	125.92M
MYPS	PLAYSTUDIOS, Inc.	Electronic Gaming & Multimedia	283.76M
MYRG	MYR Group Inc.	Engineering & Construction	2.36B
MYSZ	My Size, Inc.	Software - Application	2.29M
MYTE	MYT Netherlands Parent B.V.	Luxury Goods	355.58M
NA	Nano Labs Ltd	Semiconductors	28.30M
NAAS	NaaS Technology Inc.	Specialty Retail	64.51M
NABL	N-able, Inc.	Information Technology Services	2.54B
NAII	Natural Alternatives International, Inc.	Packaged Foods	36.03M
NAK	Northern Dynasty Minerals Ltd.	Other Industrial Metals & Mining	206.38M
NAMS	NewAmsterdam Pharma Company N.V.	Biotechnology	1.58B
NAOV	NanoVibronix, Inc.	Medical Devices	2.06M
NAPA	The Duckhorn Portfolio, Inc.	Beverages - Wineries & Distilleries	1.07B
NARI	Inari Medical, Inc.	Medical Devices	3.01B
NAT	Nordic American Tankers Limited	Marine Shipping	766.28M
NATH	Nathan's Famous, Inc.	Restaurants	298.18M
NATL	NCR Atleos Corporation	Software - Application	2.28B
NATR	Nature's Sunshine Products, Inc.	Packaged Foods	316.16M
NAUT	Nautilus Biotechnology, Inc.	Biotechnology	331.95M
NAVI	Navient Corporation	Credit Services	1.80B
NB	NioCorp Developments Ltd.	Other Industrial Metals & Mining	65.01M
NBBK	NB Bancorp, Inc.	Banks - Regional	807.57M
NBHC	National Bank Holdings Corporation	Banks - Regional	1.61B
NBIX	Neurocrine Biosciences, Inc.	Drug Manufacturers - Specialty & Generic	14.38B
NBN	Northeast Bank	Banks - Regional	573.32M
NBR	Nabors Industries Ltd.	Oil & Gas Drilling	921.78M
NBST	Newbury Street Acquisition Corporation	Shell Companies	53.70M
NBTB	NBT Bancorp Inc.	Banks - Regional	2.32B
NBTX	Nanobiotix S.A.	Biotechnology	247.33M
NBY	NovaBay Pharmaceuticals, Inc.	Biotechnology	839.97K
NC	NACCO Industries, Inc.	Thermal Coal	223.64M
NCDL	Nuveen Churchill Direct Lending Corp.	Asset Management	964.81M
NCI	Neo-Concept International Group Holdings Limited	Apparel Manufacturing	10.77M
NCL	Northann Corp.	Furnishings, Fixtures & Appliances	5.57M
NCLH	Norwegian Cruise Line Holdings Ltd.	Travel Services	7.97B
NCMI	National CineMedia, Inc.	Advertising Agencies	565.44M
NCNA	NuCana plc	Biotechnology	8.61M
NCNC	noco-noco Inc.	Auto Parts	20.15M
NCNO	nCino, Inc.	Software - Application	3.77B
NCPL	Netcapital Inc.	Capital Markets	2.97M
NCRA	Nocera, Inc.	Packaged Foods	13.42M
NCSM	NCS Multistage Holdings, Inc.	Oil & Gas Equipment & Services	43.80M
NCTY	The9 Limited	Capital Markets	63.17M
NDAQ	Nasdaq, Inc.	Financial Data & Stock Exchanges	40.23B
NDLS	Noodles & Company	Restaurants	80.26M
NDRA	ENDRA Life Sciences Inc.	Diagnostics & Research	6.48M
NDSN	Nordson Corporation	Specialty Industrial Machinery	14.11B
NE	Noble Corporation	Oil & Gas Drilling	6.52B
NECB	Northeast Community Bancorp, Inc.	Banks - Regional	310.41M
NEE	NextEra Energy, Inc.	Utilities - Regulated Electric	151.50B
NEGG	Newegg Commerce, Inc.	Internet Retail	334.50M
NEM	Newmont Corporation	Gold	53.98B
NEN	New England Realty Associates LP	Real Estate Services	248.14M
NEO	NeoGenomics, Inc.	Diagnostics & Research	2.27B
NEOG	Neogen Corporation	Diagnostics & Research	3.73B
NEON	Neonode Inc.	Electronic Components	44.71M
NEOV	NeoVolta Inc.	Electrical Equipment & Parts	92.40M
NEP	NextEra Energy Partners, LP	Utilities - Renewable	2.47B
NEPH	Nephros, Inc.	Medical Instruments & Supplies	23.51M
NERV	Minerva Neurosciences, Inc.	Biotechnology	21.05M
NET	Cloudflare, Inc.	Software - Infrastructure	25.95B
NETD	Nabors Energy Transition Corp. II	Shell Companies	404.13M
NEU	NewMarket Corporation	Specialty Chemicals	5.41B
NEUE	NeueHealth, Inc.	Healthcare Plans	54.04M
NEWP	New Pacific Metals Corp.	Other Precious Metals & Mining	257.10M
NEWT	Newtek Business Services Corp.	Banks - Regional	333.41M
NEXA	Nexa Resources S.A.	Other Industrial Metals & Mining	947.60M
NEXN	Nexxen International Ltd.	Advertising Agencies	460.66M
NEXT	NextDecade Corporation	Oil & Gas Exploration & Production	2.04B
NFBK	Northfield Bancorp, Inc. (Staten Island, NY)	Banks - Regional	562.95M
NFE	New Fortress Energy Inc.	Utilities - Regulated Gas	3.95B
NFG	National Fuel Gas Company	Oil & Gas Integrated	5.36B
NFGC	New Found Gold Corp.	Gold	519.06M
NFLX	Netflix, Inc.	Entertainment	267.38B
NG	NovaGold Resources Inc.	Gold	1.58B
NGD	New Gold Inc.	Gold	1.60B
NGG	National Grid plc	Utilities - Regulated Electric	62.42B
NGL	NGL Energy Partners LP	Oil & Gas Midstream	613.54M
NGNE	Neurogene Inc.	Biotechnology	515.97M
NGS	Natural Gas Services Group, Inc.	Oil & Gas Equipment & Services	247.50M
NGVC	Natural Grocers by Vitamin Cottage, Inc.	Grocery Stores	599.88M
NGVT	Ingevity Corporation	Specialty Chemicals	1.67B
NHC	National HealthCare Corporation	Medical Care Facilities	2.12B
NHI	National Health Investors, Inc.	REIT - Healthcare Facilities	3.25B
NHTC	Natural Health Trends Corp.	Internet Retail	83.73M
NI	NiSource Inc.	Utilities - Regulated Gas	14.03B
NIC	Nicolet Bankshares, Inc.	Banks - Regional	1.53B
NICE	NICE Ltd.	Software - Application	11.42B
NICK	Nicholas Financial, Inc.	Credit Services	47.23M
NINE	Nine Energy Service, Inc.	Oil & Gas Equipment & Services	65.77M
NIO	NIO Inc.	Auto Manufacturers	8.39B
NIPG	NIP Group Inc.	Entertainment	690.05M
NISN	Nisun International Enterprise Development Group Co., Ltd	Credit Services	46.04M
NITO	N2OFF, Inc.	Agricultural Inputs	1.65M
NIU	Niu Technologies	Auto Manufacturers	153.52M
NIVF	NewGenIvf Group Limited	Medical - Healthcare Plans	9.34M
NJR	New Jersey Resources Corporation	Utilities - Regulated Gas	4.63B
NKE	NIKE, Inc.	Footwear & Accessories	110.88B
NKGN	NKGen Biotech, Inc.	Biotechnology	27.96M
NKLA	Nikola Corporation	Farm & Heavy Construction Machinery	414.65M
NKSH	National Bankshares, Inc.	Banks - Regional	179.41M
NKTR	Nektar Therapeutics	Biotechnology	249.35M
NKTX	Nkarta, Inc.	Biotechnology	455.22M
NL	NL Industries, Inc.	Security & Protection Services	293.51M
NLOP	Net Lease Office Properties	REIT - Office	434.83M
NLSP	NLS Pharmaceutics AG	Biotechnology	10.41M
NLY	Annaly Capital Management, Inc.	REIT - Mortgage	10.08B
NMFC	New Mountain Finance Corporation	Asset Management	1.34B
NMG	Nouveau Monde Graphite Inc.	Other Industrial Metals & Mining	180.08M
NMHI	Nature's Miracle Holding Inc.	Specialty Industrial Machinery	5.10M
NMIH	NMI Holdings, Inc.	Insurance - Specialty	3.17B
NMM	Navios Maritime Partners L.P.	Marine Shipping	1.38B
NMR	Nomura Holdings, Inc.	Capital Markets	17.68B
NMRA	Neumora Therapeutics, Inc.	Biotechnology	2.01B
NMRK	Newmark Group, Inc.	Real Estate Services	2.19B
NMTC	NeuroOne Medical Technologies Corporation	Medical Devices	21.38M
NN	NextNav Inc.	Software - Infrastructure	981.91M
NNAG	99 Acquisition Group Inc.	Shell Companies	105.58M
NNBR	NN, Inc.	Conglomerates	186.02M
NNDM	Nano Dimension Ltd.	Computer Hardware	577.19M
NNE	Nano Nuclear Energy Inc.	Specialty Industrial Machinery	394.73M
NNI	Nelnet, Inc.	Credit Services	4.11B
NNN	NNN REIT Inc	REIT - Retail	8.41B
NNOX	Nano-X Imaging Ltd.	Medical Devices	497.48M
NNVC	NanoViricides, Inc.	Biotechnology	23.86M
NOA	North American Construction Group Ltd.	Oil & Gas Equipment & Services	519.88M
NOAH	Noah Holdings Limited	Asset Management	503.97M
NOC	Northrop Grumman Corporation	Aerospace & Defense	70.73B
NODK	NI Holdings, Inc.	Insurance - Property & Casualty	328.01M
NOG	Northern Oil and Gas, Inc.	Oil & Gas Exploration & Production	4.13B
NOK	Nokia Oyj	Communication Equipment	21.58B
NOMD	Nomad Foods Limited	Packaged Foods	2.96B
NOTE	FiscalNote Holdings, Inc.	Information Technology Services	215.01M
NOTV	Inotiv, Inc.	Diagnostics & Research	48.31M
NOV	NOV Inc.	Oil & Gas Equipment & Services	8.05B
NOVA	Sunnova Energy International Inc.	Solar	862.29M
NOVT	Novanta Inc.	Scientific & Technical Instruments	6.50B
NOVV	Nova Vision Acquisition Corporation	Shell Companies	40.09M
NOW	ServiceNow, Inc.	Software - Application	163.00B
NPAB	New Providence Acquisition Corp. II	Shell Companies	95.04M
NPCE	NeuroPace, Inc.	Medical Devices	211.73M
NPK	National Presto Industries, Inc.	Aerospace & Defense	547.37M
NPO	EnPro Industries, Inc.	Specialty Industrial Machinery	3.57B
NPWR	NET Power Inc.	Specialty Industrial Machinery	661.96M
NR	Newpark Resources, Inc.	Oil & Gas Equipment & Services	692.69M
NRBO	NeuroBo Pharmaceuticals, Inc.	Biotechnology	34.82M
NRC	National Research Corporation	Health Information Services	581.77M
NRDS	NerdWallet, Inc.	Internet Content & Information	1.23B
NRDY	Nerdy, Inc.	Software - Application	311.83M
NREF	NexPoint Real Estate Finance, Inc.	REIT - Mortgage	246.47M
NRG	NRG Energy, Inc.	Utilities - Independent Power Producers	15.31B
NRGV	Energy Vault Holdings, Inc.	Utilities - Renewable	165.22M
NRIM	Northrim BanCorp, Inc.	Banks - Regional	379.47M
NRIX	Nurix Therapeutics, Inc.	Biotechnology	1.36B
NRP	Natural Resource Partners L.P.	Thermal Coal	1.16B
NRSN	NeuroSense Therapeutics Ltd.	Biotechnology	14.07M
NRT	North European Oil Royalty Trust	Oil & Gas Exploration & Production	59.74M
NRXP	NRx Pharmaceuticals, Inc.	Biotechnology	24.61M
NRXS	NeurAxis, Inc.	Biotechnology	21.61M
NSA	National Storage Affiliates Trust	REIT - Industrial	5.04B
NSC	Norfolk Southern Corporation	Railroads	55.95B
NSIT	Insight Enterprises, Inc.	Electronics & Computer Distribution	7.24B
NSP	Insperity, Inc.	Staffing & Employment Services	3.89B
NSPR	InspireMD, Inc.	Medical Devices	80.16M
NSSC	Napco Security Technologies, Inc.	Security & Protection Services	1.99B
NSTS	NSTS Bancorp, Inc.	Banks - Regional	54.54M
NSYS	Nortech Systems Incorporated	Medical Devices	40.50M
NTAP	NetApp, Inc.	Computer Hardware	25.34B
NTB	The Bank of N.T. Butterfield & Son Limited	Banks - Diversified	1.82B
NTBL	Notable Labs, Ltd.	Biotechnology	6.09M
NTCT	NetScout Systems, Inc.	Software - Infrastructure	1.43B
NTES	NetEase, Inc.	Electronic Gaming & Multimedia	56.87B
NTGR	NETGEAR, Inc.	Communication Equipment	465.43M
NTIC	Northern Technologies International Corporation	Specialty Chemicals	123.21M
NTIP	Network-1 Technologies, Inc.	Specialty Business Services	37.30M
NTLA	Intellia Therapeutics, Inc.	Biotechnology	2.56B
NTNX	Nutanix, Inc.	Software - Infrastructure	12.06B
NTR	Nutrien Ltd.	Agricultural Inputs	25.04B
NTRA	Natera, Inc.	Diagnostics & Research	12.01B
NTRB	Nutriband Inc.	Biotechnology	83.32M
NTRP	NextTrip, Inc.	Travel Services	4.33M
NTRS	Northern Trust Corporation	Asset Management	18.31B
NTST	NETSTREIT Corp.	REIT - Retail	1.23B
NTWK	NetSol Technologies, Inc.	Software - Application	33.08M
NTZ	Natuzzi S.p.A.	Furnishings, Fixtures & Appliances	50.34M
NU	Nu Holdings Ltd.	Banks - Regional	57.99B
NUE	Nucor Corporation	Steel	38.39B
NUKK	Nukkleus Inc.	Software - Application	4.17M
NURO	NeuroMetrix, Inc.	Medical Devices	7.24M
NUS	Nu Skin Enterprises, Inc.	Household & Personal Products	536.90M
NUTX	Nutex Health, Inc.	Health Information Services	42.59M
NUVB	Nuvation Bio Inc.	Biotechnology	877.99M
NUVL	Nuvalent, Inc.	Biotechnology	5.06B
NUVO	Holdco Nuvo Group D.G Ltd.	Medical Devices	25.94M
NUWE	Nuwellis, Inc.	Medical Devices	1.42M
NUZE	NuZee, Inc.	Packaged Foods	8.99M
NVA	Nova Minerals Limited	Other Industrial Metals & Mining	1.23B
NVAC	NorthView Acquisition Corporation	Shell Companies	69.31M
NVAX	Novavax, Inc.	Biotechnology	1.70B
NVCR	NovoCure Limited	Medical Devices	2.53B
NVCT	Nuvectis Pharma, Inc.	Biotechnology	123.35M
NVDA	NVIDIA Corporation	Semiconductors	2,573.41B
NVEC	NVE Corporation	Semiconductors	398.78M
NVEE	NV5 Global, Inc.	Engineering & Construction	1.66B
NVEI	Nuvei Corporation	Software - Infrastructure	4.61B
NVFY	Nova LifeStyle, Inc.	Furnishings, Fixtures & Appliances	3.92M
NVGS	Navigator Holdings Ltd.	Oil & Gas Midstream	1.12B
NVMI	Nova Ltd.	Semiconductor Equipment & Materials	5.73B
NVNI	Nvni Group Limited	Software - Application	47.98M
NVNO	enVVeno Medical Corporation	Medical Devices	71.07M
NVO	Novo Nordisk A/S	Biotechnology	563.39B
NVOS	Novo Integrated Sciences, Inc.	Medical Care Facilities	11.95M
NVR	NVR, Inc.	Residential Construction	27.02B
NVRI	Enviri Corporation	Waste Management	881.94M
NVRO	Nevro Corp.	Medical Devices	354.62M
NVS	Novartis AG	Drug Manufacturers - General	217.62B
NVST	Envista Holdings Corporation	Medical Instruments & Supplies	2.87B
NVT	nVent Electric plc	Electrical Equipment & Parts	11.56B
NVTS	Navitas Semiconductor Corporation	Semiconductors	659.86M
NVVE	Nuvve Holding Corp.	Specialty Retail	3.74M
NVX	Novonix Limited	Electrical Equipment & Parts	221.73M
NWBI	Northwest Bancshares, Inc.	Banks - Regional	1.80B
NWE	NorthWestern Corporation	Utilities - Regulated Electric	3.27B
NWFL	Norwood Financial Corp.	Banks - Regional	223.11M
NWG	NatWest Group plc	Banks - Regional	39.49B
NWGL	Nature Wood Group Limited	Lumber & Wood Production	298.55M
NWL	Newell Brands Inc.	Household & Personal Products	3.54B
NWLI	National Western Life Group, Inc.	Insurance - Life	1.82B
NWN	Northwest Natural Holding Company	Utilities - Regulated Gas	1.55B
NWPX	Northwest Pipe Company	Metal Fabrication	369.95M
NWS	News Corporation	Entertainment	14.90B
NWSA	News Corporation	Entertainment	14.86B
NWTN	NWTN Inc.	Auto Manufacturers	271.90M
NX	Quanex Building Products Corporation	Building Products & Equipment	1.13B
NXE	NexGen Energy Ltd.	Uranium	3.45B
NXGL	NEXGEL, Inc.	Medical Instruments & Supplies	18.31M
NXL	Nexalin Technology, Inc.	Medical Devices	8.65M
NXPI	NXP Semiconductors N.V.	Semiconductors	64.52B
NXPL	NextPlat Corp	Software - Application	22.06M
NXRT	NexPoint Residential Trust, Inc.	REIT - Residential	1.12B
NXST	Nexstar Media Group, Inc.	Entertainment	5.97B
NXT	Nextracker Inc.	Solar	6.65B
NXTC	NextCure, Inc.	Biotechnology	45.04M
NXTT	Next Technology Holding Inc.	Software - Application	2.95M
NXU	Nxu, Inc.	Electrical Equipment & Parts	4.65M
NYAX	Nayax Ltd.	Information Technology Services	802.38M
NYC	American Strategic Investment Co	Real Estate Services	21.04M
NYCB	New York Community Bancorp, Inc.	Banks - Regional	3.71B
NYMT	New York Mortgage Trust, Inc.	REIT - Mortgage	597.54M
NYT	The New York Times Company	Publishing	8.67B
NYXH	Nyxoah S.A.	Medical Instruments & Supplies	283.13M
O	Realty Income Corporation	REIT - Retail	50.78B
OABI	OmniAb, Inc.	Biotechnology	553.42M
OAKU	Oak Woods Acquisition Corporation	Shell Companies	82.31M
OB	Outbrain Inc.	Internet Content & Information	234.93M
OBDC	Blue Owl Capital Corporation	Credit Services	6.09B
OBDE	Blue Owl Capital Corporation III	Asset Management	1.79B
OBE	Obsidian Energy Ltd.	Oil & Gas Exploration & Production	552.19M
OBIO	Orchestra BioMed Holdings, Inc.	Biotechnology	246.94M
OBK	Origin Bancorp, Inc.	Banks - Regional	1.08B
OBLG	Oblong, Inc.	Software - Application	4.85M
OBT	Orange County Bancorp, Inc.	Banks - Regional	333.39M
OC	Owens Corning	Building Products & Equipment	15.78B
OCC	Optical Cable Corporation	Communication Equipment	21.07M
OCEA	Ocean Biomedical, Inc.	Biotechnology	41.58M
OCFC	OceanFirst Financial Corp.	Banks - Regional	1.07B
OCFT	OneConnect Financial Technology Co., Ltd.	Software - Application	66.64M
OCG	Oriental Culture Holding LTD	Internet Retail	5.69M
OCGN	Ocugen, Inc.	Biotechnology	364.34M
OCS	Oculis Holding AG	Biotechnology	483.72M
OCSL	Oaktree Specialty Lending Corporation	Credit Services	1.48B
OCTO	Eightco Holdings Inc.	Packaging & Containers	3.19M
OCUL	Ocular Therapeutix, Inc.	Biotechnology	1.27B
OCUP	Ocuphire Pharma, Inc.	Biotechnology	52.89M
OCX	OncoCyte Corporation	Diagnostics & Research	43.84M
ODC	Oil-Dri Corporation of America	Specialty Chemicals	428.53M
ODD	Oddity Tech Ltd.	Software - Infrastructure	2.24B
ODFL	Old Dominion Freight Line, Inc.	Trucking	44.51B
ODP	The ODP Corporation	Specialty Retail	1.52B
ODV	Osisko Development Corp.	Gold	161.98M
OEC	Orion Engineered Carbons S.A.	Specialty Chemicals	1.40B
OESX	Orion Energy Systems, Inc.	Furnishings, Fixtures & Appliances	34.35M
OFG	OFG Bancorp	Banks - Regional	2.15B
OFIX	Orthofix Medical Inc.	Medical Devices	602.72M
OFLX	Omega Flex, Inc.	Specialty Industrial Machinery	532.58M
OFS	OFS Capital Corporation	Asset Management	114.96M
OGE	OGE Energy Corp.	Utilities - Regulated Electric	7.76B
OGEN	Oragenics, Inc.	Biotechnology	5.80M
OGI	OrganiGram Holdings Inc.	Drug Manufacturers - Specialty & Generic	169.51M
OGN	Organon & Co.	Drug Manufacturers - General	5.75B
OGS	ONE Gas, Inc.	Utilities - Regulated Gas	4.00B
OHI	Omega Healthcare Investors, Inc.	REIT - Healthcare Facilities	9.03B
OI	O-I Glass, Inc.	Packaging & Containers	1.81B
OII	Oceaneering International, Inc.	Oil & Gas Equipment & Services	2.96B
OIS	Oil States International, Inc.	Oil & Gas Equipment & Services	357.36M
OKE	ONEOK, Inc.	Oil & Gas Midstream	48.08B
OKLO	Oklo Inc.	Utilities - Regulated Electric	1.08B
OKTA	Okta, Inc.	Software - Infrastructure	14.90B
OKYO	OKYO Pharma Limited	Biotechnology	41.55M
OLB	The OLB Group, Inc.	Software - Infrastructure	4.80M
OLED	Universal Display Corporation	Electronic Components	10.30B
OLLI	Ollie's Bargain Outlet Holdings, Inc.	Discount Stores	6.06B
OLMA	Olema Pharmaceuticals, Inc.	Biotechnology	847.96M
OLN	Olin Corporation	Specialty Chemicals	5.36B
OLO	Olo Inc.	Software - Application	761.67M
OLP	One Liberty Properties, Inc.	REIT - Diversified	561.58M
OLPX	Olaplex Holdings, Inc.	Specialty Retail	1.33B
OM	Outset Medical, Inc.	Medical Devices	182.69M
OMAB	Grupo Aeroportuario del Centro Norte, SAB de CV	Airports & Air Services	3.31B
OMC	Omnicom Group Inc.	Advertising Agencies	19.02B
OMCL	Omnicell, Inc.	Health Information Services	1.33B
OMER	Omeros Corporation	Biotechnology	304.79M
OMEX	Odyssey Marine Exploration, Inc.	Other Industrial Metals & Mining	88.26M
OMF	OneMain Holdings, Inc.	Credit Services	6.35B
OMGA	Omega Therapeutics, Inc.	Biotechnology	101.49M
OMH	Ohmyhome Limited	Real Estate Services	12.07M
OMI	Owens & Minor, Inc.	Medical Distribution	1.19B
OMIC	Singular Genomics Systems, Inc.	Medical Instruments & Supplies	19.45M
ON	ON Semiconductor Corporation	Semiconductors	32.17B
ONB	Old National Bancorp	Banks - Regional	6.43B
ONCO	Onconetix, Inc.	Biotechnology	3.83M
ONCT	Oncternal Therapeutics, Inc.	Biotechnology	19.24M
ONCY	Oncolytics Biotech Inc.	Biotechnology	80.40M
ONDS	Ondas Holdings Inc.	Communication Equipment	63.94M
ONEW	OneWater Marine Inc.	Specialty Retail	379.43M
ONFO	Onfolio Holdings, Inc.	Internet Content & Information	4.49M
ONIT	Onity Group Inc.	Mortgage Finance	220.82M
ONL	Orion Office REIT Inc.	REIT - Office	226.79M
ONMD	OneMedNet Corporation	Health Information Services	34.34M
ONON	On Holding AG	Footwear & Accessories	12.41B
ONTF	ON24, Inc.	Software - Application	274.43M
ONTO	Onto Innovation Inc.	Semiconductor Equipment & Materials	8.88B
ONVO	Organovo Holdings, Inc.	Biotechnology	8.05M
ONYX	Onyx Acquisition Co. I	Shell Companies	89.39M
OOMA	Ooma, Inc.	Software - Application	267.83M
OP	OceanPal Inc.	Marine Shipping	13.49M
OPAD	Offerpad Solutions Inc.	Real Estate Services	120.40M
OPAL	OPAL Fuels Inc.	Utilities - Regulated Gas	116.10M
OPBK	OP Bancorp	Banks - Regional	190.62M
OPCH	Option Care Health, Inc.	Medical Care Facilities	5.47B
OPEN	Opendoor Technologies Inc.	Real Estate Services	1.61B
OPFI	OppFi Inc.	Credit Services	409.33M
OPGN	OpGen, Inc.	Medical Devices	4.07M
OPHC	OptimumBank Holdings, Inc.	Banks - Regional	43.07M
OPI	Office Properties Income Trust	REIT - Office	129.45M
OPK	OPKO Health, Inc.	Diagnostics & Research	1.00B
OPOF	Old Point Financial Corporation	Banks - Regional	90.60M
OPRA	Opera Limited	Internet Content & Information	1.08B
OPRT	Oportun Financial Corporation	Credit Services	111.04M
OPRX	OptimizeRx Corporation	Health Information Services	203.98M
OPT	Opthea Limited	Biotechnology	324.63M
OPTN	OptiNose, Inc.	Drug Manufacturers - Specialty & Generic	151.36M
OPTT	Ocean Power Technologies, Inc.	Specialty Industrial Machinery	21.56M
OPTX	Syntec Optics Holdings, Inc.	Electronic Components	57.67M
OPXS	Optex Systems Holdings, Inc	Aerospace & Defense	55.51M
OPY	Oppenheimer Holdings Inc.	Capital Markets	520.77M
OR	Osisko Gold Royalties Ltd	Gold	3.22B
ORA	Ormat Technologies, Inc.	Utilities - Renewable	4.61B
ORAN	Orange S.A.	Telecom Services	29.35B
ORC	Orchid Island Capital, Inc.	REIT - Mortgage	547.23M
ORCL	Oracle Corporation	Software - Infrastructure	374.98B
ORGN	Origin Materials, Inc.	Chemicals	133.05M
ORGO	Organogenesis Holdings Inc.	Drug Manufacturers - Specialty & Generic	407.00M
ORGS	Orgenesis Inc.	Biotechnology	29.27M
ORI	Old Republic International Corporation	Insurance - Diversified	9.38B
ORIC	ORIC Pharmaceuticals, Inc.	Biotechnology	743.33M
ORKT	Orangekloud Technology Inc.	Software - Application	122.65M
ORLA	Orla Mining Ltd.	Gold	1.19B
ORLY	O'Reilly Automotive, Inc.	Specialty Retail	66.64B
ORMP	Oramed Pharmaceuticals Inc.	Biotechnology	98.32M
ORN	Orion Group Holdings, Inc.	Engineering & Construction	272.70M
ORRF	Orrstown Financial Services, Inc.	Banks - Regional	676.17M
OS	OneStream, Inc.	Software - Application	6.39B
OSBC	Old Second Bancorp, Inc.	Banks - Regional	765.96M
OSCR	Oscar Health, Inc.	Healthcare Plans	3.46B
OSIS	OSI Systems, Inc.	Electronic Components	2.51B
OSK	Oshkosh Corporation	Farm & Heavy Construction Machinery	7.50B
OSPN	OneSpan Inc.	Software - Infrastructure	543.84M
OSS	One Stop Systems, Inc.	Computer Hardware	47.69M
OST	Ostin Technology Group Co., Ltd.	Electronic Components	4.93M
OSUR	OraSure Technologies, Inc.	Medical Instruments & Supplies	325.79M
OSW	OneSpaWorld Holdings Limited	Leisure	1.76B
OTEX	Open Text Corporation	Software - Application	8.54B
OTIS	Otis Worldwide Corporation	Specialty Industrial Machinery	37.26B
OTLK	Outlook Therapeutics, Inc.	Biotechnology	180.87M
OTLY	Oatly Group AB	Packaged Foods	574.25M
OTRK	Ontrak, Inc.	Health Information Services	12.14M
OTTR	Otter Tail Corporation	Utilities - Diversified	4.02B
OUST	Ouster, Inc.	Electronic Components	587.02M
OUT	Outfront Media Inc.	REIT - Specialty	2.63B
OVBC	Ohio Valley Banc Corp.	Banks - Regional	117.35M
OVID	Ovid Therapeutics Inc.	Biotechnology	73.43M
OVLY	Oak Valley Bancorp	Banks - Regional	227.38M
OVV	Ovintiv Inc.	Oil & Gas Exploration & Production	12.20B
OWL	Blue Owl Capital Inc.	Asset Management	27.36B
OWLT	Owlet, Inc.	Health Information Services	41.04M
OXBR	Oxbridge Re Holdings Limited	Insurance - Reinsurance	18.08M
OXM	Oxford Industries, Inc.	Apparel Manufacturing	1.65B
OXSQ	Oxford Square Capital Corp.	Asset Management	188.12M
OXY	Occidental Petroleum Corporation	Oil & Gas Exploration & Production	53.45B
OZ	Belpointe PREP, LLC	Real Estate - Development	258.61M
OZK	Bank OZK	Banks - Regional	5.29B
PAA	Plains All American Pipeline, L.P.	Oil & Gas Midstream	12.98B
PAAS	Pan American Silver Corp.	Gold	8.01B
PAC	Grupo Aeroportuario del Pacífico, SAB de CV	Airports & Air Services	8.12B
PACB	Pacific Biosciences of California, Inc.	Medical Devices	547.44M
PACK	Ranpak Holdings Corp.	Packaging & Containers	553.31M
PACS	PACS Group, Inc.	Medical Care Facilities	5.33B
PAG	Penske Automotive Group, Inc.	Auto & Truck Dealerships	10.91B
PAGP	Plains GP Holdings, L.P.	Oil & Gas Midstream	3.83B
PAGS	PagSeguro Digital Ltd.	Software - Infrastructure	4.19B
PAHC	Phibro Animal Health Corporation	Drug Manufacturers - Specialty & Generic	754.18M
PAL	Proficient Auto Logistics, Inc.	Integrated Freight & Logistics	523.62M
PALI	Palisade Bio, Inc.	Biotechnology	3.16M
PALT	Paltalk, Inc.	Software - Application	41.78M
PAM	Pampa Energía S.A.	Utilities - Independent Power Producers	3.49B
PANL	Pangaea Logistics Solutions, Ltd.	Marine Shipping	328.41M
PANW	Palo Alto Networks, Inc.	Software - Infrastructure	103.04B
PAPL	Pineapple Financial Inc.	Mortgage Finance	7.71M
PAR	PAR Technology Corporation	Software - Application	1.74B
PARA	Paramount Global	Entertainment	7.87B
PARAA	Paramount Global	Entertainment	7.89B
PARR	Par Pacific Holdings, Inc.	Oil & Gas Refining & Marketing	1.49B
PASG	Passage Bio, Inc.	Biotechnology	60.10M
PATH	UiPath Inc.	Software - Infrastructure	6.92B
PATK	Patrick Industries, Inc.	Furnishings, Fixtures & Appliances	2.83B
PAVM	PAVmed Inc.	Medical Devices	8.86M
PAVS	Paranovus Entertainment Technology Ltd.	Packaged Foods	7.41M
PAX	Patria Investments Limited	Asset Management	1.97B
PAY	Paymentus Holdings, Inc.	Software - Infrastructure	2.67B
PAYC	Paycom Software, Inc.	Software - Application	9.54B
PAYO	Payoneer Global Inc.	Software - Infrastructure	2.05B
PAYS	PaySign, Inc.	Software - Infrastructure	270.98M
PAYX	Paychex, Inc.	Staffing & Employment Services	46.21B
PB	Prosperity Bancshares, Inc.	Banks - Regional	6.97B
PBA	Pembina Pipeline Corporation	Oil & Gas Midstream	22.32B
PBBK	PB Bankshares, Inc.	Banks - Regional	40.26M
PBF	PBF Energy Inc.	Oil & Gas Refining & Marketing	4.77B
PBFS	Pioneer Bancorp, Inc.	Banks - Regional	289.13M
PBH	Prestige Consumer Healthcare Inc.	Drug Manufacturers - Specialty & Generic	3.52B
PBHC	Pathfinder Bancorp, Inc.	Banks - Regional	96.08M
PBI	Pitney Bowes Inc.	Integrated Freight & Logistics	1.18B
PBM	Psyence Biomedical Ltd.	Shell Companies	8.12M
PBPB	Potbelly Corporation	Restaurants	212.47M
PBR	Petróleo Brasileiro S.A. - Petrobras	Oil & Gas Integrated	88.46B
PBR.A	Petróleo Brasileiro S.A. - Petrobras	Oil & Gas Integrated	90.25B
PBT	Permian Basin Royalty Trust	Oil & Gas Midstream	512.93M
PBYI	Puma Biotechnology, Inc.	Biotechnology	178.00M
PCAR	PACCAR Inc	Farm & Heavy Construction Machinery	51.18B
PCB	PCB Bancorp	Banks - Regional	281.77M
PCG	PG&E Corporation	Utilities - Regulated Electric	39.27B
PCH	PotlatchDeltic Corporation	REIT - Specialty	3.53B
PCOR	Procore Technologies, Inc.	Software - Application	10.28B
PCRX	Pacira BioSciences, Inc.	Drug Manufacturers - Specialty & Generic	925.34M
PCSA	Processa Pharmaceuticals, Inc.	Biotechnology	6.43M
PCSC	Perceptive Capital Solutions Corp	Shell Companies	97.40M
PCT	PureCycle Technologies, Inc.	Pollution & Treatment Controls	1.26B
PCTY	Paylocity Holding Corporation	Software - Application	8.36B
PCVX	Vaxcyte, Inc.	Biotechnology	8.79B
PCYO	Pure Cycle Corporation	Utilities - Regulated Water	260.98M
PD	PagerDuty, Inc.	Software - Application	2.09B
PDCO	Patterson Companies, Inc.	Medical Distribution	2.32B
PDD	PDD Holdings Inc.	Internet Retail	165.02B
PDEX	Pro-Dex, Inc.	Medical Instruments & Supplies	68.89M
PDFS	PDF Solutions, Inc.	Software - Application	1.31B
PDLB	Ponce Financial Group, Inc.	Banks - Regional	237.64M
PDM	Piedmont Office Realty Trust, Inc.	REIT - Office	1.07B
PDS	Precision Drilling Corporation	Oil & Gas Drilling	1.03B
PDSB	PDS Biotechnology Corporation	Biotechnology	137.18M
PDYN	Palladyne AI Corp.	Software - Infrastructure	50.26M
PEB	Pebblebrook Hotel Trust	REIT - Hotel & Motel	1.66B
PEBK	Peoples Bancorp of North Carolina, Inc.	Banks - Regional	169.58M
PEBO	Peoples Bancorp Inc.	Banks - Regional	1.20B
PECO	Phillips Edison & Company, Inc.	REIT - Retail	4.34B
PED	PEDEVCO Corp.	Oil & Gas Exploration & Production	90.22M
PEG	Public Service Enterprise Group Incorporated	Utilities - Regulated Electric	38.67B
PEGA	Pegasystems Inc.	Software - Application	5.92B
PEGR	Project Energy Reimagined Acquisition Corp.	Shell Companies	128.90M
PEGY	Pineapple Energy Inc.	Solar	9.59M
PEN	Penumbra, Inc.	Medical Devices	6.69B
PENN	PENN Entertainment, Inc.	Resorts & Casinos	2.95B
PEP	PepsiCo, Inc.	Beverages - Non-Alcoholic	237.11B
PEPG	PepGen Inc.	Biotechnology	556.28M
PERF	Perfect Corp.	Software - Application	214.90M
PERI	Perion Network Ltd.	Internet Content & Information	404.08M
PESI	Perma-Fix Environmental Services, Inc.	Waste Management	194.83M
PET	Wag! Group Co.	Software - Application	54.27M
PETQ	PetIQ, Inc.	Drug Manufacturers - Specialty & Generic	636.46M
PETS	PetMed Express, Inc.	Pharmaceutical Retailers	83.05M
PETZ	TDH Holdings, Inc.	Restaurants	13.42M
PEV	Phoenix Motor Inc.	Auto Manufacturers	12.63M
PFBC	Preferred Bank	Banks - Regional	1.15B
PFC	Premier Financial Corp.	Banks - Regional	912.43M
PFE	Pfizer Inc.	Drug Manufacturers - General	173.09B
PFG	Principal Financial Group, Inc.	Asset Management	19.39B
PFGC	Performance Food Group Company	Food Distribution	10.65B
PFIE	Profire Energy, Inc.	Oil & Gas Equipment & Services	73.71M
PFIS	Peoples Financial Services Corp.	Banks - Regional	487.18M
PFLT	PennantPark Floating Rate Capital Ltd.	Asset Management	803.86M
PFMT	Performant Financial Corporation	Specialty Business Services	267.41M
PFS	Provident Financial Services, Inc.	Banks - Regional	2.45B
PFSI	PennyMac Financial Services, Inc.	Mortgage Finance	4.99B
PFTA	Perception Capital Corp. III	Shell Companies	114.27M
PFX	PhenixFIN Corporation	Asset Management	96.63M
PG	The Procter & Gamble Company	Household & Personal Products	379.19B
PGC	Peapack-Gladstone Financial Corporation	Banks - Regional	505.63M
PGEN	Precigen, Inc.	Biotechnology	387.46M
PGHL	Primega Group Holdings Limited	Waste Management	121.44M
PGNY	Progyny, Inc.	Health Information Services	2.79B
PGR	The Progressive Corporation	Insurance - Property & Casualty	126.52B
PGRE	Paramount Group, Inc.	REIT - Office	1.12B
PGRU	PropertyGuru Limited	Internet Content & Information	1.02B
PGY	Pagaya Technologies Ltd.	Software - Infrastructure	1.00B
PH	Parker-Hannifin Corporation	Specialty Industrial Machinery	70.37B
PHAR	Pharming Group N.V.	Biotechnology	590.85M
PHAT	Phathom Pharmaceuticals, Inc.	Biotechnology	666.13M
PHG	Koninklijke Philips N.V.	Medical Devices	26.59B
PHGE	BiomX Inc.	Biotechnology	13.31M
PHI	PLDT Inc.	Telecom Services	5.52B
PHIN	PHINIA Inc.	Auto Parts	1.86B
PHIO	Phio Pharmaceuticals Corp.	Biotechnology	1.68M
PHM	PulteGroup, Inc.	Residential Construction	27.57B
PHR	Phreesia, Inc.	Health Information Services	1.42B
PHUN	Phunware, Inc.	Software - Application	37.97M
PHVS	Pharvaris N.V.	Biotechnology	932.64M
PHX	PHX Minerals Inc.	Oil & Gas Exploration & Production	122.11M
PHYT	Pyrophyte Acquisition Corp.	Shell Companies	129.64M
PI	Impinj, Inc.	Communication Equipment	4.53B
PII	Polaris Inc.	Recreational Vehicles	4.60B
PIII	P3 Health Partners Inc.	Medical Care Facilities	222.50M
PIK	Kidpik Corp.	Internet Retail	5.27M
PINC	Premier, Inc.	Health Information Services	2.21B
PINE	Alpine Income Property Trust, Inc.	REIT - Retail	235.83M
PINS	Pinterest, Inc.	Internet Content & Information	25.58B
PIPR	Piper Sandler Companies	Capital Markets	4.93B
PIRS	Pieris Pharmaceuticals, Inc.	Biotechnology	20.20M
PIXY	ShiftPixy, Inc.	Staffing & Employment Services	10.61M
PJT	PJT Partners Inc.	Capital Markets	3.19B
PK	Park Hotels & Resorts Inc.	REIT - Hotel & Motel	3.20B
PKBK	Parke Bancorp, Inc.	Banks - Regional	231.90M
PKE	Park Aerospace Corp.	Aerospace & Defense	267.34M
PKG	Packaging Corporation of America	Packaging & Containers	17.89B
PKOH	Park-Ohio Holdings Corp.	Specialty Industrial Machinery	388.59M
PKST	Peakstone Realty Trust	REIT - Office	495.33M
PKX	POSCO Holdings Inc.	Steel	19.19B
PL	Planet Labs PBC	Aerospace & Defense	721.11M
PLAB	Photronics, Inc.	Semiconductor Equipment & Materials	1.57B
PLAG	Planet Green Holdings Corp.	Conglomerates	14.70M
PLAO	Patria Latin American Opportunity Acquisition Corp.	Shell Companies	263.42M
PLAY	Dave & Buster's Entertainment, Inc.	Entertainment	1.47B
PLBC	Plumas Bancorp	Banks - Regional	249.68M
PLBY	PLBY Group, Inc.	Leisure	61.16M
PLCE	The Children's Place, Inc.	Apparel Retail	104.33M
PLD	Prologis, Inc.	REIT - Industrial	115.48B
PLG	Platinum Group Metals Ltd.	Other Precious Metals & Mining	162.12M
PLL	Piedmont Lithium Inc.	Other Industrial Metals & Mining	186.33M
PLMI	Plum Acquisition Corp. I	Shell Companies	109.33M
PLMJ	Plum Acquisition Corp. III	Shell Companies	110.34M
PLMR	Palomar Holdings, Inc.	Insurance - Property & Casualty	2.27B
PLNT	Planet Fitness, Inc.	Leisure	6.48B
PLOW	Douglas Dynamics, Inc.	Auto Parts	704.60M
PLPC	Preformed Line Products Company	Electrical Equipment & Parts	639.94M
PLRX	Pliant Therapeutics, Inc.	Biotechnology	837.93M
PLSE	Pulse Biosciences, Inc.	Medical Instruments & Supplies	906.75M
PLTK	Playtika Holding Corp.	Electronic Gaming & Multimedia	2.82B
PLTR	Palantir Technologies Inc.	Software - Infrastructure	56.04B
PLUG	Plug Power Inc.	Electrical Equipment & Parts	1.91B
PLUR	Pluri Inc.	Biotechnology	31.74M
PLUS	ePlus inc.	Software - Application	2.39B
PLX	Protalix BioTherapeutics, Inc.	Biotechnology	81.75M
PLXS	Plexus Corp.	Electronic Components	3.43B
PLYA	Playa Hotels & Resorts N.V.	Resorts & Casinos	1.14B
PLYM	Plymouth Industrial REIT, Inc.	REIT - Industrial	1.10B
PM	Philip Morris International Inc.	Tobacco	178.07B
PMCB	PharmaCyte Biotech, Inc.	Biotechnology	16.96M
PMD	Psychemedics Corporation	Diagnostics & Research	12.73M
PMEC	Primech Holdings Ltd.	Specialty Business Services	19.64M
PMGM	Priveterra Acquisition Corp.	Shell Companies	97.48M
PMN	ProMIS Neurosciences, Inc.	Biotechnology	25.79M
PMNT	Perfect Moment Ltd.	Apparel Manufacturing	32.17M
PMT	PennyMac Mortgage Investment Trust	REIT - Mortgage	1.19B
PMTS	CPI Card Group Inc.	Credit Services	323.66M
PMVP	PMV Pharmaceuticals, Inc.	Biotechnology	86.17M
PNBK	Patriot National Bancorp, Inc.	Banks - Regional	6.92M
PNC	The PNC Financial Services Group, Inc.	Banks - Regional	72.36B
PNFP	Pinnacle Financial Partners, Inc.	Banks - Regional	7.44B
PNM	PNM Resources, Inc.	Utilities - Regulated Electric	3.74B
PNNT	PennantPark Investment Corporation	Asset Management	472.55M
PNR	Pentair plc	Specialty Industrial Machinery	14.55B
PNRG	PrimeEnergy Resources Corporation	Oil & Gas Exploration & Production	205.26M
PNST	Pinstripes Holdings Inc.	Restaurants	87.43M
PNTG	The Pennant Group, Inc.	Medical Care Facilities	895.36M
PNW	Pinnacle West Capital Corporation	Utilities - Regulated Electric	9.71B
POAI	Predictive Oncology Inc.	Medical Instruments & Supplies	4.88M
POCI	Precision Optics Corporation, Inc.	Medical Instruments & Supplies	37.48M
PODC	PodcastOne Inc	Internet Content & Information	35.21M
PODD	Insulet Corporation	Medical Devices	13.58B
POET	POET Technologies Inc.	Semiconductors	179.47M
POLA	Polar Power, Inc.	Electrical Equipment & Parts	7.38M
POOL	Pool Corporation	Industrial Distribution	14.22B
POR	Portland General Electric Company	Utilities - Regulated Electric	4.89B
POST	Post Holdings, Inc.	Packaged Foods	6.55B
POWI	Power Integrations, Inc.	Semiconductors	4.09B
POWL	Powell Industries, Inc.	Electrical Equipment & Parts	1.61B
POWW	AMMO, Inc.	Aerospace & Defense	221.08M
PPBI	Pacific Premier Bancorp, Inc.	Banks - Regional	2.57B
PPBT	Purple Biotech Ltd.	Biotechnology	12.59M
PPC	Pilgrim's Pride Corporation	Packaged Foods	9.89B
PPG	PPG Industries, Inc.	Specialty Chemicals	29.79B
PPIH	Perma-Pipe International Holdings, Inc.	Building Products & Equipment	75.45M
PPL	PPL Corporation	Utilities - Regulated Electric	22.09B
PPSI	Pioneer Power Solutions, Inc.	Electrical Equipment & Parts	47.27M
PPTA	Perpetua Resources Corp.	Other Precious Metals & Mining	413.08M
PPYA	Papaya Growth Opportunity Corp. I	Shell Companies	95.74M
PR	Permian Resources Corporation	Oil & Gas Exploration & Production	11.77B
PRA	ProAssurance Corporation	Insurance - Property & Casualty	623.37M
PRAA	PRA Group, Inc.	Credit Services	1.00B
PRAX	Praxis Precision Medicines, Inc.	Biotechnology	979.43M
PRCH	Porch Group, Inc.	Software - Application	194.90M
PRCT	PROCEPT BioRobotics Corporation	Medical Devices	3.20B
PRDO	Perdoceo Education Corporation	Education & Training Services	1.66B
PRE	Prenetics Global Limited	Diagnostics & Research	68.42M
PRFT	Perficient, Inc.	Information Technology Services	2.65B
PRFX	PainReform Ltd.	Drug Manufacturers - Specialty & Generic	1.42M
PRG	PROG Holdings, Inc.	Rental & Leasing Services	1.92B
PRGO	Perrigo Company plc	Drug Manufacturers - Specialty & Generic	3.82B
PRGS	Progress Software Corporation	Software - Infrastructure	2.51B
PRI	Primerica, Inc.	Insurance - Life	8.70B
PRIM	Primoris Services Corporation	Engineering & Construction	2.89B
PRK	Park National Corporation	Banks - Regional	2.91B
PRKS	United Parks & Resorts Inc.	Leisure	3.29B
PRLB	Proto Labs, Inc.	Metal Fabrication	864.80M
TRX	TRX Gold Corporation	Gold	115.18M
TS	Tenaris S.A.	Oil & Gas Equipment & Services	18.06B
TSAT	Telesat Corporation	Communication Equipment	110.93M
TSBK	Timberland Bancorp, Inc.	Banks - Regional	241.76M
TSBX	Turnstone Biologics Corp.	Biotechnology	56.61M
TSCO	Tractor Supply Company	Specialty Retail	28.35B
TSE	Trinseo PLC	Specialty Chemicals	98.82M
TSEM	Tower Semiconductor Ltd.	Semiconductors	4.54B
TSHA	Taysha Gene Therapies, Inc.	Biotechnology	451.09M
TSLA	Tesla, Inc.	Auto Manufacturers	709.99B
TSLX	Sixth Street Specialty Lending, Inc.	Asset Management	1.94B
TSM	Taiwan Semiconductor Manufacturing Company Limited	Semiconductors	702.37B
TSN	Tyson Foods, Inc.	Farm Products	21.26B
TSQ	Townsquare Media, Inc.	Advertising Agencies	180.85M
TSVT	2seventy bio, Inc.	Biotechnology	252.40M
TT	Trane Technologies plc	Building Products & Equipment	74.62B
TTC	The Toro Company	Tools & Accessories	9.95B
TTD	The Trade Desk, Inc.	Software - Application	43.86B
TTE	TotalEnergies SE	Oil & Gas Integrated	155.49B
TTEC	TTEC Holdings, Inc.	Information Technology Services	392.58M
TTEK	Tetra Tech, Inc.	Engineering & Construction	11.35B
TTGT	TechTarget, Inc.	Internet Content & Information	921.26M
TTI	TETRA Technologies, Inc.	Oil & Gas Equipment & Services	474.72M
TTMI	TTM Technologies, Inc.	Electronic Components	2.14B
TTNP	Titan Pharmaceuticals, Inc.	Biotechnology	5.10M
TTOO	T2 Biosystems, Inc.	Diagnostics & Research	86.62M
TTSH	Tile Shop Holdings, Inc.	Home Improvement Retail	318.81M
TTWO	Take-Two Interactive Software, Inc.	Electronic Gaming & Multimedia	26.36B
TU	TELUS Corporation	Telecom Services	23.76B
TUP	Tupperware Brands Corporation	Packaging & Containers	59.56M
TURB	Turbo Energy, S.A.	Solar	12.89M
TURN	180 Degree Capital Corp.	Asset Management	34.80M
TUSK	Mammoth Energy Services, Inc.	Conglomerates	186.25M
TUYA	Tuya Inc.	Software - Infrastructure	897.54M
TV	Grupo Televisa, S.A.B.	Telecom Services	1.20B
TVGN	Tevogen Bio Holdings Inc.	Biotechnology	108.32M
TVTX	Travere Therapeutics, Inc.	Biotechnology	756.72M
TW	Tradeweb Markets Inc.	Capital Markets	25.83B
TWFG	TWFG, Inc.	Insurance - Diversified	323.12M
TWG	Top Wealth Group Holding Limited	Food Distribution	24.16M
TWI	Titan International, Inc.	Farm & Heavy Construction Machinery	609.20M
TWIN	Twin Disc, Incorporated	Specialty Industrial Machinery	196.09M
TWKS	Thoughtworks Holding, Inc.	Information Technology Services	1.09B
TWLO	Twilio Inc.	Internet Content & Information	10.11B
TWO	Two Harbors Investment Corp.	REIT - Mortgage	1.42B
TWOU	2U, Inc.	Education & Training Services	8.97M
TWST	Twist Bioscience Corporation	Diagnostics & Research	3.27B
TX	Ternium S.A.	Steel	7.00B
TXG	10x Genomics, Inc.	Health Information Services	2.42B
TXMD	TherapeuticsMD, Inc.	Drug Manufacturers - Specialty & Generic	20.41M
TXN	Texas Instruments Incorporated	Semiconductors	183.62B
TXO	TXO Partners L.P.	Oil & Gas Exploration & Production	756.82M
TXRH	Texas Roadhouse, Inc.	Restaurants	11.62B
TXT	Textron Inc.	Aerospace & Defense	17.55B
TYG	Tortoise Energy Infrastructure Corporation	Asset Management	415.09M
TYGO	Tigo Energy, Inc.	Solar	94.98M
TYL	Tyler Technologies, Inc.	Software - Application	24.32B
TYRA	Tyra Biosciences, Inc.	Biotechnology	1.07B
TZOO	Travelzoo	Advertising Agencies	132.81M
U	Unity Software Inc.	Software - Application	6.27B
UA	Under Armour, Inc.	Apparel Manufacturing	3.00B
UAA	Under Armour, Inc.	Apparel Manufacturing	3.01B
UAL	United Airlines Holdings, Inc.	Airlines	15.58B
UAMY	United States Antimony Corporation	Other Industrial Metals & Mining	38.13M
UAN	CVR Partners, LP	Agricultural Inputs	813.86M
UAVS	AgEagle Aerial Systems, Inc.	Computer Hardware	4.95M
UBCP	United Bancorp, Inc.	Banks - Regional	74.09M
UBER	Uber Technologies, Inc.	Software - Application	131.96B
UBFO	United Security Bancshares	Banks - Regional	141.98M
UBS	UBS Group AG	Banks - Diversified	96.39B
UBSI	United Bankshares, Inc.	Banks - Regional	5.28B
UBX	Unity Biotechnology, Inc.	Biotechnology	24.18M
UBXG	U-BX Technology Ltd.	Software - Infrastructure	188.41M
UCAR	U Power Limited	Auto & Truck Dealerships	16.29M
UCBI	United Community Banks, Inc.	Banks - Regional	3.71B
UCL	uCloudlink Group Inc.	Telecom Services	59.35M
UCTT	Ultra Clean Holdings, Inc.	Semiconductor Equipment & Materials	1.91B
UDMY	Udemy, Inc.	Education & Training Services	1.39B
UDR	UDR, Inc.	REIT - Residential	13.36B
UE	Urban Edge Properties	REIT - Retail	2.46B
UEC	Uranium Energy Corp.	Uranium	2.28B
UEIC	Universal Electronics Inc.	Consumer Electronics	149.53M
UFCS	United Fire Group, Inc.	Insurance - Property & Casualty	564.86M
UFI	Unifi, Inc.	Textile Manufacturing	110.79M
UFPI	UFP Industries, Inc.	Lumber & Wood Production	8.27B
UFPT	UFP Technologies, Inc.	Medical Devices	2.44B
UG	United-Guardian, Inc.	Household & Personal Products	50.92M
UGI	UGI Corporation	Utilities - Regulated Gas	5.20B
UGP	Ultrapar Participações S.A.	Oil & Gas Refining & Marketing	4.38B
UGRO	urban-gro, Inc.	Farm & Heavy Construction Machinery	17.25M
UHAL	U-Haul Holding Company	Rental & Leasing Services	12.42B
UHAL.B	U-Haul Holding Company	Rental & Leasing Services	12.44B
UHG	United Homes Group, Inc.	Residential Construction	291.21M
UHS	Universal Health Services, Inc.	Medical Care Facilities	12.91B
UHT	Universal Health Realty Income Trust	REIT - Healthcare Facilities	595.17M
UI	Ubiquiti Inc.	Communication Equipment	10.69B
UIS	Unisys Corporation	Information Technology Services	331.95M
UK	Ucommune International Ltd	Real Estate Services	1.36M
UL	Unilever PLC	Household & Personal Products	151.59B
ULBI	Ultralife Corporation	Electrical Equipment & Parts	180.20M
ULCC	Frontier Group Holdings, Inc.	Airlines	918.23M
ULH	Universal Logistics Holdings, Inc.	Trucking	1.10B
ULS	UL Solutions Inc.	Specialty Business Services	9.03B
ULTA	Ulta Beauty, Inc.	Specialty Retail	17.40B
ULY	Urgent.ly Inc.	Software - Application	19.87M
UMAC	Unusual Machines, Inc.	Shell Companies	16.89M
UMBF	UMB Financial Corporation	Banks - Regional	4.81B
UMC	United Microelectronics Corporation	Semiconductors	18.68B
UMH	UMH Properties, Inc.	REIT - Residential	1.24B
UNB	Union Bankshares, Inc.	Banks - Regional	112.40M
UNCY	Unicycive Therapeutics, Inc.	Biotechnology	35.90M
UNF	UniFirst Corporation	Specialty Business Services	3.51B
UNFI	United Natural Foods, Inc.	Food Distribution	931.90M
UNH	UnitedHealth Group Incorporated	Healthcare Plans	531.90B
UNIT	Uniti Group Inc.	REIT - Specialty	862.69M
UNM	Unum Group	Insurance - Life	10.22B
UNP	Union Pacific Corporation	Railroads	149.88B
UNTY	Unity Bancorp, Inc.	Banks - Regional	345.35M
UONE	Urban One, Inc.	Broadcasting	84.74M
UONEK	Urban One, Inc.	Broadcasting	80.98M
UP	Wheels Up Experience Inc.	Airports & Air Services	1.84B
UPBD	Upbound Group, Inc.	Software - Application	2.06B
UPC	Universe Pharmaceuticals INC	Drug Manufacturers - Specialty & Generic	13.33M
UPLD	Upland Software, Inc.	Software - Application	67.74M
UPS	United Parcel Service, Inc.	Integrated Freight & Logistics	110.82B
UPST	Upstart Holdings, Inc.	Credit Services	2.22B
UPWK	Upwork Inc.	Internet Content & Information	1.53B
UPXI	Upexi, Inc.	Internet Content & Information	7.31M
URBN	Urban Outfitters, Inc.	Apparel Retail	4.35B
URG	Ur-Energy Inc.	Uranium	325.28M
URGN	UroGen Pharma Ltd.	Biotechnology	665.31M
URI	United Rentals, Inc.	Rental & Leasing Services	48.03B
UROY	Uranium Royalty Corp.	Uranium	265.25M
USAC	USA Compression Partners, LP	Oil & Gas Equipment & Services	2.67B
USAP	Universal Stainless & Alloy Products, Inc.	Steel	300.64M
USAS	Americas Gold and Silver Corporation	Other Industrial Metals & Mining	60.12M
USAU	U.S. Gold Corp.	Gold	59.62M
USB	U.S. Bancorp	Banks - Regional	71.15B
USCB	USCB Financial Holdings, Inc.	Banks - Regional	328.05M
USEA	United Maritime Corporation	Marine Shipping	23.16M
USEG	U.S. Energy Corp.	Oil & Gas Exploration & Production	25.65M
USFD	US Foods Holding Corp.	Food Distribution	13.33B
USGO	U.S. GoldMining Inc.	Other Industrial Metals & Mining	78.05M
USIO	Usio, Inc.	Software - Infrastructure	41.76M
USLM	United States Lime & Minerals, Inc.	Building Materials	2.37B
USM	United States Cellular Corporation	Telecom Services	4.53B
USNA	USANA Health Sciences, Inc.	Packaged Foods	811.84M
USPH	U.S. Physical Therapy, Inc.	Medical Care Facilities	1.47B
UTHR	United Therapeutics Corporation	Biotechnology	14.95B
UTI	Universal Technical Institute, Inc.	Education & Training Services	1.04B
UTL	Unitil Corporation	Utilities - Diversified	973.18M
UTMD	Utah Medical Products, Inc.	Medical Instruments & Supplies	246.11M
UTSI	UTStarcom Holdings Corp.	Communication Equipment	25.66M
UTZ	Utz Brands, Inc.	Packaged Foods	1.19B
UUU	Universal Security Instruments, Inc.	Security & Protection Services	3.49M
UUUU	Energy Fuels Inc.	Uranium	900.09M
UVE	Universal Insurance Holdings, Inc.	Insurance - Property & Casualty	570.58M
UVSP	Univest Financial Corporation	Banks - Regional	835.12M
UVV	Universal Corporation	Tobacco	1.32B
UWMC	UWM Holdings Corporation	Mortgage Finance	13.05B
UXIN	Uxin Limited	Auto & Truck Dealerships	321.14M
V	Visa Inc.	Credit Services	519.37B
VABK	Virginia National Bankshares Corporation	Banks - Regional	199.53M
VAC	Marriott Vacations Worldwide Corporation	Resorts & Casinos	3.02B
VAL	Valaris Limited	Oil & Gas Equipment & Services	5.55B
VALE	Vale S.A.	Other Industrial Metals & Mining	45.74B
VALN	Valneva SE	Biotechnology	496.44M
VALU	Value Line, Inc.	Financial Data & Stock Exchanges	460.13M
VANI	Vivani Medical, Inc.	Biotechnology	67.62M
VATE	INNOVATE Corp.	Engineering & Construction	73.11M
VBFC	Village Bank and Trust Financial Corp.	Banks - Regional	69.98M
VBIV	VBI Vaccines Inc.	Biotechnology	3.50M
VBNK	VersaBank	Banks - Regional	313.91M
VBTX	Veritex Holdings, Inc.	Banks - Regional	1.38B
VC	Visteon Corporation	Auto Parts	3.13B
VCEL	Vericel Corporation	Biotechnology	2.48B
VCIG	VCI Global Limited	Consulting Services	26.12M
VCNX	Vaccinex, Inc.	Biotechnology	12.49M
VCSA	Vacasa, Inc.	Software - Application	100.18M
VCTR	Victory Capital Holdings, Inc.	Asset Management	3.41B
VCYT	Veracyte, Inc.	Diagnostics & Research	1.79B
VECO	Veeco Instruments Inc.	Semiconductor Equipment & Materials	2.20B
VEEE	Twin Vee Powercats Co.	Recreational Vehicles	6.09M
VEEV	Veeva Systems Inc.	Health Information Services	31.08B
VEL	Velocity Financial, Inc.	Mortgage Finance	625.74M
VEON	VEON Ltd.	Telecom Services	657.62M
VERA	Vera Therapeutics, Inc.	Biotechnology	1.91B
VERB	Verb Technology Company, Inc.	Software - Application	9.00M
VERI	Veritone, Inc.	Software - Infrastructure	102.88M
VERO	Venus Concept Inc.	Medical Devices	5.02M
VERU	Veru Inc.	Biotechnology	129.77M
VERV	Verve Therapeutics, Inc.	Biotechnology	599.51M
VERX	Vertex, Inc.	Software - Application	6.15B
VET	Vermilion Energy Inc.	Oil & Gas Exploration & Production	1.64B
VEV	Vicinity Motor Corp.	Auto Manufacturers	19.34M
VFC	V.F. Corporation	Apparel Manufacturing	6.42B
VFF	Village Farms International, Inc.	Farm Products	125.74M
VFS	VinFast Auto Ltd.	Auto Manufacturers	8.99B
VGAS	Verde Clean Fuels, Inc.	Utilities - Renewable	41.92M
VGR	Vector Group Ltd.	Tobacco	2.02B
VGZ	Vista Gold Corp.	Gold	63.62M
VHAI	Vocodia Holdings Corp.	Software - Infrastructure	3.90M
VHC	VirnetX Holding Corp	Software - Infrastructure	23.00M
VHI	Valhi, Inc.	Chemicals	570.30M
VIAV	Viavi Solutions Inc.	Communication Equipment	1.75B
VICI	VICI Properties Inc.	REIT - Diversified	32.84B
VICR	Vicor Corporation	Electronic Components	1.82B
VIGL	Vigil Neuroscience, Inc.	Biotechnology	168.75M
VIK	Viking Holdings Ltd	Travel Services	15.28B
VINC	Vincerx Pharma, Inc.	Biotechnology	18.84M
VINE	Fresh Vine Wine, Inc.	Beverages - Wineries & Distilleries	8.06M
VINO	Gaucho Group Holdings, Inc.	Real Estate - Diversified	5.79M
VINP	Vinci Partners Investments Ltd.	Asset Management	611.16M
VIOT	Viomi Technology Co., Ltd	Furnishings, Fixtures & Appliances	58.78M
VIPS	Vipshop Holdings Limited	Internet Retail	7.24B
VIR	Vir Biotechnology, Inc.	Biotechnology	1.37B
VIRC	Virco Mfg. Corporation	Furnishings, Fixtures & Appliances	270.34M
VIRI	Virios Therapeutics, Inc.	Biotechnology	5.83M
VIRT	Virtu Financial, Inc.	Capital Markets	2.46B
VIRX	Viracta Therapeutics, Inc.	Biotechnology	19.49M
VISL	Vislink Technologies, Inc.	Communication Equipment	19.05M
VIST	Vista Energy, SAB de CV	Oil & Gas Exploration & Production	4.00B
VITL	Vital Farms, Inc.	Farm Products	1.53B
VIV	Telefônica Brasil S.A.	Telecom Services	13.96B
VIVK	Vivakor, Inc.	Oil & Gas Integrated	61.90M
VKTX	Viking Therapeutics, Inc.	Biotechnology	6.36B
VLCN	Volcon, Inc.	Auto Manufacturers	7.35M
VLD	Velo3D, Inc.	Computer Hardware	23.46M
VLGEA	Village Super Market, Inc.	Grocery Stores	402.11M
VLN	Valens Semiconductor Ltd.	Semiconductors	236.72M
VLO	Valero Energy Corporation	Oil & Gas Refining & Marketing	52.20B
VLRS	Controladora Vuela Compañía de Aviación, SAB de CV	Airlines	723.05M
VLTO	Veralto Corporation	Pollution & Treatment Controls	26.14B
VLY	Valley National Bancorp	Banks - Regional	4.17B
VMAR	Vision Marine Technologies Inc.	Recreational Vehicles	5.75M
VMC	Vulcan Materials Company	Building Materials	35.52B
VMCA	Valuence Merger Corp. I	Shell Companies	133.76M
VMD	Viemed Healthcare, Inc.	Medical Devices	278.93M
VMEO	Vimeo, Inc.	Software - Application	631.36M
VMI	Valmont Industries, Inc.	Conglomerates	6.07B
VNCE	Vince Holding Corp.	Apparel Manufacturing	21.07M
VNDA	Vanda Pharmaceuticals Inc.	Biotechnology	341.33M
VNET	VNET Group, Inc.	Information Technology Services	481.32M
VNO	Vornado Realty Trust	REIT - Office	5.60B
VNOM	Viper Energy Partners LP	Oil & Gas Midstream	7.40B
VNRX	VolitionRx Limited	Diagnostics & Research	55.56M
VNT	Vontier Corporation	Scientific & Technical Instruments	6.02B
VOC	VOC Energy Trust	Oil & Gas Exploration & Production	83.13M
VOD	Vodafone Group PLC	Telecom Services	24.93B
VOR	Vor Biopharma Inc.	Biotechnology	63.55M
VOXR	Vox Royalty Corp.	Other Precious Metals & Mining	144.92M
VOXX	VOXX International Corporation	Consumer Electronics	59.57M
VOYA	Voya Financial, Inc.	Financial Conglomerates	7.52B
VPG	Vishay Precision Group, Inc.	Scientific & Technical Instruments	454.03M
VRA	Vera Bradley, Inc.	Footwear & Accessories	198.75M
VRAR	The Glimpse Group, Inc.	Software - Infrastructure	16.70M
VRAX	Virax Biolabs Group Limited	Biotechnology	3.00M
VRCA	Verrica Pharmaceuticals Inc.	Biotechnology	293.12M
VRDN	Viridian Therapeutics, Inc.	Biotechnology	1.10B
VRE	Veris Residential, Inc.	REIT - Residential	1.49B
VREX	Varex Imaging Corporation	Medical Devices	605.32M
VRM	Vroom, Inc.	Auto & Truck Dealerships	15.84M
VRME	VerifyMe, Inc.	Security & Protection Services	12.31M
VRN	Veren Inc.	Oil & Gas Exploration & Production	4.62B
VRNA	Verona Pharma plc	Biotechnology	1.78B
VRNS	Varonis Systems, Inc.	Software - Infrastructure	5.97B
VRNT	Verint Systems Inc.	Software - Infrastructure	2.20B
VRPX	Virpax Pharmaceuticals, Inc.	Biotechnology	5.56M
VRRM	Verra Mobility Corporation	Infrastructure Operations	5.00B
VRSK	Verisk Analytics, Inc.	Consulting Services	40.61B
VRSN	VeriSign, Inc.	Software - Infrastructure	18.39B
VRT	Vertiv Holdings Co	Electrical Equipment & Parts	27.41B
VRTS	Virtus Investment Partners, Inc.	Asset Management	1.65B
VRTX	Vertex Pharmaceuticals Incorporated	Biotechnology	129.52B
VS	Versus Systems Inc.	Software - Application	3.88M
VSAC	Vision Sensing Acquisition Corp.	Shell Companies	47.90M
VSAT	Viasat, Inc.	Communication Equipment	2.46B
VSCO	Victoria's Secret & Co.	Apparel Retail	1.38B
VSEC	VSE Corporation	Aerospace & Defense	1.58B
VSEE	VSee Lab, Inc./iDoc Virtual Telehealth Solutions, Inc.	Health Information Services	39.38M
VSH	Vishay Intertechnology, Inc.	Semiconductors	3.27B
VSME	VS Media Holdings Limited	Advertising Agencies	7.65M
VST	Vistra Corp.	Utilities - Independent Power Producers	24.26B
VSTA	Vasta Platform Limited	Education & Training Services	241.39M
VSTE	Vast Renewables Limited	Shell Companies	69.54M
VSTM	Verastem, Inc.	Biotechnology	102.83M
VSTO	Vista Outdoor Inc.	Leisure	2.36B
VSTS	Vestis Corporation	Rental & Leasing Services	1.68B
VTAK	Catheter Precision, Inc.	Medical Devices	1.55M
VTEX	VTEX	Software - Application	1.16B
VTGN	VistaGen Therapeutics, Inc.	Biotechnology	94.29M
VTLE	Vital Energy, Inc.	Oil & Gas Exploration & Production	1.60B
VTMX	Corporación Inmobiliaria Vesta, S.A.B. de C.V.	Real Estate - Development	2.42B
VTNR	Vertex Energy, Inc.	Oil & Gas Refining & Marketing	73.40M
VTOL	Bristow Group Inc.	Oil & Gas Equipment & Services	1.05B
VTR	Ventas, Inc.	REIT - Healthcare Facilities	22.19B
VTRS	Viatris Inc.	Drug Manufacturers - Specialty & Generic	14.29B
VTS	Vitesse Energy, Inc.	Oil & Gas Exploration & Production	744.76M
VTSI	VirTra, Inc.	Software - Application	92.02M
VTVT	vTv Therapeutics Inc.	Biotechnology	38.93M
VTYX	Ventyx Biosciences, Inc.	Biotechnology	166.03M
VUZI	Vuzix Corporation	Consumer Electronics	80.58M
VVI	Viad Corp	Specialty Business Services	703.78M
VVOS	Vivos Therapeutics, Inc.	Medical Devices	7.88M
VVPR	VivoPower International PLC	Solar	6.17M
VVV	Valvoline Inc.	Auto & Truck Dealerships	5.88B
VVX	V2X, Inc.	Aerospace & Defense	1.65B
VWE	Vintage Wine Estates, Inc.	Beverages - Wineries & Distilleries	3.86M
VXRT	Vaxart, Inc.	Biotechnology	151.26M
VYGR	Voyager Therapeutics, Inc.	Biotechnology	500.42M
VYNE	VYNE Therapeutics Inc.	Biotechnology	27.17M
VYX	NCR Voyix Corporation	Information Technology Services	2.14B
VZ	Verizon Communications Inc.	Telecom Services	168.55B
VZIO	VIZIO Holding Corp.	Consumer Electronics	2.19B
VZLA	Vizsla Silver Corp.	Other Industrial Metals & Mining	468.31M
W	Wayfair Inc.	Internet Retail	6.52B
WAB	Westinghouse Air Brake Technologies Corporation	Railroads	27.98B
WABC	Westamerica Bancorporation	Banks - Regional	1.45B
WAFD	WaFd Inc	Banks - Regional	2.91B
WAFU	Wah Fu Education Group Limited	Education & Training Services	8.35M
WAL	Western Alliance Bancorporation	Banks - Regional	8.80B
WALD	Waldencast plc	Shell Companies	418.86M
WASH	Washington Trust Bancorp, Inc.	Banks - Regional	549.66M
WAT	Waters Corporation	Diagnostics & Research	19.19B
WATT	Energous Corporation	Scientific & Technical Instruments	5.86M
WAVD	WaveDancer, Inc.	Information Technology Services	4.19M
WAVE	Eco Wave Power Global AB (publ)	Utilities - Renewable	15.82M
WAVS	Western Acquisition Ventures Corp.	Shell Companies	37.73M
WAY	Waystar Holding Corp.	Health Information Services	3.85B
WB	Weibo Corporation	Internet Content & Information	1.88B
WBA	Walgreens Boots Alliance, Inc.	Pharmaceutical Retailers	10.58B
WBD	Warner Bros. Discovery, Inc.	Entertainment	21.80B
WBS	Webster Financial Corporation	Banks - Regional	8.41B
WBTN	WEBTOON Entertainment Inc.	Software - Application	2.71B
WBUY	WEBUY GLOBAL LTD.	Internet Retail	11.04M
WBX	Wallbox N.V.	Electronic Components	319.66M
WCC	WESCO International, Inc.	Industrial Distribution	8.65B
WCN	Waste Connections, Inc.	Waste Management	45.78B
WD	Walker & Dunlop, Inc.	Mortgage Finance	3.57B
WDAY	Workday, Inc.	Software - Application	60.15B
WDC	Western Digital Corporation	Computer Hardware	20.88B
WDFC	WD-40 Company	Specialty Chemicals	3.62B
WDH	Waterdrop Inc.	Insurance - Diversified	407.18M
WDS	Woodside Energy Group Ltd	Oil & Gas Exploration & Production	33.21B
WEAV	Weave Communications, Inc.	Health Information Services	718.34M
WEC	WEC Energy Group, Inc.	Utilities - Regulated Electric	26.76B
WEL	Integrated Wellness Acquisition Corp	Shell Companies	82.92M
WELL	Welltower Inc.	REIT - Healthcare Facilities	67.02B
WEN	The Wendy's Company	Restaurants	3.53B
WENA	Anew Medical, Inc.	Biotechnology	19.95M
WERN	Werner Enterprises, Inc.	Trucking	2.55B
WES	Western Midstream Partners, LP	Oil & Gas Midstream	15.39B
WEST	Westrock Coffee Company, LLC	Packaged Foods	889.05M
WETH	Wetouch Technology Inc.	Real Estate Services	20.88M
WEX	WEX Inc.	Software - Infrastructure	7.67B
WEYS	Weyco Group, Inc.	Footwear & Accessories	315.49M
WF	Woori Financial Group Inc.	Banks - Regional	8.54B
WFC	Wells Fargo & Company	Banks - Diversified	209.75B
WFCF	Where Food Comes From, Inc.	Software - Application	57.72M
WFG	West Fraser Timber Co. Ltd.	Lumber & Wood Production	6.93B
WFRD	Weatherford International plc	Oil & Gas Equipment & Services	8.39B
WGO	Winnebago Industries, Inc.	Recreational Vehicles	1.77B
WGS	GeneDx Holdings Corp.	Health Information Services	815.39M
WH	Wyndham Hotels & Resorts, Inc.	Lodging	6.22B
WHD	Cactus, Inc.	Oil & Gas Equipment & Services	4.04B
WHF	WhiteHorse Finance, Inc.	Asset Management	281.24M
WHG	Westwood Holdings Group, Inc.	Asset Management	125.26M
WHLM	Wilhelmina International, Inc.	Specialty Business Services	29.76M
WHLR	Wheeler Real Estate Investment Trust, Inc.	REIT - Retail	3.77M
WHR	Whirlpool Corporation	Furnishings, Fixtures & Appliances	5.39B
WILC	G. Willi-Food International Ltd.	Food Distribution	136.31M
WIMI	WiMi Hologram Cloud Inc.	Advertising Agencies	81.78M
WINA	Winmark Corporation	Specialty Retail	1.39B
WING	Wingstop Inc.	Restaurants	10.97B
WINT	Windtree Therapeutics, Inc.	Biotechnology	3.43M
WINV	WinVest Acquisition Corp.	Shell Companies	46.17M
WISA	WiSA Technologies, Inc.	Semiconductors	10.53M
WIT	Wipro Limited	Information Technology Services	32.34B
WIX	Wix.com Ltd.	Software - Infrastructure	8.52B
WK	Workiva Inc.	Software - Application	4.03B
WKC	World Kinect Corporation	Oil & Gas Refining & Marketing	1.70B
WKEY	WISeKey International Holding AG	Semiconductors	20.63M
WKHS	Workhorse Group Inc.	Auto Manufacturers	27.77M
WKME	WalkMe Ltd.	Software - Application	1.30B
WKSP	Worksport Ltd.	Auto Parts	19.16M
WLDN	Willdan Group, Inc.	Engineering & Construction	456.38M
WLDS	Wearable Devices Ltd.	Consumer Electronics	6.56M
WLFC	Willis Lease Finance Corporation	Rental & Leasing Services	567.73M
WLGS	WANG & LEE GROUP, Inc.	Engineering & Construction	7.55M
WLK	Westlake Corporation	Specialty Chemicals	18.52B
WLKP	Westlake Chemical Partners LP	Chemicals	807.40M
WLY	John Wiley & Sons, Inc.	Publishing	2.56B
WLYB	John Wiley & Sons, Inc.	Publishing	2.62B
WM	Waste Management, Inc.	Waste Management	80.65B
WMB	The Williams Companies, Inc.	Oil & Gas Midstream	51.71B
WMG	Warner Music Group Corp.	Entertainment	15.47B
WMK	Weis Markets, Inc.	Grocery Stores	2.01B
WMPN	William Penn Bancorporation	Banks - Regional	113.70M
WMS	Advanced Drainage Systems, Inc.	Building Products & Equipment	13.38B
WMT	Walmart Inc.	Discount Stores	558.74B
WNC	Wabash National Corporation	Farm & Heavy Construction Machinery	942.24M
WNEB	Western New England Bancorp, Inc.	Banks - Regional	175.40M
WNS	WNS (Holdings) Limited	Information Technology Services	2.65B
WNW	Meiwu Technology Company Limited	Internet Retail	2.86M
WOLF	Wolfspeed, Inc.	Semiconductors	2.29B
WOOF	Petco Health and Wellness Company, Inc.	Specialty Retail	935.00M
WOR	Worthington Industries, Inc.	Metal Fabrication	2.48B
WORX	SCWorx Corp.	Health Information Services	1.50M
WOW	WideOpenWest, Inc.	Telecom Services	459.20M
WPC	W. P. Carey Inc.	REIT - Diversified	13.28B
WPM	Wheaton Precious Metals Corp.	Gold	26.68B
WPP	WPP plc	Advertising Agencies	10.37B
WPRT	Westport Fuel Systems Inc.	Auto Parts	103.15M
WRAP	Wrap Technologies, Inc.	Scientific & Technical Instruments	76.93M
WRB	W. R. Berkley Corporation	Insurance - Property & Casualty	21.21B
WRBY	Warby Parker Inc.	Medical Instruments & Supplies	1.92B
WRLD	World Acceptance Corporation	Credit Services	719.50M
WRN	Western Copper and Gold Corporation	Other Industrial Metals & Mining	219.76M
WRNT	Warrantee Inc.	Software - Application	6.40M
WS	Worthington Steel, Inc.	Steel	1.96B
WSBC	WesBanco, Inc.	Banks - Regional	1.92B
WSBF	Waterstone Financial, Inc.	Banks - Regional	295.05M
WSC	WillScot Mobile Mini Holdings Corp.	Rental & Leasing Services	7.70B
WSFS	WSFS Financial Corporation	Banks - Regional	3.42B
WSM	Williams-Sonoma, Inc.	Specialty Retail	19.37B
WSO	Watsco, Inc.	Industrial Distribution	19.42B
WSO.B	Watsco, Inc.	Industrial Distribution	19.84B
WSR	Whitestone REIT	REIT - Retail	696.44M
WST	West Pharmaceutical Services, Inc.	Medical Instruments & Supplies	21.15B
WT	WisdomTree, Inc.	Asset Management	1.79B
WTBA	West Bancorporation, Inc.	Banks - Regional	341.20M
WTFC	Wintrust Financial Corporation	Banks - Regional	6.74B
WTI	W&T Offshore, Inc.	Oil & Gas Exploration & Production	343.65M
WTM	White Mountains Insurance Group, Ltd.	Insurance - Property & Casualty	4.53B
WTMA	Welsbach Technology Metals Acquisition Corp.	Shell Companies	49.47M
WTO	UTime Limited	Consumer Electronics	21.56M
WTRG	Essential Utilities, Inc.	Utilities - Regulated Water	11.09B
WTS	Watts Water Technologies, Inc.	Specialty Industrial Machinery	6.92B
WTTR	Select Energy Services, Inc.	Specialty Chemicals	1.20B
WTW	Willis Towers Watson PLC	Insurance Brokers	28.85B
WU	The Western Union Company	Credit Services	4.40B
WULF	TeraWulf Inc.	Capital Markets	1.33B
WVE	Wave Life Sciences Ltd.	Biotechnology	784.45M
WVVI	Willamette Valley Vineyards, Inc.	Beverages - Wineries & Distilleries	18.54M
WW	WW International, Inc.	Personal Services	92.36M
WWD	Woodward, Inc.	Aerospace & Defense	9.18B
WWR	Westwater Resources, Inc.	Other Industrial Metals & Mining	29.50M
WWW	Wolverine World Wide, Inc.	Footwear & Accessories	1.17B
WY	Weyerhaeuser Company	REIT - Specialty	23.14B
WYNN	Wynn Resorts, Limited	Resorts & Casinos	9.21B
WYY	WidePoint Corporation	Information Technology Services	34.45M
X	United States Steel Corporation	Steel	9.10B
XAIR	Beyond Air, Inc.	Medical Devices	27.14M
XBIO	Xenetic Biosciences, Inc.	Biotechnology	6.39M
XBIT	XBiotech Inc.	Biotechnology	215.84M
XBP	XBP Europe Holdings, Inc.	Software - Infrastructure	39.22M
XCUR	Exicure, Inc.	Biotechnology	4.15M
XEL	Xcel Energy Inc.	Utilities - Regulated Electric	32.44B
XELA	Exela Technologies, Inc.	Software - Application	15.66M
XELB	Xcel Brands, Inc.	Apparel Manufacturing	16.51M
XENE	Xenon Pharmaceuticals Inc.	Biotechnology	3.31B
XERS	Xeris Biopharma Holdings, Inc.	Biotechnology	363.60M
XFIN	ExcelFin Acquisition Corp.	Shell Companies	80.33M
XFOR	X4 Pharmaceuticals, Inc.	Biotechnology	139.52M
XGN	Exagen Inc.	Diagnostics & Research	34.57M
XHG	XChange TEC.INC	Real Estate Services	5.44M
XHR	Xenia Hotels & Resorts, Inc.	REIT - Hotel & Motel	1.44B
XIN	Xinyuan Real Estate Co., Ltd.	Real Estate - Development	17.45M
XLO	Xilio Therapeutics, Inc.	Biotechnology	34.14M
XMTR	Xometry, Inc.	Specialty Industrial Machinery	699.30M
XNCR	Xencor, Inc.	Biotechnology	1.29B
XNET	Xunlei Limited	Software - Infrastructure	108.15M
XOM	Exxon Mobil Corporation	Oil & Gas Integrated	529.47B
XOMA	XOMA Corporation	Biotechnology	309.30M
XOS	Xos, Inc.	Farm & Heavy Construction Machinery	48.50M
XP	XP Inc.	Capital Markets	9.54B
XPEL	XPEL, Inc.	Auto Parts	1.10B
XPER	Xperi Holding Corporation	Software - Application	360.28M
XPEV	XPeng Inc.	Auto Manufacturers	7.60B
XPL	Solitario Zinc Corp.	Other Industrial Metals & Mining	66.83M
XPO	XPO Logistics, Inc.	Trucking	13.07B
XPOF	Xponential Fitness, Inc.	Leisure	533.30M
XPON	Expion360 Inc.	Electrical Equipment & Parts	3.36M
XPRO	Expro Group Holdings N.V.	Oil & Gas Equipment & Services	2.69B
XRAY	DENTSPLY SIRONA Inc.	Medical Instruments & Supplies	5.56B
XRTX	XORTX Therapeutics Inc.	Biotechnology	5.08M
XRX	Xerox Holdings Corporation	Information Technology Services	1.36B
XTIA	XTI Aerospace, Inc.	Aerospace & Defense	7.46M
XTKG	X3 Holdings Co Ltd.	Software - Application	111.52M
XTLB	XTL Biopharmaceuticals Ltd.	Biotechnology	14.36M
XTNT	Xtant Medical Holdings, Inc.	Medical Devices	93.81M
XWEL	XWELL, Inc.	Diagnostics & Research	8.53M
XXII	22nd Century Group, Inc.	Tobacco	5.82M
XYF	X Financial	Credit Services	211.10M
XYL	Xylem Inc.	Specialty Industrial Machinery	32.22B
XYLO	Xylo Technologies Ltd.	Medical Devices	3.19M
YALA	Yalla Group Limited	Software - Application	681.52M
YCBD	cbdMD, Inc.	Drug Manufacturers - Specialty & Generic	2.13M
YELP	Yelp Inc.	Internet Content & Information	2.47B
YETI	YETI Holdings, Inc.	Leisure	3.39B
YEXT	Yext, Inc.	Software - Infrastructure	727.19M
YGMZ	MingZhu Logistics Holdings Limited	Trucking	5.97M
YHGJ	Yunhong Green CTI Ltd.	Packaging & Containers	18.90M
YI	111, Inc.	Medical Distribution	102.63M
YIBO	Planet Image International Limited	Computer Hardware	216.60M
YJ	Yunji Inc.	Internet Retail	13.54M
YMAB	Y-mAbs Therapeutics, Inc.	Biotechnology	524.18M
YMM	Full Truck Alliance Co. Ltd.	Software - Application	8.10B
YORW	The York Water Company	Utilities - Regulated Water	584.83M
YOSH	Yoshiharu Global Co.	Restaurants	5.41M
YOTA	Yotta Acquisition Corporation	Shell Companies	43.91M
YOU	Clear Secure, Inc.	Software - Application	1.96B
YPF	YPF SA	Oil & Gas Integrated	11.07B
YQ	17 Education & Technology Group Inc.	Education & Training Services	15.48M
YRD	Yiren Digital Ltd.	Credit Services	415.80M
YSG	Yatsen Holding Limited	Household & Personal Products	402.31M
YTRA	Yatra Online, Inc.	Travel Services	88.04M
YUM	Yum! Brands, Inc.	Restaurants	36.93B
YUMC	Yum China Holdings, Inc.	Restaurants	11.67B
YY	JOYY Inc.	Internet Content & Information	2.01B
YYAI	Connexa Sports Technologies Inc.	Leisure	40.39M
YYGH	YY Group Holding Limited	Personal Services	28.81M
Z	Zillow Group, Inc. Class C	Internet Content & Information	11.46B
ZAPP	Zapp Electric Vehicles Group Limited	Auto Manufacturers	28.89M
ZBAO	Zhibao Technology Inc.	Insurance Brokers	33.27M
ZBH	Zimmer Biomet Holdings, Inc.	Medical Devices	22.95B
ZBRA	Zebra Technologies Corporation	Communication Equipment	18.04B
ZCAR	Zoomcar Holdings, Inc.	Rental & Leasing Services	10.31M
ZCMD	Zhongchao Inc.	Health Information Services	8.46M
ZD	Ziff Davis, Inc.	Advertising Agencies	2.23B
ZDGE	Zedge, Inc.	Internet Content & Information	54.25M
ZENV	Zenvia Inc.	Software - Application	54.73M
ZEO	Zeo Energy Corp.	Solar	142.80M
ZEPP	Zepp Health Corporation	Consumer Electronics	34.63M
ZETA	Zeta Global Holdings Corp.	Software - Application	4.54B
ZEUS	Olympic Steel, Inc.	Steel	547.11M
ZG	Zillow Group, Inc. Class A	Internet Content & Information	11.43B
ZGN	Ermenegildo Zegna N.V.	Apparel Manufacturing	2.84B
ZH	Zhihu Inc.	Internet Content & Information	309.98M
ZI	ZoomInfo Technologies Inc.	Software - Application	4.24B
ZIM	ZIM Integrated Shipping Services Ltd.	Marine Shipping	2.22B
ZIMV	ZimVie Inc.	Medical Devices	574.43M
ZION	Zions Bancorporation,NA	Banks - Regional	7.66B
ZIP	ZipRecruiter, Inc.	Staffing & Employment Services	885.32M
ZJYL	Jin Medical International Ltd.	Medical Instruments & Supplies	439.90M
ZK	ZEEKR Intelligent Technology Holding Limited	Auto Manufacturers	4.10B
ZKH	ZKH Group Limited	Internet Retail	460.96M
ZKIN	ZK International Group Co., Ltd.	Steel	16.62M
ZLAB	Zai Lab Limited	Biotechnology	1.81B
ZLS	Zalatoris II Acquisition Corp.	Shell Companies	132.29M
ZM	Zoom Video Communications, Inc.	Software - Application	18.62B
ZNTL	Zentalis Pharmaceuticals, Inc.	Biotechnology	295.41M
ZOM	Zomedica Corp.	Medical Devices	146.99M
ZONE	CleanCore Solutions, Inc.	Pollution & Treatment Controls	14.07M
ZOOZ	ZOOZ Power Ltd.	Specialty Retail	25.22M
ZPTA	Zapata Computing Holdings Inc.	Software - Infrastructure	16.79M
ZS	Zscaler, Inc.	Software - Infrastructure	26.63B
ZTEK	Zentek Ltd.	Medical Instruments & Supplies	100.87M
ZTO	ZTO Express (Cayman) Inc.	Integrated Freight & Logistics	14.75B
ZTS	Zoetis Inc.	Drug Manufacturers - Specialty & Generic	82.57B
ZUMZ	Zumiez Inc.	Apparel Retail	513.45M
ZUO	Zuora, Inc.	Software - Infrastructure	1.34B
ZURA	Zura Bio Limited	Biotechnology	244.43M
ZVIA	Zevia PBC	Beverages - Non-Alcoholic	65.26M
ZVRA	Zevra Therapeutics, Inc.	Biotechnology	239.82M
ZVSA	ZyVersa Therapeutics, Inc.	Biotechnology	2.96M
ZWS	Zurn Elkay Water Solutions Corporation	Pollution & Treatment Controls	5.56B
ZYME	Zymeworks Inc.	Biotechnology	737.45M
ZYXI	Zynex, Inc.	Medical Distribution	262.83M
"""

json_output = text_to_json(text_content)
print(json_output)

# Optionally, save to a file
with open('output.json', 'w') as f:
    f.write(json_output)