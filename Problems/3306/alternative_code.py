from collections import defaultdict

class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """

        length_of_word = len(word)
        vowels = ['a','e','i','o','u']
        prefix_counts = {vowel: [0] * (length_of_word + 1) for vowel in vowels}
        prefix_counts['consonants'] = [0] * (length_of_word + 1)

        for index, current_char in enumerate(word):
            for vowel in vowels:
                prefix_counts[vowel][index + 1] = prefix_counts[vowel][index]
            prefix_counts['consonants'][index + 1] = prefix_counts['consonants'][index]
            if current_char in vowels:
                prefix_counts[current_char][index + 1] += 1
            else:
                prefix_counts['consonants'][index + 1] += 1

        valid_substring_count = 0
        minimum_substring_length = 5 + k
        for start_index in range(length_of_word):
            min_end_index = start_index + minimum_substring_length - 1
            if min_end_index >= length_of_word:
                break
            for end_index in range(min_end_index, length_of_word):
                consonant_count = prefix_counts['consonants'][end_index + 1] - prefix_counts['consonants'][start_index]
                if consonant_count != k:
                    continue
                if all(prefix_counts[vowel][end_index + 1] - prefix_counts[vowel][start_index] > 0 for vowel in vowels):
                    valid_substring_count += 1

        return valid_substring_count
    
    


if __name__ == '__main__':
    solution = Solution()
    word = "bcbcciiccibcbooouoiciuuoueeicoouucdcddeduiuiubboodudeacdieeueocaiadboudduoiociueeicidcuububaeeiuacaaubccauaicoobediaceboacoeebdciudadiuaiaieeeuabiicoecaaidaeidcuuaubbeiceecuuodcaeibdacoiiibidebdauaiuciddcuaueodeddicduoccciibucddoaedcoaucoiiuooeidaeibcedciadbiucibaoebuueiciiabbauaaidacioeadeaeeuiudcdaedduoeceaacebeieiuocuoaeiaocccudbbaeoccobcciecbccabobibouoaiccabcicdducoiadeuuodoceoeccicauedbbiebuiiecaeiaaaociddcudeueuuauceacoedicaeccobcoedoeoddecoiudidaobdboauebdecdoudidiooieaiedcuiocuiiudaaeeecuuiibaobceioiucoeaobbocdbocodeeouddedeeaiuoibaacuieeeiaoeaoauobbaooucuaduoaciacddaieobebabobceidiiodeobdbuciccaieeooudbabebuuabaobduebudadidauoibabacduiiaicdodbeoiabdiceciioooduuiddaoiiccbaoeoeoaaaidcicdoooeiciodiebaaudeuocabaaebaiiaeeaaiiadbciecuiabbducobduiueiuidaooaaodeddacbideeeddbbooidobdbdeacauooedcboeabecibiabucoccdooecoaeuoocebdooeuccdceaouoiabaieeodubdudeooeuucicbcoubuieideoiuaobobecdaduuidbcioidaaocdcbouobudabcacobceeoiaboouddcodabboueiodudadocdbuccodaoobbeoccocdcocoiibodeoubibaudcdadoaobouaieueouioeuecbuboboebuiaoieiooooubdobiuoeouucduuaeiebuuibciiiccaddduaauuobeiuodauiaaocuaabddaabcadoiaooibaiaocoeuuaieiueiaeauaeooeoiiduceauuobbobceobieobodbedaooaouucdbceeucbbiaudbadduaidbcbadcucudaocbdbuceeuadibiibccoucuueeuudbuubbaicecbabiaiiaaucdubbbboedceubccoocauioeiceieccoiiaecdaiccociuiocuuebucuoeeiubibaidudbibecdaaiddduiuceuueebeodbuoudacbceeciabcocdecbbebbacbeeiocioiedccooocieabobdiecuobuoueicuidebbaboiuuuocabeieoocbcidodocdaaeaaiaicaodbudioeadcieacuccddociiddeobibuddibibbbuccccacaoddbeoeduobuoboiecoocbeodicbibecoccdcidaoabeuuueiduibododiduauaueoaiudbdcodbubcacbioobacboiedodbbdcaecbacebcobccooauaudcuiiuouedicuccuceeccedddbiecucecebuuuuboaiaiaooebbeuoeiddicocaooauauuiuueuioiauaabuauaebdcaaaoobiouiiieouoiubibcdiiociocaecadaiaauoaibeeaacueddeubooaibaeaobadeeaaabaocucboocbaiaucicidaebuddicodeediouoiecaiiuoiuaebbadabeoboiciuieiiucccccobbiceaaobeeeebduuiaocddeuaoaobuicuioaobiciaiboeoabcuubdioidbaiboabbuaaabecadiiebeaebbdoacacicdacuaauobcodeaouuaaiiceadbieuiceabccbboeeeoibecueiaiioubdecbbdobdooiaebecucibcudbbodbeudibobdaiaoieieddbbaaeduoiocbbobdducbdeiadducaeuieoouebdauuaudubdiaeiubaaaioeoioocbccbccdcceaduibeaoebaeecdodbueiudecacauboecddacbdbdebdaoooidoiiiciucaoadbauoudbabbuaiiaaoouieuieebadoiaiiudcuiucbiecioudicioudcaoauiecboeiaaaaiaaiaoubcoidaeueduduaubbocoaiuudbubaodcooaoduacbooaiouacadebcuoibeuoouibbabaeuacidacoiuceieeuceeuuacuebuiiiaiucbbebcbecbicduibeoaieabiaeebddciboabbecedauaabceoiiiaabbiuobbeaabibdcaoaodueaoicoadubcbuboibebubiaacoiedoodooaabdcbiududibeedioiuuauaiieebuobiocdidedbicaaciuceeddocdidaoaeiiueuacadeaeodoceoaeoaoucdaacouiebeiaaoecbiicdaodidaacdcdbbaidbauiiuoaiidiceucciuobcbdabecuaubiddebuiaiccbocicbabodccoeiieudaeueieuacoccbcoidcdaouuoioiudbuuuioddooceucbucoaodcuceueeboeciooibbdoodcdaueaboiaedooaidccauioocuibubibucbuiccdaocdcioiecuibbudedooauiiaddibcbcbcccddaeuudbddioobbcoeaibiceuiuoebcbuaooeeebuoiibdbicubiioucdububibeccuacdboddcedcbdabbeebdaeoioabcubaeaiabaodiibuaebaooodobiuiocaabdacdoeuoicucieuboacuceideeuoadebuoadbiaducooueoaaiiiouicioidieoaucadacbdddioaiacueiaabuubciuddcacodoocboaubbddaboucoeoodueauabeiaiedauddiiceccoeuueodccuauiccodocoaauuceduedcoidouuiaicbiduaauouodoodueaueeaidaoueecicddbobdbaouiiecaebodubceeacdebeddobccabeobucddcauoaocueubicebbebeccucuiuacabbdcouiedaooudeiooiudduedccciedbeiducbdicabieedcbcedauuudbbuuddcobaaaeicaebeiobdeccduiibecadooudiobcaidodaobicebddiuaduuooudcaoaceoiiaoudcccciaaaauubuooaeubuuooeuadedobucuueodococucieoieuabboicducuoeoauecaooiueauaoceocueedoacibaoiduiebicuceooaoedbbceuaoiuaiccbaccuoccaecaiuooioeebodeebcdoueddoiideeocudceciobiidbebcubcbbbadoiudbiccduoebcbobcecoadddboioiiiiiiauciababcidodbicboeeiuouoibieocdeduiieceocboaucibooidoibbciedduuiieucaiducuoboucddaocduoauiiiudioobduicecoaadbcaaecoieodiaaeieubcauebbabaduceueeaeoeddueiccdudebdciiocuobbdcdabebddidoaduauudecbbauaieocucobeuaaiedbdcaoebocbedddiabiibduuueoioaabocedebdaadceeeiabaooadcdbucaaoabibieueebiudcdoeaduaoacuucaucbeuididibaceobbadoaeiuciudcudeiouieeueobouucueaducuabiibiuuadoccabdbcdaboeucecbaciiacioioaaeaucidcubabceauubdidcdcduuoceuboabcuoeaabbuoioeuccauiuudcbdobedbibiubccdeceeuoiuccabiocibdoocdboouabbubdeoecioadaeoboddbbbubaeaobcucauaidaeccaedcoooeeddboaidbbideeaooudeubeieiieddaoodcaubdiciiccuidudidiediuaidabeiiedbbeibdbucebcddcouoiodocbbaueddouicieebbdbddbeobuediadoaduoodoebeaecbcoueedaieccuubaaboaoieddidcieccbdiacdiicbuobdocbacueiobdcoducuiudebdedduoieuudeaudddaeiooueaeauaoaodibauddaaudbuadaodaubdidacbcoouoibdocobuodauuoucoobbiaueicdobidbabuuiduiouaabcbdebbcedbicicbeauuaucodicadeobuiecceoiccaacobcdiaoicabudbbbuacccabbaueeobdoucabaodbcbbaicuabcidicedcaedodcbubbicbaaadbbdiauaueciubbddbueedibbubiudbaciuuiibdaiaiocdicoaauabuubudboouiudeioaaadcaeebddebodouiioaecucdcaaibueboiauiiedoabdoddieodbceididbauocabocebdaieaduucdoiddceouidbucbauidaeaiodeboboacbieoubicecucaeieuibcouoeeaaiciuadadcbccedccuodeeodcooibeicuiubdbaeiedeabbdubebdbeiecdaiababoacuabaoodbauaacobioidecueueoaeceoecoodeuiedeiiebedbbaibiabucbdbuoauucdauobocaocecbeueaaccoacuouiieioaeibeeacubceddeuubbudiaudibddeaauiudidicaoiuebuuudbidoucacbebcaiuioobe"
    k = 890
    print(f"Input: word = {word}, k = {k}")
    result = solution.countOfSubstrings(word, k)
    print(f"Output: {result}")
        