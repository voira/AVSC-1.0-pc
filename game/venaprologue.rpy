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
define u = ("???")

init:
    $ flash = Fade(.25, 0, .75, color="#fff")





label venaprologue:
    scene blackscreen with fade
    ""
    "(Ah, seni son bir kez görebilsem…)"
    "(Ve sana olan duygularımı itiraf edebilsem…)"
    ""
    scene traincomp with fade
    ""

    show Haru Default with dissolve
    h "“Gerçekten de uyuyabildiğine inanamıyorum.”"

    "Göz ucuyla Kioko’ya baktım."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    ""
    "Kendisini endişe ve korkuyla yiyip bitirmişti."
    "Belli bir kişinin aksine…"
    hide kiokoeye with dissolve

    v "“Ben de senin bütün bu olan bitene rağmen bu kadar heyecanlı olmana inanamıyorum.”"

    show Haru Mischievous with dissolve

    "Haru cevaben yanaklarını şişirmişti."

    h "“Her gün Gümüş Oyuk’tan çıkma fırsatı yakalamıyoruz. Bu bir ilk-”"

    "Hızlıca lafını bölüverdim."

    v "“Ve muhtemelen son.”"

    show Haru Concerned with dissolve

    "Kendisini bu hayata kaptırmasa iyi olurdu. Tekrardan Gümüş Oyuk’a döndüğümüzde yüzlerce yahut binlerce sene burayı görmeme olasılığımız vardı."
    "Ki herkes için en iyisinin bu olduğu kanaatindeydim."
    "Dış Dünya’nın insanlarıyla bizim bir arada yaşayabilmemiz bütün yıldızlar bir araya gelse de olacak gibi gözükmüyordu."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    ""

    v "“Birkaç gündür gözüne stresten uyku girmiyor.”"

    show Haru Default with dissolve

    "Şimdi de pek güzel rüyalarda koşturduğu söylenemezdi."
    "Şakaklarından terler süzülüyor, ara sıra titriyor veya kaskatı kesiliyordu."
    "(Acaba “o gün”ü mü görüyor?)"
    "Her ne görüyorduysa ben de izlemek istiyordum lakin Haru’nun bunu pek hoş karşılamayacağı da kesindi."

    hide kiokoeye with dissolve

    h "“Sanıyorum ki herkes aynı problemden mustarip.”"

    v "“Sen hariç herkes…”"

    hide Haru with dissolve

    "Bana ters bir bakış atmıştı fakat önemli değildi."
    "Bir sürü kaybımız vardı, yerimizden olmuştuk, liderimiz ortalıkta yoktu. Böyle bir durumda hala tatile çıkıyormuş gibi davranan bir çocuğa sinirlendiğim için vicdan azabı duymama gerek yoktu."

    show Haru Sideway with dissolve

    h "“Ben birazcık hava alacağım.”"

    "(İşte beklediğim fırsat…)"
    "Yine de fazla istekli görünerek şüphe uyandırmak istemiyordum."
    "Gerçi… Haru’nun insanları okumakta pek iyi olduğunu söyleyemezdiniz ama bazen garip bir şekilde çok zeki yorumlarda da bulunabiliyordu."

    v "“Nerede?”"

    show Haru Default with dissolve

    h "“Koridorda dolaşacağım, bacaklarım uyuştu.”"

    v "“Keyfin bilir. Başını belaya sokma da…”"

    hide Haru with dissolve

    "Kafasını sallamış, ardından kompartımandan çıkmıştı."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    ""

    "Hızlıca Kioko’ya doğru döndüm. Kaybedecek zamanım yoktu."
    "Gözlerimi kapatıp manamı uyandırmadan önce elimi eline dolamıştım."
    "(Üzgünüm Kioko. Yapmak zorundayım.)"

    scene fogforest with fade

    "Kardeşimin rüyası beni alıp özlemini çokça çektiğim o yere geri götürmüştü."
    "Buradaki her ağacı bilirdim, hatta her ağacın her kovuğu dahi ezberimdeydi."
    "Ama en nihayetinde Kioko’nun anılarındaki Gümüş Oyuk’ta saadet bulmak için gelmemiştim buraya."
    "Bir yerlerde Kioko Kara Katliam’a dair önemli bir şeyler görüyor olmalıydı."

    play sound walking

    "Ağır adımlarla yerleşim alanına doğru, ağaçların arkasında kendimi kollayarak yürümeye başladım."

    stop sound

    "Rüyadaki varlığım onu daha gerçekçi bir hale getiriyor, zihnin sahibinin bilincini de buraya sürüklüyordu."
    "Bu nedenle “asıl” Kioko’yla karşılaşmak istemiyordum."
    "Yıldızların ışığının normalde yıkadığı o güzelim ormana karanlık bir gücün etkisiyle sis çökmüştü."
    "Vücudum her ne kadar kararlı bir şekilde ilerlese de kafamın içinde bir ses beni buradan çıkmak için çekiştiriyordu."
    "Bu düşünceleri hemencecik susturdum. Sonuçta bir rüya aleminde yürüyordum, olan da olmuştu artık. Geçmişte takılı kalamazdım."
    "Korkmanın da vakti değildi."
    "Fakat Kioko’nun kabusu cesaretimin kırılmamasından yüz bulmuş olacaktı ki…"

    scene blackscreen with fade
    # Buraya Dead Bodies CG'si eklenecek!

    "Karşıma bunları çıkarmıştı."
    "(Az daha üzerlerine basıyordum.)"
    "Gözlerimi kıstım ve dikkatlice kızların suratlarını süzdüm."
    "Bunların birçoğu şu an hayatta olan insanlardı. Şimdiyse bu rüyada, o gün ölenler gibi cansız, cam misali gözlerle bana bakıyorlardı."
    "Vücutlarında herhangi bir yara yoktu. Öldüklerini atmayan damarlarından, havayla dolmayan ciğerlerinden ve kapanmamaya ant içmiş gözlerinden anlıyordunuz."
    "Fazla duygusal bir ruh haliyle yere eğilmiş, bir tanesinin göz kapaklarını indirmiş ve önüme çıkan bedenlere basmamaya dikkat ederek yola tekrardan düşmüştüm."

    scene fogforest with fade

    "Tahminlerimde yanılmıyorduysam rüya ormanın tam ortasında, yerleşkede geçiyor olmalıydı."
    "Hala yaşayan insanların ölü gözükmesi dolayısıyla rüyanın anıları ne kadar iyi yansıttığı bir muammaydı. Yine de hiç yoktan iyiydi."
    "Öyle ya da böyle Kioko’nun zihninin kilitlediği anılara ulaşmam lazımdı."

    play sound walking

    ""
    ""

    scene shd with fade
    stop sound

    "Köy açıklığına en sonunda varmıştım. Aradığım kişi de çeşmenin yanına çökmüş, ölü bir vücuda sımsıkı sarılmış inleye inleye ağlıyordu."

    show Kioko Crying with dissolve

    "Acıklı bir sahne olduğu kesindi ve içimden ona uzanıp omzunu sıvazlamak, bir çocuğunki gibi başını okşamak geçmiyor değildi."
    "Fakat ben buraya bunun için gelmemiştim."
    "Faili arıyordum."

    hide Kioko

    scene forest with flash

    show Kioko Default with dissolve

    k "“Vena ben… Galiba bundan sorumlu olan kişiyi gördüm.”"

    show Kioko Concerned with dissolve

    k "“Ama hatırlayamıyorum. Olmuyor.”"

    hide Kioko with dissolve

    scene shd with flash

    show Kioko Crying with dissolve

    "(Neredesin… Neredesin? Hadi, kendini göster!)"

    show Kioko Shocked with dissolve

    ""

    hide Kioko with dissolve

    scene fogforest with fade

    scene fogforest with vpunch

    "Dikkatsizliğim yüzünden Kioko’yla göz göze gelmiş, ardından bir hışımla yaslandığım ağacın arkasına saklanmıştım."
    "Fakat istenmeyen bu karşılaşmanın üzerinden daha saniyeler bile geçmeden endişemin yersiz olduğunun farkına vardım."
    "Rüya Kioko’nun beni görmesi bir sorun değildi."
    "Önemli olan gerçeğine yakalanmamaktı ve muhtemelen bilinci de rüyasına bu şekilde gasp eden düşmanını her yerde didik didik arıyordu şu an."
    "(Kaybedecek zamanım yok.)"
    "Kafamı ağacın öteki tarafından uzatıp baktım."

    scene shd with fade

    "Eski meclisten birtakım sesler yükseliyor, yer yer üzerine inşa edilmiş olduğu yaşlı meşe sallanıyordu."
    "Yanlış hatırlamıyorduysam Kioko’nun da anılarını kaybetmeden önce en son gittiği yer burasıydı."
    "Kioko’nun neyi veya kimi gördüğünü bilmiyorduk. Bu bizden biriydi ise anılarını özenle kendi de silmiş olabilirdi."
    "Veyahut doğal bir şekilde, gördüğü şeylerin şokundan tetiklenmiş de olabilirdi."
    "İki türlü de ben katliamın sorumlusuyla karşılaşmış olabileceğini düşünüyordum."
    "Tabii bu bir rüya olduğundan gerçek failin yüzünü görüp göremeyeceğimin de bir güvencesi yoktu. Yine de-"

    scene shd with vpunch

    "…!"
    "Aniden yükselen bir çığlık bütün dikkatimi ve çabalarımı çöpe atmış, ne yaptığımı bilemeden geri bağırmama sebep olmuştu."

    v "“Waceera!”"

    "Koşmak için ileri atıldım."
    "Şimdi dönüp bakınca ne utanç vericiydi, gerçek bile olmayan bir insanı kurtarmak için bir anlığına akla karayı seçmiştim."
    "Ama o sırada birinin kolumdan tutup geri çekmesi kendimi daha da rezil etmemin önüne geçmişti."
    "Şaşkınlıktan nefesim kesilerek dirseğimdeki elin sahibine döndüm."

    scene fogforest with fade

    show Kioko Gaping with dissolve

    k "“Vena? Gerçek Vena’sın sen, değil mi?”"

    "{i}Güzel{/i}. Yakalanmıştım. Fakat kendimi açıklayacak vaktim yoktu."
    "Uzanıp Kioko’yu omuzlarından tuttum."

    v "“Kiki, beni dinle. Açıklayacak vaktim yok. Hemen eski meclise gitmemiz gerekiyor-”"

    scene fogforest with vpunch

    hide Kioko with dissolve

    "Büyük bir patlama sesi lafımı bölmüş, ardından yer sallanmıştı."
    "Kioko’yla birlikte en yakınımızdaki ağaca sımsıkı tutunduk."
    "Hızlıca kafamı kaldırıp sesin geldiği yöne doğru baktım."

    scene shd with fade

    show VoidCrawler with dissolve

    "(Hayır, hayır…)"
    "Meclis kulübesinin olduğu yerde koca bir Hiçlik girdabı belirmişti."
    "Geç kalmıştık. Görebileceğimiz bir şey vardıysa da ellerimin arasından kayıp öylece gidivermişti."
    "Parmaklarımı huzursuzca saçlarım arasında gezdirerek girdaptan dışarı fırlayan Gölgeleri izlemekten başka yapacak bir şeyim kalmamıştı."
    "Uyanmak hariç…"

    scene traincomp with fade

    "Tekrardan başladığım noktadaydım."
    "Dışarıdan birtakım sesler geliyordu, kompartıman da hala boştu. Gözlerimi ovuştururken Haru’nun nerede olabileceğini düşündüm."

    show Kioko Confused with dissolve

    "(Ah…)"
    "Dudaklarımı ıslatıp derin bir nefes aldım. Tam olarak kızgın değildi fakat rahatsız olduğu da her halinden belli oluyordu."

    v "“Kabus gördüğünü anlayınca bilincinin bloke ettiği anılara ulaşabilirim diye düşündüm.”"

    show Kioko Melancholic with dissolve

    k "“Sen de benden şüpheleniyorsun, değil mi?”"

    k "“Diğerleri gibi.”"

    "Duyduklarım beni hayrete düşürmüştü."
    "Ama daha çok şaşırdığım içimde bir yerlerde bu dediklerinde bir miktar doğruluk payı olduğunu fark etmemdi."

    v "“Kioko-”"

    "Kompartımanın kapısının açılmasıyla lafım bölünmüştü."

    hide Kioko with dissolve

    show Haru Concerned with dissolve

    "Kafamı çevirip içeri giren Haru’ya baktım."

    v "“Dışarıdan gürültüler geliyordu, bir şey mi oldu?”"

    show Haru Smiling with dissolve

    h "“Bir sorun yok, klasik tartışmalar işte.”"

    "Ne tür tartışmalardan bahsediyordu?"
    "Aman… Uzun zamandır mana meditasyonu yapmadığım için fazlasıyla yorulmuştum ve bunun peşine düşecek halim de yoktu."
    "Omuz silkip gözlerimi kapattım."
    "Whemond’a varmadan da açmaya niyetim yoktu."

    scene blackscreen with fade

    "Büyük, soğuk beton binalar, arka sokaklarında açlıktan ölen insanlar ve ciğerlere dolan o pis, yapışkan nem…"
    "Üç yüz yılı aşkındır ormanın ortasında, her akşam yıldızları izleyerek ağaç kulübesinde uyuyan bir insanın bir gecede sindirebileceği şeyler değillerdi bunlar."
    "Ve ben kendimi yalnız hissediyordum."
    "Yalnız, dışlanmış ve “göçebe” adı altında yaşayan bir sığıntı."

    scene academylivingroom with fade

    "Kraliyet Akademisi’ne sonunda varmıştık."
    "Katliam’ın sonrasında bir ay kadar kaldığımız köyde toplamış olduğum bitkilerin kavanozlarını bir bir bez çantamdan çıkarmaktaydım."
    "Yorgundum lakin en azından yerleşme işlemini bu gece tamamlamak istiyordum."
    "Bu sırada Haru, Kioko ve Asha da camın etrafına dizilmiş, şehir dedikleri cehennemi izliyorlardı."
    "Kardeşlerimin yüzündeki o hayranlık canımı sıktığından en iyisi kendimi işlere vermekti. Aksi takdirde tatsız yorumlar yapıp can sıkacaktım."
    "Ama denilenleri kulak ardı da edemiyordum."

    show Asha Grinning at left with dissolve

    a "“Bundan o kadar etkilendiyseniz bir de gün batımını izlemeniz lazım kızlar! O zaman güneş sanki kanayarak denize dökülüyormuş gibi bir görüntü oluşuyor.”"
    a "“Şafakları da aynı şekilde, bir kan göledinden çıkıyormuşçasına…”"
    a "“Ama kabul etmem lazım, ben en son buraları göreli her şey çok ama çok değişmiş.”"

    "Dişlerimin arasından konuşmaya başladım."

    v "“Rezil bir yer burası. Etkilenilecek hiçbir şey yok.”"

    show Asha Default with dissolve

    v "“Işığın bu kadar gereksiz kullanılabileceğini düşünmezdim.”"

    "Öyle bir ışık kirliliği vardı ki bana hayatım boyunca rehber olmuş yıldızlar yüzlerini bir kez bile göstermemişti geldik geleli."
    "Bu kötü bir talihin habercisi değildi de neydi?"

    show Kioko Shy at right with dissolve

    k "“Bence… Bence ışıklar çok sevimli duruyor.”"

    "(…Sen de mi Kioko?)"

    show Asha Smiling with dissolve

    a "“Şehirde gezme fırsatını elbet yakalarsınız sanıyorum ki.”"

    "En küçük kardeşimin dönütünden yaşadığım şoku atlatamamışken bir darbe de Asha’dan gelmişti."

    play sound loudthud

    hide Asha

    show Asha Gaping

    show Kioko Gaping

    show Haru Gaping at left

    "Elimdeki kavanozu yerleştirirken sinirden istemsizce tezgaha çarpıvermiştim."
    "Şimdi bütün gözler bendeydi."
    "Dışarı çıkmak, eğlenmek… Ölülerimiz için bir tören dahi düzenleyememişken nasıl böyle planlar yapabiliyorlardı?"
    "Liderimiz kayıptı; arkadaşlarımız, diğer kız kardeşlerimiz ölmüştü ve bedenlerini dahi geri getirememiştik."
    "Nasıl hiçbir şey olmamış gibi davranabilirlerdi? Hele ki Asha!"

    v "“Asha, lütfen kimsenin aklına böyle şeyler sokma.”"
    v "“Ne Haru’nun, ne Kioko’nun, ne de başka birinin.”"

    show Asha Default with dissolve
    show Kioko Default at right with dissolve:
        ypos 1.63 zoom 1
    show Haru Default at left with dissolve:
        xpos 0.03 ypos 1.63 zoom 1

    a "“Ne olacak yahu? Bir günlük şehir gezisi ayarlayabiliriz.”"

    v "“Kesinlikle olmaz.”"
    v "“Her zamankinden daha çok kendimize dikkat etmemiz gereken bir dönemdeyiz. Olanlara neyin sebebiyet verdiğini bile bilmiyoruz.”"
    v "“Eğer insanlar ölmek istemiyorlarsa asla bu Akademi’den çıkmamalılar.”"
    v "“Hatta ölmek istiyorlarsa da çıkmamalılar. Bir lider olarak senin en büyük vazifelerinden biri herkesin güvenliğini sağlamak Asha.”"
    v "“Kaldı ki buraya eğlenmeye de gelmedik, ölülerimiz var.”"

    "Geçici liderimiz olarak, hatta bunu geçtim, binlerce yılı devirmiş bir insan olarak Asha’nın böylesine umursamaz davranmaması gerekiyordu."
    "Kendi içimizde çatlaklar oluşmaya başlamışken özellikle…"

    hide Kioko with dissolve
    hide Haru with dissolve
    show Asha Grinning with zoomin

    a "“İnanamıyorum. Tıpkı Waceera gibisin…”"

    "Bu noktada bunu beni eleştirmek için mi, yüceltmek için mi diyor anlayamamıştım. Önemli de değildi."

    v "“Gülebilmen ne hoş. Yine de bunun önemli bir konu olduğunu unutma, özellikle Almasi’nin her açığını yakalamaya çalıştığını.”"

    show Asha Smiling with dissolve

    a "“Görünen o ki Waceera’ya güvendiğinin yarısı kadar bile bana güvenmiyorsun.”"

    "Gözlerimi bir süreliğine yumdum."
    "Dediklerinin doğru olduğunu sokaktan geçen bir insan dahi anlayabilirdi. Yalan söylemenin lüzumu yoktu."

    v "“Senin iyiliğin için konuşuyorum, bunu kendine bir yarış haline getirmezsen iyi olur.”"

    a "“Getirmiyorum, sadece gözler önünde olan bir doğruyu söyledim.”"
    a "“Ah Vena… Dert etmeni gerektirecek bir şey yok, Waceera’yı da bulup Gümüş Oyuk’a geri döneceğiz.”"

    "Bu sözlerinden sonra ayaklanmıştı."

    show Asha Default:
        xalign 0.5
        linear 0.8 xpos 0.2

    a "“Sizlere daha da rahatsızlık vermeyeyim. Yataklarınıza dağılın bakalım.”"

    show Kioko Laughing at right with dissolve

    k "“Hala çocukmuşuz gibi davranıyorsun Asha.”"

    show Asha Default:
        xalign 0.2
        linear 1 xpos 0.6

    ""
    "Asha elini Kioko’nun kafasına götürüp saçlarını hafifçe karıştırdı."

    a "“Hala çocuksunuz çünkü. Hep öyle kalacaksınız.”"

    hide Asha with dissolve
    hide Kioko with dissolve
    play sound doorclose
    ""

    scene shd with flash

    show Waceera Smiling with dissolve

    u "“Benim için asla büyümeyeceksin, Vena.”"

    scene academylivingroom with flash

    "(…)"
    "Anılarımda kaybolmak üzereyken Haru’nun sesi beni salona döndürmüştü."

    show Haru Default at left with dissolve
    show Kioko Default at right with dissolve

    h "“Öyleyse… Odalarımıza mı dağılıyoruz?”"
    v "“Siz ikiniz gidebilirsiniz. Benim biraz daha işim var.”"
    k "“Lütfen kendini yorma.”"

    show Haru Concerned with dissolve

    h "“Kioko’ya katılıyorum Vena. Ayrıca, iyi geceler.”"

    v "“Size de.”"

    hide Haru with dissolve
    hide Kioko with dissolve

    "İkisi de odayı terk ettiğinde yüzümü ellerimin arasına aldım ve derin bir iç geçirdim."

    scene blackscreen with fade

    "İşlerimi daha bitirmemiştim."
    "Aynı zamanda ne kadar yorgun olursam olayım kafam bu denli doluyken uyuyabileceğimi düşünmüyordum."

    scene academylivingroom with fade

    "Arkamdaki raflara uzanıp biberiyeden yapmış olduğum bir merhemi aldım."
    "Hayatımda hiç bu kadar fazla saatimi oturarak geçirmemiştim. Sihir yoluyla ışınlanmak varken insanlar neden kendilerine “tren” isimli bu işkenceyi çektiriyorlardı emin değildim."
    "(Bütün kaslarım ağrıyor. Harika…)"
    "Kafamı sallaya sallaya bacaklarımı açıp merhemle masaj yapmaya başladım. Bunun bir de dönüşü vardı."
    "(Tabii dönebilirsek…)"
    "Kafamdan bu negatif düşünceleri kovdum. Dönecektik. Her ne olursa olsun dönecektik."
    "Ayağa kalkıp cama yaklaştım. Akademi havada süzüldüğünden bütün bir şehri izlemek mümkün oluyordu."

    scene whemond with fade

    "Whemond…"
    "Şehre verdikleri isim buydu."
    "Göz korkutan binalar zavallı bir heybetli görünme çabası içerisinde boyanıp bezenmiş fakat kullandıkları sıva bütün bu pisliği örtmeye yetmemişti."
    "Hissediyordum, Akademi’yi saran sihir bariyerine rağmen insanların gerginliği, üzüntüleri ve sıkıntıları ulaşabiliyordu bana."
    "Hiçbir zaman bunca yoğun duyguya bir arada şahit olmamıştım. Huzurlu günlerimi geri istiyordum."
    "Burada tıpkı diğer her şey gibi çürümeye niyetim yoktu."

    scene blackscreen with fade

    ""

    # Buraya sonraki gün ibaresi eklenecek!

    scene academyclass with fade

    "Yorucu bir gün beni bekliyordu."
    "Bugün Kara Katliam sonrası ilk konsey toplanacaktı."
    "(Ne kadar sonuç odaklı olur bilmiyorum, daha çok ortamın gergin havasından bütün günü kavga ederek geçireceğiz gibi.)"
    "(Özellikle Almasi’yi hesaba katarsak.)"

    scene academyclass with zoomin

    play sound crowdtalking loop

    "Haru’yla birlikte Akademi’nin bize verdiği sınıftaki amfilerden birine geçtik."

    play sound sitting
    queue sound crowdtalking volume 0.6 loop

    "Elimdeki hatıra taşını masaya koydum. Kioko bugün yorgun olduğu için aramıza katılamamıştı."
    "Olan bitenden geri kalmasını da istemiyordum. O yüzden anıları kaydetmek en mantıklısıydı."

    play sound doorclose
    queue sound crowdtalking volume 0.3 loop
    show Asha Default at right with dissolve
    show Zuri Default at left with dissolve

    "Çok geçmeden Asha ve Zuri de sınıfa geldiler."
    "Tam tahmin ettiğim gibi Zuri Asha’yı sahnede bir başına bırakıp ön koltuklardan birine geçmişti."

    hide Asha with dissolve
    hide Zuri with dissolve

    "(Anlaşılan yine suçlamaları üzerine çekmek istemiyor. Kioko’nun çekingen yapısı Zuri’den geliyor olabilir mi?)"

    show Asha Default with zoomin

    a "“Ah, güzel… Hepiniz buradasınız sanıyorum ki- bir kişi hariç.”"

    "Kioko…"

    show Asha Sideways with zoomin

    a "“O da sıkıntı değil.”"
    a "“Sizlere söz vermiştim Whemond’a varır varmaz sorularınızı cevaplayacağıma dair.”"

    show Asha Default with zoomin

    a "“O sözü tutmak için şimdi önünüzdeyim ve bütün-”"

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    al "“İşe ablanın neden ölü olabileceğini düşündüğünü anlatarak başlayabilirsin.”"

    "(Yıldızlar bize yol gösterin.)"

    hide kiokoeye with dissolve

    hide Asha with dissolve

    "Daha oturum başlamadan koca bir ateş yakmaya karar vermiş olan Almasi’ye dönüp baktım."

    show Almasi Angry with zoomin

    "Zaten halinden de anlaşılıyordu ki buraya kavga çıkarmaya gelmişti."

    hide Almasi with dissolve

    show Asha Default with zoomin

    a "“Sanıyorum ki yalan söylemenin bir manası yok.”"
    a "“Waceera, ben ve Zuri’nin çemberi sizinkine kıyasla daha genişti.”"

    play sound whispering

    hide Asha with dissolve

    "(…)"
    "Bu konuda şüphelerim vardı. Doğru çıkmasını beklemiyordum da diyemem, daha çok bunu istememiştim."
    "Açıkçası işin etiğinde de değildim. Sadece Waceera’nın güvenliğinin garanti olmaması beni tedirgin ediyordu."
    stop sound
    "Bizler, doğduğumuzda yıldız haritalarına göre çemberlerde doğardık."

    scene constellation with fade

    "Aramızdaki büyü bağı kardeşlerin birbirlerini hissetmeleri, daha güçlü büyüler yapmaları gibi becerilere yarardı."
    "Ama bir al-ver ilişkisi olarak çember bağı ne kadar yoğunsa risk ve negatif etkilerin yoğunluğu o kadar yüksekti."
    "Örneğin çember bizleri “bir” olmaya itelediğinden duygu noksanlığı çekerdik."
    "Ve birinin yaralanması herkesin yaralanması, birinin ölmesi o çembere mensup herkesin ölmesi demekti."

    scene academyclass with fade

    "Bu durum bize Kara Katliam’da çok büyük bir dezavantaj sağlamış, sayımızın hızla azalmasına sebep olmuştu."
    "Dış dünyaya varır varmaz çemberleri genişletmenin de yapılan ilk iş olma nedenlerinden biri buydu."

    al "“Yani bizleri birer zombi misali yaşamaya iteklediğinizi ve bu sırada sizin sefa sürdüğünüzü kendi ağzınla kabul ediyorsun.”"

    show Asha ClosedEye with zoomin

    a "“…”"

    show Asha Default with zoomin

    a "“Kendi durumumuzu ‘sefa çekmek’ olarak tabir edebilir miyiz emin değilim.”"
    a "“Bu karar bizzat Waceera tarafından verilmişti. Gümüş Oyuk’taki işleri daha bilinçli bir şekilde çekip çevirmek namına…”"
    al "“Saçmalık!”"

    show Asha ClosedEye with zoomin

    a "“Ben bu toplantıda sizlere sadece gerçekleri söylemekle yükümlüyüm.”"

    show Asha Default with zoomin

    a "“Waceera’nın bir şeyleri neden yaptığı yahut bir art niyet güdüp gütmediği ona sorabileceğiniz şeyler.”"
    a "“Bana ne kadar kızsanız da sinirlenseniz de verebilecek başka bir cevabım ne yazık ki yok.”"
    a "“O yüzden asiliğinizi Waceera’nın dönüşüne saklamanızı öneririm.”"

    play sound commotion loop
    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    al "“Ne güzel, ne güzel! Sorumluluklarından kaçmanın ne de güzel bir yolunu bulmuşsun!”"
    stop sound

    "Dişlerimi sıktım. Asha’nın liderliği bana göre de biraz daha cila gerektirmekteydi fakat Gümüş Oyuk güruhu arasında sırf bu yüzden kavga çıkarmaya değer miydi?"
    "Özellikle en çok birlik olmamız gereken anda…"

    hide kiokoeye with dissolve

    show Asha Sighing with zoomin

    a "“Şu an umabileceğimiz tek şey Waceera’nın bize sağ salim dönmesi ve hakkındaki her suçlamaya kendisinin cevap vermesi.”"

    show Asha Default with zoomin

    a "“Başka sorularınızı da cevaplamaya hazırım.”"

    hide Asha with dissolve

    bbg "“Dış Dünya’nın varlığını bizden ne kadar süre boyunca saklamayı düşünüyordunuz?”"
    obg "“İçimizde bir hain mi var?”"
    dbg "“Ya bizi burada öldürürlerse? Burası Akademi değil, hapis resmen!”"

    scene blackscreen with fade

    "Asha’nın verdiği yarım yamalak cevapları dinlerken derin bir iç çekip yüzümü ellerime gömdüm."
    "Bu konsey düşündüğümden bile daha kötü bir hal alacak gibiydi."

    scene academyclass with fade

    "Fakat kendi düşüncelerimde kaybolamadan Haru’nun kolumu dürtmesiyle irkildim ve dönüp ona baktım."

    show kiokoeye at left with easeinleft:
        xalign -0.2 yalign 1

    h "“Vena, kapının oradaki kişi kim?”"

    "(…Huh?)"

    show Ealdwine Default with dissolve

    "Dikkatimi toplantıya o kadar çok vermiştim ki kapımızda yabancı birinin olduğunu fark edememiştim."
    "Demek bizi şimdiden izlemeye başlamışlardı."

    hide kiokoeye with dissolve

    v "“Ben de bilmiyorum ama üstündekilere bakılırsa sanırım Akademi’nin bir üyesi.”"

    hide Ealdwine with dissolve

    "(Hah… Ne kadar acı… Ne kadar aşağılayıcı!)"
    "Belli ki bizlere kafesteki bir hayvan muamelesi yapacaklardı."
    "Elden boyun eğmekten başka ne gelirdi?"

    scene academyhallway with dissolve

    "(Öf…)"
    "Saatler sonra toplantı bitmişti."
    "Ve biz hala içimizdeki sorunlara dair hiçbir ilerleme kaydedememiştik. Başlangıç çizgisinde öylece çakılı kalmıştık."

    show Asha Default at right with dissolve

    v "“Kafalarındaki soru işaretlerinden sonsuza kadar kaçamazsın.”"

    "Haru’nun da yanımızdan ayrılmasıyla sonunda Asha ile baş başa kalmıştık. İşleri zaten başından aşkın olduğu için üzerine tepki çekmek istemiyordum."

    show Asha Concerned with dissolve

    a "“Bu yüzden bir an önce Waceera’yı bulmamız lazım.”"
    v "“Aklında nasıl bir plan var?”"

    show Asha Ruminant with dissolve

    a "“Çeşitli seferler düzenlemek niyetindeyim.”"

    "Tek kaşımı sorarcasına kaldırdım."

    v "“Nereye? Gümüş Oyuk’a şu anki haliyle dönemeyeceğimizi söylediğini sanıyordum.”"

    show Asha Default with dissolve

    a "“Kastım Gümüş Oyuk değil zaten.”"
    a "“Ölüler Diyarı.”"

    "Derin bir iç çektim. Aklında kim olduğu belliydi."

    v "“Kioko’yu buna ikna edebileceğimi sanmıyorum.”"

    show Asha ClosedEye with dissolve

    ""

    show Asha Default with dissolve

    a "“En azından bir gidip konuşmamız lazım.”"

    v "“Denerim ama çok şey bekleme.”"

    show Asha Sighing with dissolve

    a "“Birimizi Kıyı’ya sokması dahi yeterli olur aslında.”"

    v "“Onu ayarlayabiliriz.”"

    show Asha Default with zoomin

    "Yaklaşıp omzumu sıvazlamıştı."

    show Asha Smiling with zoomin

    a "“Güzel, sana güveniyorum. Hatta kalanlar arasında en çok sana güveniyorum.”"

    show Asha Sideway with zoomin

    a "“Ayrıca Vena…”"

    hide Asha with dissolve

    scene academyhallway with zoomin

    "Yalnız olmamıza rağmen beni izole bir köşeye sürüklemesinden önemli bir şeyler yumurtlayacağını anlamıştım."
    "Sorar bir ifadeyle onu süzüyordum. Asha ise hızlıca yaptığı bir büyüyle etrafta kimseler var mı kontrol ediyordu."
    "Emin olduktan sonra rahatlamış bir ifadeyle bana döndü."

    show Asha Default with zoomin

    a "“Şimdi diyeceklerimin Işık Hamilleri arasından çıkmaması çok önemli…”"

    show Asha Concerned with dissolve

    a "“Bizi buraya sürükleyen şeyin veya hainin Dış Dünya’dan bir güruhla iş birliği içerisinde olduğunu düşünüyorum.”"

    "Cevap vermeden önce dediklerini kafamda bir tarttım. Bu olasılığın varlığını reddedemesem de kimin neden böyle bir şey yapacağına akıl erdiremiyordum."

    v "“Elinde buna dair bir kanıt mı var? Fark ettiğin bir şey…?”"

    "Böyle temelsiz açıklamalar yapacak bir insan değildi."

    hide Asha with dissolve

    "Eteğinin cebinden bir kağıt tomarı çıkardı. Kafamı yana eğip dikkatlice bakınca bunun iki adet rün kartı olduğunu gördüm."

    a "“‘Hain’.”"

    "Kartlardan birini yüzüme yaklaştırmıştı. Ardından diğerini de gösterdi."

    a "“‘Yabancı’.”"

    "Asha aramızdaki en iyi kart okuyucuydu, o yüzden gördüklerini kulak ardı etmek pek akıl kârı değildi."
    "Kara Katliam’ın kehanetini veren de Asha olmuştu ne de olsa."
    "(Komik; bilmemize, tedbirler almamıza rağmen olacakları engelleyememiştik.)"
    "(Fakat bu sefer…)"
    "Homurdanarak konuşmaya başladım."

    show Asha Default with zoomin

    v "“Bu konuda ne yapmamızı önerirsin? Buraya tıkılıp kaldık. Her yerde Kraliyet askerleri var.”"

    show Asha Sideway with dissolve

    a "“Sadece biz değil… Whemond’da da garip şeyler oluyor.”"

    v "“Ve sen bu olayların arasında bir bağlantı olduğunu düşünüyorsun.”"

    show Asha Default with dissolve

    a "“Sadece ben değil. Onlar da…”"

    "“Onlar”dan kastın bu ülkenin önde gelen insanları olduğunu anlamıştım."

    a "“Bu akşam, diğer Işık Hamilleriyle bir toplantı yapacağız.”"
    a "“Kral’ın çocukları ve Grandük de bizimle birlikte olacak.”"

    "Kafamı onaylarcasına salladım."

    v "“Merak etme, orada olacağım.”"

    show Asha Smiling with dissolve

    a "“Güzel, çünkü Almasi’yi birinin zapt etmesi gerekiyor o bir iç savaşa sebep olmadan önce.”"

    hide Asha with dissolve

    "Güldüm ve destek olurcasına kolunu sıvazladım."
    "Toplantının saati ve kimin hangi Hamil’e haber salacağını kararlaştırdıktan sonra ayrılmıştık."
    "(Haru’yu bulmam lazım. Onu diğer piranalarla bir başına bırakmasam iyi olur.)"
    "Dalgın bir şekilde ilerideki koridordan Güney Kanadı’na doğru döndüm-"

    scene academyhallway with hpunch

    # Buraya CG gelecek!

    v "(…!)"

    u "“Offff!”"

    "…Dönmemle kızın tekinin bana toslayıvermesi bir olmuştu."
    "O düşmeden hızlıca iki omzundan yakaladım ve kendisini doğrulttum."

    v "“İyi misin?!”"

    "Sesimde endişeli bir tını olduğu kadar azarlarcasına bir ton da vardı."

    u "“Çek ellerini üzerimden! Aptal köylü seni! Sakın bir daha bana dokunmaya kalkma.”"

    "(…Ne?)"
    "Duyduklarıma inanamayarak, hayretler içerisinde ellerimi kızın üstünden çektim."

    show Orphina Default with dissolve

    v "“Pardon?”"

    u "“Önüne bak diyorum, önüne!”"

    "(Fazla olmaya başladın sen.)"
    "Kaşlarımı çattım."

    v "“Kusura bakma, benim boyumdaki bir insan için aşağıda neler oluyor görmek biraz zor.”"

    show Orphina Annoyed with dissolve
    pause 1.5
    show Orphina AnnoyedSide with dissolve

    u "“…Tch.”"

    hide Orphina with dissolve

    "Üzerime yürüyüp bana çarpmış, ardından hızlı adımlarla uzaklaşmaya başlamıştı."
    "Bense hala şaşkınlık içerisinde bu küstahlığı yedirmeye çalışıyordum."
    "Arkasından bağırdım."

    v "“Sana dokunmamı istemediğini söyledin sanıyordum.”"

    "Fakat dönüp bakmadı."
    "(Bu şımarık da nereden çıktı şimdi?)"
    "Omuz silktim. Vakit kaybetmeye bile değmezdi."

    scene academylivingroom with fade

    "Yorucu bir günün ardından en nihayetinde akşam çökmüştü."
    "Ki işlerim burada da bitmiyordu. Yemeğimi bitirdikten sonra toplantıya gitmem lazımdı."
    "Tembel bir insan hiç olmamıştım ama benim için bile hareketli geçecek gibi duruyordu önümüzdeki günler."
    "(Bakalım kralın oğulları neler diyecekler. Umarım işimize yarar bir bilgi verirler.)"

    show Haru Default at left with dissolve
    show Kioko Default at right with dissolve

    k "“Bir şey… Diyeceğim.”"

    show Kioko ClosedEye with dissolve

    k "“Fakat lütfen paniklemeyin.”"

    "…"
    "(Çok geç Kioko, iş sen olunca paniklememek elde değil.)"
    "Endişeli gözlerle ona baktım."

    show Kioko Sideway with dissolve

    k "“Sanırım ben… Bugün odamda birini gördüm.”"

    "Bir anlığına elimde olmadan gözlerim fal taşı gibi açılmıştı."
    "(Topla kendini, hemen. Stres yapman onu da korkutur.)"

    show Haru Gaping with dissolve

    h "“Ne?”"
    v "“Kimi?”"

    show Kioko Concerned with dissolve

    k "“B-Bilmiyorum ki.”"
    k "“Rüya da olabilir, tam emin değilim.”"

    hide Haru
    hide Kioko

    scene shd with flash

    show VoidCrawler with dissolve
    pause 2.0
    scene academylivingroom with flash

    show Haru Gaping at left
    show Kioko Concerned at right

    "Düşündüğüm kişi olabilir mi?"
    "Ya Kioko yüzünü gördüğü için onu öldürmek namına geri geldiyse?"
    "Gerçi, bu yersiz bir endişe de olabilirdi."

    v "“Kioko, sakin ol.”"

    show Kioko BitingLip with dissolve

    k "“Yeni uyanmıştım. Sonra odamda biri olduğunu fark ettim. Cam kenarında duruyordu.”"

    show Haru Concerned with dissolve

    h "“Nasıl biriydi? Arkadaşlarından biri olmasın?”"

    show Kioko Concerned with dissolve

    k "“Hayır! Hayır… Öyle bir arkadaşım yok benim.”"

    show Kioko Sideway with dissolve

    k "“Turuncu saçları vardı. Yüzünü tam göremedim ama, uykuluydum.”"

    show Kioko ClosedEye with dissolve

    k "“Yanıma geldi sonra. Çok korktum, hareket edemedim, ardından öylece uyuyakaldım!”"

    "Elimi alnına götürdüm. Onun anlatmasındansa benim anılarını izlemem daha iyiydi."

    v "“İzin verirsen bir de ben bir bakacağım.”"

    "Kafasını sallayarak bana sözsüz bir izin vermişti. Derin bir nefes alarak manamı odakladım."

    hide Kioko with dissolve
    hide Haru with dissolve

    # Buraya CG gelecek!

    "Dikkatimi ilk çeken şey anının ne kadar bulanık olduğuydu."
    "Kioko’nun önündeki kadını zar zor seçebiliyordum."

    "Turuncu saçlar, beyaz bir ten, gülen bir surat…"
    "Ama başka bir şey yoktu."

    "Yine de bu kadar az ipucuyla bile bunun bir yabancı olduğunu söyleyebilirdim."
    "Sahneyi biraz daha inceledikten sonra manamı daha fazla tüketmemek adına anıdan çıktım."

    scene academylivingroom with fade

    show Kioko Default at right with dissolve
    show Haru Default at left with dissolve

    "Kızların ikisi de bana sorarcasına bakıyordu."

    v "“Ya gelen her kimdiyse anılarını bulutlamış ya da gerçekten rüya görmüşsün.”"

    show Haru Concerned with dissolve

    h "“Ayırt edemiyor musun, Vena?”"

    "Normalde anılar sihir aracılığıyla kapatıldığında büyünün izlerini hızlıca bulabilirdim."
    "Fakat bu sefer öyle esrarengiz, abes bir atmosferle karşılaşmamıştım."
    "Bu da demek oluyordu ki Kioko ya cidden rüyayla gerçeği karıştırıyordu, ki yorgun olmasını hesaba katardıysam bu pekala olabilirdi."
    "Ya da bu kişi her kimdiyse ne yaptığını çok iyi biliyordu."
    "Tıpkı Kara Katliam’dan sonra yaşadığı ilk hafıza kaybı gibi…"

    h "“Bu akademiden bir kimse olabilir mi?”"

    v "“Sanmam. Üniforma giymiyordu, bizden birine de benzemiyordu. Kioko, bize neden daha önceden haber vermedin?”"

    show Kioko ClosedEye with dissolve

    k "“Gereksiz panik yaratmak istememiştim.”"

    "Uzanıp elini kavradım. Böyle çekinceler bulunduğumuz zamanda çok tehlikeli sonuçlar doğurabilirdi."

    v "“Sakın böyle şeyler düşünme. Çalkantılı bir dönemdeyiz o yüzden şüpheli görünen her şeyi bize söylemelisin.”"

    h "“Çok garip gerçekten… Ne yapacağız?”"

    v "“Ben…”"

    "Aklımda bir fikir vardı. Belki beni diğer işlerimden alıkoyacaktı ama olsun."
    "(Kardeşimden önemli değil.)"
    "Hem hala olayların kilidini açacak anahtarın Kioko olduğunu düşünüyordum; o yüzden onu korumak, yanında olmak da bir nevi işti."

    v "“Kioko, benim odamda yatmak ister misin?”"

    show Kioko Concerned with dissolve

    k "“Sana yük olmayı istemem.”"

    v "“Lütfen saçma şeyler söyleme, sen benim kardeşimsin.”"

    k "“Ama işine engel olmaz mıyım?”"

    v "“Hayır, önceliğim sizsiniz.”"

    show Haru Troubled with dissolve

    h "“Benle… Benle yatabilir isterse. Odamı paylaşabilirim.”"

    "Gözlerimi şaşkınlıkla kırpıştırarak Haru’ya döndüm. Bu bir ilkti."
    "Yani… Yalnız kalmak isteyip Akademi’den kaçmaya çalışması gözümde daha olasıydı."

    v "“Olmaz. Ya senin de başına bir şey gelirse?”"

    show Haru Sideway with dissolve

    h "“Hey… Tamam biliyorum senin kadar güçlü değilim ama o kadar da ne yaptığımı bilmiyor değilim.”"

    "Haklıydı."
    "Haru aslına bakılırsa hızlı mana yenileme yeteneğiyle içinde çok fazla potansiyel barındıran bir insandı."
    "Tabii bu avantajını kullanmayı biliyor muydu, orası ayrıydı. Evet, pratik büyülerde üstüne yoktu fakat iş kompleks büyülere gelince kelimenin tam anlamıyla patlıyordu."
    "Yine de hızlı olması sayesinde başlarına bir şey gelse dahi oradan kardeşini de kendini de çıkarabileceğine emindim."

    v "“Pekala… Öyle olsun. Fakat dikkatinizi çeken olağandışı en küçük olayda bile beni haberdar edin. Çekinmek yok.”"
    v "“Anlaştık mı?”"

    "İkisi de onaylarcasına kafasını salladı."

    hide Haru with dissolve
    hide Kioko with dissolve

    "(Ne olur ne olmaz, en iyisi mi bu odaya birkaç tane koruyucu totem koymalı…)"

    scene academyhallwaynight with fade

    "Toplantıya geç kalmıştım."
    "Ve Akademi’yi başlı başına iyi bilmediğim için ışınlanamıyordum da."
    "Aynı zamanda Asha yabancıların yanında kullandığımız büyüler konusunda dikkatli olmamızı, onları ürkütebileceğimizi söylemişti."
    "(Koca koca binalar dikmeye, ulaşım araçları adı altında devasa kütleleri bir oradan bir buraya hareket ettirmeye bayılıyorlar fakat en basit büyülere bile hakim değillerdi, öyle mi?)"

    scene academyhallwaynight with dissolve:
        xpos 0.2 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    "(Pekala, burası olmalı.)"

    play sound doorknocking noloop

    "Kapıyı tıklattıktan sonra cevap beklemeden içeri girdim."

    scene 4knights with fade

    pause 1.5

    scene 4knights with fade:
        xpos 0.9 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade:
        xpos 0.6 ypos 1.5 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade:
        xpos 0.3 ypos 1.8 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade:
        xpos 0.1 ypos 1.3 xanchor 0.5 yanchor 1.0 zoom 2.0

    pause 1.5

    scene 4knights with fade

    "Gözüme ilk çarpan odanın en gözler önünde olan kanepesine yerleşmiş birkaç tanımadık yüzdü."
    "Sarışın üçlünün prensler, ötekininse Grandük olduğu kanısına varmıştım."
    "Hareketsiz ve sessiz durmaları kaldığımız köydeki çiftçinin vitrin bebeklerini anımsatmıştı bana."
    "Her biri göz kamaştıracak kadar güzel insanlardı ama ben de böyle şeylerden etkilenecek biri değildim."

    a "“Vena! Sonunda geldin, biz de seni bekliyorduk.”"

    "Asha’nın neşeli bir sesle konuşmasıyla Grandük’ün de elinde tuttuğu kağıdın arkasından homurdanması bir olmuştu."

    gr "“Evet, bir oda dolusu insan bir olmuş sizi bekliyorduk.”"
    gr "“Hem geç kalma cüretinde bulunuyor hem odaya izin istemeden dalıyor, üstüne üstlük özür dilemiyor ve tahtın varislerine saygısızlık ediyorsunuz.”"
    gr "“Ki bunun bizim ülkemizde ölüm cezası vardır.”"

    "Şaşkınlıktan ağzım açık kalmıştı."
    "Aynı gün içerisinde bu iki oluyordu."

    scene academyhallway with flash
    show Orphina Gritting with dissolve
    pause 2.0
    hide Orphina
    scene 4knights with flash

    "Nasıl bir yere gelmiştik biz böyle? Şuna bak, öldürecekmiş beni! Hele hele!"

    v "“Senin ülken, senin kralın, senin tahtın… Benim değil. Bunların hiçbiri beni bağlamıyor ne yazık ki.”"

    "En sonunda bana bakma tenezzülünde bulunmuştu. Mavi gözlerinde saklamadığı soğuk bir öfke vardı."
    "Sanki bir düşmanı süzüyor gibiydi. Bu düşünce elimde olmadan suratımda alaycı bir gülümseme belirmesine sebep oldu."

    gr "“Size hangi ülkeye, krala, tahta sığındığınızı hatırlatmak isterim {i}Leydi Vena{/i}.”"

    "İsmimi söyleyişinde kinayeli bir tını vardı."

    u "“Sorun değil. Doğru diyor zaten.”"

    "Grandük derin bir iç çekmiş ve tekrardan önündeki kağıda odaklanmıştı."

    gr "“Bu fırsatı genç hanıma bir ders vermek adına kullanmanızı öneririm Ekselansları, zira yılanın başını küçükken ezmeli.”"

    "(Genç hanım mı?)"
    "Burada genç olan biri varsa o da bu kendini bilmezdi."

    v "“Üzülerek söylüyorum ki {i}Grandük{/i}, ben 386 yaşındayım.”"

    "Gözlerinde şaşkınlığını belli edercesine küçük bir ışıltı belirmiş, ardından sanki hiçbir şey olmamış gibi önündeki dosyaya ilgisini vermişti."

    gr "“Ne güzel, ne güzel! Bu yaşınıza gelmiş ama adabımuaşeretten payınızı alamamışsınız.”"

    "(Bakalım hayatına bir domuz olarak devam ederken de adabımuaşeretten bahsedebilecek misin?)"

    a "“Ahem!”"

    "Manamın etrafımda toplanmaya başladığını fark edince Asha araya girme gereği duymuştu."

    a "“Gerilmeyelim lütfen, ne de olsa birlikte çalışacağız.”"
    a "“Dük, lütfen Vena’nın başka bir dünyada doğduğunu unutmayın. Kendisi saygısız bir insan değildir, hatta Waceera’nın en sevdiği öğrencilerinden biriydi.”"
    a "“Ve aynı zamanda burada bana en çok yardımcı olan insan.”"

    gr "“Hah…”"

    a "“Vena… Sana beraber iş yapacağımız insanları takdim edeyim.”"
    a "“Ekselansları Birinci Prens Lionel Nicolas Asquith…”"
    a "“Ekselansları İkinci Prens Landon Cyril Asquith…”"
    a "“Ekselansları Üçüncü Prens Andrel Xerxes Asquith…”"
    a "“Ve Ekselansları Pertone Grandükü Marley Augustine Arkwright.”"

    scene academylivingroom with fade
    show Marley Irritated at right with dissolve

    m "“Cyril ve Xerxes’in unvanlarını unuttun.”"

    show Asha Confused at left with dissolve

    a "“Pardon?”"

    show Marley Sighing with dissolve

    m "“Cyril Credale, Xerxes de Millford Dükü.”"
    m "“Ve Lionel de Brefcaster.”"

    "Başkalarını haşlasa da kendisinin prenslere isimleriyle hitap etmesinden Grandük’ün çocuklara yakın olduğu anlaşılıyordu."

    show Asha Default with dissolve

    a "“Ah… Anlıyorum.”"

    "(Neden kendini ezdiriyorsun Asha?)"

    hide Marley with dissolve
    pause 0.5
    show Cyril Irritated at right with dissolve

    c "“Lütfen onu dinlemeyin, gerçekten önemli değil.”"

    hide Asha with dissolve
    pause 0.5
    show Lionel Default at left with dissolve

    l "“Evet, böyle şeylerle vakit de kaybetmeyelim.”"
    l "“Sanıyorum burada olmamızın sebebini hepiniz biliyorsunuz.”"

    "Salondan onaylarcasına sesler yükseldi. Bense bir köşeye geçip sessizce izlemeye koyuldum."

    l "“Grandük, rica etsem durumu izah edebilir misiniz?”"

    hide Cyril with dissolve
    hide Lionel with dissolve
    show Marley Default at truecenter with dissolve:
        zoom 1.5

    "Grandük sonunda elindeki kağıdı indirmiş ve laubali bir hareketle önündeki masanın üstüne fırlatmıştı."
    "Bacak bacak üzerine atarken odadaki herkesi adeta yukarıdan süzüyordu."
    "(Komik… Aralarındaki rütbesi en düşük kişi o fakat en kibirlileri de o.)"

    m "“Whemond, Kızıl Körfez’in göz bebeğidir. Bilmiyorsanız öğrenin.”"
    m "“Whemond’da bir şeylerin ters gitmesi demek, buradaki deniz ticaretinin sekteye uğraması demek.”"

    show Marley ClosedEye with dissolve
    m "“Deniz ticaretinin sekteye uğraması demekse sadece bizim değil, bizimle ticari anlaşmaları olan ülkelerin de sinirlenmesi demek.”"

    "Dediklerini bir çocuğa anlatır gibi sabırla, tane tane açıklıyordu fakat gözlerindeki o huzursuz parıltı tahammül seviyesinin son raddede olduğunu göstermekteydi."

    show Marley Default with dissolve

    m "“Whemond’ın yüzyıllardır bozulamayan huzuru şu geride bıraktığımız sene boyunca birtakım alışılagelmedik olaylar silsilesiyle çalkalanıp durdu.”"

    show Marley Frowning with dissolve

    m "“Ve bu ne tesadüftür ki sizin varışınızın hemen öncesi.”"

    "Dramatik bir şekilde sözlerini kesip odayı sessizlik kaplamasına neden oldu. Bunu fırsat bilen Asha da konuşmaya başlamıştı."

    show Marley Default:
        xalign 0.5
        linear 1 xpos 0.8
    show Asha Default at left with dissolve

    a "“Whemond’ın yüzyıllarca yıldır huzuruna karşın bizim binlerce yıllık huzurumuz…”"

    "Grandük sorar bir ifadeyle Asha’ya dönmüştü."

    m "“Binlerce? Sadece bin yıldır burada değilsiniz diye biliyorum.”"

    hide Marley with dissolve
    hide Asha with dissolve

    "(…Ah.)"
    "Söyledikleri kısa bir süre de olsa kafamda yankılanmıştı."
    "Neden hala şaşırıyordum bilmiyordum, Dış Dünya’da doğup büyüdükleri son bir aydır sır değildi zaten."
    "Waceera’nın bana yalan söylemesi miydi canımı sıkan?"
    "(Hayır, hayır… Onun bir bildiği vardır elbet. Öyle körü körüne hareketlerde bulunmaz.)"
    "Odaya göz gezdirdim."
    "Işık Hamillerinin birçoğunun Asha kadar yaşlı kadınlar olduğunu düşünürsem onların da Dış Dünya’da doğmuş olmaları muhtemeldi."
    "Peki onlar neden daha önce hiç seslerini çıkarmadılar?"
    "Cevabı aslında gün gibi ortadaydı, sadece kabullenmekte sıkıntı yaşıyordum."
    "(Çemberler…)"
    "Bu bulutlu düşüncelerden kendimi kurtarmak için Dük’ün söylediklerine odaklanmaya karar verdim."

    scene blackscreen with fade
    pause 1.5
    scene academylivingroom with fade

    "Toplantının üstünden bir süre geçmiş, bizlere ne konularda yardım istenildiği anlatılmıştı."
    "İlgimize çarpan olağan dışı hareketleri hemen kendileriyle paylaşmamızı istiyorlardı."
    "Aklıma Kioko’nun bugün yaşadığı olay gelmişti fakat bizleri göz hapsinde tutmak isteyen insanlara ne kadar güvenebilirdim, muammaydı."
    "Kardeşimin Kara Katliam’la ilişiğini bizim dışımızda bir tek Asha ve Zuri biliyordu."
    "Göz ucuyla Almasi’ye baktım."

    show Almasi Default with dissolve

    "(Onu bu kurtların önüne atmaya niyetim yok.)"

    hide Almasi with dissolve

    show Marley Default at truecenter with dissolve:
        zoom 1.5

    m "“…Evet. Böylelikle bugünkü toplantımıza noktayı koyuyorum.”"
    m "“Fakat son olarak… Ben veya Lionel ile direkt çalışacak iki kişi lazım. Raporları getirip götürecek…”"
    m "“Hem cadı tarafının hem de bizim tarafımızın sözcüsü olacak iki insan.”"

    "(Cadı…)"
    "Dış Dünya’ya vardığımızdan beri bize böyle sesleniyorlardı: Cadı."
    "Bu kelime bazen ağızlarından tükürürcesine çıkıyor, öteki zamanlardaysa sanki herkesin bildiği bir erdemmişçesine izah ediliyordu."
    "Ama bir şeyin farkındaydım."
    "Her ne tür bir bağlamda kullanılırsa kullanılsındı, her zaman dışlayıcı bir tınısı vardı."
    "Elimde değildi, rahatsız oluyordum."
    "…"
    "Dük, şöyle bir Asha’ya bakmıştı."

    show Marley Mocking with dissolve:
        zoom 1.5

    m "“Kardeşiniz olduğundan bahsetmiştiniz. Sanırım siz ve o bizimle çalışacaksınız, yoksa işiniz başınızdan aşkın olduğundan başka birini mi tercih edersiniz?”"

    "Ne kadar kibar konuşsa da laflarının altında bir kinaye yatmaktaydı resmen. Elimde olmadan dişlerimi sıktım."
    "Asha ise adamın dediklerine gülmüştü."

    a "“Ahaha, hayır. Ben çalışacağım lakin kardeşime, yani Zuri’ye gelirsem… O kimseyle çalışabilecek durumda değil. O yüzden…”"

    hide Marley with dissolve

    "Sırtımda bir el hissettim."
    "(Şaka yapıyorsun Asha.)"

    a "“Vena, kimle çalışmak istersin?”"

    "Bir saniyeliğine şaşkınlıktan nefesimi tutmuş, ardından hızlıca kendimi toparlamıştım. İnanılır gibi değildi ama Asha’yı da ortada bırakmayacaktım."

    v "“Önce sen seç.”"

    a "“Önden gençler.”"


    menu:
        "Tartışmanın bir anlamı yoktu. Tekrardan koltukta oturan figürlere baktım ve kararımı verdim."

        "Lionel":
            jump venalionel

        "Marley":
            jump venamarley



label venalionel:


    "Kraliyet ailesiyle arayı iyi tutmaya çalışmak bir Dük’e yaranmaktan çok daha faydalı geliyordu kulağa."
    "Ve bu Asha’ya bırakmamam gereken bir görevdi."

    v "“Öyleyse Birinci Prens ile birlikte çalışacağım.”"

    show Lionel Laughing with dissolve

    l "“Peki o zaman. Güzel oldu, iyi anlaşabileceğimizi düşünüyorum.”"

    "Sorarcasına tek kaşımı kaldırsam da dediklerine daha fazla açıklık getirmemişti."

    hide Lionel with dissolve
    show Asha Default at left with dissolve

    a "“Ben de Grandük ile birlikte çalışıyorum o halde.”"

    show Marley ClosedEye at right with dissolve

    m "“Yarın Arkwright Şatosu’na gelmeniz için size bir araç göndereceğim.”"

    hide Marley with dissolve
    hide Asha with dissolve
    show Lionel Default with dissolve

    l "“Ben de size Saray’a gelmeniz için bir tane göndereceğim leydim.”"

    "{i}Leydi{/i}… Daha şehre varalı bir gün bile olmamıştı fakat şimdiden buradaki herkesin unvanlara garip bir şekilde takıntılı olduğunu fark etmiştim."

    v "“Sabah görüşürüz öyleyse, {i}prensim{/i}.”"

    show Lionel Laughing with dissolve

    "Lionel cevabıma gülmüştü."
    "Samimi bir gençle vakit geçirmek en azından yanındaki huysuzla bir gecede bin sene yaşlanmaktan iyiydi."
    pause 3.0
    return

label venamarley:

    "Asha’yı Grandük’e bırakamazdım. Onu çiğ çiğ yiyeceğine şüphem yoktu."
    "(Aynı zamanda biri bu adamı denetim altında tutmalı ki destek yerine köstek olmasın.)"

    show Marley Sighing with dissolve

    "Gözlerimi kısıp söz konusu kişiye şöyle bir süre baktım. O da kendisini seçtiğimi anlamış olacaktı ki derin bir nefes çekti."

    v "“Ben Grandük ile çalışayım o halde.”"

    show Marley Troubled with dissolve

    m "“İkimize de işkence çektirmeyi bu kadar mı istiyorsun?”"

    show Marley Irritated with dissolve

    m "“Hadi bakalım. Öyle olsun. Yarın sabaha seni alması için buraya bir araç göndereceğim.”"

    show Marley Sighing with dissolve

    m "“Olur da ona da geç kalırsan Arkwright desteği bu projeden elini kolunu tamamıyla çeker.”"

    "Cüretkar bir şekilde gülümsedim."

    v "“‘Geç kalmak’ benim lügatımda olan bir şey değil, yaptığım büyüler gereksiz yere kısıtlanmadığı müddetçe.”"

    hide Marley with dissolve

    "Asha dediklerimiz üzerine iç geçirmişti."

    show Asha concerned with dissolve

    a "“Siz ikiniz birbirinizi boğazlamadan bu süreci atlatırsanız iyi olur.”"

    show Asha ClosedEye with dissolve

    a "“Her neyse, geç oldu. Dağılalım artık.”"

    pause 3.0
    return



return
