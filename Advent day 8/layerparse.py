def layerparse(data, w, l):
	pixels = w * l #size of image
	datastring = str(data) #input
	layers = int(len(datastring)/ pixels) #number of layers
	layer = [] 
	image = ''
	#zeros = 10000
	for i in range(0,layers): #parse layers
		layer.append(datastring[pixels*i:pixels*(i+1)]) 
		#if layer[i].count('0') < zeros: #part 1
		#	zeros = layer[i].count('0')
		#	l = i
	#print(layer[l].count('1')*layer[l].count('2'))
	for i in range(0,pixels): #for each pixel
		j = 0
		while int(layer[j][i]) == 2: #find first non-transparent pixel
			j += 1
		image += layer[j][i]
	#print(image)
	for i in range(0,150,25):
		print(image[i:i+25])





layerparse(222222220222222222222222222220200120222222222220222022222220222222222022122222221220222222122222221220222222221222020222222202122220202222222212022222122222222222222222222222222222202120222222222220222222222222222222222122222222221221222222022202222221222222221222122222222202022222222222222212022222122222220222222222222222222221201120222222222222222122222220222222222121022222220221222222022212220221222222220220120222222222222020212222222202122222022222221222222222222222222220200120222222222222222122222221222222222021022222222222222222122212221220222222222220021222222222022020222222222212022222022222222222222222222222222221202021222222222220222022222222222222222020122222220221222222022212221221222222220220120222222222022120222222222202112222022222222222222222222222222221221222222222222221222222222221222222222020022222220221222222022212222220222222221220221222222212222221202222222222022222122222220222222222222222222222210222222222222221222222222221222222222021122222221220222222222222222221222222222201120222222202022222212222222222122222122222220222222222222222222222211021222222222222222022222221222222222222222222221220222222122211222222222222222221120222222222222021222222222212202222222222222222222222222222222222221120222222222221222022222222222222222121122222221220222222122202222220222222220202121222222222222222202222222222202222022222122222222222222222222220220122222222222222222022222220222222222221122222221220222222102221220222222222221211022222222202122221222222222222002222222222122221222222222222222220200220222222222220222022222222222222222122222222221222222222212210222220222222220201122222222212022221222222222212222222222222221221222222222222222220200120222222222220222022222220222222222021222222220221222222222212220222222222222210220222222222222121202222222212112222222222021222222222222222222220220122222222222220222022222222222222222221222222222221222222222212220220222222022220220222222212122020012222222202112222122222020220222222222222222220222020222222222221222022222220222222222221222222221220222222122210222220222222221202022222222222222120212222222202222222122222022221222222222222222220201221222222222220222122222222222222222021222222221221222222102211222221222222120222021222222212222221012222222222112222221222021221222122222222222220202121222222222220222122222222222222222220022222220220222222012211222222222222022210221222222212122121002222222222212222021222120221222222222222222020210022222222222220222122222222222222222220222222220222222222012210222220222222221210020222222202222221122222222222012222221222021221222022222222222122220020222222222220222122222221222222222220122222222222222222122210220221222222222201022222222212022022012222222202022222220222020221222222222222222221210220222222222222222122222222222222222222222222222220222222212221221220222222221212222222222212122222102222222202022222221222221220222022222222222120200220222222222221222122222222222222222022122222221222222222002201221221222222122220120222222212022020002222222222022222220222021220222022222222222121201220222222222222222222222220222222222221222222222221222222222201220222222222122210221222222212122022112222222222122222221222222220222022222222222221201121222222222221220022222221222222222120222222220220222222022222220220222222121222222222222202022121102222222202102222122222221222222122222222222220101121222222222220220022222222222222222021022222221221222222222201220220222222122202222222222202022020220222222212202222222222122222222222222222222121111121222222222222222022222220222222222220222222221220222222222200220221222222021202020222222222222122101222222202002222220222020222222122222222222121021221222222222220222122222222222222222220222222222220222222202222222220222222021202220222222212122122220222222212112222221222022221222122222222222022021121222222222220220022222222222222222121222222220220222222112220202222222222222212021222222222022021121222222222112222122222220221222022222222222222221120222222222222222022222222222222222020122222220220222222022221200221222222120202220222222222222022021222222202022222122222021220222022222222222020102220222222222220221122222221222222222122222222220220222222002211221221222222221211120222202222022221002222222222112222222222220221222122222222222122122221222222222221222022222222222222222221122222222220222222212202200221222222121201120222202222022022010222222212112222021222021220222022222222222220210021222222222221221222222222222222222122122222221222222222112201200221222222222200122222222202022120200222222222112222221222022221222222222222222222222221222222222221221122222221222222222021222222220221222222122211212022222202120220022222222202122221022222222222112222020222121221222222222222222021000021222222222221222022222222222222222222122222221221222222022221221120222212221220120222202222022221000222222202222222022222021221222022122220222121121020222222222120221022222222222222222120122022222221222222022211212022222222121200121222212202222120022222222222002222221222122220222222022220222122112120222222222122222012222220222222222220222122222222221222002202221122222202022212122222222211122121011222222222002222121222022222222122222222222122221121222222222020222102222222222222202220022022222222221222122222202020222222220201122222212202122021212222222202222222220222021222222022122222222020010021222222222120221212222222222222212221222022221221222222012211222220222202020210122222222211122120010212222222112222120222221222222022122222222222111221222222222221221212222220222222212221122122222221221222122221212120222202221200120222212220122222201212222202102222222222122222222222022220222021111022222222222120222012222221222222202022022122220221222222012221220221222222220212022222202222222221102212222222112222122222222220222122122220222120112221222222222122220102222221222222212121022222220221220222102221221122222212022202122222202222122121201202222202222222220222122220222022202222222221100120222222222222221102222221222222212120122022220220220220202221222222222212021211012222222201222122001222222222212222120222220221222122102221222121011121222220222220220122222220222222222222222122220220221220102211212222222212122222000222202202022220121212122202022222122222120222222222122221222020110221222221222122220222222222222222212022222022202222222221022200201221222212122212221220212200222222020222222212022222220222021220222222012220222120001221222221222121221212222222222222202120022222200222220221122200222020222222222222221220212222022021012202022212222222121222021220222022222221222020110221222220022122221102222222222022212220022122212222220220212202200022222222220210002220202211112222111222122212012222020222222222222222022221222220211020222221222220220000222222222122202020022122222222221220122101212021222210121222021221222200122122022202222222022220020222120221222222112221222120200220222221122222222002222221222122222020222222220211220220022222201021222200120222010220222210222222000212022212212222022222221222222120012220222221200020222221222120222220222220222222222021022222200200221222222010221222222201120200102222212221212122201222222202002221121222221220222221102222222121112020222222222022222010222221222022222021122122220221220220022010220121222211022220212222212210002220022222122222222220222222021221212020112222222122010121222222222022222212222221222022222121022122222210221221122102200020222212122221022220212202002122212222222222102220220222122221222021202222222021210022222220222121220211220220222022212022222122212220221022202202200120222222022201201222222222012021020212022212102220120222022221102222112220222222111120222221012022221011220221222222202221022122221202220220022111211220222222221200021222212221022221112212122212022221120222220222112122202222222221002120222221102222221000022221222022212221022022221210221220202012211122222211021202001221212210122120220212222202102220120222022221222222122222222211010221222220202220222101020220222122222222022222210211221020122112200222222221020220000221202202202221201212122202202122120222222221202022012221222102000220222222022122221220020222222222212022022222220211221122212020222220222200021201220222222211202122011202122212122020121222020222122222122221222120111120222220212020221120222222222022212221022222212211222120222021211222222220120212020222222211112222000202122202222222121222221221022221002220222001000022222220002220222101020222222122202021122222220202222122112011201022222222020221102220202210222012120222122202222222021222121222012021202221022021020020222220022221221211220222222222222121222222211220222122202120221121222210122212020222222202012000211202222212112121020222221220112121212220022101000121222221122020221022121221222022222022022122210202222222202202212121222200122200210221222221112100012222022202212222020222222221012222012220022202121022222220202121221000020220222122212222122122211220220021112100200220022220020221111220202202212210210212022212222221121222222220212222102221022211122021222222112220220002221220222222202122122212221200222122122022202021222200221201002220222200112020001202022202202222121222121221012122122221022220001122222222202122222201220221222222012222222212201222221220202012212222220211222201121222212221102220111212222212212120020222021221102120022220222112200221222222022122222112022222222022222022222012220212220022002012220120121210122202120220212200212120100212222222212121222222021220102220212221122020201220221220212122220100221220222221022222222022200202221120122111211220022222222210210220212222112122222222222212212022022222120221022121222220122102120020220222002121220002220222222220122020022222222210221221112120202022220222220221100222202200122221112202222222212221020222120220222121102222122202101121221221022222222011021220222022002021220112221201222101002022222022122220121220220220212220022021011222022202002120121222120220212121222220122002001222221220112222221121122220222022112121021002222211022100002121212021021210020202001221212220222022212202022222002022221222120222022122102122222011201120221221112020220021120220222121102021122202201201221101122121202020120212020200001222212200212012200202022222022022121222222222222222102021022010021220221221012020222110022222222120022212220012210211121210002112221022221220122210002222202202212202220222222202002022021222220221012220112221222220020220222222222220222122120220222221222220222102222220220102202222202122020211222222121220212222022101122222122212002020121222121220222022002221122220110022222221102122222021222222222122022102122122212202121122002101220021122211022202102222202201112100200212022212102021120222120221000021122120222001221122222220112222222001020221222122012020021222202212121221212120201122122200122201020222202201102102102222022222222020222222022220201220012120122012011222221220202221220220121221222221112211221202220201021020022220211221120200121200012222202221202010010212022202012002021222021222211222212020222220112122222220112220222222020222222022222200120222222221122212012021222021022201221201220220202220202112100122022212222010021222022222021222212121022101122021222221202222220011022220222020222122221022202220220000022011211020122222022020212220222211202020220022122202002000022222222221222022002122122100101021221220112020222221021222222021202102022212202212121002202121201022120221221210101220212221012210212012222202122120222222110222210120002020122010002020222220022220222101221220222020212012021202212200121111222020212020121202121202212222202220122111012212122202212011120222021221022121212221022112220020221222022121222102121221222021102102221012200222120122022110201021022102022102211220202210002001202022022212222201021222212220101122112022022200010020220221222220222012121222001102102202222012222211022110022100201120121021020112221221222201212201221102122212022120020222111222101220102120122020001121221221012121222112122020020011102000022102220200020020012000211020220200022120112222212212112000101212022222022200221222121220102120002221222111210020222220022220220222122120000022212210021102211200022101212102222220020220220100200221122211102120121102022222222110020222201220011122222222122011210122222220002022222121120010102001012102122122201212120112102020210022020111122201222221002211122012011122222222202100021222001222220122102222222212120122220222022100222021120100021022022000020012201222122002002112222021120120121011011222122211112121200202222212222111021222201221221121112121022210220022222220102200221122120210010000002101222002200212122102222020210121122222222212111221222221122121202122022202202111220222212221120020122222122202201122221211122121222101221120002202122222022122202212222212122020200221122220120021101221222221022020202102122222221212122222221220110120022121022112200120221212012221221011120221010121222211221122211221222100122202222221222020022010211221122210202122200022222202110201222222110222210122212120122221210021021221222111220111020122002022122201222022222202122112102101202121122201121101112220122222122112101122222222022002021222202221002021202122122222120022022212002012221121022000120101122121221012220200221001002200201120122000221001102220102220202102021202222212001220021222002222000020022022122212110022220210212200222221022200222012022010022112220222021211202221210210121222122000120222202211002011111202122222221100020222212222012220202220122010111220022222002111220000020111122222222111021202211202222121122112221210222102221210210221022212222100201112022222012201222122222220202121102222122021012221120212222220222000222020202220202200020122212210221200002120212002020100022010022222212200112220200212222202100201020221101222011220212022102122121222220211212222222201021011010002222010120022220212021222112121221121020020121100220222112220012221211112222212012120020222210220100220112220112222202122020000112122220211220000000212212101122212210221122222102210202022121011122112221222212222012110201122122222102122222220022220020020022110112200022221221102010220221010121001201202202121021102212222120220222121220200121210100000011220002201002212212222220212002000122021010221022222122001012100011021222000202202220220020021222012012120120002212201222212212021202000222020112102220222022212012112020122120202112201212221011221012221002202122011021021120122010110220202120122222002222002020112212212121120222202222212220220102221210220202210122111201222221222122110112221110221210121022220112001010020221210022020222020021001210010002221020220212210120212012202201100221210220121002222222211122022012022022222021200012220002222210120212210122211222121021121011122222221121100101011222121122110201220021201202001211001122201022101021221202200212120210022221212111000020021122211000021012210012021022021120220110222222021120110201012222111120011200201221012202120222202021000212112220222102220022202010102020102002111101022020221122122202012112200012021020202221002122222121011212211022000121020201220020022002000200120022102202020020220012201122100020022221122010120000101002000221002221200100212201102200100122222200012110100110101021211202022012122200011120212000210002210100101200011100122111121121211001200020122, 25, 6)
#layerparse('0222112222120000',2,2)

#answers
#1690
#ZPZUB
