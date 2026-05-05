from app import app, db, Character, Event, Location

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Add Characters
        import json
        characters = [
            Character(name="柯爾市長", role="現狀維持者", description="蓬萊首都的市長，務實派，重視經濟成長與外資引進，迴避敏感議題。試圖在各方勢力中取得平衡。", is_playable=False, image_filename="char_mayor.png",
                      relationships_text="與【威廉總裁】關係密切，常私下會面討論標案；對【艾達議員】的激進提案感到頭痛。",
                      stances_text="支持：外資免稅法案、開發特定保護區\n反對：大幅調漲基本工資、激進環保法案",
                      personal_stats_config=json.dumps({"政治資本": 70, "公眾信任": 50})),
            Character(name="莫長老", role="保守派大老", description="地方派系領袖與宗族代表，重視傳統價值與秩序。認為社會變遷太快會帶來動亂，掌控著大量傳統選票。", is_playable=False, image_filename="char_elder.png",
                      relationships_text="與【雷將軍】是多年老友；極度厭惡【艾達議員】與【學生運動者】。",
                      stances_text="支持：家庭價值維護法、嚴格治安法\n反對：同性婚姻、廢除死刑",
                      personal_stats_config=json.dumps({"派系影響力": 80, "金錢獲利": 60})),
            Character(name="艾達議員", role="進步派領袖", description="推動平權與激進改革的年輕世代政治家，受學生歡迎。但也常因過於理想化而受到既得利益者的強烈批評。", is_playable=False, image_filename="char_councilor.png",
                      relationships_text="經常支援【學生運動者】；強烈批評【柯爾市長】與【威廉總裁】的官商勾結。",
                      stances_text="支持：同性婚姻全面合法、碳排放重稅\n反對：都市更新迫遷、網路言論審查",
                      personal_stats_config=json.dumps({"年輕選票": 70, "影響力": 50})),
            Character(name="威廉總裁", role="資本家", description="蓬萊最大科技集團的 CEO，利益導向，主張自由市場，強烈反對過度的勞工保護與高稅收政策。", is_playable=False, image_filename="char_ceo.png",
                      relationships_text="常透過【柯爾市長】施壓政策；視【龐頭目】為眼中釘。",
                      stances_text="支持：企業減稅、彈性工時法案\n反對：嚴格勞檢、加重污染罰金",
                      personal_stats_config=json.dumps({"企業資產": 90, "媒體控制力": 60})),
            Character(name="莉亞記者", role="第四權", description="知名獨立傳媒的調查記者，挖掘真相，但有時會為了點閱率與話題性而使用聳動的標題，對輿論有強大影響力。", is_playable=False, image_filename="char_journalist.png",
                      relationships_text="曾多次爆料【威廉總裁】的醜聞；與【蘇網紅】在網路上有激烈的流量競爭。",
                      stances_text="支持：政府資訊公開、新聞自由保護法\n反對：國家機密保護法擴權",
                      personal_stats_config=json.dumps({"獨家內幕": 50, "公信力": 60})),
            Character(name="龐頭目", role="勞工代表", description="全國總工會的強勢領袖，具有民粹傾向。為了爭取基層勞工權益，不惜發動罷工與激烈抗爭。", is_playable=False, image_filename="char_union.png",
                      relationships_text="與【威廉總裁】勢不兩立；認為【柯爾市長】軟弱無能。",
                      stances_text="支持：調漲基本工資 30%、勞工董事法案\n反對：引進廉價移工、派遣工合法化",
                      personal_stats_config=json.dumps({"動員能力": 70, "談判籌碼": 40})),
            Character(name="雷將軍", role="國安強硬派", description="退役國防將領，極度保守，強調國家安全與社會秩序，對內外威脅都主張絕對強硬的手段。", is_playable=False, image_filename="char_general.png",
                      relationships_text="與【莫長老】關係良好；認為【莉亞記者】與【學生運動者】是動亂之源。",
                      stances_text="支持：網路言論管制法、擴大國防預算\n反對：縮減兵役、裁減警察權力",
                      personal_stats_config=json.dumps({"軍方人脈": 80, "影響力": 50})),
            Character(name="蘇網紅", role="意見領袖", description="擁有百萬粉絲的網路意見領袖，善於操弄網路風向，立場搖擺。誰的聲量大、哪邊有流量，就往哪邊靠攏。", is_playable=False, image_filename="char_influencer.png",
                      relationships_text="偶爾收受【威廉總裁】的公關費；經常在網路上嘲諷【費教授】。",
                      stances_text="支持：無特定核心理念，依賴流量決定立場\n反對：任何會限制網路流量的法案",
                      personal_stats_config=json.dumps({"網路聲量": 80, "信任值": 20})),
            Character(name="費教授", role="理想主義者", description="頂尖大學的政策智囊，但常脫離基層現實。提出許多宏觀但難以落實的烏托邦藍圖。", is_playable=False, image_filename="char_professor.png",
                      relationships_text="為【柯爾市長】提供政策建議，但常不被採納；被【蘇網紅】嘲笑為蛋頭學者。",
                      stances_text="支持：漸進式民主改革、永續能源發展\n反對：民粹式的極端抗爭、暴力手段",
                      personal_stats_config=json.dumps({"學術地位": 70, "影響力": 30})),
            Character(name="基層公務員", role="體制執行者", description="在體制內掙扎的執行者。負責將上層的政策落實到民間，經常面臨上級壓力與民眾不滿的兩難。", is_playable=True, image_filename="char_civil_servant.png",
                      relationships_text="直接承受【柯爾市長】的壓力；經常被【市民】與【中小企業主】抱怨。",
                      stances_text="支持：穩定的加薪與年金制度、增加人力\n反對：朝令夕改的政策、無意義的加班",
                      personal_stats_config=json.dumps({"升遷考績": 50, "過勞指數": 50})),
            Character(name="學生運動者", role="街頭倡議者", description="在街頭抗爭的青年倡議者。充滿熱情，希望能打破舊有體制，快速改變社會上的不公不義。", is_playable=True, image_filename="char_student.png",
                      relationships_text="視【艾達議員】為盟友；將【莫長老】與【威廉總裁】視為打倒的目標。",
                      stances_text="支持：降低投票年齡、徹底的財富重分配\n反對：維穩重於人權的政策",
                      personal_stats_config=json.dumps({"社會影響力": 40, "退學危機": 30})),
            Character(name="中小企業主", role="一般百姓", description="受政策與經濟波動影響最深的一般百姓。只求安穩賺錢度日，對複雜的政治鬥爭感到厭煩。", is_playable=True, image_filename="char_generic.png",
                      relationships_text="害怕【龐頭目】的罷工行動；對【柯爾市長】的偏袒大財團感到不滿。",
                      stances_text="支持：減稅降息、穩定的治安\n反對：無預警停電、過高的工資調漲",
                      personal_stats_config=json.dumps({"公司資金": 50, "黑白兩道人脈": 30}))
        ]
        db.session.add_all(characters)

        # Add Events
        events = [
            Event(
                title="《家庭價值維護法》與平權公投",
                description="社會正因為同婚議題撕裂。進步派發起了大遊行，而保守派則推動《家庭價值維護法》公投。身為社會的一份子，你的公開表態與實際行動將會帶動輿論的風向。",
                image_filename="event_marriage.png",
                persuasion_config=json.dumps({
                    "if_option": 0, # Index 0 is Option A
                    "target": "莫長老",
                    "reason": "莫長老對你的公開表態極度不滿，揚言要動員地方派系全面抵制你。",
                    "persuasion_high": {
                        "text": "私下拜會長老，承諾在其他傳統議題上讓步 (高說服力)",
                        "result_text": "長老勉強接受了你的善意，雖然依然不滿，但取消了全面抵制的行動。",
                        "effects": {"order": 5, "progress": -5}
                    },
                    "persuasion_low": {
                        "text": "強硬回擊，批評長老的守舊 (低說服力)",
                        "result_text": "談判破裂！長老發動了激烈的街頭反制，社會爆發了大規模肢體衝突。",
                        "effects": {"order": -15, "progress": 5}
                    }
                }),
                option_a_text="積極參與平權遊行並捐款",
                option_a_freedom=15, option_a_order=-5, option_a_progress=10, option_a_populism=5,
                option_a_explanation="【社會運動與法案推動】你的參與展現了由下而上的草根力量。在政治學中，這稱為『關鍵少數（Critical Mass）』效應：當單一議題的動員跨過臨界點，便能引發『蝴蝶效應』，逼迫政府必須順應『主流民意』。自由與進步因此提升，但觸發了保守派的『文化焦慮』。",
                option_a_result_text="你的行動帶動了更多人上街，平權法案在強大民意下驚險過關！但也引發了保守派群眾極度憤怒與恐慌。",
                option_b_text="支持保守派，連署維護傳統",
                option_b_freedom=-5, option_b_order=10, option_b_progress=-10, option_b_populism=-5,
                option_b_explanation="【傳統價值的防禦機制】面對快速變遷，社會往往會出現『保守主義反撲』。你的連署成為了保守派集結的『破窗效應』起點，賦予了他們發聲的正當性。這能維持社會既有秩序，但會壓抑少數群體的權利，讓進步派對你感到失望。",
                option_b_result_text="保守派勢力大增，傳統法案通過。社會秩序得以維持，但進步派青年極度失望，認為這是一種變相的隔離。"
            ),
            Event(
                target_role="中小企業主",
                title="【企業主面臨抉擇】同婚專法與抵制風波",
                description="社會正為了同婚法案爭論不休。學生團體揚言要在網路上抵制所有不支持平權的在地店家；但另一方面，你的大客戶與供應商（多半是莫長老的保守派信徒）私下警告你，如果敢表態支持，他們就會撤單。這直接影響了你的公司存亡。",
                image_filename="event_marriage.png",
                option_a_text="發布聲明支持平權",
                option_a_freedom=10, option_a_order=-5, option_a_progress=15, option_a_populism=5,
                option_a_personal_effects=json.dumps({"公司資金": -20, "黑白兩道人脈": -10}),
                option_a_explanation="【粉紅經濟】支持平權吸引了年輕客群，但短期內流失了傳統大客戶的訂單，導致資金周轉困難。同時你得罪了保守派長輩，人脈受損。",
                option_a_result_text="你贏得了年輕人的掌聲與『良心企業』的稱號，但現實是殘酷的，傳統訂單大量流失，公司面臨嚴重的資金缺口。",
                option_b_text="與保守派妥協，反對法案",
                option_b_freedom=-5, option_b_order=5, option_b_progress=-10, option_b_populism=5,
                option_b_personal_effects=json.dumps({"公司資金": +10, "黑白兩道人脈": +20}),
                option_b_explanation="【抵制效應】雖然學生在網路上發起抵制，但傳統客戶為了獎勵你的『忠誠』，給了你更多訂單，你在商界的人脈也更穩固了。",
                option_b_result_text="你的店鋪在網路上被刷一星負評，但大戶的訂單讓公司賺了一筆。社會變得更保守，而你選擇了向現實低頭。"
            ),
            Event(
                target_role="基層公務員",
                title="【公務員的兩難】科技廠污染與長官施壓",
                description="你在審核星鏈科技園區的廢水排放報告時，發現了嚴重的數據造假。但柯爾市長的親信直接來到你的辦公室，暗示這家公司是重點保護對象，要求你『閉一隻眼』讓公文過關。若不從，你的考績與職涯可能就此完蛋。",
                image_filename="event_pollution.png",
                persuasion_config=json.dumps({
                    "if_option": 0,
                    "target": "柯爾市長",
                    "reason": "你將資料洩漏給媒體，市長震怒，準備將你免職並面臨洩密起訴。",
                    "persuasion_high": {
                        "text": "暗示手中還有更多高層把柄，要求和平離職 (高說服力)",
                        "cost": {"升遷考績": -20},
                        "result_text": "市長投鼠忌器，讓你安全下莊並調往偏鄉，免除了牢獄之災。",
                        "effects": {"order": 5, "progress": 0}
                    },
                    "persuasion_low": {
                        "text": "拒絕溝通，在媒體上全面開戰 (低說服力)",
                        "cost": {"過勞指數": +50},
                        "result_text": "你遭到了整個官僚體系的無情追殺，身心俱疲，社會對政府的信任也徹底崩盤。",
                        "effects": {"order": -15, "populism": 15}
                    }
                }),
                option_a_text="拒絕蓋章，並向媒體吹哨",
                option_a_freedom=10, option_a_order=-10, option_a_progress=5, option_a_populism=15,
                option_a_personal_effects=json.dumps({"升遷考績": -40, "過勞指數": +20}),
                option_a_explanation="吹哨引發社會譁然，政府被迫嚴查星鏈科技，你的行動造成了全國性的影響。",
                option_a_result_text="事情曝光引發社會譁然！星鏈科技被迫停工受檢。但你徹底得罪了高層，被調到冷衙門。",
                option_b_text="明哲保身，配合長官蓋章",
                option_b_freedom=-5, option_b_order=5, option_b_progress=-5, option_b_populism=0,
                option_b_personal_effects=json.dumps({"升遷考績": +20, "過勞指數": -10}),
                option_b_explanation="體制內的默契讓你獲得了長官的信任，但代價是環境的持續惡化。",
                option_b_result_text="星鏈科技順利擴廠，看著日益污濁的河水，你學會了在體制內閉嘴生存。"
            ),
            Event(
                target_role="學生運動者",
                title="【學運的抉擇】基本工資抗爭的升級",
                description="為了聲援龐頭目發起的基本工資大遊行，你的學生組織原本只計畫在廣場靜坐。但群眾情緒越來越高漲，有些激進派提議衝入行政院癱瘓政府運作，但這絕對會引來雷將軍手下鎮暴警察的強力鎮壓。你要帶頭衝鋒嗎？",
                image_filename="event_wage.png",
                option_a_text="帶領群眾衝擊政府機關",
                option_a_freedom=5, option_a_order=-20, option_a_progress=10, option_a_populism=20,
                option_a_personal_effects=json.dumps({"社會影響力": +30, "退學危機": +40}),
                option_a_explanation="【激進公民不服從】衝擊體制迅速抓住了媒體版面，你成為了學運新星，但隨之而來的是警方的暴力驅離與校方的退學警告。",
                option_a_result_text="你們成功佔領了行政院大廳一晚！你的名字響徹全國，但也遭到警方逮捕。校方迫於高層壓力，正在研擬將你開除學籍。",
                option_b_text="堅守和平非暴力底線",
                option_b_freedom=5, option_b_order=5, option_b_progress=5, option_b_populism=-10,
                option_b_personal_effects=json.dumps({"社會影響力": -10, "退學危機": -10}),
                option_b_explanation="【溫和派邊緣化】在情緒高漲的群眾運動中，理性溫和的聲音往往被視為懦弱，導致你在組織內的影響力下滑。",
                option_b_result_text="你成功阻止了流血衝突，但也因此被激進派罵作『妥協份子』。遊行最終和平落幕，但政府並未給出實質承諾，工資法案不了了之。"
            ),
            Event(
                title="「翠綠之河」科技污染案",
                description="莉亞記者爆出『星鏈科技』長期將有毒廢水排入首都水源地。龐頭目率領群眾包圍市府抗議。作為社會中有影響力的一員，你的公開表態將影響市府最終的處置。",
                image_filename="event_pollution.png",
                option_a_text="強烈要求勒令工廠停工",
                option_a_freedom=5, option_a_order=5, option_a_progress=-5, option_a_populism=10,
                option_a_explanation="【環境正義 vs 經濟發展】這是經典的『雙刃劍』困境。你作為社會公民的強烈表態，打破了官商之間的『默契（Information Asymmetry）』，引爆了輿論。要求停工伸張了公共利益，但也打擊了當地的經濟動能，並激怒了利益受損的資本家。",
                option_a_result_text="在強大輿論壓力下，市府勒令停工！環境得到保護，但大量基層員工瞬間失業，引發了另一波恐慌。",
                option_b_text="呼籲罰款了事，保住就業機會",
                option_b_freedom=-5, option_b_order=-10, option_b_progress=10, option_b_populism=15,
                option_b_explanation="【發展型國家的妥協】為求穩定，你的呼籲給了政府『民意台階』去對資本做出讓步。在社會學中這被批評為『利潤私有化、外部成本公共化』。這會嚴重損害政府公信力（秩序下降，民粹上升），並讓環保團體對你徹底失望。",
                option_b_result_text="市府最終只輕罰了事。資本家鬆了一口氣，但民眾對體制徹底失去信任，『官商勾結』的標籤被深深貼上。"
            ),
            Event(
                title="國家網路安全與言論管制法案",
                description="大選將近，網路上充斥著由不明境外勢力與極端網軍（如蘇網紅等）散佈的假消息。雷將軍與國安高層強烈建議設立專責機構來監管言論，賦予政府封禁帳號的權力。社會亟需有影響力的聲音來定調，你的公開表態將成為關鍵的風向球。",
                image_filename="event_fakenews.png",
                option_a_text="發起連署，全力支持國安立法",
                option_a_freedom=-20, option_a_order=15, option_a_progress=-5, option_a_populism=-10,
                option_a_explanation="【國家權力擴張與寒蟬效應】你的連署帶動了『沉默螺旋（Spiral of Silence）』的反轉，讓支持管制的聲音瞬間成為主流。當社會讓渡『自由』以換取『安全』時，政治學警告這容易讓國家機器過度膨脹，引發『寒蟬效應』——民眾因害怕受罰而進行自我審查。",
                option_a_result_text="你的連署行動在網路上迅速發酵，給予了政府強大的民意後盾！雷厲風行的執法讓社會秩序迅速獲得控制。但許多人擔心政府會藉此打壓異己，政治寒蟬效應蔓延。",
                option_b_text="串聯抗議，堅守言論自由底線",
                option_b_freedom=15, option_b_order=-15, option_b_progress=5, option_b_populism=20,
                option_b_explanation="【民主防衛機制的脆弱性】你的串聯成為了抵抗極權的『社會防線』。拒絕監管意味著民主體制必須赤裸裸地面對假訊息攻擊。這會導致社會極化加劇、信任破裂（秩序下降，民粹急遽飆升），這是自由民主必須承受的代價。",
                option_b_result_text="你帶領群眾成功阻擋了法案，捍衛了得來不易的言論自由！但代價是社會持續被演算法與假訊息撕裂，民粹主義高漲，不同陣營間的對立更加不可理喻。"
            ),
            Event(
                title="「勞工生存權」大遊行與薪資法",
                description="通膨嚴重物價飛漲，龐頭目號召了十萬人上街，要求一次性大幅調漲基本工資 30% 以維持生存底線。威廉總裁等企業界代表強烈反彈，在媒體上揚言若法案通過將引發全國性的大規模倒閉潮。作為具備社會聲量的人物，你的動員與聲援，將決定這場運動的成敗。",
                image_filename="event_wage.png",
                option_a_text="動員身邊資源，全力聲援勞工",
                option_a_freedom=10, option_a_order=-10, option_a_progress=15, option_a_populism=15,
                option_a_explanation="【勞工運動與議價能力】作為有影響力的人，你的聲援賦予了勞工作為『弱勢群體』正當的『議價能力（Bargaining Power）』。藉由群眾抗爭，勞工成功爭取了分配正義。但資方往往會將增加的薪資成本『轉嫁』給消費者或裁員，導致部分弱勢失業。",
                option_a_result_text="你的聲援帶動了更多人加入！十萬勞工在街頭歡欣鼓舞，成功逼迫政府讓步！但隨之而來的是物價進一步轉嫁，許多無法負擔成本的中小企業黯然倒閉。",
                option_b_text="發表聲明反對，呼籲共體時艱",
                option_b_freedom=-5, option_b_order=10, option_b_progress=-5, option_b_populism=-10,
                option_b_explanation="【論述權力與涓滴經濟學】你的聲明在媒體上取得了『論述霸權（Hegemony）』，成功瓦解了勞工運動的士氣。這雖然穩定了市場秩序，但這是基於『涓滴效應』的迷思——認為富人賺錢最終會流向窮人。這只會固化階級，累積下一次爆發的怒火。",
                option_b_result_text="你的聲明成為了資方與政府下台階的理由，遊行氣勢被削弱。宏觀經濟指標保持了穩定，但貧富差距的裂痕被進一步拉大，被遺忘的基層勞工在底層悶燒。"
            ),
            # --- 新增的 5 個一般事件 ---
            Event(
                title="教育改革與課綱爭議",
                description="費教授聯合民間教改團體，提出了一套強調批判性思考與多元史觀的新課綱。然而，莫長老與保守家長團體認為這會摧毀傳統價值觀，甚至削弱國族認同。兩派人馬在教育部前發生了推擠，教育部長正看著網路輿論猶豫不決。",
                image_filename="event_education.png",
                option_a_text="在網路上發動串聯，力挺新課綱",
                option_a_freedom=10, option_a_order=-5, option_a_progress=15, option_a_populism=5,
                option_a_explanation="【意識形態國家機器】教育在社會學中被視為傳遞意識形態的工具。你的網路串聯成功創造了『同溫層效應（Echo Chamber）』，讓政府誤以為這就是絕對多數民意。推動多元史觀能解放思想，但也打破了單一國族認同，引發了強烈的文化撕裂。",
                option_a_result_text="你的網路串聯成為了壓垮駱駝的最後一根稻草，部長順應民意宣布新課綱上路！年輕世代獲得了更開放的教育，但也引發了跨世代的嚴重對立。",
                option_b_text="呼籲冷靜，連署暫緩實施",
                option_b_freedom=-5, option_b_order=10, option_b_progress=-10, option_b_populism=-5,
                option_b_explanation="【社會維穩與體制慣性】你的保守連署啟動了官僚體系的『路徑依賴（Path Dependence）』，給了政府極佳的藉口來維持現狀。雖然成功將衝突降溫（秩序上升），但這犧牲了思想的進步與創新潛力，讓改革派感到強烈背叛。",
                option_b_result_text="你的保守連署給了政府極佳的台階下。傳統史觀得以保留，社會避免了短期的撕裂，但教育界痛批政府在改革上退縮，國家的創新競爭力也受到了質疑。"
            ),
            Event(
                target_role="莉亞記者",
                title="【記者的抉擇】威廉總裁的封口費",
                description="你掌握了威廉總裁旗下公司大規模逃漏稅的關鍵證據。但就在你要發布獨家新聞的前一晚，總裁的特助找上了你，開出一張足以讓你提早退休的支票，並暗示如果報導曝光，你在業界將永無立足之地。",
                image_filename="event_bribe.png",
                option_a_text="拒絕收買，果斷爆料",
                option_a_freedom=15, option_a_order=-10, option_a_progress=10, option_a_populism=10,
                option_a_personal_effects=json.dumps({"公信力": +30, "獨家內幕": -20}),
                option_a_explanation="你贏得了空前的公信力！但也遭到了總裁動用媒體資源的全面封殺，甚至收到了死亡威脅。",
                option_a_result_text="這則爆料震驚全國，威廉總裁被迫辭職接受調查。但你也因此被業界高層聯手打壓，失去了許多內線消息來源。",
                option_b_text="收下支票，銷毀證據",
                option_b_freedom=-10, option_b_order=5, option_b_progress=-5, option_b_populism=-5,
                option_b_personal_effects=json.dumps({"公信力": -20, "獨家內幕": +50}),
                option_b_explanation="你變得極度富有，甚至有了跨足政商高層的資本，但你違背了新聞倫理，這成為你一輩子的未爆彈。",
                option_b_result_text="報導石沉大海。你在市中心買了一套豪宅，威廉總裁也順利連任商會主席。表面風平浪靜，但社會的不公不義依然橫行。"
            ),
            Event(
                title="能源危機與重啟核電",
                description="夏季即將到來，供電吃緊導致數次無預警分區停電，引發強烈民怨。威廉總裁要求重啟封存的核電廠以維持產業運作，但艾達議員與環保團體堅決反對，認為這是拿下一代的安全作為賭注。",
                image_filename="event_energy.png",
                option_a_text="重啟核電，確保供電無虞",
                option_a_freedom=-5, option_a_order=15, option_a_progress=-10, option_a_populism=-5,
                option_a_result_text="燈火通明的夜晚安撫了企業與多數民眾的焦慮。經濟命脈得以保全，但環保團體痛批政府背信忘義，並在核電廠外紮營長期抗爭。"
                ,
                option_b_text="堅持非核，推動嚴格限電",
                option_b_freedom=5, option_b_order=-15, option_b_progress=15, option_b_populism=10,
                option_b_result_text="你選擇了艱難的能源轉型之路。限電讓生活變得不便，企業出走潮開始湧現，民怨沸騰。但也逼迫社會加速發展了綠能科技。"
            ),
            Event(
                target_role="雷將軍",
                title="【軍方的抉擇】邊境衝突與軍費擴張",
                description="鄰國在邊界海域舉行了極具挑釁意味的大規模軍演。國內民族主義情緒高漲，群眾要求政府採取強硬措施。柯爾市長希望低調處理，但身為軍方代表的你，掌握著是否要提升戰備層級的關鍵權力。",
                image_filename="event_military.png",
                option_a_text="下令軍隊進入最高戒備，強力回應",
                option_a_freedom=-15, option_a_order=20, option_a_progress=-5, option_a_populism=20,
                option_a_personal_effects=json.dumps({"軍方人脈": +30, "影響力": +20}),
                option_a_explanation="強硬的態度讓你成為民族英雄，軍方影響力大增，但過度的擴軍排擠了其他民生預算，且有引發實際戰爭的風險。",
                option_a_result_text="戰機升空，軍艦出航！國內士氣大振，但鄰國也立即升級了軍事行動。區域局勢陷入劍拔弩張的危機邊緣。",
                option_b_text="保持克制，透過外交管道斡旋",
                option_b_freedom=5, option_b_order=-5, option_b_progress=5, option_b_populism=-15,
                option_b_personal_effects=json.dumps({"軍方人脈": -20, "影響力": -10}),
                option_b_explanation="克制避免了戰爭，但被國內激進派視為懦弱。你在軍中的威望受損。",
                option_b_result_text="冷靜的克制化解了熱戰的危機，股市與外資鬆了一口氣。但你在網路上被罵作『投降派』，民族主義者的怒火轉向了政府內部。"
            ),
            Event(
                title="全民基本收入 (UBI) 實驗法案",
                description="面對日益擴大的貧富差距，社會團體提出了『全民基本收入』倡議，主張每月無條件發放生活費給每一位國民。這需要極大幅度地提高企業稅與富人稅，引發了資方強烈抗議。身為有影響力的人，你的連署將起到關鍵作用。",
                image_filename="event_ubi.png",
                persuasion_config=json.dumps({
                    "if_option": 0,
                    "target": "威廉總裁",
                    "reason": "威廉總裁對於你連署 UBI 法案極度不滿，揚言聯合商會將資金大舉撤出本國。",
                    "persuasion_high": {
                        "text": "提出針對特定產業的稅收減免作為配套 (高說服力)",
                        "result_text": "你成功安撫了資方，總裁同意暫緩撤資，但 UBI 的財源也因此縮水。",
                        "effects": {"order": 5, "progress": -5}
                    },
                    "persuasion_low": {
                        "text": "強硬要求企業承擔社會責任 (低說服力)",
                        "result_text": "談判破裂！大批企業將總部遷往海外，國家面臨嚴重的資本外流與失業潮。",
                        "effects": {"order": -15, "progress": -10}
                    }
                }),
                option_a_text="積極連署，推動財富重分配",
                option_a_freedom=10, option_a_order=5, option_a_progress=20, option_a_populism=10,
                option_a_explanation="【福利國家與議程設定】你利用自身的影響力達成了『議程設定（Agenda Setting）』，成功逼迫政府將這個極端左派政策排入施政計畫。UBI 能有效消除貧窮，但你引發的稅賦恐慌可能引發『資本外逃（Capital Flight）』，導致財政崩潰風險。",
                option_a_result_text="在輿論壓力下，政府開始試辦 UBI！底層人民生活獲得保障。但沉重稅賦讓大企業相當不滿。",
                option_b_text="拒絕連署，擔憂財政破產",
                option_b_freedom=-5, option_b_order=5, option_b_progress=-15, option_b_populism=-5,
                option_b_explanation="【階級固化與相對剝奪感】你的拒絕切斷了這項運動的最後一絲希望，鞏固了既得利益者的優勢（威廉總裁支持）。雖然保障了財政紀律，但底層的『相對剝奪感（Relative Deprivation）』會隨著貧富差距持續累積，這是一顆隨時會引爆的民粹炸彈。",
                option_b_result_text="倡議失敗。傳統經濟秩序得以維持，但底層民眾的剝奪感越來越重，社會火藥庫正在倒數計時。"
            ),
            # --- 新增的 3 個隨機新聞事件 (is_news=True) ---
            Event(
                title="跨國財團併購在地傳媒，新聞自由亮紅燈？",
                description="震驚社會的消息傳出！威廉總裁旗下的投資公司正式收購了莉亞記者所在的『獨立傳媒總部』。外界擔憂未來的報導將會受到資本家的嚴格審查，寒蟬效應已經在媒體圈蔓延。",
                image_filename="news_media.png",
                is_news=True,
                relationship_effects_text="【莉亞記者】與【威廉總裁】由敵對轉為上下屬關係；【蘇網紅】趁機接收了大量不滿的閱聽眾，聲量大增。",
                option_a_text="繼續", # 只有這個按鈕會顯示
                option_a_freedom=-15, option_a_order=10, option_a_progress=-5, option_a_populism=5,
                option_a_result_text="資本的力量再次證明了它的無孔不入。獨立傳媒的批判聲浪瞬間小了許多，取而代之的是更多歌舞昇平的娛樂新聞。",
                option_b_text="", option_b_result_text=""
            ),
            Event(
                title="網路偶像蘇網紅遭起底，爆料影片引發百萬粉絲脫粉潮",
                description="知名意見領袖蘇網紅被駭客流出一段私下影片，內容顯示他同時收受不同政治陣營的黑錢，並嘲笑自己的粉絲是『好操弄的提款機』。網路輿論瞬間炸鍋，各大論壇充滿了憤怒的討伐聲。",
                image_filename="news_scandal.png",
                is_news=True,
                relationship_effects_text="【蘇網紅】信任值歸零；【學生運動者】利用此機會發起了『拒絕網軍洗腦』的社會運動，影響力上升。",
                option_a_text="繼續",
                option_a_freedom=5, option_a_order=-10, option_a_progress=10, option_a_populism=-15,
                option_a_result_text="曾經呼風喚雨的網紅跌落神壇。民眾開始反思盲從網路風向的危險，社會的理智程度有了短暫的回升，但也讓網路環境陷入短期的混亂互相指責。",
                option_b_text="", option_b_result_text=""
            ),
            Event(
                title="首都發生嚴重連環車禍，牽扯出官商勾結黑幕",
                description="首都第一廣場發生了嚴重的公車暴衝意外，造成多名市民死傷。調查指出肇事客運公司長期強迫司機超時加班，而負責勞檢的市府高層卻屢屢放水。龐頭目率領憤怒的家屬包圍了市府大門。",
                image_filename="news_accident.png",
                is_news=True,
                relationship_effects_text="【柯爾市長】公眾信任度重挫；【龐頭目】與【基層公務員】的矛盾加劇；【莫長老】趁機抨擊市府無能。",
                option_a_text="繼續",
                option_a_freedom=-5, option_a_order=-20, option_a_progress=-5, option_a_populism=25,
                option_a_result_text="這場悲劇成為了壓垮駱駝的最後一根稻草。對於體制腐敗的憤怒，讓越來越多本來冷漠的市民加入了激進抗爭的行列。",
                option_b_text="", option_b_result_text=""
            )
        ]
        db.session.add_all(events)
        
        # Add Locations
        locations = [
            Location(name="首都第一廣場", description="城市的政治核心地帶，經常是大型集會與抗爭的發生地。當群眾的不滿累積到頂點時，這裡將被怒火淹沒。", x_pos=50, y_pos=50),
            Location(name="星鏈科技園區", description="威廉總裁的商業帝國核心，為國家貢獻了龐大的稅收與就業機會，但同時也帶來了嚴重的環境污染問題。", x_pos=80, y_pos=30),
            Location(name="蓬萊頂尖大學", description="學術與思想的搖籃。費教授在此發表演說，而無數的學生運動者則在這裡策劃下一場街頭革命。", x_pos=20, y_pos=70),
            Location(name="傳統舊城區", description="莫長老勢力盤根錯節的地方。這裡保留了古老的文化與價值觀，但也抗拒著過於激進的社會變遷。", x_pos=70, y_pos=80),
            Location(name="獨立傳媒總部", description="莉亞記者與蘇網紅活躍的戰場。這裡製造出無數的新聞與輿論，影響力甚至凌駕於實體政治之上。", x_pos=30, y_pos=30)
        ]
        db.session.add_all(locations)
        
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
