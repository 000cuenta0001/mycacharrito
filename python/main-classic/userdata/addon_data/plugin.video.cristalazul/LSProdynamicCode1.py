# -*- coding: utf-8 -*-
#$pyFunction
 
def GetLSProData(page_data,Cookie_Jar,m):
 
   import xbmcgui
 
   dialog = xbmcgui.Dialog()
 
   ret = dialog.select('[ [COLOR white]ELIJE LA PAGINA[/COLOR]]  ', [' [COLOR orange]arenavision.[COLOR white]in[/COLOR]/Agenda[/COLOR] ', ' [COLOR orange]arenavision.[COLOR white]us[/COLOR]/Agenda[/COLOR] ', ' [COLOR orange]arenavision.[COLOR white]2018.gq[/COLOR]/Agenda[/COLOR] '])
   lists = ['.in', '.us', '2018.gq']
 
   return lists[ret]
 
