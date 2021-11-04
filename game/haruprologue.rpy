define v = ("Vena")
define h = ("Haru")
define k = ("Kioko")
define a = ("Asha")
define al = ("Almasi")
define bbg = ("Başka Bir Gümüş Oyuk Sakini")
define obg = ("Öteki Gümüş Oyuk Sakini")
define dbg = ("Diğer Bir Gümüş Oyuk Sakini")
define gr = ("Grandük")
define m = ("Marley")
define c = ("Cyril")
define l = ("Lionel")
define x = ("Xerxes")
define u = ("???")
define bks = ("Bir Kadın Sesi")
define io = ("Ionyr")

init:
    $ flash = Fade(.25, 0, .75, color="#fff")


label haruprologue:

    stop music fadeout 1.0

    scene blackscreen

    "Bilinmeyene olan arzum vücudumu alevler halinde sarıyordu."
    "Ve karşı koymak çok zordu."

    scene traincomp with fade
    show Kioko ClosedEye at left with dissolve
    show Vena Default at right with dissolve

    h "“Uyuyabildiğine inanamıyorum gerçekten de.”"

    "Vena, Kioko’ya göz ucuyla baktıktan sonra derin bir iç çekmişti."

    v "“Ben de senin bütün bu olan bitene rağmen bu kadar heyecanlı olmana inanamıyorum.”"

    "Yanaklarımı bir çocuğun huysuzluğunu andıracak şekilde şişirdim."

    h "“Her gün Gümüş Oyuk’tan çıkma fırsatı yakalamıyoruz. Bu bir ilk-”"

    show Vena Frowning with dissolve

    v "“Ve muhtemelen son.”"

    "Lafımı bölmesi diyeceklerimi ağzıma tıkıvermişti."
    "Dedikleri sanki an be an daha zehirli oluyor, kanıma daha çok işliyordu."
    "(Bunun sebebi muhtemelen çemberimizin zayıflatılması."
    "Eskisi gibi tepki vermeye çalışmak sanırım en iyisi.)"
    "Neyse ki onun da konuyu değiştireceği tutmuştu."

    show Vena Sideway with dissolve

    v "“Birkaç gündür gözüne stresten uyku girmiyor.”"

    hide Vena with dissolve

    show Kioko ClosedEye with dissolve:
        zoom 1.5

    "Bunun farkındaydım, aramızdaki bağın güçsüzleşmesine rağmen Kioko’nun bütün stresi benim göğsümde de köklerini salmıştı."
    "Fakat herhangi bir yatıştırıcı kelime ağzımdan çıkamadı."
    "Yılların duygusal noksanlığı aniden gelen hislerle birleşince beni böyle garip, şaşkın bir ruh haline sokmuştu."

    hide Kioko
    show Kioko ClosedEye at left with dissolve
    show Vena Frowning at right with dissolve

    h "“Sanıyorum ki herkes aynı problemden mustarip.”"

    v "“Sen hariç herkes…”"

    "(İşte yine başlıyoruz.)"
    "Bu dünyaya vardık varalı Vena’nın azarlamalarının sonunu görememiştim."
    "Rahatsız bir şekilde gözlerimi kaçırıp camın ötesinde bir noktaya odakladım. Ne zaman kavga etsek karnıma tanıdık olmadığım bir ağrı giriyor ve midem bulanmaya başlıyordu."
    "Fakat kendimi rahatlatma çabalarım boşunaydı. Kompartımanın küçüklüğüne daha fazla dayanamayıp konuştum."

    h "“Ben birazcık hava alacağım.”"

    show Vena ArchedEye with dissolve

    v "“Nerede?”"

    "Ayağa kalktım."

    h "“Koridorda dolaşacağım, bacaklarım uyuştu.”"

    "Vena derince bir nefes aldı."

    show Vena Default with dissolve

    v "“Keyfin bilir. Başını belaya sokma da…”"

    "Kafamı belli belirsiz sallayıp kapıyı açtığım gibi kendimi koridora attım."
    "Bana izin vereceğini düşünmemiştim, o yüzden daha fazla orada kalarak şansımı riske atmasam iyi olurdu."

    play sound slidedoor

    scene traincorridor with fade

    pause 1.0

    "Kirli camlardan sızan gün ışığı, kirpiklerimi kavuruyordu."
    "Geldiğim yerde Güneş gökte asla yükselmez, günün bütün ihtişamı koyu mavi gökte asılı kalan yıldızlara bahşedilirdi."
    "Şimdi ise semada bu koca yıldız tek başına hüküm sürüyor, akşama kadar kardeşlerinin sahneye çıkmasına izin vermiyordu."
    "(Eh, yıldızları okuyabilen biri değilim zaten. Hem bu dev yıldız diğerlerine kıyasla daha çok mana veriyor.)"
    "Gün ışığı daha önce hiç olmadığı kadar güçlü hissetmemi sağlıyordu."
    "Geldiğimizden beri böyle hissediyordum. Diğerleri için de aynı durum söz konusuydu."
    "(…)"

    "Vena bu konudaki düşüncelerimi bilse bana ne çok kızardı. Yiyeceğim azarı hayal etmek bile tüylerimi diken diken ediyordu."

    play sound walking

    scene traincorridor with fade:
        xpos 0.1 ypos 1.7 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 2.0

    stop sound

    "Bir camın kenarına yaklaştım ve pervazına dirseğimi dayayıp manzarayı izleyerek hayal etmeye koyuldum."
    "Whemond nasıl bir yerdi, insanlar vaktini nasıl harcıyordu?"
    "Nasıl evlerde yaşıyorlardı? Neler yiyorlardı?"
    "Yaklaşık bir aydır kaldığımız o küçük köyde bunlardan başka bir şey düşünememiştim."
    "Kalbim, özgürlüğün o tatlı rüzgarıyla kıpır kıpır olmuştu."
    "Fakat bu huzurlu, kısacık an arkamda tanıdık bir sesin yankılanmasıyla son buldu."

    u "“Haru? Burada ne yapıyorsun?”"

    "Yavaşça dönüp tebessüm ettim."

    show Asha Smiling with dissolve

    a "“Kimsenin kompartımanını terk etmediğinden emin olmaya çalışıyorum.”"

    h "“Ah… Hahah…”"

    "Mahcup bir şekilde ensemi kaşımaya başladım, tepkim Asha’yı güldürmüştü. Yavaşça yanıma yaklaştı."

    show Asha Smiling at truecenter with dissolve:
        zoom 1.5

    a "“Sorun yok, anlıyorum. Odalar küçük ve kendini boğulur gibi hissediyorsun.”"

    "Kafamı onaylarcasına salladım. Aynı anda Asha’nın gözleri de manasının izleriyle hafifçe parlamıştı."
    "Zihnimde beklenmedik bir misafirin varlığını hissetmeye başladım."

    show Asha Default with dissolve

    a "“Ama herkesin aksine seni boğan şey korkuların değil. Aksine heyecanlısın, mutlusun.”"

    "Yavaşça alt dudağımı dişledim."

    h "“Vena bu konuda bana çok kızıyor. Ölülere hakaret ettiğimi düşünüyor.”"

    a "“Ben öyle olduğunu düşünmüyorum. Sadece insanlarımızı kaybetmedik, aynı zamanda köklerimizden kopup savrulduk.”"

    show Asha Sideway with dissolve

    a "“Ve kendimizi, en azından sizin için, bilinmeyenin ortasında bulduk.”"
    a "“Zaten herkes her şeye aynı tepkiyi de veremez.”"

    show Asha Smiling with dissolve

    a "“Ama burada Vena’yı da anlamalısın. Waceera onun için çok, çok… Önemliydi.”"
    a "“Onun özellikle böyle sıkıntılı bir vakitte ortadan kaybolması kardeşini yıkıp geçti.”"

    "Kafamı merakla yana eğdim."

    h "“Gerçekten ölmediğini mi düşünüyorsun?”"

    show Asha ClosedEye with dissolve
    pause 2.0
    show Asha Smiling with dissolve

    a "“Ölmediğini umuyorum ve bu konuda kimsenin kasvetli düşüncelerde boğulmasına izin vermemek de benim görevim.”"

    u "“Kasvetli mi? O yüzsüz orospunun ölümünün haberi anca bayram sebebi olur.”"

    "(Ah, Almasi…)"
    "Kendimi istemediğim bir laf ebeliğinin ortasında bulmak üzere olduğumu fark edince yeniden paniklemiştim."
    "Almasi, emin adımlarla bize yaklaşmaktaydı."

    "Yüzünde küçümseyen bir ifade eşliğinde kara gözleri Asha’ya bir hınçla sabitlenmişti."

    hide Asha
    show Asha Default:
        xalign 0.5
        linear 0.5 xpos 0.15
    show Almasi Default at right with dissolve

    al "“Ne o? Ablanın yokluğunda Gece Anne rolüne mi büründün?”"

    "(Şükürler olsun ki Asha sakin bir insan.)"

    a "“Öyle bir niyetim yok Alma. Sadece genç kuzuların kaybolmasına engel olabilecek bir çobanın rolüne büründüm, o kadar.”"

    "Bu sözlerinin ardından manidar bir şekilde bana bakıp gülümsedi."

    show Asha Smiling with dissolve

    "Almasi ise onun sözlerini samimi bulmuş gözükmüyordu."

    show Almasi Frowning with dissolve

    al "“Çoban dediğin rehberdir. Hayvanların boynuna tasma vurup gezdirmezler.”"
    al "“Küçüğüm, sakın bu kadının zihnini zehirlemesine izin verme.”"

    "(O-uh. Beni bu kavganın dışında tutun.)"
    "Ne diyeceğimi bilemediğimden ikisi hariç her yere baktım."

    hide Asha with dissolve
    hide Almasi with dissolve

    "Taraf tutmak istemiyordum."
    "Emindim ki Vena burada olsaydı Asha’ya güzel bir şekilde destek çıkardı fakat ben Almasi’yi agresif bulduğum kadar onu da suçsuz göremiyordum."
    "Birkaç saniyenin ardından Asha elini sakince omzuma koymuştu."

    show Asha Smiling at truecenter with dissolve:
        zoom 1.5

    a "“Haru, kompartımanına dönsen iyi olacak.”"

    show Asha Sideway with dissolve

    a "“Aynı şekilde sen de Almasi.”"

    show Almasi at left with dissolve

    al "“Senden emir aldığımı da nereden çıkardın?”"

    show Asha ClosedEye with dissolve

    "Asha uzunca iç çekmişti."
    "(Onun da sabrının bir sınırı var ne de olsa.)"

    show Asha Default with dissolve

    a "“Bizi bu topraklardan sürebilirlerdi ama yardım etmeyi kabul ettiler, hem de Whemond’da.”"

    show Asha Frowned with dissolve

    a "“Tek istedikleri kurallara uymamız. Usluca oturup birkaç saat tartışma yaratmadan durmak çok mu zor?”"

    show Almasi Frowned with dissolve

    al "“Sen benimle bu tondan konuşamazsın.”"

    show Almasi Angry with dissolve

    al "“Omurgasız ablan, sen ve hiçbir halta yaramayan kız kardeşin ‘topraklardan sürülmemeyi’ bir başarı olarak görebilirsiniz fakat bu benim için bir hakaret.”"

    hide Almasi with dissolve

    "(Bu benim kavgam değil, araya girmek zorunda değilim. Başım ağrısın istemiyorum.)"

    hide Asha
    show Asha Frowned at right with dissolve
    show Almasi Angry at left with dissolve

    al "“Whemond zaten bizim evimiz, bizim topraklarımız. Pertone, Ulu Orman-”"

    show Asha Sighing with dissolve

    a "“Alma, gerçekten yeter.”"

    "İkili arasında çıkan kıvılcımlara daha fazla dayanamayarak araya girdim."

    h "“Ben… Kompartımanıma döneyim en iyisi mi.”"

    show Asha Default with dissolve
    pause 2.0
    hide Almasi with dissolve
    hide Asha with dissolve

    "Asha’nın gözlerinde “zavallıcık” dercesine bir parıltı belirmişti. Hızlı adımlarla aralarından geçip kendi bölmemize doğru ilerledim."

    scene traincorridor with dissolve:
        zoom 2.0
        xalign 0.75
        yalign 0.3
        linear 1 xalign 0.5
    pause 1.0

    al "“Waceera aşığı ablacığına selamlarımı iletmeyi de unutma.”"

    "Artık dedikleri can sıkıyordu. Kapı kulpuna kendisine doğru dönmeden, yorgunca konuştum."

    h "“Yok, teşekkürler. Siz kendi kavgalarınızı kendi konseylerinize saklayabilirsiniz ama.”"

    play sound slidedoor

    scene traincomp with fade
    pause 2.0

    show Kioko Default at left with dissolve
    show Vena Default at right with dissolve

    v "“Dışarıdan gürültüler geliyordu, bir şey mi oldu?”"

    "Şaşırmıştım, normalde böyle bir olayda Vena güçleri aracılığıyla olan bitene hemen kulak kabartırdı."
    "Neyse, bu demek oluyordu ki en azından sinir krizi bir süre daha ertelenmişti."

    h "“Bir sorun yok, klasik tartışmalar işte.”"

    hide Kioko with dissolve
    hide Vena with dissolve

    "Vena önce bir kaşını kaldırdı, ardından omuz silkerek olayın peşini bırakmaya karar verdi."
    "Ben de yolculuğun geri kalanında içine düştüğüm sıkıntılarla dolu çukurun beni derin bir uykuya çekmesine izin verdim."

    scene blackscreen with fade
    pause 1.0

    "Whemond’a varmamız neredeyse gece yarısını bulmuştu."
    "Apar topar Kraliyet Akademisi’ne tıkıldığımız için heyecanım kursağımda kalsa da en azından odamızdan dışarıyı izleyebiliyordum."
    "Aynı zamanda Akademi de daha önce gördüğüm hiçbir yere benzemiyordu."
    "Süslemeleriyle, dekorlarıyla, ormanımızdan o kadar farklıydı ki her şey…"

    scene whemond with fade

    a "“Kızlar, bundan o kadar etkilendiyseniz bir de gün batımını izlemeniz lazım! O zaman güneş sanki kanayarak denize dökülüyormuş gibi bir görüntü oluşuyor.”"
    a "“Şafakları da aynı şekilde, bir kan göletinden çıkıyormuşçasına…”"
    a "“Ama kabul etmem lazım, ben en son buraları göreli her şey çok ama çok değişmiş.”"

    v "“Rezil bir yer burası. Etkilenilecek hiçbir şey yok.”"
    v "“Işığın bu kadar gereksiz kullanılabileceğini düşünmezdim.”"

    "Dediklerine karşı çıkacak halim yoktu. Yorgundum fakat görünen oydu ki Kioko da önünde uzanan manzarayı en az benim kadar sevmişti."

    k "“Bence… Bence ışıklar çok sevimli duruyor.”"

    "Şaşkınlıkla kafamı ondan yana çevirdim. Öyle düşünüyor olsaydı bile Kioko’nun Vena’nın söyledikleriyle ters düşen şeyler dediğini sık sık duyamazdınız."
    "Vena kendince homurdandıysa da konuyu uzatmadı. Asha ise kıkırdıyordu."

    a "“Şehirde gezme fırsatını elbet yakalarsınız sanıyorum ki.”"

    play sound loudthud
    scene whemond
    pause 1.0
    "(!)"
    "Gümbürtü Vena’nın olduğu taraftan geldiği için hepimiz ona dönüp baktık."

    scene academylivingroom with fade
    pause 0.5

    show Vena Irritated with dissolve

    v "“Asha, lütfen kimsenin aklına böyle şeyler sokma.”"
    v "“Ne Haru’nun, ne Kioko’nun, ne de başka birinin.”"

    show Vena Irritated:
        xalign 0.5
        linear 0.5 xpos 0.8
    show Asha Default at left with dissolve

    a "“Ne olacak yahu? Bir günlük şehir gezisi ayarlayabiliriz.”"

    show Vena Angry with dissolve

    v "“Kesinlikle olmaz.”"

    show Vena Frowning with dissolve

    v "“Her zamankinden daha çok kendimize dikkat etmemiz gereken bir dönemdeyiz. Olanlara neyin sebebiyet verdiğini bile bilmiyoruz.”"

    show Vena Angry with dissolve

    v "“Eğer insanlar ölmek istemiyorlarsa asla bu akademiden çıkmamalılar.”"

    show Vena Frowning with dissolve

    v "“Hatta ölmek istiyorlarsa da çıkmamalılar. Bir lider olarak senin en büyük vazifelerinden biri herkesin güvenliğini sağlamak Asha.”"

    show Vena Sideway with dissolve

    v "“Kaldı ki buraya eğlenmeye de gelmedik, ölülerimiz var.”"

    "Ortamda bir sessizlik oluşmuştu, merakla bir Asha’ya bir de Vena’ya bakıyordum."
    "(Eğer ki kavga çıkarsa odama tüyüp uyuyacağım.)"

    show Asha Grinning with dissolve

    "Ama beklenilen tartışma yerine Asha’nın kahkahası odada yankılandı."

    a "“İnanamıyorum. Tıpkı Waceera gibisin…”"

    show Vena Frowning with dissolve

    v "“Gülebilmen ne hoş. Yine de bunun önemli bir konu olduğunu unutma, özellikle Almasi’nin senin her açığını yakalamaya çalıştığını.”"

    show Asha Smiling with dissolve

    a "“Görünen o ki Waceera’ya güvendiğinin yarısı kadar bile bana güvenmiyorsun.”"

    "Vena, cevap vermeden önce gözlerini yumup bir süre bekledi."

    show Vena ClosedEye with dissolve

    v "“Senin iyiliğin için konuşuyorum, bunu kendine bir yarış haline getirmezsen iyi olur.”"

    a "“Getirmiyorum, sadece gözler önünde olan bir doğruyu söyledim.”"

    show Asha ClosedEye with dissolve

    a "“Ah Vena… Dert etmeni gerektirecek bir şey yok, Waceera’yı da bulup Gümüş Oyuk’a geri döneceğiz.”"

    "Gözlerini şöyle bir odada gezdirmiş, kendisine cevap gelmeyince şalını toplayıp ayağa kalkmıştı."

    hide Vena with dissolve
    show Asha ClosedEye with dissolve:
        zoom 1.5

    a "“Sizlere daha da rahatsızlık vermeyeyim. Yataklarınıza dağılın bakalım.”"

    show Kioko Laughing at right with dissolve

    k "“Hala çocukmuşuz gibi davranıyorsun Asha.”"

    show Asha Default:
        xalign 0.2
        linear 1 xpos 0.6

    "Asha elini Kioko’nun kafasına götürüp saçlarını hafifçe karıştırdı."

    a "“Hala çocuksunuz çünkü. Hep öyle kalacaksınız.”"

    pause 1.0
    hide Kioko with dissolve
    hide Asha with dissolve

    play sound doorclose

    "(Çocuk…)"
    "Tıpkı buraya gelmeden önce kaldığımız köydeki çocukların anneleri gibi konuşmuştu."
    "Sanıyorum ki bunun sebebi Asha’nın Gümüş Oyuk’ta değil; burada, Dış Dünya’da büyümüş olmasıydı."
    "Zira “anne” kavramı benim hayatıma Aelthus’a gelmemle girmişti."
    "Bir de ara sıra Zuri’nin Kioko’ya olan hasretli bakışlarına şahit oluyordum, o kadar."
    "(Ah… Benim annem…)"

    scene blackscreen with flash
    pause 2.5
    scene academylivingroom with flash

    "…"
    "Sanki kötü anılar boğazıma takılıp düğüm oluşturmuş misali şiddetle yutkundum."
    "Ardından Vena’ya baktım."

    h "“Öyleyse… Odalarımıza mı dağılıyoruz?”"

    "Bu soruyu yöneltmemin ardından, farkına vardığım bir gerçek hemencecik modumu değiştirmişti."
    "Hayatımda ilk kez kız kardeşlerimden ayrı yatacaktım."
    "(Bu konuda biraz heyecanlı hissetmem beni kötü bir insan yapar mı?)"

    show Vena Default at right with dissolve

    v "“Siz ikiniz gidebilirsiniz. Benim biraz daha işim var.”"

    show Kioko Default at left with dissolve

    k "“Lütfen kendini yorma.”"

    hide Vena with dissolve
    hide Kioko with dissolve

    "Kioko’yu onaylayıp iyi geceler diledikten sonra odama çekildim."

    scene academybedroom with fade
    pause 2.0
    scene academybedroom with dissolve:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    play sound sitting

    "Ne kadar yorulduğumu ancak yatağımın üzerine oturunca fark etmiştim."
    "Yine de uykunun tatlı sesi bile beni camdan ötesini izlemekten alıkoyamıyordu."

    scene whemond with fade

    "(Whemond…)"
    "(Hazır Vena da yokken istediğim kadar bakabilirim.)"
    "Küçük bir çocuk edasıyla pencere pervazına kollarımı yaslayıp hayal kurmaya koyuldum."
    "Şehir acaba sabah ışıklarıyla nasıl gözüküyordu? Ya kutlama yaparken etrafı çiçeklerle, çelenklerle çevreliyorlardıysa?"
    "Herhangi bir festivali görebilecek kadar kalır mıydık? Dışarı çıkmamıza ne zaman izin verirlerdi? Sokaklarda koşuşturmayı, insanlarla tanışmayı o kadar çok istiyordum ki!"
    "Tabii bir de “güneşin kanama” durumu vardı."
    "Yorgun olmasaydım şafağı bekler, insanların anlattığı kadar muazzam bir manzara var mı yok mu kendim bir bakardım."

    scene academybedroom with fade:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "(Fakat şimdi uyumam lazım.)"
    "(Ne de olsa yarın yoğun bir gün.)"

    scene blackscreen with fade
    pause 3.0

    scene academyclass with fade
    show Vena ClosedEye with dissolve:
        xpos 0.3 ypos 1

    play sound commotion
    pause 4.0
    stop sound

    v "“Son kez söylüyorum. Bu konunun peşini bırak.”"

    h "“Sadece merakımdan soruyorum, merakımdan!”"

    hide Vena with dissolve

    "Sanki benden kaçmak istiyormuş gibi adımlarını sıklaştırmıştı."
    # Slow screen shake gelecek.
    "Koşarak yanına varıp kolundan tuttum."

    play sound sitting

    h "“Vena!”"

    show Vena Sideway with dissolve

    "Tekrardan ilgisini üzerime çekebilmiştim."
    "Düşünceli bir hali vardı."
    "Kafasından artık her ne geçiyorduysa en sonunda derin bir nefes vererek pes etti."

    show Vena ClosedEye with dissolve:
        ypos 1.5 zoom 1.5

    v "“Haru, dinle.”"

    "İki elimi de sıkıca kavrayıp kalbinin üstüne götürmüştü."
    "Uzun zamandır ikimiz ne zaman bir araya gelsek tartıştığımız için bu sıcaklığa ne kadar ihtiyacım olduğunu ancak o an fark edebildim."

    show Vena Concerned with dissolve

    "Fakat Vena’nın gözlerinde beklediğim gibi bir sevgi yerine endişe görülüyordu."

    v "“Eğer sana seni anlayabildiğimi söylersem bu yalan olur.”"

    show Vena Sideway with dissolve

    v "“Şu anki ruh halini hiçbir şekilde anlayamıyorum.”"
    v "“Kafanın içinde kıyametler kopuyor da göstermiyor musun veya orası güneşli bir gündeki deniz kadar sakin mi… Bilemiyorum Haru.”"

    show Vena Sighing with dissolve

    v "“Ama kendini de bizi de zor bir duruma sokmamalısın.”"

    "Derin bir iç çekip ellerimi Vena’nınkilerden yavaşça kurtardım."

    show Vena Default with dissolve:
        xpos 0.4 ypos 1.0 zoom 1.0

    v "“‘Sihir teknolojisi’ dedikleri şey ne kadar gelişmiş bilmiyoruz.”"
    v "“Fakat senin sihrinin ne kadar komplikeden uzak, basit olduğunu düşünürsek yakalanma olasılığının çok yüksek olduğunu söyleyebilirim.”"
    v "“O yüzden böyle bir şeye sakın kalkışma.”"

    hide Vena with dissolve

    play sound walking

    "Diyeceklerini daha fazla dinlemek istemiyordum."

    v "“Haru, beni duydun mu?”"

    h "“Evet, evet…”"

    "Hemen dibimdeydi zaten. Duymamak mümkün olamazdı."

    stop sound

    scene academyclass:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.0

    play sound sitting

    "Bir grup insanı kibarca ittirip kendime amfide oturacak bir yer buldum. Vena da gelip yanıma oturmuştu."
    "Bugün yanımızda, tıpkı çoğu zaman gibi, Kioko yoktu."
    "Eskiden böyle toplantılara katılmasına Waceera izin vermezdi, bugünse yorgun olduğundan ötürü dinlenmek istemişti."
    "(Keşke ben de bu şekilde kaytarabilsem.)"

    "Vena olan biteni kaydedip Kioko’ya göstermek için yanında bir hatıra taşı getirmişti."

    "Ama ben, tanıdığım Kioko’nun kibarlık gereği taşı alacağını ve asla dinlemeyeceğinden emindim."
    "Ki ben bile tahmin edebiliyorduysam Vena’nın şüphesiz bunu düşünmüş olması gerekiyordu."

    scene academyclass
    play sound doorclose

    show Zuri Default at left with dissolve
    show Asha Default at right with dissolve

    "O anki düşüncelerim Asha’nın kız kardeşiyle salona girişiyle son bulmuştu."

    hide Zuri with dissolve

    show Asha Default:
        xalign 0.8
        linear 0.5 xpos 0.6

    "Asha podyuma çıkıp sınıfı şöyle bir süzmüş, Zuri ise ön koltuklardan birine yerleşmişti."

    a "“Ah, güzel… Hepiniz buradasınız sanıyorum ki- bir kişi hariç.”"

    "Bizden yöne manidar bir bakış attı."

    show Asha Sideway with dissolve:
        ypos 1.5 zoom 1.5

    a "“O da sıkıntı değil.”"
    a "“Sizlere söz vermiştim Whemond’a varır varmaz sorularınızı cevaplayacağıma dair.”"

    show Asha Default with dissolve

    a "“O sözü tutmak için şimdi önünüzdeyim ve bütün-”"

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    al "“İşe ablanın neden ölü olabileceğini düşündüğünü anlatarak başlayabilirsin.”"

    "Vena, Almasi’nin yaptığı saygısızlığa Asha’dan daha çok sinirlenmiş gibi görünüyordu."
    "Salonda tamamıyla bir sessizlik olmuş, herkes Asha’nın diyeceklerine kulak kesilmişti."

    hide kiokoeye with dissolve

    show Asha Sighing with dissolve
    pause 2.0
    show Asha Default with dissolve

    a "“Sanıyorum ki yalan söylemenin bir manası yok.”"
    a "“Waceera, ben ve Zuri’nin çemberi sizinkine kıyasla daha genişti.”"

    play sound commotion

    "Açıkçası son bir, bir buçuk aydır başımıza gelenlerden ötürü buna şaşıramamıştım."
    "Artık böyle skandallar bile o kadar normal bir mertebeye ulaşmıştı ki gözümde…"

    stop sound

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    al "“Yani bizleri birer zombi misali yaşamaya iteklediğinizi ve bu sırada sizin sefa sürdüğünüzü kendi ağzınla kabul ediyorsun.”"

    show Asha ClosedEye with dissolve

    a "“…”"

    show Asha Default with dissolve

    a "“Kendi durumumuzu ‘sefa çekmek’ olarak tabir edebilir miyiz emin değilim.”"

    show Asha ClosedEye with dissolve

    "“Bu karar bizzat Waceera tarafından verilmişti. Yaşam sürelerimizi uzatmak namına…”"

    al "“Saçmalık!”"

    show Asha Default with dissolve

    a "“Ben bu toplantıda sizlere sadece gerçekleri söylemekle yükümlüyüm.”"

    show Asha Frowning with dissolve

    a "“Waceera’nın bir şeyleri neden yaptığı yahut bir art niyet güdüp gütmediği ona sorabileceğiniz şeyler.”"

    show Asha ClosedEye with dissolve

    a "“Bana ne kadar kızsanız da sinirlenseniz de verebilecek başka bir cevabım ne yazık ki yok.”"

    show Asha Sideway with dissolve:
        ypos 1.0 zoom 1.0

    a "“O yüzden asiliğinizi Waceera’nın dönüşüne saklamanızı öneririm.”"

    hide kiokoeye with dissolve
    hide Asha with dissolve

    "Normalde, yani bizim durumumuzda, bireysel kimliklerimiz çember büyüsüyle harmanlanır ve ortaya daha kolektif bir birim çıkarırdı."
    "Bu durum insanlarımız arasında geçmişten beri hep kardeşlerin birbirilerinin hislerini, düşüncelerini okumalarına; beraber yapılan büyülerin ortak bir manayla çok daha güçlü hale gelmesine yaramıştır."
    "Kötü bir yan etki olarak ise içimizden biri yaralanınca hepimiz yaralanıyor…"
    "…Birimiz ölünce ise hepimiz ölüyorduk."
    "Kara Katliam’ın ardından kaçarken Waceera’nın ortalarda olmadığını görünceyse çemberinin diğer iki üyesinin hala hayatta olduğunu bilmek bizler için bir güvence olmuştu."
    "Ve Asha bir sabah Waceera’nın ölü olabileceği olasılığından bahsedene dek de bu böyleydi."
    "Derin bir nefes alıp başımı ellerimin arasına koydum."

    play sound commotion

    "Almasi car car bağırmaya devam ediyor, diğerleri de dediklerini onaylayarak adeta bir kaos orkestrası düzenliyorlardı."
    "Bunu dinlemek istemiyordum. Hatta direkt reddediyordum. Olan olmuştu, üzerine saatlerce konuşmanın ne anlamı vardı?"
    "Dikkatim konuşmacıları tamamen bırakıp odanın detaylarına yoğunlaşmıştı."

    stop sound

    scene academyclass:
        xpos 0.5 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Bu sıralarda öğrenciler eğitim görüyor olmalıydı."
    "Gümüş Oyuk’tayken derslerden nefret ederdim fakat buradaki atmosfer insanı çalışmaya bile isteklendirebilirdi."
    "Parmağımı yavaşça ahşabın üzerinde gezdirdim. Yer yer çeşit çeşit harfler kazınmış, anlayamadığım formüller ve tablolar çizilmişti."
    "Kafamı kaldırıp tekrardan sınıfa baktığımdaysa kapı eşiğinde duran tanımadığım bir figür dikkatimi çekmişti."

    scene academyclass:
        zoom 1.0

    show Ealdwine Sideway at right with dissolve

    "Kendisini daha önce hiç görmemiştim, bizden birisi değildi."
    "Dirseğimle hafifçe Vena’nın kolunu dürttüm."

    h "“Vena, kapının oradaki kişi kim?”"

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“Ben de bilmiyorum ama üstündekilere bakılırsa sanırım Akademi’nin bir üyesi.”"

    hide kiokoeye with dissolve

    "Ah, Asha buraya varmadan önce Aelthus Krallığı tarafından denetim altında bulunacağımızı söylemişti."
    "O yüzden bu kişinin bizim sıkıcı sorunlarımızı kendi isteğiyle dinlemesindense görevinden ötürü burada olması bana daha mantıklı gelmişti."
    "Yumuşak hatları bir çocuğunkini andırmaktaydı. Saçları da pamuk gibi bembeyazdı, yumuşacık görünüyordu."
    "{i}İlginç{/i}, insanı çeken bir güzelliği vardı bu kişinin."
    "Fakat aklım bir konuda karışmıyor değildi."

    h "“Vena…”"

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“Hmm?”"

    h "“O kişi… Sence kız mı erkek mi?”"

    hide kiokoeye with dissolve

    "Gümüş Oyuk’ta sadece “kadın” nüfusu olduğu için “erkek”ler hayatıma Aelthus ile birlikte girmiş bir başka kavramdı."
    "Birçoğu kadınlardan daha uzundu. Sesleri daha kalındı."
    "Göğüsleri yontulmuş bir mermer gibi düz, bazılarının boyları ise kavak ağaçlarıyla yarışacak kadar uzundu."
    "Çeneleri sertti, yüzleri köşeliydi."
    "Her biri dağları, devleri tepip devirmeye hazır görünüyordu. Aslında güçsüz olsalar bile kendilerini böyle hissediyor gibilerdi."
    "Bu, kapıda duran genç ise ne erkeksi ne de kadınsıydı. Sanki ikisi arası bir yerde takılmıştı."
    "Vena bir süre o kişiye bakıp, sonra konuştu."

    show kiokoeye at left with easeinleft:
        ypos 0.4 zoom 0.5

    v "“Ben de bilemedim.”"

    "Sesi düşünceli çıkmıştı. Vena’nın bile ikileyeceği şeylerle karşılaşmak çok komikti."

    v "“Herhalde erkek.”"

    h "“Galiba.”"

    hide kiokoeye with dissolve

    "Gözlerim tekrardan çocuğun üzerinde gezinmeye başladı. Bir elimi çeneme dayayarak kendisini izlemeye koyuldum."
    "Kız da olsa erkek de olsa çok sevimli görünüyordu."

    show Ealdwine Surprised with dissolve

    "Fakat bir süre sonra çocuk kafasını benden yana kaldırmış, gözlerimiz buluşmuştu."

    hide Ealdwine with dissolve

    scene academyclass with hpunch

    "Yakalanmanın paniğiyle oturuşumu düzeltmeye ve bakışlarımı kaçırmaya çalışmış, bu süreçte yanlışlıkla Vena’nın taşını masadan ittirivermiştim."
    "Lakin reflekslerim sayesinde taş düşüşe geçmeden bir rüzgar büyüsü yardımıyla onu havada yakalamış, ardından kendi avucuma getirmiştim."

    v "“Dikkat et Haru.”"

    h "“Özür dilerim.”"

    show Ealdwine Grinning with dissolve

    "Kafamı kaldırıp kapıya baktığımda çocuğun bana bakarak güldüğünü gördüm."
    "(…Ne utanç verici.)"

    scene sundown with fade

    "Toplantı bittikten sonra Akademi içerisinde verilen çeşitli görevleri yerine getirmiştik."
    "(O kutuyu aç, bu erzağı say, sor bakalım eksik bir ihtiyacı olan var mı, herkes mutlu mu falan filan işte.)"
    "İş güneşin batışını izlemeye gelinceyse, elimde ne var ne yok umursamadan bırakıp pencerenin kenarına konuşlanmıştım."

    play sound seagull

    "(E hani? Battı batacak neredeyse! Sakın demeyin bana kanlı gökyüzünden kastınızın bu olduğunu.)"

    scene blackscreen with fade

    "Ben hayıflanırken güneş denize iyice yaklaşmış ve semanın renkleri bir anda değişivermişti."

    scene sundown with fade

    "(Ooh…)"
    "(Vay…)"

    h "“Kıpkırmızı oldu cidden de!”"

    "Şaşkınlığımı gizleyemeyip kendi kendime söylenmiştim."
    "Gökyüzünün değişimine mi, denizin kıpkırmızı oluşuna mı yoksa güneşin gerçekten de kanar gibi gözükmesine mi daha çok hayret etmeliydim bilemiyordum."
    "Ve bu sahne, buradaki insanların normaliydi. Her gün iki kez onları bu görüntü bekliyordu."

    h "“Hah…”"
    stop sound

    "(Böyle bir şey nasıl “normal” olabilirdi?)"
    "Elimi kaldırıp ileri doğru uzattım. Güneş ışınları tenime temas ediyor ve vücudumda hiç hissetmediğim kadar güç topluyordu."
    "Böyle bir yerde yaşamak demek, bir insanın asla manasının bitmemesi demekti."
    "Havada resmen sihir vardı."
    "Buna rağmen ayaklarımın altındaki bu şehrin insanları, duyduklarıma göre büyüye bir o kadar uzaktı."
    "(Ne ironik…) Derin bir iç çekip işlerime dönmeden önce manzaraya bir daha baktım."
    "Şimdiden buradan ayrılırsak yaşayacağım buruk acıyı düşünüyor, kendi kendimi üzüyordum."

    scene academylivingroom with fade
    pause 1.5
    show Kioko Default at left with dissolve
    show Vena Default at right with dissolve

    v "“…Benim anlatacaklarım bu kadar. Geri kalanını anı taşından izleyebilirsin.”"

    k "“Teşekkürler Vena.”"

    hide Kioko with dissolve
    hide Vena with dissolve

    "Birlikte Asha’nın dağıttığı yemeklerden yiyorduk. İçten içe günün bu kadar yorucu geçmesinden ötürü şikayetleniyordum."
    "(Kioko çok şanslı… Bütün gün rahat rahat odasında yatabildi. Kimse de ona bir şey demiyor!)"
    "En azından yakında yerleşme işlerimiz bitecekti."
    "O zaman geriye kalan problemlerin birçoğunu çözmek Işık Hamillerinin omuzlarına düşecekti."
    "(Belki bu bana sıvışma şansı verirdi.)"
    "Gerçekten aylarca buraya kısılıp kalmak istemiyordum."

    show Kioko ClosedEye at left with dissolve

    k "“Bir şey… Diyeceğim.”"
    k "“Fakat lütfen paniklemeyin.”"

    "Vena tabağını bir kenara koyup kulak kesilmişti."
    "Benimse çatalım Kioko’ya meraklı bir şekilde bakarken havada kalmıştı."

    k "“…”"

    "(Güzel, şimdiden panikledik.)"
    "Tam da kaytarabilirim diyordum oysaki."

    show Kioko Sideway with dissolve

    k "“Sanırım ben… Bugün odamda birini gördüm.”"

    "Şaşkınlıkla bakakalmıştım."

    h "“Ne?”"

    show Vena Frowning at right with dissolve

    v "“Kimi?”"

    show Kioko Concerned with dissolve

    k "“B-Bilmiyorum ki.”"
    k "“Rüya da olabilir, tam emin değilim.”"

    "Ne zaman sıkıntıya girse yaptığı gibi tırnağını yemeye başlamıştı."
    "Vena öne doğru eğilip nazikçe elini ağzından çekti."

    show Vena Default with dissolve

    v "“Kioko, sakin ol.”"

    k "“Yeni uyanmıştım. Sonra odamda biri olduğunu fark ettim. Cam kenarında duruyordu.”"

    show Vena Arched with dissolve

    h "“Nasıl biriydi? Arkadaşlarından biri olmasın?”"

    show Kioko Protesting with dissolve

    k "“Hayır! Hayır… Öyle bir arkadaşım yok benim.”"

    show Kioko ClosedEye with dissolve

    k "“Turuncu saçları vardı. Yüzünü tam göremedim ama, uykuluydum.”"

    "Ellerini kollarını kontrol edemiyor, konuşurken bir sürü jest kullanıyordu."

    show Kioko Concerned with dissolve

    k "“Yanıma geldi sonra. Çok korktum, hareket edemedim, ardından öylece uyuyakaldım!”"

    "Vena tekrardan ona doğru uzanıp parmaklarını şakağına yerleştirdi."
    "(Ah, anılarını izleyecek.)"

    v "“Müsaadenle bir de ben bir bakacağım.”"

    show Kioko ClosedEye with dissolve

    "Kioko onaylarcasına kafasını sallayıp kendisini hazırladı."

    hide Vena with dissolve
    hide Kioko with dissolve

    "Ardından Vena’nın gözlerinden de parmak uçlarından da çıkan mavi, cılız bir ışık büyünün başladığını göstererek odaya yayılmıştı."
    "Zihne dair büyüler Vena’nın uzmanlık alanıydı."
    "Normalde uzun bir odak ve çokça mana gerektiren bu büyülerin Vena için nefes almak kadar kolay olmasına hep hayret etmişimdir."
    "(Özenmek… O ayrı bir konu şimdi.)"
    "Özenmiyordum çünkü “Psişik alanında uzmanlaşmayı tercih edenler kendilerine büyük tehlikeleri de davet etmiş olurlar.” derdi Asha."
    "Bu kolay bir zanaat değildi."
    "İnsan kendisini çok kaptırırsa gerçeklikten kolayca kopabilirdi."
    "Vena’nın, kontrol bağımlısı olduğunu göz önünde bulundurursak, bu seviyeye geleceğini hiç düşünmüyordum."
    "Ama o bile ara sıra elinde olmadan başkalarının rüyalarını gasp ediyordu."
    "Belki de bu kadar sinirli olmasının sebebi başkalarının düşüncelerinin, ruh hallerinin sürekli kendisini dürtüklemesiydi."
    "Aradan çok geçmeden Vena kendini geri çekip Kioko ile arasına mesafe koymuştu."
    "Merakla ikisine baktım."

    show Kioko Default at left with dissolve
    show Vena Sideway at right with dissolve

    v "“Ya gelen her kimdiyse anılarını bulutlamış ya da gerçekten rüya görmüşsün.”"

    h "“Ayırt edemiyor musun, Vena?”"

    show Vena Default with dissolve

    "Bu bir ilk olabilirdi."
    "(Veya iki… Gümüş Oyuk’ta Kioko’nun başına gelenleri de sayarsak…)"
    "Kafasını {i}hayır{/i} anlamında sallamıştı."

    h "“Bu akademiden bir kimse olabilir mi?”"

    show Vena Frowning with dissolve

    v "“Sanmam. Üniforma giymiyordu, bizden birine de benzemiyordu. Kioko, bize neden daha önceden haber vermedin?”"

    show Kioko ClosedEye with dissolve

    k "“Gereksiz panik yaratmak istememiştim.”"

    show Vena Concerned with dissolve

    "Vena hızlıca Kioko’nun elini kavradı."

    v "“Sakın böyle şeyler düşünme. Çalkantılı bir dönemdeyiz o yüzden şüpheli görünen her şeyi bize söylemelisin.”"

    "Bir süre sessizlik olmuştu."

    h "“Çok garip gerçekten… Ne yapacağız?”"

    show Vena Sideway with dissolve

    v "“Ben…”"

    "Vena derin bir iç çekti."

    show Vena Default with dissolve

    v "“Kioko, benim odamda yatmak ister misin?”"

    show Kioko Gaping with dissolve

    k "“Sana yük olmayı istemem.”"

    show Vena Frowning with dissolve

    v "“Lütfen saçma şeyler söyleme, sen benim kardeşimsin.”"

    show Kioko Concerned with dissolve

    k "“Ama işine engel olmaz mıyım?”"

    show Vena ClosedEye with dissolve

    v "“Hayır, önceliğim sizsiniz.”"

    hide Kioko with dissolve
    hide Vena with dissolve

    "Sanırım bu noktada araya girip Kioko’nun sorumluluğunu benim üstleneceğimi söylemem en doğru seçenek olurdu."
    "Böylece Vena bir Işık Hamili olarak görevlerini yerine getirebilecek, aynı zamanda da gözü arkada kalmayacaktı."
    "Ama ben…"
    "(Hah…)"
    "Kioko’ya bakmak öyle kolay bir iş değildi."
    "Kara Katliam’ın sır perdesini aralayabilecek belki de tek kişiydi."
    "Şimdilik Asha’nın kehanetinden ve Kioko’nun itirafından sadece ben, Vena, Asha ve muhtemelen Zuri haberdardık."
    "Ya bir başka insan, diyelim ki Kara Katliam’a sebep olan kişi yahut şey Kioko’nun peşine düşmüştüyse? Ben onu olası bir acil durumda nasıl savunabilirdim?"
    "Bütün bu bahaneleri bir kenara bırakırdıysam da…"
    "Hayatımda ilk kez tek başıma kalacak olmanın, tek özgürlük şansımın ellerimden öylece alınmasını istemiyordum."
    "Belki de bunu kabul etmek utanç vericiydi lakin istemiyordum işte."
    "O yüzden, en nihayetinde ses çıkarmamaya karar verdim."

    show Vena Default with dissolve:
        xpos 0.3

    v "“Öyleyse Asha’ya Işık Hamilleri için düzenlenen toplantıya gidemeyeceğimi bildirmem lazım.”"

    "Yutkundum ve kafamı eğip ellerime baktım."
    "(Suçlu hissetme, suçlu hissetme.)"

    scene academybedroom with fade
    pause 2.0
    scene academybedroom with dissolve:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Oturma odasında bir süre daha vakit geçirdikten sonra odalarımıza ayrılmıştık."
    "Of… Ne yorucu bir gün olmuştu ama!"
    "En nihayetinde kendimle baş başa kalabilmiştim."
    "Bir süredir cam kenarına kurulmuş, olan biteni değerlendirirken altımda nefes alan şehri izliyordum."

    scene whemond with fade

    "Saat gece yarısını geçeli çok olmuştu. Benimse gözüme uyku girmiyordu."
    "Akşam boyunca insanlar vızır vızır sokaklarda dolanmış, rüzgar kulaklarıma kah ayyaşların kahkahalarını kah gecenin karanlık örtüsüne güvenilip söylenen sırları taşımıştı."
    "Ardından dükkanların ışıkları bir bir sönmüş, insanlardan birçoğu evlerine dönmüştü."

    scene academybedroom with fade:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Ne kadar çok eğleniyor olmalılardı."
    "Stresten, zincirlerden, olağanüstü durumlardan uzak; özgür bir hayat…"
    "Ne güzel olmalıydı insanın istediği zaman istediğini yapabilmesi."
    "Sıkıntılarım nefes almamı güçleştirirken dudaklarımı birbirine gergince bastırdım."
    "Bir taraftan bir elimle pencere pervazını kavramış ve zavallı tahtayı eklemlerim beyazlayana kadar sıkmıştım."
    "Ben de bu hayatı, bu özgürlüğü istiyordum. Ne vardı hazır Gümüş Oyuk yok olmuşken de buraya yerleşiverseydik, insanlarla kaynaşıverseydik? Ne olurdu?"
    "(Böyle düşünmemelisin, böyle düşünmemelisin.)"
    "Yatağımda doğrulup pencereye tırmandım, ardından pervaza oturdum."
    "Bu sırada aklımda Vena’yla sabah gerçekleştirdiğim konuşma vardı."

    scene academyclass with flash
    show Vena Default with dissolve

    h "“Sanırım buradan çıkmamıza izin vermezler, hm Vena?”"

    v "“Daha çok dönüş günümüze dek tutsaklarıyız diyebiliriz.”"

    show Vena ClosedEye with dissolve

    v "“Tabii gitmemize izin verirlerse…”"

    show Vena Default with dissolve

    h "“Bizi burada istemiyorlarsa neden vermesinler ki? Boşuna endişeleniyorsun bence.”"
    h "“Acaba gizlice dışarı çıkabilir miyiz?”"

    show Vena Frowning with dissolve

    v "“…”"

    hide Vena with dissolve

    scene academybedroom with flash:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Son sorumun ardından tartışmıştık."
    "Dışarıda en fazla ne olabilirdi ki? Bir sürü insanın, muhafızın gözü önünde herhalde bana saldırmazlardı."
    "Öte yandan başıma bir şey gelmesi durumunda yardım istersem Akademi’den izinsiz çıktığım da belli olacaktı."

    scene academyclass with flash

    show Vena Sighing with dissolve:
        xpos 0.3 zoom 1.5

    v "“Ama kendini de bizi de zor bir duruma sokmamalısın.”"

    scene academybedroom with flash:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Gergince alt dudağımı dişledim."
    "Vena ve Kioko şu an uyuyor olmalıydı, yani şehri görmek istiyorduysam bundan daha uygun bir an yoktu."
    "Fakat dışarı çıkmak…"
    "Gözlerimi kısıp şehre doğru baktım."

    scene whemond with fade

    "Akademi’nin etrafında bir sihir kalkanı vardı."
    "{i}Komik{/i}… Muhtemelen burası için usta işi sayılacak bu bariyeri benim, yani derslerinde pek de parlak olmayan bir öğrencinin dahi görmesi aslında kalitesi hakkında çok şey söylüyordu."
    "Yine de bu, kalkanı uçarak geçemezsiniz demekti."
    "Sanıyordum ki ışınlanmaları saptamak için Akademi’nin içinde de çeşitli efsunlar vardı."
    "Yani Vena’ya göre benim herhangi bir kaçma denememde yakalanmamam imkansızdı."
    "Dudaklarım bu düşünce karşısında yavaşça yukarı kıvrılmıştı."
    "Kimseye yakalanmadan kaç kez Gümüş Oyuk’tayken dışarı çıktığımı bilseydi ne kadar da şaşırırdı. Kendi yöntemim sayesinde buradan da sıvışabileceğimi biliyordum."
    "Öteki taraftan da bir problem çıkar da başım belaya girer, Vena’yla tartışırız diye dertleniyordum."

    menu:
        "(…)"

        "Dışarı çıkmak istiyorum.":
            jump outside

        "Belki de içeride kalmalıyım.":
            jump inside


label outside:

    "(Bir kerecik… Sanıyorum ki bir kerecik dışarı çıkmaktan bir şey olmaz. Hemencecik geri gelirim hem, aynı zamanda bu konuda daha fazla kafa da ütülemem.)"
    "Elimi ileriye doğru uzattım."
    "Rüzgar avucumun içine toplanmaya başlamış, ardından parmaklarım yavaşça toz bulutlarına dönüşerek havaya karışmıştı."
    "Bunu ellerim, ayaklarım, kollarım, bacaklarım ve en sonunda bütün vücudum sırayla izledi. Ve ben en sonunda rüzgarla bir oldum."

    scene sundown with fade

    "(Her seferinde ilk kez yapıyormuşum gibi hissettiriyor.)"
    "Her defasında beni bağlayan hayali zincirlerden kurtulmuş gibi hissediyordum."
    "İçim içime sığmayarak yükseldim de yükseldim, sihir bariyerini hiçbir sorun yaşamadan geçtim, ardından şehrin üzerinde diğer rüzgar bulutlarıyla dans etmeye başladım."
    "Bu yeteneğimi çok küçük yaşlarda keşfetmiştim. Bildiğim kadarıyla köyde bunu benden başka yapabilen bir kız da yoktu."
    "Ve bundan haberi olan arkadaşlarım da zaten-"
    pause 2.0
    "Hayır, yersiz düşüncelere dalmanın vakti değildi."
    "Daha önemli bir görevim vardı: En azından bu geceyi eğlenerek geçirebilmek."

    scene whemond with fade

    "Dönüp tekrardan şehre baktım. Akademi’den oldukça uzaklaşmıştım şimdi."
    "Hayatımda ilk kez böyle koca binalar, döşeli yollar, uçan ya da hareket eden araçlar, hatta deniz görüyordum ben."

    scene whemond with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    "83 yılımı bir ormanda, ağaç kulübelerde, aynı insanlarla aynı havayı soluyarak ve gri renkli bir gölde yıkanarak geçirmiştim."
    "Güneş bile doğmazdı, sabah akşam gök aynı renkti."
    "Dış Dünya’ya karşı heyecanlanmamak benim gibi bir insan için nasıl mümkün olabilirdi?"

    scene whemond with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.0

    "(Tamam, pekala. Yakalanmamayı başardığıma göre şimdi nereye insem acaba?)"
    "Herhalde gözlerden ırak bir yere inmek en iyisiydi."
    "Öte yandan bu yer şehir merkezinden de çok uzak olmamalıydı."

    scene whemond with dissolve:
        xpos 0.8 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Yüksek binaların süslediği bir arka sokağa gözümü diktim. Koca koca evler vardı bu bölgede. Gezmek, görmek istediğim ışıklı alanlara da çok uzak sayılmazdı."
    "Yere inmeye koyuldum."

    scene whemond with dissolve:
        xpos 0.8 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 2.5

    pause 1.0
    scene alleyway with fade

    "Kimsecikler yok gibi görünüyordu. Yere iyice yaklaştım."
    "Önce parmak uçlarım, ardından tüm vücudum tekrardan insan formunu almıştı."
    "(Hehehe… Buraya kadar hiçbir sorun yaşamadım, süper!)"
    "Şimdi, o rengarenk ışıklar ne tarafta kalıyordu-"
    "{i}…Huh?{/i}"
    "Duyduğum bir grup insan sesiyle paniklemiş, hemen kukuletamı gözlerimi kapatacak şekilde yüzüme geçirmiştim."
    "Eğer biri beni görürse sakin olmalı, üzerime şüphe çekmemeliydim."

    play sound walking

    "Ağır adımlarla yürürken bir taraftan da rüzgarın kulağıma konuşmaları taşımasına izin verdim."

    stop sound

    bks "“Xerxes, bu saatte buraya gelmemeliydin.”"

    x "“Nişanlımı özleyemez miyim?”"
    x "“Lea… Sana o kadar aşığım ki seni görmediğim her gece bana ıstırap gibi geliyor.”"

    "(Aha! Ne kadar ilginç, ne kadar ilginç!)"
    "Yolumu az önce kaçtığım insanlara doğru çevirmiştim. Aşk, romantizm, bunlar hep bana ve diğer Gümüş Oyuk sakinlerine uzak hislerdi. O yüzden merakım körüklenmişti."
    "Şöyle ucundan bir bakıp, geri dönecektim."

    play sound walking

    scene alleyway with dissolve:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    pause 1.5
    stop sound

    "Sesler demir korkuluklarla çevrili koca bir bahçeden geliyordu."
    "Fakat beni daha da şaşırtan şey çitlerin önünde yere çökmüş bir figür görmek oldu. Anlaşılan o da konuşanları izliyordu."

    show Cyril HoodDefault with dissolve

    "(İşte, ben garip bir insan değilim. Başkaları da izliyor!)"

    hide Cyril with dissolve

    "Olabildiğince sessiz bir şekilde arkadan yaklaştım. İsmi Xerxes olan adam ve diğer kadın bahçenin ortasında birbirlerine sarılmaktaydılar."
    "Önümdeki çocukla yorumlarımı paylaşmanın iyi bir fikir olduğunu düşünerek eğildim."

    h "“Çok güzel değil mi? Hayatımda ilk kez böyle bir şeye şahit oluyorum-”"

    scene alleyway with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    play sound sitting

    "Fakat o an kukuletalı figür ayaklanmış ve-"

    scene alleyway with vpunch:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.5

    show Cyril HoodSword with dissolve

    "Kılıcını bana doğru savurmuştu!"
    "Yeterince hızlı olmasaydım deşip geçecekti neredeyse."
    "(Ne yapmalıyım? Büyü mü yapmalıyım?)"

    show Cyril HoodDefault with dissolve
    pause 1.0
    show Cyril HoodDefault with dissolve:
        ypos 1.5 zoom 1.5
    pause 0.5
    hide Cyril

    "Fakat benim daha karar vermeme kalmadan çocuk üzerime atılmış, eliyle ağzımı kapatıp beni sokağın öteki tarafına sürüklemeye başlamıştı."

    scene alleyway with dissolve:
        zoom 1.0

    "Arkamızdan az önceki kişinin bağırdığını duydum."

    x "“Kim var orada?!”"

    "(Ben! Lütfen yardım et!)"
    "Ne kadar silkelensem de, çırpınsam da çocuğun ellerinden bir türlü sıyrılamıyordum."
    "(Çok güzel Haru… Yere indiğin gibi başını derde soktun.)"
    "Sonuçlarına katlanacaktım artık."

    pause 3.0
    return

label inside:

    scene academybedroom with fade:
        xpos 0.5 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    play sound sitting

    "Camın kenarından ağır hareketlerle geri çekildim."
    "Belki de bu kötü bir fikirdi. Aşağıya inmesi, geri gelmesi kolaydı."
    "Ama ya aşağıdayken ters bir şeyler olsaydı?"
    "Ya da Vena yokluğumu fark etseydi? O zaman ne olacaktı?"
    "En kötüsü de bizimkilerle Aelthus arasında diplomatik bir sıkıntının benim yüzümden çıkması olurdu."
    "O zaman Vena sonsuza dek konuşurdu. O zaman onu asla susturamazdım."
    "Ve sonsuza kadar burada tıkılı kalırdım."
    "Hayallerime veda edercesine camı kapattım."

    scene academybedroom with dissolve:
        zoom 1.0

    "(Olsun, Asha bizi dışarı götürmeyi düşündüğünü söylemişti sonuçta.)"
    "Hem ben de Vena’ya baskı yapar dururdum. En sonunda başı ağrır, “Hayır.” diyemezdi."
    "Ayrıca kendi başıma buyruk davranmaktansa böylesi daha uygun geliyordu kulağa."
    "(Yine de…)"
    "Yatağımdan kalktım ve salona çıktım. Uykum yoktu."

    scene academylivingroom with fade

    "Kioko ve Vena tahmin ettiğim gibi odalarına çekilmişlerdi. Kapılarının altından da ışık gelmiyordu."
    "(Acaba başka uyanık olan var mıdır Akademi’de?)"

    scene academylivingroom with dissolve:
        xpos 0.7 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    "Rafların olduğu kısma doğru yürüdüm. Gözlerim kavanozları inceliyor lakin aklım başka yerlerde cirit atıyordu."
    "Normalde Akademi’deki her ortak odaya altı oda, haliyle de on iki yatak düşmekteydi."
    "Fakat Vena, Asha’ya yakın olmasının ayrıcalığını kullanıp bir ortak odayı tamamıyla kendimize ayırtmayı başarmıştı."
    "Bu durum insanlar arasında şikayetler yükseltmemiş değildi tabii."
    "(…Ama yalnız kalabildiğimiz için mutlu olduğumu itiraf etmem lazım.)"
    "Böylece olan biten bana her dakika hatırlatılmıyordu; kendimle, hayallerimle baş başa kalabiliyordum."

    scene academylivingroom with dissolve:
        zoom 1.0

    "Vakit geçmemekteydi."
    "Acaba odamı terk etmeme bir şey derler miydi?"
    "Geç olmuştu evet lakin Akademi sınırları içerisinde kaldığım müddetçe bir sorun çıkacağını sanmıyordum."
    "Hem ben de binayı daha iyi tanımış olurdum."

    scene academylivingroom with dissolve:
        xpos 0.2 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    play sound doorclose

    scene academyhallwaynight with fade

    "Karanlık olduğundan bir şeyleri seçmek zordu."
    "Avucumda küçük bir ateş topu oluşturup yürümeye başladım."

    "Yapının bu kanadında sadece ortak odalar olması lazımdı."
    "Yanlış hatırlamıyorduysam, binanın bir noktasında bahçesi de vardı. Fakat sadece ilk geldiğimizde görebilmiştim."
    "Çiçeklerin, çeşmelerin ve bankların süslediği bir bahçeydi bu, altında da koca bir şehir manzarası yatıyordu."
    "(Orada bir şeyler yiyip içmek güzel olmalı, belki Kioko’yu piknik yapmaya ikna ederim.)"
    "(Şimdi… Sanırım bu yönden gitmem gerekiyor.)"

    "Bir süre boyunca yürümüş lakin hiçbir yere varamamıştım."
    "Dahası, artık nasıl geri döneceğimi de bilmiyordum."
    "Sinirle tepindim."

    h "“Labirent mi burası yahu? Okul, okul!”"
    h "“Okul dediğin böyle karmaşık mı olur?!”"
    h "“Nasıl kaybolursun, salak Haru, salak Haru…”"

    "Kendimi sakinleştirmeye çalıştım."
    "Ben ne de olsa, dışarıdaki insanların deyimiyle, bir cadıydım."
    "Ayak izlerini aydınlatabilirdim. Hiç yapmamıştım ama çok da zor olacağını sanmıyordum."
    "Bana ait küçük bir parça da -saçım, tırnağım veya büyüyü daha etkili yapmak için kanım- sadece kendiminkileri aydınlatmama yarayabilirdi."
    "Öfleyerek saçımdan bir tutam koparmaya yeltendim fakat o an duyduğum bir ses dikkatimi dağıtmıştı."

    play sound doorknocking
    pause 1.0
    play sound doorknocking
    pause 2.0

    "Dikkat kesilip nereden geldiğini saptamaya çalıştım."
    "(Herhalde ileriki odalardan birinden…)"

    play sound walking

    "Ağır adımlarla sese doğru yürümeye başladım. Aynı zamanda etrafımı da kolluyordum."

    scene academyhallwaynight with dissolve:
        xpos 0.2 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    stop sound
    pause 1.0

    "En sonunda bir kapının önünde duraksadım."
    "İşte buradan geliyordu. Acaba içeriye bir şey mi tıkılıp kalmıştı?"
    "Merakla elimi kapı tokmağına götürdüm."

    "Fakat ben kapıyı açmadan önce bir el kapıyı sertçe geri ittirmişti."
    "Korkudan yerimden sıçrayarak arkama döndüm."

    scene blackscreen with fade

    u "“Size nasıl yardım edebilirim, leydim?”"

    "Şaşkınlıktan bir süre cevap verememiştim."

    u "“Bu saatlerde dışarıya çıkmamanız lazım. Özellikle cadıların içinde bulunduğu tehlikeli durumu düşünürsek…”"

    "Beyaz saçlar, kırmızı gözler…"
    "{i}Ah, evet{/i}! Sabahleyin gördüğüm çocuktu bu."

    h "“Sen erkeksin!”"

    u "“Elbette öyleyim.”"

    "(…)"
    "Fark etmeden düşüncemi sesli olarak söylemiştim."

    h "“Evet, evet, öylesin. Haha…”"

    "Tedirgince ensemi kaşıdım. Resmen rezil etmiştim kendimi!"

    "Bir anda gülmeye başladı."

    u "“Tamam, tamam. Hatırladım. Sen O’sun.”"

    "Ardından elini kafamın yanından çekmiş, doğrulmama izin vermişti."

    scene academyhallwaynight with fade

    show Ealdwine ClosedEye with dissolve

    u "“Bu sabah konsey esnasında benim kız mı erkek mi olduğuma karar veremeyen ikili.”"

    "Gözlerimi kırpıştırdım. Şaşırmıştım."

    h "“Duymuşsun!”"

    show Ealdwine Smiling with dissolve

    u "“Sır olması mı gerekiyordu?”"

    h "“Yoo… Hayır, sadece… Büyü mü kullandın?”"

    "Tekrardan gülmeye başlamıştı."

    show Ealdwine ClosedEyeGrinning with dissolve

    u "“Neden kullanmayayım? Burası bir büyü akademisi.”"

    show Ealdwine Smiling with dissolve

    u "“Yoksa büyü sadece cadılara has bir şey mi sanıyorsunuz?”"

    h "“Hayır! Öyle demek istemedim. Sadece buraya vardığımızdan beri sizlerin büyüye karşı biraz mesafeli olduğunu gözlemledim, o kadar.”"

    show Ealdwine SidewayThinking with dissolve

    u "“Hmm, bu konuda haklı sayılırsın.”"

    "Bu sözlerden sonra geri çekilip önümde hafifçe eğildi."

    show Ealdwine Default with dissolve

    u "“İsmim Ionyr Foliot.”"

    io "“Bu akademinin bir öğretim görevlisiyim.”"

    "(Acaba ben de eğilmeli miyim?)"
    "Emin olamayıp yerimde bir süre sallandıktan sonra kendimi tanıttım."

    h "“Ben de Haru.”"

    show Ealdwine ClosedEye with dissolve

    io "“Tanıştığıma memnun oldum, Haru.”"

    show Ealdwine Default with dissolve

    io "“Sana odana kadar eşlik edeyim.”"

    h "“Gerek yok, gerek yok!”"

    "Ellerimi önümde hızlıca salladım. Skandal yaratmak istemiyordum."

    h "“Ben kendim giderim, senin kendini yormana gerek yok.”"

    show Ealdwine ClosedEye with dissolve

    io "“Peki öyleyse, iyi geceler dilerim.”"

    show Ealdwine Default with dissolve:
        ypos 1.5 zoom 1.5

    io "“Ve Haru, bu saatlerde dışarı çıkmamaya özen göster.”"

    hide Ealdwine with dissolve

    "Kafamı “Tamam.” anlamında sallayıp, geldiğim yöne doğru yürümeye başladım."
    "Koridordan dönmeden önce; başımı son kez çevirip baktığımda Ionyr’in hala aynı yerde durmuş, bana bakıp gülümsediğini görmüştüm."

    pause 3.0
    return
































return
