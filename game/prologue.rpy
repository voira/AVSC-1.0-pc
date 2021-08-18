define sin = ("Sinirli Bir Ses")
define sak = ("Daha Sakin Bir Ses")
define ea = ("Ealdwine")
define ma = ("Marley")
define wa = ("Wilbur Asquith")
define li = ("Lionel")
define fastdissolve = Dissolve(0.1)

label prologue:
    scene shd with dissolve
    ""
    scene blackscreen with fade
    centered "Nerede olursam olayım, \n {p}
    Vakit ne olursa olsun, \n {p}
    İstediğinde orada olacağım. \n {p}
    {b}Çağırdığında{/b} uyanacağım."

    ""
    scene hqin with fade
    ""

    sin "“Aptal...”"
    sin "“Her şeyi yüzüne gözüne bulaştırdı.”"

    sak "“Kendisinden bir iz var mı?”"

    sin "“Hayır! Manasının izi bir anda kayboldu. Sanki yer yarıldı da içine girdi.”"
    sin "“Kim olduğunu bile bilmiyorum zaten.”"
    sin "“Aptal! Aptal! Eminim ki bu beceriksizlikle kendisini de öldürüvermiştir.”"
    sin "“...”"
    sin "“Ealdwine.”"

    ea "“Dinliyorum.”"

    sin "“Gözünü dört aç, Vivian’a da söyle. Eğer ki yaşıyorsa onu her türlü bulmamız lazım.”"
    sin "“Ötmeye başlamadan önce.”"
    ""
    # Text box will disappear slowly here.

    scene hallbg with fade

    "Sabrımın artık son demlerindeydim."
    "Seneler boyunca büyük bir ustalıkla sakladığım duygularım şimdi, kralın önünde, taşarcasına maskemin kırıklarından çıkmaya çalışıyordu."
    "Öfkemi yatıştırmak için taht odasında bir ileri bir geri yürümek harici yapacak bir şeyim yoktu."

    ma "“Şehirde ardı kesilmeyen ölüm vakaları görülmeye başladı. Bir tane seri katilimiz olsa neyse…”"
    ma "“Heyhat, zavallıların ölüm şekline bakıldığında iki farklı oldukça tehlikeli kimseyle baş başayız.”"

    "Adımlarımı durdurdum ve odaya şöyle bir göz gezdirdim. Beni dinleyen gözlerin bu kadar ilgisiz olduğunu fark etmek ne denli acıydı."

    ma "“Bir tanesi kurbanlarının yaşam enerjisini çalıp gidiyor. Ötekininse yaptığı canilikleri anlatmaya dilim varacak gibi değil.”"
    ma "“Öyle ki bunları yapan bir insan mı yoksa gözü dönmüş bir hayvan mı, ayırt dahi edemiyorum.”"

    "Kralla tekrardan göz göze geldik. Yüzünde donuk bir ifade vardı, sanki dediklerim bir kulağından gidiyor ve diğerinden çıkıyordu."
    "Üç uzun adımda aramızdaki mesafeyi kapatıp önünde diz çöktüm."

    ma "“Lordum, size yalvarıyorum. Bunun üzerine düşünün.”"
    ma "“Onların buraya gelmesine izin vermeyin. Sadece ve sadece karışıklığa sebep olacaklar-”"

    wa "“Bu kadarı yeter Marley.”"

    "Yetmezdi. Yetemezdi. Kendisi ne kadar vasıfsız bir insan olsa da Aelthus’u da peşinden mezara sürüklemesine izin vermeyecektim."
    "Dişlerimin arasından sinirlice konuşmaya başladım."

    ma "“İnsanlar Khaunet’in dönüşünü konuşuyorlar. Şafak Şövalyelerinin ne kadar gereksiz bir birim olduğundan dert yanıyorlar.”"
    ma "“Bir de yetmiyormuş gibi ortalıkta kendilerine ‘avcı’ diyen iki üç zibidi koşuşturuyor arbaletleriyle.”"
    ma "“Hepsi de ne hikmetse bu kadınların Whemond’a varışı öncesinde oluyor.”"

    wa "“Marley, babanı sevdiğimden bu yersiz çıkışlarına ara sıra göz yumuyorum. Ama bazen çok fazla oluyorsun genç adam.”"
    wa "“Toplum olarak bir sihir devrimine ihtiyacımız var ve bunun için şans ayağımıza kadar geldi.”"
    wa "“Kadim büyüyü öğrenip araştırabiliriz, geliştirebiliriz.”"
    wa "“İyileşmeyen hastalıkları rafa kaldırabiliriz, ölümle vedalaşabiliriz-”"

    ma "“Aklınız hala karınızda! Onu göz önünde bulundurarak konuşuyorsunuz. O öleli çok oldu, bırakın artık peşini.”"

    "Ne yazık ki dediklerimin ağır olduğunu laflar ağzımdan çıktıktan birkaç saniye sonra anlamıştım."
    "Senelerdir ruhsuz bakan gözler bir anda öfkeyle parıldayarak beni gelen azardan haberdar etti."

    wa "“Sakın bir daha benimle böyle konuşayım deme. Pişman ederim seni.”"

    "Sesinin tonu o sımsıcak odaya kışı getirmişti."
    "(Neden şaşırıyorsam, gerektiği zamanlarda otoriter bile olamayan bir insandan kral olamazdı zaten.)"
    "Oğullarından Xerxes ile Cyril’in hafifçe irkilmesi, Lionel’inse yüzünde oluşan o hınzır gülümseme gözümden kaçmadı. Yüzümü buruşturdum."

    wa "“Bu konu burada kapanıyor artık.”"
    wa "“Cadılar Whemond’a gelecek, son kararım budur ve tartışmaya kapalıdır.”"
    wa "“Sen de canını bununla sıkacağına emrinde olan Şafak Şövalyelerine işlerini daha iyi yapmalarını öğütleyebilirsin, yoksa işi Lionel’e devredeceğim.”"

    show Lionel Smiling at left with easeinleft

    li "“Bana güvenebilirsin, baba.”"

    "(Sinsi velet…)"
    "Yavaşça, kafamı toplamaya çalışarak doğruldum."

    ma "“Pekala, her zamanki gibi emrinize amadeyim, ne kadar farklı görüşlerde olsak da.”"
    ma "“Bu konu hakkında daha fazla sesimi çıkartmayacağım ama bir şartım var.”"
    ma "“Beni de Lionel ile birlikte cadıların gözetmeni olarak atayacaksınız.”"

    "Böylelikle hem Lionel’e hem de cadılara aynı anda göz kulak olabilecektim."

    show Lionel Frown with dissolve

    wa "“Vazgeçmiyorsun hiç. Aynı baban gibisin. Her neyse, nasıl istersen öyle yap ve daha fazla başımı ağrıtma.”"
    ""

return
