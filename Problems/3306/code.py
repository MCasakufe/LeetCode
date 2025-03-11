class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        def is_dict_valid(letters_dict):
            vowels = ['a', 'e', 'i', 'o', 'u']
            consonants_count = letters_dict.get('consonants', 0)      
            if consonants_count != k:
                return False        
            for vowel in vowels:
                if letters_dict.get(vowel, 0) == 0:
                    return False      
            return True
    
        
        valid_cases_counter = 0
        for word_length in range( 5 + k, len(word) + 1):
            letters_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'consonants': 0}
            for char in word[:word_length]:
                if char in letters_dict:
                    letters_dict[char] += 1
                else:
                    letters_dict['consonants'] += 1
            if is_dict_valid(letters_dict):
                valid_cases_counter += 1

            for i in range(1, len(word) - word_length + 1):
                if word[i - 1] in letters_dict:
                    letters_dict[word[i - 1]] -= 1
                else:
                    letters_dict['consonants'] -= 1
                if word[i + word_length - 1] in letters_dict:
                    letters_dict[word[i + word_length - 1]] += 1
                else:
                    letters_dict['consonants'] += 1
                if is_dict_valid(letters_dict):
                    valid_cases_counter += 1
        return valid_cases_counter
            

            


if __name__ == '__main__':
    solution = Solution()
    word = "bcbcciiccibcbooouoiciuuoueeicoouucdcddeduiuiubboodudeacdieeueocaiadboudduoiociueeicidcuububaeeiuacaaubccauaicoobediaceboacoeebdciudadiuaiaieeeuabiicoecaaidaeidcuuaubbeiceecuuodcaeibdacoiiibidebdauaiuciddcuaueodeddicduoccciibucddoaedcoaucoiiuooeidaeibcedciadbiucibaoebuueiciiabbauaaidacioeadeaeeuiudcdaedduoeceaacebeieiuocuoaeiaocccudbbaeoccobcciecbccabobibouoaiccabcicdducoiadeuuodoceoeccicauedbbiebuiiecaeiaaaociddcudeueuuauceacoedicaeccobcoedoeoddecoiudidaobdboauebdecdoudidiooieaiedcuiocuiiudaaeeecuuiibaobceioiucoeaobbocdbocodeeouddedeeaiuoibaacuieeeiaoeaoauobbaooucuaduoaciacddaieobebabobceidiiodeobdbuciccaieeooudbabebuuabaobduebudadidauoibabacduiiaicdodbeoiabdiceciioooduuiddaoiiccbaoeoeoaaaidcicdoooeiciodiebaaudeuocabaaebaiiaeeaaiiadbciecuiabbducobduiueiuidaooaaodeddacbideeeddbbooidobdbdeacauooedcboeabecibiabucoccdooecoaeuoocebdooeuccdceaouoiabaieeodubdudeooeuucicbcoubuieideoiuaobobecdaduuidbcioidaaocdcbouobudabcacobceeoiaboouddcodabboueiodudadocdbuccodaoobbeoccocdcocoiibodeoubibaudcdadoaobouaieueouioeuecbuboboebuiaoieiooooubdobiuoeouucduuaeiebuuibciiiccaddduaauuobeiuodauiaaocuaabddaabcadoiaooibaiaocoeuuaieiueiaeauaeooeoiiduceauuobbobceobieobodbedaooaouucdbceeucbbiaudbadduaidbcbadcucudaocbdbuceeuadibiibccoucuueeuudbuubbaicecbabiaiiaaucdubbbboedceubccoocauioeiceieccoiiaecdaiccociuiocuuebucuoeeiubibaidudbibecdaaiddduiuceuueebeodbuoudacbceeciabcocdecbbebbacbeeiocioiedccooocieabobdiecuobuoueicuidebbaboiuuuocabeieoocbcidodocdaaeaaiaicaodbudioeadcieacuccddociiddeobibuddibibbbuccccacaoddbeoeduobuoboiecoocbeodicbibecoccdcidaoabeuuueiduibododiduauaueoaiudbdcodbubcacbioobacboiedodbbdcaecbacebcobccooauaudcuiiuouedicuccuceeccedddbiecucecebuuuuboaiaiaooebbeuoeiddicocaooauauuiuueuioiauaabuauaebdcaaaoobiouiiieouoiubibcdiiociocaecadaiaauoaibeeaacueddeubooaibaeaobadeeaaabaocucboocbaiaucicidaebuddicodeediouoiecaiiuoiuaebbadabeoboiciuieiiucccccobbiceaaobeeeebduuiaocddeuaoaobuicuioaobiciaiboeoabcuubdioidbaiboabbuaaabecadiiebeaebbdoacacicdacuaauobcodeaouuaaiiceadbieuiceabccbboeeeoibecueiaiioubdecbbdobdooiaebecucibcudbbodbeudibobdaiaoieieddbbaaeduoiocbbobdducbdeiadducaeuieoouebdauuaudubdiaeiubaaaioeoioocbccbccdcceaduibeaoebaeecdodbueiudecacauboecddacbdbdebdaoooidoiiiciucaoadbauoudbabbuaiiaaoouieuieebadoiaiiudcuiucbiecioudicioudcaoauiecboeiaaaaiaaiaoubcoidaeueduduaubbocoaiuudbubaodcooaoduacbooaiouacadebcuoibeuoouibbabaeuacidacoiuceieeuceeuuacuebuiiiaiucbbebcbecbicduibeoaieabiaeebddciboabbecedauaabceoiiiaabbiuobbeaabibdcaoaodueaoicoadubcbuboibebubiaacoiedoodooaabdcbiududibeedioiuuauaiieebuobiocdidedbicaaciuceeddocdidaoaeiiueuacadeaeodoceoaeoaoucdaacouiebeiaaoecbiicdaodidaacdcdbbaidbauiiuoaiidiceucciuobcbdabecuaubiddebuiaiccbocicbabodccoeiieudaeueieuacoccbcoidcdaouuoioiudbuuuioddooceucbucoaodcuceueeboeciooibbdoodcdaueaboiaedooaidccauioocuibubibucbuiccdaocdcioiecuibbudedooauiiaddibcbcbcccddaeuudbddioobbcoeaibiceuiuoebcbuaooeeebuoiibdbicubiioucdububibeccuacdboddcedcbdabbeebdaeoioabcubaeaiabaodiibuaebaooodobiuiocaabdacdoeuoicucieuboacuceideeuoadebuoadbiaducooueoaaiiiouicioidieoaucadacbdddioaiacueiaabuubciuddcacodoocboaubbddaboucoeoodueauabeiaiedauddiiceccoeuueodccuauiccodocoaauuceduedcoidouuiaicbiduaauouodoodueaueeaidaoueecicddbobdbaouiiecaebodubceeacdebeddobccabeobucddcauoaocueubicebbebeccucuiuacabbdcouiedaooudeiooiudduedccciedbeiducbdicabieedcbcedauuudbbuuddcobaaaeicaebeiobdeccduiibecadooudiobcaidodaobicebddiuaduuooudcaoaceoiiaoudcccciaaaauubuooaeubuuooeuadedobucuueodococucieoieuabboicducuoeoauecaooiueauaoceocueedoacibaoiduiebicuceooaoedbbceuaoiuaiccbaccuoccaecaiuooioeebodeebcdoueddoiideeocudceciobiidbebcubcbbbadoiudbiccduoebcbobcecoadddboioiiiiiiauciababcidodbicboeeiuouoibieocdeduiieceocboaucibooidoibbciedduuiieucaiducuoboucddaocduoauiiiudioobduicecoaadbcaaecoieodiaaeieubcauebbabaduceueeaeoeddueiccdudebdciiocuobbdcdabebddidoaduauudecbbauaieocucobeuaaiedbdcaoebocbedddiabiibduuueoioaabocedebdaadceeeiabaooadcdbucaaoabibieueebiudcdoeaduaoacuucaucbeuididibaceobbadoaeiuciudcudeiouieeueobouucueaducuabiibiuuadoccabdbcdaboeucecbaciiacioioaaeaucidcubabceauubdidcdcduuoceuboabcuoeaabbuoioeuccauiuudcbdobedbibiubccdeceeuoiuccabiocibdoocdboouabbubdeoecioadaeoboddbbbubaeaobcucauaidaeccaedcoooeeddboaidbbideeaooudeubeieiieddaoodcaubdiciiccuidudidiediuaidabeiiedbbeibdbucebcddcouoiodocbbaueddouicieebbdbddbeobuediadoaduoodoebeaecbcoueedaieccuubaaboaoieddidcieccbdiacdiicbuobdocbacueiobdcoducuiudebdedduoieuudeaudddaeiooueaeauaoaodibauddaaudbuadaodaubdidacbcoouoibdocobuodauuoucoobbiaueicdobidbabuuiduiouaabcbdebbcedbicicbeauuaucodicadeobuiecceoiccaacobcdiaoicabudbbbuacccabbaueeobdoucabaodbcbbaicuabcidicedcaedodcbubbicbaaadbbdiauaueciubbddbueedibbubiudbaciuuiibdaiaiocdicoaauabuubudboouiudeioaaadcaeebddebodouiioaecucdcaaibueboiauiiedoabdoddieodbceididbauocabocebdaieaduucdoiddceouidbucbauidaeaiodeboboacbieoubicecucaeieuibcouoeeaaiciuadadcbccedccuodeeodcooibeicuiubdbaeiedeabbdubebdbeiecdaiababoacuabaoodbauaacobioidecueueoaeceoecoodeuiedeiiebedbbaibiabucbdbuoauucdauobocaocecbeueaaccoacuouiieioaeibeeacubceddeuubbudiaudibddeaauiudidicaoiuebuuudbidoucacbebcaiuioobe"
    k = 890
    print(f"Input: word = {word}, k = {k}")
    result = solution.countOfSubstrings(word, k)
    print(f"Output: {result}")
        