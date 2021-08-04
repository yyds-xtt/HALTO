import matplotlib.pyplot as plt
import numpy as np

#y=[0.1663042338112493, 0.164000540755917, 0.1933994472284181, 0.2022048741077659, 0.22043569496477014, 0.3127447614655932, 0.21333243464134197, 0.16424471785038772, 0.2002892148609049, 0.24344008802839057, 0.23989224041968038, 0.291787240292229, 0.3793136018574963, 0.29034562158629684, 0.30993419955514445, 0.34706297828268357, 0.3104958874139228, 0.34127310036059133, 0.3548346474775068, 0.3178583554037604, 0.3681209778514649, 0.3586221374041334, 0.3128483478023252, 0.3433231559186679, 0.34284674924441316, 0.29821419796215326, 0.310216227918997, 0.35721964960650354, 0.3374097046053487, 0.38492523007741775, 0.43473936878091607, 0.3816730247975947, 0.42667103168062614, 0.44399201791118353, 0.48761702059392514, 0.49610961934127157, 0.5240366260157149, 0.5373694825432094, 0.552048313202557, 0.5140974675603498, 0.54363161224294, 0.55112936546718, 0.5212474320418339, 0.5356229806366141, 0.523490014036477, 0.5311598376600016, 0.563461356664834, 0.5286559512245729, 0.5592812503747435, 0.5533069976790638, 0.5458598054259799, 0.5447389224455728, 0.5474441812977511, 0.5467980959803231, 0.5373466510756938, 0.5622487802115743, 0.5356375002897222, 0.5505490233000347, 0.5394966566494703, 0.5553604842489054, 0.5472108244985867, 0.5517788941067323, 0.5502969153563919, 0.5613172390956006]
#y=[-0.37434552195273196, -0.3000298459674596, -0.33434162521070576, -0.22981625758934815, -0.29682170626408966, -0.1608813645592952, -0.13116507153583973, -0.15583156358317926, -0.08685135380428774, -0.07205321693728019, -0.07604386696063904, -0.0939714334206095, 0.01972516681063355, 0.05286440918645036, -0.13580216058418784, 0.12545132998921665, 0.15542627166053163, 0.13600687844380493, 0.15695049562737565, 0.08253599348193454, 0.36516842893440526, 0.18196852798064322, 0.3286913584655335, -0.09779763628508954, -0.12922596983577309, 0.11536632953751498, 0.18520113107315556, 0.2864377756422854, 0.3715384933309121, 0.35362792498692713, 0.3584672956303755, 0.35000909538236885, 0.35482334190683007, 0.38312056620404905, 0.3519882609221377, 0.37954001879479576, 0.3271343226413514, 0.34769606708911716, 0.29080393236126045, 0.358769665676036, 0.39411240312008194, 0.3482093391320625, 0.45490030893259314, 0.4501943989164512, 0.4408359318822389, 0.4397443416322493, 0.45122045570785513, 0.4408194246310655, 0.4488133337494765, 0.4539149938916962, 0.45638194906361684, 0.4506133720510902, 0.45294643911635557, 0.41456375139136004, 0.4423109580623456, 0.4430616720868196, 0.44560813055624815, 0.43639620232516935, 0.45159233258937376, 0.4285823206578518, 0.4532197848239727, 0.40066388911693396, 0.41015750510479376, 0.46245968204972987]
#y=[-0.23313597993826687, -0.5381369015725527, -0.19369363204839954, -0.18032697503299067, -0.3192374924610148, -0.16223474152914477, -0.37069012617124564, -0.08172607374107838, -0.22817228695456945, -0.1499987220817151, -0.12693013280211965, -0.07096007584224223, -0.12707351986741855, 0.02727524087937009, 0.09693000795454733, -0.08188650841100646, 0.0047684057391155455, -0.02610892473826426, -0.014307010161064728, -0.2325539309617537, 0.20166073121781436, -0.495707164124432, -0.11507146797649005, 0.1709915365817558, 0.2815086537852947, 0.020023169997830218, -0.5001965646699321, -1.8629387849529415, -1.85599483101014, -1.8542121059135288, -1.8499374555429249, -0.02671345487684901, 0.2360412139434069, 0.19992539238508691, 0.24149577707575587, 0.24905709149885863, 0.25643079298485594, 0.28363369167946006, 0.28709535006420484, 0.28812475352441186, 0.2596957558584986, 0.24613346792163804, 0.2723657604293694, 0.2816452139194667, 0.3009340949229614, 0.32393072874334544, 0.3237372115997974, 0.32461421015317976, 0.3461131835481028, 0.3193773872482849, 0.3093839488198723, 0.30435910871270294, 0.30562055861946064, 0.3472597596331046, 0.31061242915118836, 0.32006315101494714, 0.36255835786791973, 0.3243269050069629, 0.3256543944703529, 0.33765693453674656, 0.3570098969103701, 0.314124448611494, 0.32824832032459444, 0.3369831153106003]
#y=[-0.4725162123017899, -0.4178132937090107, -0.2879421230495323, -0.21422076436899118, -0.28927520969023174, -0.11945265957433068, -0.038166094020062366, -0.14067411960976678, -0.2871708418530281, -0.3302057083058606, -0.16478005911618987, -0.05600435762925114, -0.007995242857820184, -0.1707334367228587, -0.07454704255429861, -0.1410819798121007, 0.05410625808432827, -0.03789482972971156, -0.10755033220592866, 0.06729903884908262, -0.7164379676854945, -0.7310953822471635, -0.7256189760838636, -0.7227063732974967, -0.7270796410739113, -0.7521107960736898, -0.970677745952566, -0.9810818138079263, -1.0270230950780548, -0.9904241425764225, -0.9662481099799427, -0.878701098481022, -0.8655893635370638, -0.5590354868997996, -0.15471614031549327, 0.3002799257326705, 0.3162806926604302, 0.3121390061421408, 0.33976149617421986, 0.3411236076120338, 0.34904256159943525, 0.3623338779619186, 0.36808928794903883, 0.35949928937020925, 0.36554037421990676, 0.3593872093549228, 0.3693087854699537, 0.3721702751753242, 0.37845658336419397, 0.3673240938473909, 0.38577243262545885, 0.38108132692871644, 0.3783565853600329, 0.38135039355773764, 0.3984647576960117, 0.3663004129686853, 0.3544747869325366, 0.36955982235975543, 0.37688647201681996, 0.388469708935303, 0.3701373256161, 0.3698367981563827, 0.3584031318096911, 0.3721056574867378]
#DQL=[-0.36229699723130415, -0.3090852396608812, -0.42414967393850445, -0.2507953055741209, -0.2832552869100774, -0.2957336992505925, -0.17260678458639944, -0.1181441294239155, -0.1496346097206389, -0.05184748596242927, 0.021699511565270415, -0.029445549061729564, 0.017377530998192697, 0.09084865807128456, 0.14047344507394077, -0.23073421694783497, 0.029393019633663413, 0.02420955581690674, 0.07206653008369521, 0.03181087041403316, 0.09178292984414664, 0.15665499509089653, 0.14522332049199604, 0.200726807853573, 0.22625294455708958, 0.24679757277856648, 0.2157810351482739, 0.2838711856717071, 0.2964461502687932, 0.08642974458761539, 0.26671268436724893, 0.25182097738583603, 0.3037215959346974, 0.3693665818814249, 0.2537744630975879, 0.33784266675223834, 0.47723169981765823, 0.44696455352658226, 0.333262269955163, 0.4416041938621658, 0.3548272820246386, 0.31477980566545943, 0.39281319113209845, 0.4355717715840312, 0.38914511821504005, 0.47332366930994185, 0.4708420861212292, 0.4638333113800559, 0.43123552031221, 0.5080164329515643, 0.4108854734780846, 0.530786552277743, 0.4731057347266507, 0.4532160747008604, 0.48612370132451155, 0.47230851677395674, 0.5252123134445206, 0.5218636848264805, 0.5025553022190169, 0.5456564394296385, 0.5277558047813358, 0.49247553534162686, 0.5604048298894241, 0.48433664623014083, 0.4558414071654763, 0.449587377616311, 0.4696925058082618, 0.5137980819018433, 0.5100307751464733, 0.5165821632334114, 0.5064840965024928, 0.4593847755048844, 0.5169635699782609, 0.5085391527500631, 0.5457187832031655, 0.5409637865143238, 0.538853527206947, 0.523841047726296, 0.5359800501078268, 0.5264021854049394, 0.5334884456746759, 0.5057626429472264, 0.49815042681796706, 0.538603562541204, 0.5511281427089845, 0.49610910374552053, 0.48409674279410947, 0.5463968367472182, 0.5693046973797021, 0.5237954640891158, 0.5488608388173385, 0.5428841818053199, 0.5302019008041761, 0.5027433133800585, 0.4569893374945283, 0.4909888000221484, 0.5343185677497684, 0.500667721114283, 0.5378156493511099, 0.5300258873029883, 0.49507694083781667, 0.4314784054292004, 0.48009754555269835, 0.5283847505706357, 0.45100664342535607, 0.4712324365048392, 0.48394828409816404, 0.46212810397437715, 0.4655730902482875, 0.4824675352488552, 0.48075869500497387, 0.48688652637106367, 0.49057197246250617, 0.49721206429150244, 0.47531266996582205, 0.47412740817864235, 0.4968305654336235, 0.4505354147407894, 0.4667631844742367, 0.4603509674929679, 0.470613510816811, 0.4604134352694696, 0.4715367779120072, 0.47071523894677997]
#DQL=[-0.25672648168525103, -0.3968495639866526, -0.2751542855915247, -0.27748395092391664, -0.23761678499416067, -0.44140519458185956, -0.20473608176590624, -0.30339348585423354, -0.10320907686047695, -0.2765489629473986, -0.21232664587158656, -0.06916554190512345, -0.0848909102592061, -0.0008037690284460867, -0.05050710214254516, -0.17028088244763204, 0.0728023337564262, -0.193810620643324, 0.08998258941463493, 0.034648131987691906, -0.007747587478332518, -0.20005761057981944, -0.008830797171663398, -0.029936444972142543, -0.1408231088143983, -0.07228159117532082, 0.010363568827958752, 0.09165615222671677, 0.06036812995863839, 0.09584795513771006, 0.10837661301543243, 0.05286691854608077, 0.1375350206896904, 0.22765701810750963, 0.30860426415605086, 0.2630355716498961, 0.2055896966978974, 0.29105547257882763, 0.33179934577179704, 0.3272034097340242, 0.4271276401222534, 0.4668567758055498, 0.41601046013598314, 0.3685271067528567, 0.4495944019738687, 0.4296881311349905, 0.45288529062780947, 0.34839222354667293, 0.5419126200839193, 0.5449011028482714, 0.48631816075505735, 0.5631058653997099, 0.5877150998007827, 0.5595292099891707, 0.5532081322420386, 0.570557071009994, 0.5745850207276475, 0.5902610788329498, 0.5850587611725947, 0.5686364786530005, 0.590245846660735, 0.5657358138812518, 0.5084145193242144, 0.5598579586715614, 0.5724203185955196, 0.5600020261935738, 0.5985996523585942, 0.5730886186542516, 0.5699177705954434, 0.5646823202915254, 0.5771061149962925, 0.579488496940997, 0.5769775064446167, 0.5585282866769055, 0.5922177436912577, 0.562827614068436, 0.5743127815719818, 0.5945040072824367, 0.550379679208931, 0.5878937609621175, 0.5941706443814874, 0.5838506412946906, 0.5805108422576712, 0.5533998553996554, 0.5903680764578145, 0.5392246884710865, 0.5840132414180071, 0.5733862707955969, 0.5972657273536819, 0.5781831716235826, 0.5906115271344091, 0.5578217708384168, 0.5875107273845573, 0.5820656154509688, 0.5898515344247122, 0.5578719645755739, 0.5437124351054605, 0.5386588498615753, 0.532251050692603, 0.5171938744181974, 0.5442683446758011, 0.5221134089223978, 0.5384674176196739, 0.5272016609814134, 0.5512885494765359, 0.5447337817892635, 0.53742700567224, 0.5315935833829721, 0.5359487652425869, 0.5368854267244615, 0.5464166265409601, 0.5518537635792038, 0.5350624441694459, 0.5526641355444891, 0.5382571928370177, 0.5473216627819161, 0.5470125488610033, 0.5611137419046446, 0.5553821504332799, 0.5393185831142007, 0.49350808332272894, 0.4974568675970691, 0.4999482899993568, 0.5598334160180505]
DQL=[-0.008955021453364374, -0.022973419835314143, -0.049581042501114614, -0.1402952497435814, -0.729977134736535, -0.8305241509987006, -0.4988820884687928, -0.3903922525167193, 0.17131369734823126, 0.22707466155058217, 0.1428503263953894, -0.2176007970584162, -0.287647359744135, -0.3025010343765758, -0.28269936637927606, -0.22587931746804302, -0.25980805010888575, -0.17572234101093812, -0.1618516891972527, -0.02709250283266956, -0.19109126926006365, -0.1780209672006346, -0.17784316382052281, -0.0673336871867144, -0.032749117369502, -0.012625003744467784, -0.08427094772596692, -0.0690815218414839, -0.20110463382216992, -0.24026098752063127, -0.29889659817534797, -0.3643471841120155, 0.19929575201035216, 0.2883062234943754, 0.45731959146653833, 0.44685700044512383, 0.4489067730986343, 0.45739789038354806, 0.45945480417188256, 0.43561101103379196, 0.44046194476618883, 0.44024798873227106, 0.44184026379974295, 0.4287603974468004, 0.44138417803654334, 0.4274932087137881, 0.4460088612533352, 0.45564656596007225, 0.452536841782862, 0.4661724987852362, 0.46359225279585486, 0.45367423324680006, 0.42609599253309727, 0.4486339341537633, 0.46020400278770607, 0.4636559460163818, 0.4553659356818644, 0.4631563339370474, 0.4562530292566126, 0.4635699996146971, 0.4616541731613921, 0.4662432397536262, 0.4647846320293745, 0.4817935069029989, 0.42875327567798577, 0.42799890040344646, 0.4764718215002109, 0.4796169633352683, 0.47683056945800634, 0.4640444039858991, 0.48900316580057906, 0.45470570889164175, 0.5285168223374267, 0.5346922215572432, 0.5183763068038062, 0.5086838566464597, 0.5342174786323945, 0.53794784577001, 0.5291520676037103, 0.5166717617278115, 0.5142334115212598, 0.5427697134366327, 0.5429741856926265, 0.5272983443968223, 0.5455774930231712, 0.5576006107944865, 0.5601977439421802, 0.545899215330759, 0.5370530028460795, 0.5544585370009245, 0.5371632117933672, 0.5420052194914087, 0.5521530802575821, 0.5554122554908087, 0.5417988408839853, 0.5402680318812655, 0.5543262615897215, 0.5516051910726424, 0.5565954797842717, 0.5536540245515573, 0.5596400950999731, 0.5671887977856515, 0.5584520814803701, 0.546109675880053, 0.5489053058340242, 0.5595970875181844, 0.5545484449150349, 0.5543492731647526, 0.5698640724791059, 0.5704313178745489, 0.551176629322628, 0.5732188062069034, 0.5569078521012957, 0.5513950541172921, 0.5643411755781159, 0.5472608649054914, 0.5711143529176063, 0.5630598097500116, 0.5719799973826031, 0.5604745751892104, 0.5699313636381875, 0.5639831458043086, 0.5715138090824989, 0.5680249196758396]
QL=[-0.27984963089933645, -0.33979562733170227, -0.22199416679234873, -0.0613691797915805, -0.44968796203303274, -0.19830353150987404, -0.020545908685652283, -0.30224746840070343, -0.2547053163081294, -0.01644596621529442, -0.12964301065537426, 0.018503358101601582, -0.03868391396745073, 0.028674685265869054, 0.01410651415652729, -0.01588996558533544, -0.001537340143936803, 0.006825039826042648, -0.04943959981317227, 0.018413332513005972, -0.019138864221974902, 0.1272712872029833, -0.08885919367311665, 0.13733894865403443, 0.16374704521433592, 0.31321328188021924, 0.10519648031287172, 0.19581280527122844, 0.13708883100361302, 0.170436400233818, 0.18052747273463873, 0.10543892633744306, 0.25171967681411594, 0.25856700865316484, 0.41613692847204753, 0.3223477758369392, 0.509439878573525, 0.4430919532534149, 0.44694889695519396, 0.34969629758642296, 0.48925649233147617, 0.5170038384733199, 0.522625492545469, 0.5042176113234605, 0.5131831966827733, 0.5075198402553152, 0.4137100524543521, 0.47335880182095946, 0.464664043430794, 0.401764549613605, 0.4604116707196232, 0.44830367724631986, 0.5075137287552215, 0.4902585010725408, 0.4536235798413536, 0.4419328202890799, 0.38674853338116927, 0.40797943995956254, 0.4363883207932476, 0.4905290960288304, 0.5366019180937832, 0.4570977536503605, 0.5202235347934691, 0.5269260116357474, 0.5217136411800026, 0.41894112512301246, 0.4960574801077858, 0.47041406869021896, 0.5316900918568125, 0.5019311607083997, 0.4441273854114738, 0.47870635301965425, 0.43480935319400904, 0.5669185954068752, 0.5190646705319274, 0.5687954293988537, 0.5395464163369539, 0.5366753045306044, 0.48200292953599455, 0.5205005405458842, 0.5240958978367534, 0.570975886463441, 0.5206235164110702, 0.5014197956387783, 0.529188164562176, 0.5279546659942492, 0.5026906983437458, 0.5187978825585006, 0.4589509553907691, 0.5369356302616152, 0.5101427406574388, 0.49707538693109293, 0.56335149684655, 0.5330847406810638, 0.5317170085881336, 0.5122556780157596, 0.5010471212721209, 0.41323107870985565, 0.44720870020420195, 0.4546031313428085, 0.506435344073849, 0.5490064665973549, 0.5175839709934976, 0.4798411031138659, 0.5462913146980246, 0.5180563453582857, 0.5761460505309789, 0.5356166484514198, 0.5362979839957973, 0.5386923711212339, 0.5377737724498918, 0.5496726882055747, 0.5375530781437636, 0.5191919428319322, 0.5237134757284313, 0.5257695374948683, 0.5254077688172045, 0.5228714012715687, 0.5238735220455664, 0.5242646758557603, 0.5389157741401238, 0.5746715231489469, 0.5550519341198447, 0.5425646683160199]
#DQL=[-0.37655720324285197, -0.2587776488323006, -0.20035102681880645, -0.1759703882423191, 0.31217786151310206, 0.33293550361444885, 0.4037980469830224, 0.4307512605243598, 0.392601902995125, 0.42609296058744545, 0.42439458599897406, 0.42378949246507275, 0.40647770319654375, 0.41261192521751405, 0.42109361310781623, 0.419064144101855, 0.38822184981722135, 0.4383895097518222, 0.42492749617358694, 0.41472314737511184, 0.41374769477101087, 0.4506292425915195, 0.43602627130684163, 0.41732430680060767, 0.4070695947639324, 0.4181432036094329, 0.41264603437170316, 0.41915208099002554, 0.3970551876535018, 0.4037719342603561, 0.4401627827349786, 0.44308208470296645, 0.42851734615872394, 0.4110352850150382, 0.40979757320737353, 0.40199137817961383, 0.4010216965659516, 0.39333662289616433, 0.3743758264974524, 0.38935201477347775, 0.40168237164597104, 0.4228548266565884, 0.3750010920975559, 0.410100656615124, 0.4100698015709167, 0.42666031698641177, 0.4239417819603916, 0.42634814377143604, 0.4299377988801037, 0.43305625866155617, 0.44068295049020684, 0.4355744163877905, 0.3493484133344231, 0.44259996350044856, 0.46945600866219184, 0.45256364128715443, 0.4655307828520705, 0.41967069844617433, 0.3993896777713173, 0.404251639071572, 0.4619122262658734, 0.4114491698168397, 0.40034939374135686, 0.43547638840732567, 0.4342282634162517, 0.4329999406806715, 0.45916229120247654, 0.4610740105437056, 0.45678979038784717, 0.4391134654155687, 0.4537195579336982, 0.45281183238719735, 0.4469210733610173, 0.4452767897393701, 0.4413627492977981, 0.44994413607775624, 0.46002680622605907, 0.44326014492291366, 0.44779163945163025, 0.45113741752952136, 0.4461938362988323, 0.447618598167135, 0.4518878783514519, 0.4542392194890237, 0.4375756220599477, 0.4612808526809711, 0.44919676729520563, 0.44011445782954756, 0.4594293567079332, 0.4416503630382569, 0.464206798314877, 0.4498825490023883, 0.45027762126169896, 0.4587709963095758, 0.4384628538556028, 0.4569253498114543, 0.46826323365504363, 0.44606715770950595, 0.4364135018825264, 0.4678496070407924]
#DQL=[-0.9524316158898102, -0.7143829734173034, 0.0318683166584651, 0.26372579498419296, 0.3211515919320504, 0.35165300216877565, 0.4071661233439768, 0.4134891699395622, 0.43193245239932393, 0.42059579659696306, 0.419940520169861, 0.4354161820374098, 0.4284832146637698, 0.4218163080000169, 0.43681285977582973, 0.42624696893589276, 0.44599549274100353, 0.43345578416402514, 0.44472900278711053, 0.4412013934350096, 0.4452735797997818, 0.4584437670797154, 0.44164091060359323, 0.447739431767406, 0.4443431037652049, 0.44884639099996704, 0.44639759775623644, 0.45062841629669953, 0.47511467422546005, 0.43793634094959005, 0.44082347004745653, 0.44762563696594354, 0.45287687678749283, 0.44683487934525973, 0.4489211684482538, 0.45927336077595854, 0.45108627090861597, 0.4608234907825049, 0.4574827304980837, 0.44113318909462834, 0.4593314899536439, 0.459913717722688, 0.4476800238313907, 0.45654413834104596, 0.44445355060592356, 0.45844030070259395, 0.4613448576400795, 0.4555640399616555, 0.44977326497712433, 0.437472909686439, 0.4612658655136796, 0.41345397446116217, 0.447532240086403, 0.44415466863300396, 0.4482482693850083, 0.47706023716802204, 0.427656823914886, 0.4542148060837365, 0.4276672115523497, 0.4057806857759465, 0.44747911970723714, 0.4021099757052568, 0.4607262912771765, 0.45584009863349917, 0.4429953800005543, 0.3629482438455895, 0.4102596996819521, 0.41099449143135836, 0.40311824809106567, 0.3856508811444108, 0.45059134071312357, 0.3948732709046069, 0.4552785422324336, 0.36722960151294454, 0.4179102927426999, 0.4516489452811092, 0.372783302728709, 0.42930054835098624, 0.401223984106185, 0.395763261914795, 0.43868236546403594, 0.4286908200080094, 0.39014574572190064, 0.4009365979540426, 0.43506764311999985, 0.44743761841319163, 0.44393956997503403, 0.3780292494570636, 0.4404241573271574, 0.3954025476041514, 0.42908698476067025, 0.4328601882792449, 0.45406531240098785, 0.4121606195180619, 0.4353682037957001, 0.40858788661934126, 0.4022640648693297, 0.412756299153983, 0.44518498699439174, 0.44122683748054675]
QL=[-0.4766196425382778, -0.418471020937314, -0.16706008478202927, 0.049206965648693986, 0.13193832434336358, 0.21603366329111975, 0.1266303926057101, 0.19176563180706313, 0.3542499022231033, 0.33085973161356286, 0.3214452209473416, 0.41765835412320035, 0.4353572513758351, 0.36045323640995836, 0.393989386689605, 0.3603785336641302, 0.3905742661756861, 0.4526806134919, 0.43721186626709535, 0.36945188280706187, 0.38974434926531437, 0.33151450645899155, 0.40320988681595904, 0.3816447418766746, 0.43615440072494477, 0.42686999252994073, 0.404845224846178, 0.40155735712552376, 0.46681968193140483, 0.4228293300003643, 0.38396543264855404, 0.4187120636645643, 0.42617364049518863, 0.45047809369701053, 0.3599664849087427, 0.48481374806284844, 0.3747897122738871, 0.41155829129070964, 0.4508932586662359, 0.40308882926166156, 0.38349170608998, 0.5452783024123172, 0.4516468007687859, 0.4089639171426346, 0.37841599448898144, 0.41973923178861017, 0.4533736995107233, 0.504196392513983, 0.38115314188135657, 0.47457231120015825, 0.43724443749292274, 0.4315485431778771, 0.4926139885456325, 0.47230222774163755, 0.3672956276985424, 0.44460117520997616, 0.4430498086732269, 0.47656137020789896, 0.5007724879027601, 0.45312281576381935, 0.38298850030431797, 0.4582303237895778, 0.38917972050167887, 0.3593023376617444, 0.4283066032405263, 0.3539809454201628, 0.4413710316303589, 0.39398465020761775, 0.3731257064707326, 0.48317639720131095, 0.4363929309310127, 0.38138892858949186, 0.4442178753599404, 0.45410484871093043, 0.5210105856005565, 0.4810066112278725, 0.4473920963323253, 0.32646953246433646, 0.4480160469899243, 0.42453121384459463, 0.46704570627860237, 0.37206469797062874, 0.3907840162099349, 0.49757067264992433, 0.2944314350829615, 0.4718117440710756, 0.4557667551452891, 0.28925126943433804, 0.36544885963534973, 0.4242225237116225, 0.37686810265200643, 0.35857898244344977, 0.40776926659003293, 0.3840355634477258, 0.5101597693634966, 0.32484278337190375, 0.4212630399091553, 0.43173761768924307, 0.3400797789585941, 0.40224423336247805]
DQL=[-0.955279090552257, -0.5649324714774407, 0.360797141260613, 0.18083150273689963, 0.3206883756040199, 0.3136804837057403, 0.494486628323376, 0.4840397071283876, 0.4871248382170037, 0.4911784469382261, 0.5260068881838317, 0.5274804171768793, 0.5165610152540675, 0.48020794981723275, 0.5101129797418559, 0.5179209068039068, 0.4788945676773823, 0.49419252824214355, 0.4582213043693054, 0.4563919756696889, 0.4753594969400499, 0.4592314945732502, 0.4682544732621581, 0.4838626650011604, 0.4648062923688994, 0.4808414506018256, 0.49277019951160794, 0.4897559735427091, 0.4721039399625857, 0.462444519989715, 0.4861103104554541, 0.5026338166143149, 0.46747703150337017, 0.4851077541709532, 0.5084480791002591, 0.5112625841268739, 0.511266451924942, 0.5006165227072806, 0.49614627799373673, 0.5038503367787562, 0.49414112842051355, 0.428825010072954, 0.39596062924832137, 0.34304420626808746, 0.3596569925042143, 0.3656581794937043, 0.4009863291218893, 0.4283701270512638, 0.38903460853342225, 0.36298267644812704, 0.3936664221073023, 0.39343040207329677, 0.40887356926492985, 0.40800573952639535, 0.3810314439970635, 0.4159978423782898, 0.45407795737656276, 0.4135142160715008, 0.41456379619826134, 0.44924185135094946, 0.43141996147974626, 0.45250930898914415, 0.385064271572822, 0.4106744429911676, 0.42039871309600535, 0.45406180853591505, 0.4308238526162712, 0.4247771285534583, 0.4203026686318796, 0.4326758453763797, 0.4360224487821585, 0.4611825148047585, 0.4365992117133211, 0.445025788580364, 0.44069361207979374, 0.4508136095692866, 0.44854986766816374, 0.4386747365997977, 0.45442623168364515, 0.4670024232412774, 0.45674105533014925, 0.43795012134012373, 0.4704333602892197, 0.47191765186374485, 0.45311776362421685, 0.4476764926224938, 0.4999883044218465, 0.4483408532420804, 0.4514800029239176, 0.47658796587249413, 0.4470580520650532, 0.4670208314413914, 0.4459557511271929, 0.4758836368760223, 0.48189440487343776, 0.4692095980193077, 0.4695405177356429, 0.47447036907518964, 0.47265407794792047, 0.4156097847623772]
#QL=[-0.27005745820920646, -0.26903673011587975, -0.35129902279839437, -0.25105466251888736, -0.3183434895417341, -0.35304503383743613, -0.07182538443714244, -0.11761551117636998, -0.1104387994843667, -0.279177651121533, 0.0009082005391369903, -0.13810922123381744, 0.008935345100732234, 0.02361671647405365, -0.19211217311793774, -0.11984141352426958, -0.11064623516459705, 0.046042780059866034, 0.10377974320923414, -0.1710937936116193, 0.13481538569752372, 0.04493330337972025, 0.012317770210992326, 0.08303923692734169, 0.13662567439318235, 0.10080172922862796, 0.013007354436798471, 0.05726689590250025, 0.1434854077975769, 0.22907573214641552, 0.2920836386639332, 0.30866719109807045, 0.3062723234780816, 0.28749678929591976, 0.36477142961245373, 0.4766435929296138, 0.4220358784734737, 0.41165255087383856, 0.4050792221248677, 0.4095974821620943, 0.4028723909051578, 0.45173203146342067, 0.4794310202555672, 0.4182459190671606, 0.40748438179692625, 0.3982069056986965, 0.35042352337035143, 0.4501521198193972, 0.4818176793925377, 0.3434517254863402, 0.4434264918344701, 0.4542393059936268, 0.4527662841906533, 0.4666582739244293, 0.4729978878562226, 0.4247334829364049, 0.3897178972492126, 0.4325384208381295, 0.44924400221754757, 0.4679176209034425, 0.47035527393489485, 0.46077416320607817, 0.44252730409802354, 0.4647238823744228, 0.4605153001457587, 0.3539629006191183, 0.4755570215193088, 0.40423519542413916, 0.3820890513031636, 0.4284417868979889, 0.4327745179405554, 0.41545710931504587, 0.42896309376480524, 0.3268814140925255, 0.4501331099523696, 0.4843250683486532, 0.46114390423164686, 0.4134079392517374, 0.39483462737935643, 0.44601397857662933, 0.4190376928929231, 0.4731531331932906, 0.48253313624373717, 0.4221427677934797, 0.47862107043576807, 0.3985295617433553, 0.4307195262918804, 0.5153681498425061, 0.39314599951282114, 0.42483389583687536, 0.3641536314954029, 0.4111914171603338, 0.4432700097295646, 0.42531427334619193, 0.4753059144230618, 0.4318842846119604, 0.45633324475434195, 0.46756126598263426, 0.46002447276740394, 0.4126123812881818, 0.4004478913219555, 0.4410092458743095, 0.4117105814770762, 0.47522371640102024, 0.484312802821657, 0.48393316384145674, 0.4164285890626387, 0.4693921343430465, 0.4009723904598163, 0.4374642248097548, 0.39794708296360026, 0.41948069231431373, 0.4414279106586619, 0.4859430696636715, 0.43411813996932036, 0.4404576727621166, 0.3803479692093111, 0.44020450567455677, 0.4694442032118791, 0.3599206086631401, 0.4856417803733638, 0.3670419749516833, 0.37744575332146185, 0.38252265751398595]
'''
y=list()
with open("train.dat") as f:
	a=f.read().split('\n')
	count=0
	hour=0
	for e in a:
		e=e.split()
		if int(e[0][:10])-1201639675>3600*hour:
		#if int(e[0][:10])-1189809385>3600*hour:
			y.append(round(count*1.5/100))
			count=0
			hour+=1
		else:
			count+=1'''
#plt.plot(DQL, "go-")
#plt.plot(QL, "bo-")
#plt.show()