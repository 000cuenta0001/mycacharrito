# -*- coding: utf-8 -*-
#$pyFunction
def GetLSProData(page_data,Cookie_Jar,m):
   import xbmcgui
   dialog = xbmcgui.Dialog()
   ret = dialog.select('Elige un Canal ', ['AV 1','AV 2','AV 3','AV 4','AV 5','AV 6','AV 7','AV 8','AV 9','AV 10','AV 11','AV 12','AV 13','AV 14','AV 15','AV 16','AV 17','AV 18','AV 19','AV 20','AV 21','AV 22','AV 23','AV 24','AV 25','AV 26','AV 27','AV 28','AV 29','AV 30','AV 31','AV 32','AV 33','AV 34','AV 35',])
   lists = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35']
   return lists[ret]
