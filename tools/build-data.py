# Builds site/data/grants.json, graph.json, grants.jsonld and sources.json.
# This file is where the data is written: each programme is the keeper's own entry from the programme's official page,
# read on 2026-11-25. Run from anywhere inside the repository:  python3 tools/build-data.py
# Facts are changed here, in a signed commit, never by a script that reads the web.
import json
D="2026-11-25"
def P(id,name,org,countries,geo,stages,sectors,amount,rate,how,dl_type,dl_text,dl_dates,elig,url,notes="",kind="programme",notion=True,extra_urls=None,**kw):
    return dict(id=id,name=name,organisation=org,countries=countries,geography=geo,kind=kind,stages=stages,sectors=sectors,
      funding_amount_text=amount,funding_rate_text=rate,how_to_apply=how,deadline_type=dl_type,deadline_text=dl_text,deadline_dates=dl_dates,
      eligibility_notes=elig,official_url=url,further_official_urls=extra_urls or [],date_checked=D,notes=notes,in_starting_list=notion)
progs=[
P("innosuisse-start-up-innovation-projects","Start-up Innovation Projects","Innosuisse, the Swiss Innovation Agency",["CH"],"national",
 ["early-stage"],["any"],"Not stated as a sum; the page gives a share of costs only.","Up to 70 per cent of direct project costs; the start-up pays at least 30 per cent.",
 "Apply on the Innosuisse application platform once the stated requirements are met.","rolling","Projects can be submitted on an ongoing basis; the page asks for submission at least eight weeks before a meeting of the Innovation Council. Meeting dates are not in the text read.",[],
 "Swiss-registered start-up about to enter the market for the first time, no more than five years old (ten in exceptional cases), fewer than 50 full-time equivalent staff. Only the start-up is funded, not research partners. The company needs the means to pay its own share.",
 "https://www.innosuisse.admin.ch/en/start-up-innovation-projects","Page lists five thematic subgroups: ICT, energy and environment, engineering, life sciences, social sciences and business management."),
P("go-bio-next","GO-Bio next","Federal Ministry of Research, Technology and Space (BMFTR), Germany",["DE"],"national",
 ["research","early-stage"],["life-sciences"],"Not stated: the page says the amount depends on the project. Each of the two phases lasts up to three years.","Not stated.",
 "Research teams submit project outlines twice a year.","fixed","Outline submission dates stated as 15 March and 15 September. Lateral entry to phase 2 stated as open until 1 February 2027.",["2027-02-01"],
 "Phase 1 is for research teams at German universities or research institutions who want to found a company. Phase 2 is for small technology companies, normally founded from phase 1, with investor co-financing. Agricultural, food and nutrition research is excluded.",
 "https://www.go-bio.de/gobio/en/go-bio/go-bio-next/go-bio-next.html","Administered through Projekttraeger Juelich according to the contact details on the page."),
P("women-tech-eu","Women TechEU","EU-funded project run by a consortium; granting authority EISMEA",["EU"],"eu",
 ["early-stage"],["deep-tech"],"EUR 75,000 per beneficiary, non-dilutive, as stated.","Not stated.",
 "Start with the phase 1 eligibility check, reached from the active calls page.","fixed","The page gives a full proposal deadline of 16 September 2026 and also describes a continuous open call with four cut-off dates that it does not list. Check the active calls page before relying on any date.",["2026-09-16"],
 "Early-stage deep tech start-up founded or co-founded by a woman in a top management role, women holding at least 25 per cent of shares, registered for between six months and five years, technology readiness level 4 to 6, less than EUR 1 million equity raised. Not open to foundations or non-profits.",
 "https://womentecheurope.eu/","Programme budget stated as EUR 12 million in grants over 2026 to 2028."),
P("eic-pathfinder","EIC Pathfinder","European Innovation Council, European Commission",["EU"],"eu",
 ["research"],["deep-tech"],"Grants of up to EUR 4 million, or more if justified; booster grants of up to EUR 50,000.","Not stated.",
 "Submit through the EU Funding and Tenders Portal before the deadline.","fixed","Pathfinder Open stage 1: 25 February 2027; stage 2: 16 September 2027. Pathfinder Challenges: 29 September 2027.",["2027-02-25","2027-09-16","2027-09-29"],
 "Aimed at research teams at the earliest stages (technology readiness level 1 to 4), not companies. Needs a consortium of at least three independent legal entities in different countries; single applicants only for Challenges.",
 "https://eic.ec.europa.eu/eic-funding-opportunities/eic-pathfinder_en","Page states 2027 budgets of EUR 82 million (Challenges) and EUR 166 million (Open).",notion=True),
P("eic-accelerator","EIC Accelerator","European Innovation Council, European Commission",["EU"],"eu",
 ["early-stage","scale-up"],["any"],"Grant component up to EUR 2.5 million; investment component EUR 1 million to EUR 10 million. Higher sums are described under STEP Scale Up.","Not stated.",
 "Submit a short proposal at any time; successful applicants then write a full proposal for a batch date, through the Funding and Tenders Portal.","fixed","Short proposals can be submitted at any time. Full proposal batch dates: 20 January 2027, 17 March 2027, 1 September 2027, 4 November 2027.",["2027-01-20","2027-03-17","2027-09-01","2027-11-04"],
 "Start-ups and SMEs in an EU Member State or Horizon Europe associated country. Small mid-caps (up to 499 staff) may apply for investment only. Technology readiness level 6 to 8 for grants, 6 to 9 for investment. The final step is an interview with an EIC jury.",
 "https://eic.ec.europa.eu/eic-funding-opportunities/eic-accelerator_en","The page says both 3 steps and 4 steps for the process."),
P("eic-transition","EIC Transition","European Innovation Council, European Commission",["EU"],"eu",
 ["research","early-stage"],["any"],"Grants of up to EUR 2.5 million; booster grants of up to EUR 50,000.","Not stated.",
 "Submit through the Funding and Tenders Portal before the deadline, in three steps: proposal, expert evaluation, jury interview.","fixed","Proposal deadline stated as 14 September 2027, 17:00 Brussels time. A letter of intent date of 20 October 2026 is also mentioned.",["2027-09-14"],
 "SMEs, start-ups, spin-offs and research organisations. The proposal must build on results of an eligible earlier project (for example EIC Pathfinder or ERC Proof of Concept). Starts at technology readiness level 4, aiming for 5 or preferably 6.",
 "https://eic.ec.europa.eu/eic-funding-opportunities/eic-transition_en","The page says the 2026 list of eligible projects applies and a 2027 list is being prepared."),
P("aws-preseed-innovative-solutions","aws Preseed: Innovative Solutions","aws (Austria Wirtschaftsservice)",["AT"],"national",
 ["pre-seed","early-stage"],["any"],"Maximum grant EUR 100,000 with the gender bonus, otherwise EUR 89,000. Non-repayable.","80 per cent of eligible costs, raised to 90 per cent with the gender bonus; 10 per cent equity from shareholders.",
 "Apply online through the aws funding manager.","rolling","Stated as ongoing, with several decision dates a year (usually quarterly).",[],
 "Project located in Austria. Teams before incorporation, or companies up to six months after entry in the commercial register; micro and small enterprises if established. Not for deep tech (that has its own aws line). Social or ecological value at the core.",
 "https://www.aws.at/en/aws-preseed-innovative-solutions/","Found through the hub page https://www.aws.at/en/aws-preseed-seedfinancing/, which lists the other aws lines (deep tech, seed financing) that this entry does not cover.",
 extra_urls=["https://www.aws.at/en/aws-preseed-seedfinancing/"]),
P("erc-starting-grant","ERC Starting Grant","European Research Council",["EU"],"eu",
 ["research"],["any"],"Up to EUR 1.5 million over 5 years; a further EUR 1 million can be requested with justification; up to EUR 2 million for researchers relocating from outside associated countries.","Up to 100 per cent of eligible direct costs plus 25 per cent for indirect costs.",
 "A principal investigator submits through a host institution in response to the annual call, via the Funding and Tenders Portal.","annual","Annual calls; the closing date is set in each call and is not in the page text.",[],
 "Individual researchers with 0 to 10 years since their PhD, hosted by an institution in an EU Member State or associated country. Any field of research. This is a research grant for people, not a company programme.",
 "https://erc.europa.eu/apply-grant/starting-grant","Included because it is in the starting list; it suits researchers, not start-ups directly."),
P("innobooster","Innobooster","Innovation Fund Denmark",["DK"],"national",
 ["early-stage","sme"],["green-tech","life-sciences","digital","defence-security"],"Between DKK 200,000 and DKK 5 million.","Co-financing of up to 35 per cent of project costs; projects last up to two years.",
 "Apply through the e-grant system under the relevant call.","windows","Applications are processed in batches. Windows listed: 27 May to 6 August 2026 and 20 August to 15 October 2026. The page says there are currently no calls available.",[],
 "SME (EU definition) registered in Denmark with a CVR number, with a financial foundation (at least 100,000 in risk capital or development grants in the past three years, or gross profit of at least DKK 250,000 in one of the past three published years). High-risk, challenge-driven development within the listed themes.",
 "https://danmarksinnovationsfond.dk/en/programmes/innobooster/","The starting list's address, innovationsfonden.dk/en/p/innobooster, redirected here. The page lists four themes in one place and three in another (defence is missing from the second).",
 extra_urls=["https://innovationsfonden.dk/en/p/innobooster"]),
P("life-close-to-market","LIFE close-to-market projects","CINEA, European Commission (LIFE Programme)",["EU"],"eu",
 ["scale-up","sme"],["green-tech","environment-climate"],"Not stated.","Not stated.",
 "Respond to the annual LIFE call for proposals under the relevant thematic area.","annual","Calls are published every year; the deadline is not stated on the pages read.",[],
 "Public authorities, NGOs, universities and institutes as well as companies bringing green products, technologies or services to market. Needs a high level of technical and business readiness and a business plan.",
 "https://cinea.ec.europa.eu/life/life-close-market-projects_en","Found through the hub page https://cinea.ec.europa.eu/programmes/life_en, which also links the current calls page.",
 extra_urls=["https://cinea.ec.europa.eu/programmes/life_en"]),
P("sprind-your-project","SPRIND: Your Project Proposal","SPRIND (Federal Agency for Breakthrough Innovation), Germany",["DE"],"national",
 ["research"],["any"],"Not stated. The page says there are no funding guidelines and financing is set case by case.","Not stated.",
 "Describe the project idea through the submission form on the site. The page says this is not a formal application.","not-stated","No closing date is stated; the page says every submission is considered.",[],
 "People with expert or scientific knowledge and a breakthrough idea, civilian or dual-use. The page says fewer than ten per cent of ideas are pursued.",
 "https://www.sprind.org/en/actions/your-project","A route for submitting ideas rather than a grant programme with set terms.",kind="route"),
P("exist-gruendungsstipendium","EXIST Business Start-up Grant (EXIST Gruendungsstipendium)","EXIST, a start-up funding programme of the Federal Ministry for Economic Affairs and Energy, Germany",["DE"],"national",
 ["pre-seed","research"],["any"],"","",
 "Contact the founders' network at your university or research institution first; it advises on eligibility and documents. The programme's own application page gives the steps.","not-stated","",[],
 "Aimed at founding ideas from research and science in the pre-founding phase: students, graduates, researchers and founding teams. A link to a university or research institution is key. The page links an eligibility check tool.",
 "https://www.exist.de/EXIST/Navigation/EN/Start-upFunding/EXIST-Business-Start-up-Grant/exist-business-start-up-grant.html","The page states no amount or deadline. It is mostly in German. The address in the starting list returned 404, so this is the current official page found by search on exist.de; the application page itself has not been read."),
P("innovate-uk-ktp","Knowledge Transfer Partnerships","Innovate UK, part of UK Research and Innovation",["GB"],"national",
 ["sme","scale-up"],["any"],"A typical project is described as a package of support worth around GBP 80,000 to GBP 100,000 a year.","The business pays a share of costs: typically 67 per cent of project costs for SMEs and 50 per cent for larger businesses, as stated; grant covers the rest.",
 "Apply through the Innovation Funding Service competitions.","fixed","Round four of 2026 to 2027 closes 20 January 2027; 2027 to 2028 round one closes 21 April 2027 and round two 23 June 2027. The page says dates may change and the programme runs throughout the year.",["2027-01-20","2027-04-21","2027-06-23"],
 "A business working with a university, college, research organisation or Catapult. Full eligibility is on a separate page that was not read.",
 "https://www.ukri.org/councils/innovate-uk/guidance-for-applicants/guidance-for-specific-funds/knowledge-transfer-partnership-guidance/","In Northern Ireland the scheme is run with Invest NI.",
 notion=False,extra_urls=["https://www.ukri.org/councils/innovate-uk/guidance-for-applicants/guidance-for-specific-funds/knowledge-transfer-partnership-guidance/dates-and-deadlines-for-ktp-applicants/","https://www.investni.com/support-for-business/innovation-support/innovate-uk-knowledge-transfer-partnerships"]),
P("seis","Seed Enterprise Investment Scheme (SEIS)","HM Revenue and Customs",["GB"],"national",
 ["pre-seed","early-stage"],["any"],"A company can receive a maximum of GBP 250,000 through SEIS.","Investor tax relief rate not stated on the page read.",
 "Issue the shares, then send HMRC a compliance statement (form SEIS1) through the page's start link.","rolling","No closing date stated. Money raised must be spent within three years of the share issue.",[],
 "A tax relief for individual investors, not a grant. Company with a new qualifying trade, established in the UK, gross assets not over GBP 350,000 and fewer than 25 full-time equivalent staff. Not available if the company has had EIS or VCT investment.",
 "https://www.gov.uk/guidance/venture-capital-schemes-apply-to-use-the-seed-enterprise-investment-scheme","Page last updated 25 May 2023, according to the page. The address in further_official_urls is the earlier one, which now redirects here.",kind="tax-relief",notion=False,extra_urls=["https://www.gov.uk/guidance/seed-enterprise-investment-scheme"]),
P("eis","Enterprise Investment Scheme (EIS)","HM Revenue and Customs",["GB"],"national",
 ["early-stage","sme","scale-up"],["any"],"Most companies can raise up to GBP 10 million in any 12 months and up to GBP 24 million in their lifetime from these sources.","Investor tax relief rate not stated on the page read.",
 "Issue the shares, then send HMRC a compliance statement (form EIS1) through the page's start link, after four months of qualifying activity and within two years.","rolling","No fixed closing date stated.",[],
 "A tax relief for individual investors, not a grant. Fewer than 250 full-time equivalent staff, gross assets up to GBP 30 million before and GBP 35 million after the shares are issued, usually within seven years of first commercial sale. Knowledge-intensive companies have different limits.",
 "https://www.gov.uk/guidance/venture-capital-schemes-apply-for-the-enterprise-investment-scheme","Page last updated 6 April 2026, according to the page.",kind="tax-relief",notion=False),
P("invest-ni-support-for-start-ups","Support for start-ups (Invest NI)","Invest Northern Ireland",["GB-NIR"],"regional",
 ["early-stage"],["advanced-manufacturing","digital","life-sciences","financial-services","green-tech"],"Groundwork for Growth: up to GBP 15,000. Innovation Vouchers: up to GBP 10,000 (from a linked card, not its own page). Ambition to Grow (Supporting Women): up to GBP 30,000 (from the Invest NI home page).","Not stated.",
 "Call the Business Support Team or use the enquiry form on the page.","fixed","Only Ambition to Grow gives a date: closes 12:00 on Friday 11 December 2026. Others not stated.",["2026-12-11"],
 "New or early-stage businesses developing innovative products or tradeable services for customers outside Northern Ireland, with the ambition to grow quickly.",
 "https://www.investni.com/support-for-business/support-for-start-ups","Sector list is the page's list of priority sectors.",notion=False,extra_urls=["https://www.investni.com/"]),
]
notread=[
 ("French Tech Rise","FR","https://lafrenchtech.gouv.fr/en/programme/french-tech-rise-2/","The address in the starting list returned 404 Not Found when read on 25 November 2026. The Mission French Tech page found by search also redirects to a 404."),
 ("Horizon Europe (clusters)","EU","https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/programmes/horizon","The portal page returned only its title, with no programme text."),
 ("ZIM","DE","https://www.zim.de/ZIM/Navigation/DE/Meta/Englisch/englisch.html","The site showed a browser-verification page to the reader and gave no programme text."),
 ("VLAIO research project","BE","https://www.vlaio.be/en/subsidies/research-project","The site refused the request (403)."),
 ("Innovasjon Norge start-up support","NO","https://en.innovasjonnorge.no/article/startups","The address redirected to a general home page, not the article."),
 ("EXIST Forschungstransfer","DE","https://exist.de/programm/exist-forschungstransfer/foerderantrag-stellen/","The address in the starting list returned 404 Not Found."),
 ("CDTI Neotec","ES","https://www.cdti.es/en/ayudas/neotec","The page returned no content to the reader."),
 ("Eurostars","EU","https://www.eurekanetwork.org/programmes/eurostars/","The site refused the request (403)."),
 ("Bpifrance i-Nov","FR","https://www.bpifrance.fr/nos-appels-a-projets-concours/appel-a-projets-concours-dinnovation-i-nov","The site refused the request (403)."),
 ("i-Lab innovation contest","FR","https://www.bpifrance.fr/nos-appels-a-projets-concours/concours-dinnovation-i-lab","The starting list links a news article, not an official page. The official pages found by search (Bpifrance and the research ministry) refused the request (403), so none is written up."),
 ("FFG general programme","AT","https://www.ffg.at/en/programme/general-programme","The site refused the request (403)."),
 ("Vinnova funding","SE","https://www.vinnova.se/en/apply-for-funding/","This is a hub of many calls, not one programme; individual calls are not yet read."),
 ("EIT opportunities","EU","https://www.eit.europa.eu/our-activities/opportunities","This is a hub of current calls; individual calls are not yet read."),
 ("ESA BIC Booster funding opportunities","DE","https://booster.esa-bic.de/funding-opportunities/","This is a hub; the page states no amounts or deadlines and sends applicants to their ESA BIC."),
 ("EU cascade funding (FSTP)","EU","https://webgate.ec.europa.eu/funding-tenders-opportunities/spaces/IT/pages/25559615/Cascade+Funding+Calls+Financial+Support+for+Third+Parties+FSTP","A how-to guide for the portal, not a programme."),
 ("UKRI apply for funding","GB","https://www.ukri.org/apply-for-funding/","A hub for all UKRI funding, not one programme."),
 ("Start Up Loans","GB","https://www.startuploans.co.uk/","The site refused the request (403)."),
 ("Wales start-up funding","GB-WLS","","The host for the Development Bank of Wales could not be reached from the builder's network; Business Wales not yet tried."),
 ("Scottish Enterprise grants","GB-SCT","https://www.scottish-enterprise.com/how-we-can-help/funding-and-grants/business-grants-and-funding-calls","An index of grants and calls with no start-up programme stated; the research and development grants page is not yet read."),
]

IFS=[("Increasing Energy Efficiency of AI Systems Strand 2","2026-11-24","2027-01-20","",""),
("Increasing Energy Efficiency of AI Systems Strand 1","2026-11-24","2027-01-20","",""),
("Healthy Soils and Water for a Sustainable Environment","2026-11-19","2027-01-28","a share of up to GBP 28 million","Farming Futures R&D Fund"),
("ICURe Exploit FY 27/28 - FY29/30","2026-11-16","2027-01-15","up to GBP 7 million for a three year period","Innovate UK"),
("Scaling Interoperable V2X: bidirectional charging","2026-11-10","2027-01-27","a share of up to GBP 15 million",""),
("DRIVE35 Scale-up Fund Drawdown 6","2026-11-04","2027-01-27","a share of up to GBP 150 million",""),
("UK-Netherlands Co-Innovation for Quantum Technology 2026","2026-11-03","2027-02-09","a share of up to GBP 1.5 million",""),
("Investor Partnerships - National Materials Innovation Programme 1","2026-11-02","2027-01-19","",""),
("Underground hydrogen storage demonstrator DEVEX support","2026-10-23","2027-01-13","a share of up to GBP 1.5 million",""),
("Testing and validating underground hydrogen storage components","2026-10-23","2027-01-27","a share of up to GBP 5 million",""),
("Growth Cohorts: Next-gen low carbon concrete cohort entry Round 2","2026-10-21","2026-12-02","",""),
("BridgeAI Deployment Catalyst: AI for Operational Systems","2026-10-21","2026-12-08","a share of up to GBP 5 million","Innovate UK"),
("BridgeAI Deployment Catalyst: AI for Decision Critical Systems","2026-10-21","2026-12-08","a share of up to GBP 5 million","Innovate UK"),
("BridgeAI Deployment Catalyst: AI for Assurance and Compliance","2026-10-21","2026-12-08","a share of up to GBP 5 million","Innovate UK"),
("Knowledge Transfer Partnership (KTP): 2026 - 2027 Round 4","2026-10-19","2027-01-27","a share of up to GBP 12.5 million",""),
("Full ADOPT Grant: Round 10","2026-10-08","2026-12-02","a share of up to GBP 5 million",""),
("Eureka collaborative R&D: Globalstars Japan 2027","2026-10-07","2027-01-20","a share of GBP 2 million",""),
("Sustainable Medicines Manufacturing Innovation: CR&D Round 2","2026-10-05","2026-12-02","invest up to GBP 7 million","Innovate UK, working with the Department of Health and Social Care"),
("Investor Partnerships - Battery Innovation Programme","2026-10-05","2026-11-25","",""),
("Engineering Biology Investor Partnerships Round 1","2026-10-01","2026-12-02","a share of up to GBP 8 million",""),
("UK-Germany Bilateral Collaborative R&D: Round 5","2026-09-28","2026-12-01","a share of up to GBP 2.4 million",""),
("Commercialising Knowledge Assets Fund (CKAF) Winter","2026-09-17","2026-12-01","grants from GBP 50,000 up to GBP 250,000","Government Office for Technology Transfer"),
("Battery Innovation: Feasibility Studies Rd 3","2026-09-11","2026-12-02","a share of up to GBP 25 million","The Battery Innovation Programme"),
("Battery Innovation: Concept Development Rd 3","2026-09-11","2026-12-02","a share of up to GBP 25 million","The Battery Innovation Programme"),
("UK-Singapore CRD 2026","2026-08-24","2026-12-16","a share of up to GBP 3 million","")]
out=dict(
 schema_version="1.0",
 title="Startup grants in Europe and the UK",
 generated=D,
 licence_note="Each entry is written by the site's keeper from the programme's own official page. Reuse the data freely and keep the official_url and date_checked with each entry.",
 schema_doc="https://startup-grants.tool.sovereignweb.site/data/SCHEMA.md",
 credits=dict(starting_list=dict(name="European Startup Grant Programs (2026 Edition)",url="https://humble-lantern-cdb.notion.site/e00ec34ecf5a44699910c36cf9e23c93?v=62ed8ff847c4409da264b1f156c9efd4",
   used_for="The list of programme names and official links only. No descriptions or text were copied.")),
 vocabularies=dict(
  stages={"research":"Researchers or research teams","pre-seed":"Before or around incorporation","early-stage":"Early-stage start-ups","sme":"Established small or medium-sized businesses","scale-up":"Scale-ups"},
  sectors={"any":"Open to any field","deep-tech":"Deep tech","life-sciences":"Life sciences","green-tech":"Green and clean technology","environment-climate":"Environment and climate","digital":"Digital","defence-security":"Defence and security","advanced-manufacturing":"Advanced manufacturing","financial-services":"Financial and professional services"},
  countries={"AT":"Austria","CH":"Switzerland","DE":"Germany","DK":"Denmark","EU":"EU-wide","GB":"United Kingdom","GB-NIR":"Northern Ireland"}),
 programmes=progs,
 open_competitions=dict(source='https://apply-for-innovation-funding.service.gov.uk/competition/search',date_checked=D,nation='GB',note='All 25 competitions listed on the Innovation Funding Service on this date, none marked closed or paused. These are competitions with fixed closing dates, many for specific sectors or for collaborations. Eligibility on each competition page has not been read; check before applying. Funder is given only where the listing names one. An empty award means the listing states no total.',items=[dict(title=t,opens=o,closes=c,award_text=a,funder=f) for t,o,c,a,f in IFS]),
 not_yet_read=[dict(name=n,country=c,starting_list_url=u,reason=r) for n,c,u,r in notread])

import hashlib,re
from urllib.parse import urlparse
REPO="https://github.com/SovereignWebsite/Site__Tool__Startup-Grants/blob/dev/"
KEEPER="startup-grants.a@SovereignWebsite.dinis"
SUB="a web-fetch sub-agent started by the keeper (model not recorded)"
# Host licences, from PrompTugal's own record (PrompTugal__News__Startups data/source-licences.json, read 2026-11-25). Only hosts it lists.
HOST_LIC={"eic.ec.europa.eu":{"licence":"CC BY 4.0, under Commission Decision 2011/833/EU","licence_url":"https://creativecommons.org/licenses/by/4.0/","terms_url":"https://commission.europa.eu/legal-notice_en","from":"PrompTugal data/source-licences.json (read 2026-11-18)"}}
def lic(u):
    h=urlparse(u).netloc; return HOST_LIC.get(h,{"licence":"not checked yet","from":"no record"})
# Structured eligibility, only from what each page states. Types: country_in, age_years_max, age_months_between, fte_lt, trl_between, equity_raised_lt_eur, women_led, text_only.
C=lambda t,**k:dict(type=t,**k)
CRIT={
"innosuisse-start-up-innovation-projects":[C("country_in",values=["CH"],text="Headquarters in Switzerland and entered in the Swiss commercial register."),C("age_years_max",value=5,text="Not more than five years old when you apply (up to ten in exceptional cases)."),C("fte_lt",value=50,text="Fewer than 50 full-time equivalent staff.")],
"go-bio-next":[C("country_in",values=["DE"],text="Phase 1 is for research teams at German universities or research institutions."),C("sector_in",values=["life-sciences"],text="Life sciences; agricultural, food and nutrition research is excluded.")],
"women-tech-eu":[C("women_led",text="Founded or co-founded by a woman in a top management role, with women holding at least 25 per cent of the shares."),C("age_months_between",min=6,max=60,text="Registered for at least six months and no more than five years."),C("trl_between",min=4,max=6,text="Technology readiness level 4 to 6."),C("equity_raised_lt_eur",value=1000000,text="Less than EUR 1 million equity raised."),C("text_only",text="Registered in an EU Member State or Horizon Europe associated country, as the programme's FAQ lists them.")],
"eic-pathfinder":[C("trl_between",min=1,max=4,text="Technology readiness level 1 to 4."),C("text_only",text="Needs a consortium of at least three independent legal entities in different countries (single applicants only for Pathfinder Challenges). Aimed at research teams, not companies.")],
"eic-accelerator":[C("trl_between",min=6,max=8,text="Technology readiness level 6 to 8 for grants (6 to 9 for investment)."),C("text_only",text="Start-up or SME in an EU Member State or associated country; small mid-caps (up to 499 staff) for investment only.")],
"eic-transition":[C("trl_between",min=4,max=9,text="Starts at technology readiness level 4, aiming for 5 or preferably 6."),C("text_only",text="Must build on results of an eligible earlier project (for example EIC Pathfinder or ERC Proof of Concept).")],
"aws-preseed-innovative-solutions":[C("country_in",values=["AT"],text="Project located in Austria."),C("age_months_max",value=6,allow_pre_incorporation=True,text="Before incorporation, or no more than six months after entry in the commercial register."),C("sector_not",values=["deep-tech"],text="Not deep tech (that has its own aws line).")],
"erc-starting-grant":[C("text_only",text="An individual researcher with 0 to 10 years since their PhD, hosted by an institution in an EU Member State or associated country. Not a company programme.")],
"innobooster":[C("country_in",values=["DK"],text="Registered in Denmark with a CVR number."),C("text_only",text="EU-definition SME with a financial foundation (risk capital or development grants of at least 100,000 in the past three years, or gross profit of at least DKK 250,000 in one of the past three published years).")],
"life-close-to-market":[C("text_only",text="Needs a high level of technical and business readiness and a business plan. Open to public authorities, NGOs, universities and companies.")],
"sprind-your-project":[C("text_only",text="A person with expert or scientific knowledge and a breakthrough idea. This is a way to submit an idea, not an application.")],
"exist-gruendungsstipendium":[C("country_in",values=["DE"],text="Programme of the German Federal Ministry for Economic Affairs and Energy."),C("text_only",text="A founding idea from research and science in the pre-founding phase, with a link to a university or research institution.")],
"innovate-uk-ktp":[C("country_in",values=["GB"],text="UK business (in Northern Ireland the scheme is run with Invest NI)."),C("text_only",text="A business working with a university, college, research organisation or Catapult; full eligibility is on a page not yet read.")],
"seis":[C("country_in",values=["GB"],text="Company established in the UK."),C("fte_lt",value=25,text="Fewer than 25 full-time equivalent staff."),C("gross_assets_le_gbp",value=350000,text="Gross assets of no more than GBP 350,000 when the shares are issued."),C("text_only",text="A new qualifying trade. Not available if the company has had EIS or VCT investment. This is a tax relief for investors, not a grant.")],
"eis":[C("country_in",values=["GB"],text="Permanent establishment in the UK."),C("fte_lt",value=250,text="Fewer than 250 full-time equivalent staff."),C("gross_assets_le_gbp",value=30000000,text="Gross assets up to GBP 30 million before the shares are issued."),C("text_only",text="Usually within seven years of first commercial sale; knowledge-intensive companies have different limits. A tax relief for investors, not a grant.")],
"invest-ni-support-for-start-ups":[C("country_in",values=["GB-NIR"],text="Northern Ireland."),C("text_only",text="New or early-stage business developing innovative products or tradeable services for customers outside Northern Ireland, with the ambition to grow quickly.")],
}
HOW={ # how each entry was read, beyond the default
"aws-preseed-innovative-solutions":"hub page read first; its Innovative Solutions page read next, on the same domain",
"innobooster":"the starting list's address redirected to a renamed domain, which was followed",
"life-close-to-market":"hub page read first; its close-to-market page read next, on the same domain",
"exist-gruendungsstipendium":"the starting list's address returned 404; the current official page was found by a web search limited to exist.de and then read",
"innovate-uk-ktp":"the guidance page and its costs and dates pages read; the gov.uk address redirects to ukri.org",
"seis":"read twice: first at the earlier gov.uk address, and again at the address it now redirects to",
"invest-ni-support-for-start-ups":"the start-up support page and the Invest NI home page read; two amounts come from linked cards, not their own pages",
}
CROSS={ # programmes also in PrompTugal__News__Startups data/research/eu.json (read 2026-11-21 by startups.b.eu@PrompTugal.dinis)
"eic-accelerator":"Agrees: grant up to EUR 2.5 million plus EUR 1 million to EUR 10 million; batching dates 20 January, 17 March, 1 September and 4 November 2027.",
"eic-pathfinder":"Listed there with no amount; same address.",
"eic-transition":"Agrees: up to EUR 2.5 million per project; same address.",
"women-tech-eu":"Agrees: EUR 75,000 per company (there from the EISMEA programmes page; here from womentecheurope.eu).",
}
for p in progs:
    u=p["official_url"]; pid=p["id"]
    p["criteria"]=CRIT.get(pid,[])
    how=HOW.get(pid)
    p["provenance"]=dict(source_url=u,further_source_urls=p["further_official_urls"],read_on=p["date_checked"],file="site/data/grants.json",file_url=REPO+"site/data/grants.json",
      read_by=SUB,written_by=KEEPER+" (Claude Sonnet 5.5, per the commit trailer)",
      how_read="page text fetched and summarised by "+SUB+"; the keeper wrote this entry from that report and did not read the page itself. Amounts, rates and dates are short quotes from the page."+((" Also: "+how+".") if how else ""),
      license="CC BY 4.0 for the keeper's text; the programme's own page keeps its own terms",source_license=lic(u),
      cross_check=CROSS.get(pid))
# Sources registry: every address tried, whether it worked, and who tried it.
S=[]
def add(id,url,outcome,programmes,method,note="",read_on="2026-11-25"):
    S.append(dict(id=id,url=url,host=urlparse(url).netloc if url else "",outcome=outcome,programmes=programmes,method=method,read_on=read_on,note=note,license=lic(url) if url else None))
for p in progs:
    add("src-"+p["id"],p["official_url"],"read",[p["id"]],"fetched by a web-fetch sub-agent",HOW.get(p["id"],""))
    for j,fu in enumerate(p["further_official_urls"]):
        add(f"src-{p['id']}-{j+2}",fu,"read" if p["id"] not in ("seis","innobooster") else "redirects to the address above",[p["id"]],"fetched by a web-fetch sub-agent" if p["id"]!="seis" else "checked with a redirect request (curl)")
add("src-ifs","https://apply-for-innovation-funding.service.gov.uk/competition/search","read",["open_competitions"],"fetched by a web-fetch sub-agent (three result pages)","25 competitions; none marked closed or paused")
add("src-ukri-opportunity","https://www.ukri.org/opportunity/","read",["innovate-uk-ktp"],"fetched by a web-fetch sub-agent","two open Innovate UK items seen; not used as programmes")
for n,c,u,r in notread:
    if u: add("gap-"+re.sub(r"[^a-z0-9]+","-",n.lower()).strip("-"),u,"not read",[],"fetched by a web-fetch sub-agent" if "403" in r or "404" in r or "refused" in r else "fetched by a web-fetch sub-agent",r)
add("gap-bpifrance-ilab-ministry","https://www.enseignementsup-recherche.gouv.fr/fr/france-2030-lancement-de-la-27e-edition-du-concours-d-innovation-i-lab-98536","not read",[],"fetched by a web-fetch sub-agent","refused the request (403)")
add("gap-british-business-bank","https://www.british-business-bank.co.uk/","not read",[],"fetched by a web-fetch sub-agent","refused the request (403)")
add("gap-development-bank-wales","https://www.developmentbankofwales.com/","not read",[],"fetched by a web-fetch sub-agent","host could not be reached from the builder's network")
add("gap-lafrenchtech-com","https://lafrenchtech.com/en/how-france-helps-startups/french-tech-rise-en/","not read",[],"fetched by a web-fetch sub-agent","redirects to a lafrenchtech.gouv.fr address that returns 404")
add("gap-browser-reread","","refused",[],"browser re-read of the blocked pages","The session's permission check refused re-reading blocked pages in a browser. The keeper stopped and did not work round it.")
add("lead-notion","https://humble-lantern-cdb.notion.site/e00ec34ecf5a44699910c36cf9e23c93?v=62ed8ff847c4409da264b1f156c9efd4","starting list","*","read in a browser (Playwright) by the keeper","29 programme names and official links taken; no descriptions or text copied",read_on="2026-11-25")
add("lead-chatgpt-report","","lead only","*","a PDF supplied by Dinis Cruz","A research brief (ChatGPT, 8 pages) with a data model, a source registry and a pipeline. It says the Notion page is private; the page is in fact public and was read. Its citations were not checked. Used for ideas, never as a source of facts.",read_on="2026-11-25")
add("xcheck-promptugal-startups","https://github.com/PrompTugal/PrompTugal__News__Startups/blob/dev/data/research/eu.json","cross-check",["eic-accelerator","eic-pathfinder","eic-transition","women-tech-eu"],"git clone (read only) by the keeper","PrompTugal's own EU research, read 2026-11-21 by startups.b.eu@PrompTugal.dinis. Amounts and dates agree where both give them.")
out["sources"]=S
import os
_vid="req343ij"
out["vault"]=dict(name="Startup grants in Europe and the UK: data and provenance",vault_id=_vid,host="dev.vault.sgraph.ai",created="2026-11-25",status="Created and readable with a read-only key. The address is not linked from this site yet: the site's leak scan blocks read keys, so publishing it is the owner's decision.",holds="data/ (grants, sources, graph, linked data, schema), screenshots/, README.md and a page that shows the provenance")
out["schema_version"]="1.1"
out["licence_note"]="The keeper's text and structure are CC BY 4.0. Each entry links to the official page it was written from, which keeps its own terms. Keep official_url and date_checked with any entry you reuse."
out["vocabularies"]["criteria_types"]={"country_in":"Registered or located in one of the listed places","age_years_max":"Company no older than this many years","age_months_max":"Company no older than this many months (may be before incorporation if allow_pre_incorporation)","age_months_between":"Company age in months between min and max","fte_lt":"Fewer full-time equivalent staff than this","gross_assets_le_gbp":"Gross assets no more than this, in pounds","trl_between":"Technology readiness level between min and max","equity_raised_lt_eur":"Equity raised so far below this, in euros","women_led":"Founded or co-founded by a woman in a top management role (the page also sets a share)","sector_in":"Sector is one of the listed","sector_not":"Sector is not one of the listed","text_only":"Stated on the page but not machine-checkable; shown for the reader to judge"}
# Graph
nodes={};edges=[]
def node(id,type,label,url=None):
    nodes.setdefault(id,dict(id=id,type=type,label=label,url=url))
for p in progs:
    node(p["id"],"programme",p["name"],p["official_url"])
    node("org:"+hashlib.sha1(p["organisation"].encode()).hexdigest()[:8],"funder",p["organisation"])
    edges.append(dict(source="org:"+hashlib.sha1(p["organisation"].encode()).hexdigest()[:8],target=p["id"],rel="funds"))
    for c in p["countries"]:
        node("country:"+c,"country",out["vocabularies"]["countries"].get(c,c));edges.append(dict(source=p["id"],target="country:"+c,rel="open_to"))
    for st in p["stages"]:
        node("stage:"+st,"stage",out["vocabularies"]["stages"][st]);edges.append(dict(source=p["id"],target="stage:"+st,rel="suits"))
    for se in p["sectors"]:
        node("sector:"+se,"sector",out["vocabularies"]["sectors"][se]);edges.append(dict(source=p["id"],target="sector:"+se,rel="covers"))
    node("page:"+p["id"],"official_page",urlparse(p["official_url"]).netloc,p["official_url"]);edges.append(dict(source="page:"+p["id"],target=p["id"],rel="written_from"))
node("agent:keeper","agent","startup-grants.a (keeper)")
node("agent:fetch","agent","web-fetch sub-agents")
node("lead:notion","lead","Notion starting list",out["credits"]["starting_list"]["url"])
node("lead:report","lead","ChatGPT research brief (lead only)")
node("xcheck:promptugal","cross_check","PrompTugal News Startups data","https://github.com/PrompTugal/PrompTugal__News__Startups")
for p in progs:
    edges.append(dict(source="agent:fetch",target="page:"+p["id"],rel="read"))
    edges.append(dict(source="agent:keeper",target=p["id"],rel="wrote"))
    if p["in_starting_list"]: edges.append(dict(source="lead:notion",target=p["id"],rel="named_by"))
    if p["id"] in CROSS: edges.append(dict(source="xcheck:promptugal",target=p["id"],rel="agrees_with"))
graph=dict(about="Nodes and edges of the grants data: funder, programme, country, stage, sector, official page, who read and wrote it, and where the name came from. Built from grants.json by tools in the repository.",nodes=list(nodes.values()),edges=edges)
# JSON-LD
ctx={"@vocab":"https://schema.org/","sg":"https://startup-grants.tool.sovereignweb.site/data/SCHEMA.md#"}
ld={"@context":ctx,"@graph":[]}
for p in progs:
    ld["@graph"].append({"@id":"https://startup-grants.tool.sovereignweb.site/#"+p["id"],"@type":"MonetaryGrant" if p["kind"]=="programme" else "Thing","name":p["name"],"url":p["official_url"],
      "funder":{"@type":"Organization","name":p["organisation"]},"areaServed":[out["vocabularies"]["countries"].get(c,c) for c in p["countries"]],
      "sg:stages":p["stages"],"sg:sectors":p["sectors"],"sg:deadlineType":p["deadline_type"],"sg:dateChecked":p["date_checked"],
      "sg:criteria":p["criteria"],"sg:readBy":p["provenance"]["read_by"],"sg:writtenBy":p["provenance"]["written_by"],"sg:sourceUrls":[u for u in [p["official_url"]]+p["further_official_urls"]]})
import subprocess
base=subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip()+"/site/data/"
json.dump(out,open(base+"grants.json","w"),indent=1,ensure_ascii=False)
json.dump(graph,open(base+"graph.json","w"),indent=1,ensure_ascii=False)
json.dump(ld,open(base+"grants.jsonld","w"),indent=1,ensure_ascii=False)
json.dump(dict(about="Every address the keeper tried, with the outcome, who tried it and when. Same records as grants.json sources.",sources=S),open(base+"sources.json","w"),indent=1,ensure_ascii=False)
print(len(progs),len(S),len(graph["nodes"]),len(graph["edges"]))
t=open(base+"grants.json").read()
print('emdash',chr(0x2014) in t, len(t)//1024,'KB')
