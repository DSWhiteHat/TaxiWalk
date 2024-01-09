def test_submultiplicative(s):
    flag = False
    for i in range(1, len(s)-1):
        for j in range(1, len(s) - i):
            if s[i] * s[j] < s[i + j]:
                flag = True
                print(f"{s[i]} * {s[j]} < {s[i + j]}")
    if flag == False:
        print("The sequence is submultiplicative (for the given elements)!")

def test_supermultiplicative(s):
    flag = False
    for i in range(1, len(s)-1):
        for j in range(1, len(s) - i):
            if s[i] * s[j] > s[i + j]:
                flag = True
                print(f"{s[i]} * {s[j]} > {s[i + j]}")
    if flag == False:
        print("The sequence is supermultiplicative (for the given elements)!")

# Ratio < 1 implies not submultiplicative.
def lowest_ratios(s, offset=1, n_multiplier=1):
    for i in range(len(s)-offset//n_multiplier):
        min_ratio = float("inf")
        min_j = float("inf")
        for j in range(len(s) - i - offset//n_multiplier):
            ratio = s[i] * s[j] / s[i + j + offset//n_multiplier]
            if ratio < min_ratio:
                min_ratio = ratio
                min_j = j
        print(f"i={i * n_multiplier + offset}: worst j={min_j * n_multiplier + offset}, with ratio {min_ratio} vs {i * n_multiplier + offset + min_j * n_multiplier + offset}")
        # print(f"{ratio}")

def highest_ratios(s, offset=1, n_multiplier=1):
    for i in range(len(s)-offset//n_multiplier):
        max_ratio = 0
        max_j = 0
        for j in range(len(s) - i - offset//n_multiplier):
            ratio = s[i] * s[j] / s[i + j + offset//n_multiplier]
            if ratio > max_ratio:
                max_ratio = ratio
                max_j = j
        print(f"i={i * n_multiplier + offset}: worst j={max_j * n_multiplier + offset}, with ratio {max_ratio} vs {i * n_multiplier + max_j * n_multiplier + 2 * offset}")

# Prints a table of s_i * s_j / s_{i+j}
def ratio_table(s, offset=1, n_multiplier=1):
    with open("ratio_table.csv", "w") as file:
        file.write("," + ",".join(list(map(str, range(1, len(s))))) + "\n")
        for i in range(len(s)-offset//n_multiplier):
            out = [str(i+1)]
            for j in range(len(s) - i - offset//n_multiplier):
                out.append(str(round(s[i] * s[j] / s[i + j + offset//n_multiplier], 5)))
            file.write(",".join(out) + "\n")
        file.flush()
        file.close()
        

def bounds(s, offset=1, n_multiplier=1):
    for n in range(len(s)):
        # print(f"{n_multiplier * n + offset}: {round((s[n] ** (1/(n_multiplier * n + offset))) ** 4 - 1, 4)}")
        print(round((s[n] ** (1/(n * n_multiplier + offset))) ** 4 - 1, 4))
        # print("\n" * (n_multiplier - 2))


self_avoiding_walks = [4, 12, 36, 100, 284, 780, 2172, 5916, 16268, 44100, 120292, 324932, 881500, 2374444, 6416596, 17245332, 46466676, 124658732, 335116620, 897697164, 2408806028, 6444560484, 17266613812, 46146397316, 123481354908, 329712786220, 881317491628, 2351378582244, 6279396229332, 16741957935348, 44673816630956, 119034997913020, 317406598267076, 845279074648708, 2252534077759844, 5995740499124412, 15968852281708724, 42486750758210044, 113101676587853932, 300798249248474268, 800381032599158340, 2127870238872271828, 5659667057165209612, 15041631638016155884, 39992704986620915140, 106255762193816523332, 282417882500511560972, 750139547395987948108, 1993185460468062845836, 5292794668724837206644, 14059415980606050644844, 37325046962536847970116, 99121668912462180162908, 263090298246050489804708, 698501700277581954674604, 1853589151789474253830500, 4920146075313000860596140, 13053884641516572778155044, 34642792634590824499672196, 91895836025056214634047716, 243828023293849420839513468, 646684752476890688940276172, 1715538780705298093042635884, 4549252727304405545665901684, 12066271136346725726547810652, 31992427160420423715150496804, 84841788997462209800131419244, 224916973773967421352838735684, 596373847126147985434982575724, 1580784678250571882017480243636, 4190893020903935054619120005916, 11107224538074654820152678182884, 29442884996760677051402398150644, 78023796077779727644807609460228, 206797849568186990141402577046860, 547952781764285893561169365957068, 1452142167241575828091155500636684, 3847327231644550282490410907667972, 10194710293557466193787900071923676]
# Any of the 4 cardinal directions equal.
# s = [1, 2, 4, 6, 10, 16, 22, 38, 56, 82, 130, 188, 288, 420, 676, 942, 1496, 2094, 3576, 4844, 8226, 11094, 20160, 26140, 44694, 60398, 113032, 143800, 264054, 339658, 650678, 819138, 1488128, 1932820, 3810506, 4691186, 8920932, 11254046, 22262610, 27422366, 51866584, 65615248, 132266318, 160593806, 311968438, 388031466]
# s_odd = [1, 2, 6, 16, 38, 82, 188, 420, 942, 2094, 4844, 11094, 26140, 60398, 143800, 339658, 819138, 1932820, 4691186, 11254046, 27422366, 65615248, 160593806, 388031466]
s_even = [4, 10, 22, 56, 130, 288, 676, 1496, 3576, 8226, 20160, 44694, 113032, 264054, 650678, 1488128, 3810506, 8920932, 22262610, 51866584, 132266318, 311968438, 783580732, 1839049714]
s_mul_4 = [10, 56, 288, 1496, 8226, 44694, 264054, 1488128, 8920932, 51866584, 311968438, 1839049714, 11107306076]

# Non-self avoiding walks
manhattan_no_2_turn = [2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 288, 466, 754, 1220, 1974, 3194, 5168, 8362, 13530, 21892, 35422, 57314, 92736, 150050, 242786, 392836, 635622, 1028458, 1664080, 2692538, 4356618, 7049156, 11405774, 18454930, 29860704, 48315634, 78176338, 126491972, 204668310, 331160282, 535828592, 866988874, 1402817466, 2269806340, 3672623806, 5942430146, 9615053952, 15557484098, 25172538050, 40730022148, 65902560198, 106632582346, 172535142544, 279167724890, 451702867434, 730870592324, 1182573459758, 1913444052082, 3096017511840, 5009461563922, 8105479075762, 13114940639684, 21220419715446, 34335360355130, 55555780070576, 89891140425706, 145446920496282, 235338060921988, 380784981418270, 616123042340258, 996908023758528, 1613031066098786, 2609939089857314, 4222970155956100, 6832909245813414, 11055879401769514, 17888788647582928, 28944668049352442, 46833456696935370, 75778124746287812, 122611581443223182, 198389706189510994, 321001287632734176, 519390993822245170, 840392281454979346, 1359783275277224516, 2200175556732203862, 3559958832009428378, 5760134388741632240, 9320093220751060618, 15080227609492692858, 24400320830243753476, 39480548439736446334, 63880869269980199810, 103361417709716646144, 167242286979696845954, 270603704689413492098, 437845991669110338052, 708449696358523830150, 1146295688027634168202, 1854745384386157998352, 3001041072413792166554]
# Taxi walks
c = [2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 288, 460, 740, 1192, 1918, 3064, 4910, 7872, 12620, 20114, 32150, 51396, 82160, 130730, 208506, 332616, 530588, 843222, 1342662, 2138280, 3405346, 5406522, 8597632, 13674278, 21748530, 34501460, 54807754, 87077354, 138346766, 219324398, 348109128, 552582790, 877163942, 1389806294, 2204289314, 3496483316, 5546212122, 8783360626, 13922238632, 22069957494, 34986181158, 55383388278, 87740467384, 139014623272, 220254102104, 348536652664, 551914140382, 874039817792, 1384184997874, 2189670407434]
# Taxi Polygons (my enumeration, which somehow has more than the previous works)
p = [6, 16, 90, 480, 2548, 13696, 74052, 402800, 2205148, 12146352, 67290626, 374798032, 2097959250]
# Taxi Bridges
b = [1, 1, 1, 2, 3, 5, 7, 11, 16, 25, 37 , 57, 86, 132, 201, 309, 473, 728, 1118, 1722, 2653, 4090, 6318, 9751, 15093, 23322, 36151, 55927, 86786, 134395, 208755, 323568, 503042, 780368, 1214138, 1884969, 2934662, 4559364, 7102383, 11041558, 17208806, 26768870, 41739891, 64962451, 101336620, 157794160, 246241076, 383602565, 598828298, 933263764, 1457349924, 2272129746, 3549120141, 5535348349, 8648706714, 13493340066, 21088018133, 32910788292, 51446635013, 80312795498]

c_start_straight = [1, 999, 2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 284, 458, 736, 1186, 1892, 3036, 4864, 7802, 12430, 19876, 31764, 50794, 80794, 128910, 205592, 328044, 521182, 830120, 1321794, 2105468, 3341944]
c_ss_odd = [99, 4, 10, 26, 68, 178, 458, 1186, 3036, 7802, 19876, 50794, 128910, 328044, 830120, 2105468]
c_ss_even = [1, 2, 6, 16, 42, 110, 284, 736, 1892, 4864, 12430, 31764, 80794, 205592, 521182, 1321794, 3341944]

# L-R, U-D parity pairs.
# Straight start variation provides a 5.1 bound, regular provdes 5.3659 at N=40, which is not true.
parity_even = [2, 6, 14, 36, 92, 232, 602, 1528, 3942, 9998, 25668, 64966, 165998, 419318, 1067134, 2690706, 6825636, 17182920, 43475306, 109296314, 275946018, 692919990, 1746359322, 4380859590, 11024674242]
parity_even_start_straight = [2, 4, 10, 24, 60, 148, 378, 954, 2446, 6198, 15860, 40160, 102448, 258986, 658504, 1661616, 4212660, 10611828, 26838528, 67507852, 170387398, 428044368, 1078524630]

# Any 2 parities equal:
any_parity_even_start_straight = [1, 2, 6, 16, 42, 110, 284, 736, 1892, 4864, 12430, 31764, 80794, 205592, 521182, 1321794, 3341944, 8453328, 21327558, 53832650, 135583622]

# Given +N steps can reach the origin:
origin = [0, 0, 0, 106, 1402, 12734, 99600, 713958, 4868292, 32246280, 209839580]

plus_two_ratios = [1.33333, 1.6, 1.5, 1.53846, 1.52381, 1.52941, 1.52727, 1.52809, 1.52778, 1.54783, 1.55676, 1.54362, 1.54327, 1.55614, 1.56253, 1.55691, 1.55626, 1.56548, 1.57014, 1.56541, 1.56524, 1.57258, 1.57617, 1.57214, 1.57189, 1.57783, 1.5807, 1.57738, 1.57712, 1.582, 1.58432, 1.58152, 1.58128, 1.58536, 1.58726, 1.58486, 1.58465, 1.5881, 1.58969, 1.58763, 1.58743, 1.59039, 1.59174, 1.58995, 1.58976, 1.59232, 1.59348, 1.59191, 1.59174, 1.59398, 1.59498, 1.5936, 1.59344, 1.59541, 1.59629, 1.59506, 1.59491, 1.59666]

# Submultiplicative but approaching too low of a mu.
not_all_directions = [2, 4, 6, 10, 16, 26, 42, 66, 106, 164, 262, 402, 638, 974, 1536, 2338, 3666, 5570, 8690, 13188, 20486, 31066, 48078, 72870, 112416, 170322, 262042, 396914, 609242, 922628, 1413382, 2140066, 3272830, 4954910, 7566592, 11454274, 17469858, 26443522, 40287842, 60977924, 92816390, 140474282, 213649166, 323333558, 491421984, 743677810, 1129609706, 1709393394, 2595135882]


# Closable no Narrows
cnn = [2, 4, 6, 10, 16, 26, 42, 68, 110, 178, 288, 456, 728, 1168, 1870, 2964, 4726, 7544, 12038, 19050, 30274, 48172, 76640, 121182, 192316, 305324, 484784, 766186, 1214422, 1925022, 3051988, 4820984, 7633566, 12086054, 19139454, 30219178, 47809176, 75626214, 119650972, 188843126, 298566820, 471989524, 746262146, 1177558154]


# mu = []
# for x in plus_two_ratios:
#     print((4/x)**2-1)
    # mu.append((4/x)**2-1)
# print(mu)

# p = float("inf")
# for i in range(len(self_avoiding_walks)-2):
#     c = (self_avoiding_walks[i+2]/self_avoiding_walks[i])**0.5
#     print(c)
#     if c >= p:
#         print("OOP")
#     p = c

# last = -float("inf")
# for i in range(len(cnn)):
#     current = (c[i] ** (4/(i+1)) - 1) - (cnn[i] ** (4/(i+1)) - 1)
#     print(current)
#     if current < last:
#         print("DECREASE")
#     last = current

s = cnn
# test_submultiplicative(s)
# test_supermultiplicative(s)
# lowest_ratios(s)
# highest_ratios(s, 12, 4)
# ratio_table(s)
bounds(s, 1, 1)