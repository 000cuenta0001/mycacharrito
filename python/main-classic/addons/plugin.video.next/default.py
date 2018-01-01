# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: NEXT
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.next'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLShKu0sRclF_fn7Yf69tRuq_xcEjEN1wE" 	#REGGAETON
YOUTUBE_CHANNEL_ID_2 = "PLChOO_ZAB22UcOXiE-IO6m7Vm25to6Njg" 	#2017
YOUTUBE_CHANNEL_ID_3 = "PLO_1AmtK1TMQrdl967xW8z6NiMfuBLdtf" 	#HOUSE 2017
YOUTUBE_CHANNEL_ID_4 = "PLXLXo07HMXlj6swhszmAX54CNYWRONg76" 	#EL ULTIMO DE LA FILA
YOUTUBE_CHANNEL_ID_5 = "PLwMub1irLfLgV1Wdm09gEEvy-l9iA6KtH" 	#HOMBRES G
YOUTUBE_CHANNEL_ID_6 = "PL579BDFCE2C76B890" 	#DANI MARTIN
YOUTUBE_CHANNEL_ID_7 = "PLIhsN0NS3ECS_N9vIAS6m6v-LkA1WTuEy" 	#DAVID BISBAL
YOUTUBE_CHANNEL_ID_8 = "PLAtuHZ7V5lmvmLtBmU8fQ8rOKLoJz39s4" 	#CAMARÓN DE LA ISLA
YOUTUBE_CHANNEL_ID_9 = "PLFEDB1FF66180AD87" 	#CELTAS CORTOS
YOUTUBE_CHANNEL_ID_10 = "PLA_I2ay5YcUUKiZshI4cgp9fTOS-Q6B1E" 	#FLAMENCO
YOUTUBE_CHANNEL_ID_11 = "PLSL9DB9AUS4P1v4E1KtXJ1Y2lca7UOdo_" 	#ESTOPA
YOUTUBE_CHANNEL_ID_12 = "PLAFFD17207690FCCB" 	#JOAQUIN SABINA
YOUTUBE_CHANNEL_ID_13 = "PLF855900B37228AA8" 	#EL SUEÑO DE MORFEO
YOUTUBE_CHANNEL_ID_14 = "PLlkLqylYSdn8A0NLLeRZPsBPoqPAO4Qu9" 	#ENRIQUE IGLESIAS
YOUTUBE_CHANNEL_ID_15 = "PL4iSbgi3WlCpM2bG4ybcZdttLzyWxbEzf" 	#RAPHAEL
YOUTUBE_CHANNEL_ID_16 = "PL5viewcavnJRLBTzfr2lotjfbBec_WfsO" 	#DAVID BUSTAMANTE
YOUTUBE_CHANNEL_ID_17 = "PLAtuHZ7V5lmuUtrWh3nahsrZIJrZvGnSR" 	#ALEJANDRO SANZ
YOUTUBE_CHANNEL_ID_18 = "PLDC97A0259A1EFD2E" 	#MANOLO GARCIA
YOUTUBE_CHANNEL_ID_19 = "PLeC3KXKbXai5nLfjLi3pVVLIeg58ZaqH5" 	#ANTONIO OROZCO
YOUTUBE_CHANNEL_ID_20 = "PLBEB584BD45473BDE" 	#ROSARIO
YOUTUBE_CHANNEL_ID_21 = "PLJaT5gj1oqPRFg3Dd-SV3aQ93EB3kqOxc" 	#MANUEL CARRASCO
YOUTUBE_CHANNEL_ID_22 = "PLPjGUVv110e9QXFwcPqFaQDwK4YvX56zD" 	#FITO & FITIPALDIS
YOUTUBE_CHANNEL_ID_23 = "PL898D5E9D83F409FA" 	#MALÚ
YOUTUBE_CHANNEL_ID_24 = "PLA536BC4F1B31A9C1" 	#EL BARRIO
YOUTUBE_CHANNEL_ID_25 = "PL7m5sbJepdm3ockFdYWANXDdAAG7_EdHE" 	#MAÍTA VENDE CÁ
YOUTUBE_CHANNEL_ID_26 = "PLB9032D4443BB4BC2" 	#MECANO
YOUTUBE_CHANNEL_ID_27 = "PLEBC434AD360A2736" 	#NAVAJITA PLATEADA
YOUTUBE_CHANNEL_ID_28 = "PLDC02FA9F86F96406" 	#DIANA NAVARRO
YOUTUBE_CHANNEL_ID_29 = "PLpYAMryr-j0U_HN5ekDG47yGZAPp76l6V" 	#HUECO
YOUTUBE_CHANNEL_ID_30 = "PL1290CFA5F6423A67" 	#MIGUEL BOSÉ
YOUTUBE_CHANNEL_ID_31 = "PL10100EA06AD634CB" 	#OBK
YOUTUBE_CHANNEL_ID_32 = "PLV4qtz56dfJRpnGD_SYDdaBsIQvmLK8p0" 	#PABLO ALBORÁN
YOUTUBE_CHANNEL_ID_33 = "PL829D9CD223E56943" 	#ANDY & LUCAS
YOUTUBE_CHANNEL_ID_34 = "PLqK1JpL0Zp67nUaNRno9iVn5nt6IBrAGW" 	#LOS DEL RÍO
YOUTUBE_CHANNEL_ID_35 = "PL64953A1F7A8BEB9B" 	#JOAN MANUEL SERRAT
YOUTUBE_CHANNEL_ID_36 = "PLeMIN33KXnN7MRUXKU7nR_gp1EBBoevxz" 	#SERGIO DALMA
YOUTUBE_CHANNEL_ID_37 = "PLFcqPhJvt_qlD4jxBPhr5K1rozvlPLLnm" 	#BECKY G
YOUTUBE_CHANNEL_ID_38 = "PL6CM2Se7zfnUtP-AMRsAm-lp-vQ8ZhNeJ" 	#RADIO FUTURA
YOUTUBE_CHANNEL_ID_39 = "PL69d5IZlV8KHs8xmgpz9B4MbrpSkS8TdO" 	#DUNCAN DHU
YOUTUBE_CHANNEL_ID_40 = "PL5881D08E87DFC944" 	#M-CLAN
YOUTUBE_CHANNEL_ID_41 = "PLVXMccjVOpZrxptx1K9P8-m_2NfkwV2Y4" 	#MAGO DE OZ
YOUTUBE_CHANNEL_ID_42 = "PL0AF81C7A187B0356" 	#EXTREMODURO
YOUTUBE_CHANNEL_ID_43 = "PL86319EE69F06D828" 	#LOQUILLO Y LOS TROGLODITAS
YOUTUBE_CHANNEL_ID_44 = "PL67DF7EA7DDAF6978" 	#NACHA POP
YOUTUBE_CHANNEL_ID_45 = "PLusS9CtXL7ZJELy7rbJ2g3vggC8qVrwOm" 	#LOS SECRETOS
YOUTUBE_CHANNEL_ID_46 = "PLAB1FCDB25219C487" 	#TRIANA
YOUTUBE_CHANNEL_ID_47 = "PL9FBEE2F34574AF5B" 	#LOS SUAVES
YOUTUBE_CHANNEL_ID_48 = "PLB90F809164467950" 	#CHAMBAO
YOUTUBE_CHANNEL_ID_49 = "PLB495E60E77E742C6" 	#JULIO IGLESIAS
YOUTUBE_CHANNEL_ID_50 = "PL2F6DF509D3AE319B" 	#LA OREJA DE VAN GOGH
YOUTUBE_CHANNEL_ID_51 = "PL5B7E414263FC6041" 	#DAVID DE MARIA
YOUTUBE_CHANNEL_ID_52 = "PLMKA1irNvQ9JX-BMtK7wRKshg7R04haGO" 	#51 CHART MAXIMA FM
YOUTUBE_CHANNEL_ID_53 = "PLTg70_BqgFusp1FzXheTTHUCv68MW4ZYh" 	#INDIA MARTINEZ
YOUTUBE_CHANNEL_ID_54 = "PLWBHUwiEdo5eMW7dFc0HnDsn-97HD4NMt" 	#MARIA ARTES
YOUTUBE_CHANNEL_ID_55 = "PLC833837DB7F34B1C" 	#NIÑA PASTORI
YOUTUBE_CHANNEL_ID_56 = "PLTtT3vD5-GEwZ0KEdzkn8ExjZBy_V9XOb" 	#IL DIVO
YOUTUBE_CHANNEL_ID_57 = "PLC9AEA85693A20A70" 	#JUAN LUIS GUERRA
YOUTUBE_CHANNEL_ID_58 = "PLSL9DB9AUS4OrZ_N7izVrudQLS-SHtcIS" 	#JARABE DE PALO
YOUTUBE_CHANNEL_ID_59 = "PL96A1E611FB808DFC" 	#CANELITA
YOUTUBE_CHANNEL_ID_60 = "PL3dCng0ynzekOZWUlPZNSCVavBqsQGJCW" 	#ANTONIO JOSE
YOUTUBE_CHANNEL_ID_61 = "PLE5C671B6432FD04D" 	#PASTORA SOLER
YOUTUBE_CHANNEL_ID_62 = "PLCFA0232C20A9AC52" 	#HAZE
YOUTUBE_CHANNEL_ID_63 = "PLpEJ4CNLsMCwCjT16L7rDGPrET-2jh4QY" 	#LOS REBUJITOS
YOUTUBE_CHANNEL_ID_64 = "PL41B59E099C7FD32A" 	#SERGIO CONTRERAS
YOUTUBE_CHANNEL_ID_65 = "PLE412E602C73D59B9" 	#CAMELA
YOUTUBE_CHANNEL_ID_66 = "PL6lqml5OGdIlMo4g-DEs5vdptW21L6Z6Z" 	#JOSE MERCÉ
YOUTUBE_CHANNEL_ID_67 = "PL6E7CDC1991D82CD8" 	#EL BICHO
YOUTUBE_CHANNEL_ID_68 = "PLEARaKwcZx2byI-bsIOCXz3VPX56iz5du" 	#JUANES
YOUTUBE_CHANNEL_ID_69 = "PL279E6CCC11AA0723" 	#SHAKIRA
YOUTUBE_CHANNEL_ID_70 = "PLduvqUwkyHjjPBTJhvyTC2WDq3jpKsnrM" 	#DADDY YANKEE
YOUTUBE_CHANNEL_ID_71 = "PL08EC2C91BD4CED55" 	#MARC ANTHONY
YOUTUBE_CHANNEL_ID_72 = "PLC9021EB8097866B4" 	#CHAYANE
YOUTUBE_CHANNEL_ID_73 = "PLC64FCC947043B911" 	#GLORIA STEFAN
YOUTUBE_CHANNEL_ID_74 = "PLDCA6F12BCB939D38" 	#CARLOS BAUTE
YOUTUBE_CHANNEL_ID_75 = "PLtJ0WuqMOzkpBG8Dxd9tSCO6i0qWgrDDu" 	#CARLOS SANTANA
YOUTUBE_CHANNEL_ID_76 = "PLBN9UtpzNFo-PgcajpX8iOlfTWCy7JMHd" 	#CARLOS VIVES
YOUTUBE_CHANNEL_ID_77 = "PL54C1C720168A2471" 	#CAMILA
YOUTUBE_CHANNEL_ID_78 = "PLiaJ-1S3mua3hyNnqiM1k9hRJ4l8lTV7O" 	#CALLE 13
YOUTUBE_CHANNEL_ID_79 = "PLduvqUwkyHjjMVqdNuk7K-d3BzJwW11n7" 	#J BALVIN
YOUTUBE_CHANNEL_ID_80 = "PLl6kGKreorFN67kEWbnjHdxKFzFbuvB7N" 	#MALUMA
YOUTUBE_CHANNEL_ID_81 = "PLgogOWaoJDEeuBDGTxfYzcSzV38DFmeqC" 	#LOS 80 NEXT MUSIC
YOUTUBE_CHANNEL_ID_82 = "PLgogOWaoJDEftROXzw6QnfE2sjwWiRBze" 	#LOS 70 NETX MUSIC
YOUTUBE_CHANNEL_ID_83 = "PLgogOWaoJDEf-Ga54WmhkFMClZs3zCPQO" 	#LOS 90 NEXT MUSIC
YOUTUBE_CHANNEL_ID_84 = "PLgogOWaoJDEff6SiaB441t0gfk9ByM492" 	#30-40-50- NEXT MUSIC
YOUTUBE_CHANNEL_ID_85 = "PLgogOWaoJDEd3__X_eSrlf7xNHeq88lNp" 	#LOS 60 NEXT MUSIC
YOUTUBE_CHANNEL_ID_86 = "PLgogOWaoJDEcDAeQN_KWRvsDEkQZwvFO8" 	#LOS 70 NEXT MUSIC 2
YOUTUBE_CHANNEL_ID_87 = "PLgogOWaoJDEfXfRuSCp_jek7-0omILRre" 	#LOS 80 NEXT MUSIC 2
YOUTUBE_CHANNEL_ID_88 = "PLgogOWaoJDEeJqml2u9MUH-eUNMNDFrGi" 	#LOS 90 NEXT MUSIC 2
YOUTUBE_CHANNEL_ID_89 = "PLgogOWaoJDEdD_bHcZhjJwzkXH7-dDIvj" 	#2000-2003 NEXT MUSIC
YOUTUBE_CHANNEL_ID_90 = "PLgogOWaoJDEfFRpyyyagmZFKLPMXhoVE_" 	#2004-2007 NETX MUSIC
YOUTUBE_CHANNEL_ID_91 = "PLgogOWaoJDEeeypF8rH7YoAFOD8l_m_97" 	#2007-2009 NEXT MUSIC
YOUTUBE_CHANNEL_ID_92 = "PLgogOWaoJDEc5JYdHi-58TK50r8u3ZlRE" 	#2010 NEXT MUSIC
YOUTUBE_CHANNEL_ID_93 = "PLgogOWaoJDEehJ-za-t4DCzC5W2e8__CU" 	#2011 NEXT MUSIC
YOUTUBE_CHANNEL_ID_94 = "PLgogOWaoJDEc3bU_ELHsv_e7EvqZPqpkE" 	#2012 NEXT MUSIC
YOUTUBE_CHANNEL_ID_95 = "PLgogOWaoJDEcaOamJEH6msLYtckR1Ifny" 	#2013 NEXT MUSIC
YOUTUBE_CHANNEL_ID_96 = "PLgogOWaoJDEcm6FvA366YUiVA67k5em2g" 	#2014 NETX MUSIC
YOUTUBE_CHANNEL_ID_97 = "PLaq655wqcKDnUvTOizhqwNCiiF_grL1vh" 	#ED SHEERAN
YOUTUBE_CHANNEL_ID_98 = "PLDb6I-R27ee3_0gvGEXQ71Z3aST4qQ2KH" 	#JUSTIN BIEBER
YOUTUBE_CHANNEL_ID_99 = "PLWBHUwiEdo5eMW7dFc0HnDsn-97HD4NMt" 	#MARIA ARTES
YOUTUBE_CHANNEL_ID_100 = "PL3767D7CA131A911F" 	#LUIS MIGUEL
YOUTUBE_CHANNEL_ID_101 = "PLSFitF4B6yNS82pcRx5XvD1PB6m8lIs5J" 	#40 PPRICIPALES LISTA
YOUTUBE_CHANNEL_ID_102 = "PLmo4pBukfRoN8SB5RKvfiY9CTl9pI_IFc" 	#THE BEATLES
YOUTUBE_CHANNEL_ID_103 = "PL768F750024200832" 	#THE KILLERS
YOUTUBE_CHANNEL_ID_104 = "PLe52M8z8EbA9hv-sYL8dcJmng_HBvtDvq" 	#THE DOORS
YOUTUBE_CHANNEL_ID_105 = "PLIPoTusqlz4kndDGhxYTApa2jcnq08fGI" 	#THE CHAINSMOKERS
YOUTUBE_CHANNEL_ID_106 = "PL36494E8634856791" 	#THE POLICE
YOUTUBE_CHANNEL_ID_107 = "PLiH2bZpSPIDwfTndWrIah2rNLrKELHqax" 	#THE CRANBERRIES
YOUTUBE_CHANNEL_ID_108 = "PLze5jhu6M0TV09Sxy-NWAjjlEkuPgDeeD" 	#THE SMITHS
YOUTUBE_CHANNEL_ID_109 = "PLDIv8Cip85C-mEslQxxNOlfERCBJg6Cuw" 	#THE CORRS
YOUTUBE_CHANNEL_ID_110 = "PLEE22292DBF9E4DF6" 	#THE BLACK EYED PEAS
YOUTUBE_CHANNEL_ID_111 = "PLhE8kJaMlI43iCypJnIl1ILfE20DqAEoZ" 	#THE ROLLING STONES
YOUTUBE_CHANNEL_ID_112 = "PLxbtmwASynrtj8SB0TqacOysknGUgnHHp" 	#QUEEN
YOUTUBE_CHANNEL_ID_113 = "PLQhDqD3lVKe8XR5orpuC2LCNrFd-eRvyi" 	#BOB MARLEY
YOUTUBE_CHANNEL_ID_114 = "PL51B8DE984734D7AA" 	#BEYONCÉ
YOUTUBE_CHANNEL_ID_115 = "PLjUShF4dYZPjvg3BGRtEwSCaz0nb_kG9N" 	#BON JOVI
YOUTUBE_CHANNEL_ID_116 = "PLI6Wzy3GVpd6N7Ob5SR87AbNJEcqJUE2P" 	#BRUNO MARS
YOUTUBE_CHANNEL_ID_117 = "PL7B7E250ABE8B4E64" 	#BOB DYLAN
YOUTUBE_CHANNEL_ID_118 = "PLbOvZh1OHOLd6UF_M_wr-LmR0MC0sMgb3" 	#ADELE
YOUTUBE_CHANNEL_ID_119 = "PL9NY5axt700GDqS0Cm62ubDxjsQckjQ4s" 	#ARIANA GRANDE
YOUTUBE_CHANNEL_ID_120 = "PLDB7DC9620C6A9B1F" 	#AVENTURA
YOUTUBE_CHANNEL_ID_121 = "PLFE1E1A7DBB0D2EAF" 	#AEROSMITH
YOUTUBE_CHANNEL_ID_122 = "PL583E639C5C24130C" 	#AC-DC
YOUTUBE_CHANNEL_ID_123 = "PLBE8F82E1B77B1127" 	#ALEJANDRO FERNÁNDEZ
YOUTUBE_CHANNEL_ID_124 = "PL2DF7E3EFCC17330E" 	#RICARDO ARJONA
YOUTUBE_CHANNEL_ID_125 = "PLD2293042C2942431" 	#COLDPLAY
YOUTUBE_CHANNEL_ID_126 = "PL127FF7A0CE49BF91" 	#DON OMAR
YOUTUBE_CHANNEL_ID_127 = "PLPL5dBlIqDB9gFSYx-LxjgQ0zxAoBtwCY" 	#DAVID GUETTA
YOUTUBE_CHANNEL_ID_128 = "PL9A1600EA18716662" 	#DAFT PUNK
YOUTUBE_CHANNEL_ID_129 = "PLxP-MeqGc6jBNoKZFuxVMqkOmdLulDOJY" 	#DRAKE
YOUTUBE_CHANNEL_ID_130 = "PL0H665cH71EZogv7mnsUS8pF_3m-YDEMD" 	#ELVIS PRESLEY
YOUTUBE_CHANNEL_ID_131 = "PL9LZtJZTt668OxYcRaDpPXcPkcRFVoTYV" 	#R.E.M
YOUTUBE_CHANNEL_ID_132 = "PLF26E2C9C284630EE" 	#EMINEM
YOUTUBE_CHANNEL_ID_133 = "PLeNcN7ztY6vKSOPqx3IycIUqsf9m5G8Fg" 	#GUNS N ROSES
YOUTUBE_CHANNEL_ID_134 = "PLo6aG-353Cqkrei8GU5adW9ZDbW_5Nl1X" 	#GREEN DAY
YOUTUBE_CHANNEL_ID_135 = "PLUyZcmdcNTpTnA8a0-IQOsFVAQDS1KTPr" 	#GLORIA TREVI
YOUTUBE_CHANNEL_ID_136 = "PL935D1A0369781629" 	#MAROON 5
YOUTUBE_CHANNEL_ID_137 = "PL2xrKm3nXkPOQH2gWsCLQpihl5-CzPr4u" 	#METALLICA
YOUTUBE_CHANNEL_ID_138 = "PL73B7E7EAE510ABEC" 	#NIRVANA
YOUTUBE_CHANNEL_ID_139 = "PLn5WUujnvlppi1X8soscLXrXaQCaO5HTi" 	#NEXT LO MEJOR DEL ROCK
YOUTUBE_CHANNEL_ID_140 = "PLCEA6486A867A6E84" 	#PINK FLOYD
YOUTUBE_CHANNEL_ID_141 = "PLI6CjkN988Lrx885kxTzGeOhR090Rfm7z" 	#U2
YOUTUBE_CHANNEL_ID_142 = "PLZ4BAv1SLe4y3sEXoue_g5pwlUfnmqfCu" 	#TAYLOR SWIFT
YOUTUBE_CHANNEL_ID_143 = "PLBC65F362D3A92109" 	#AMY WINEHOUSE
YOUTUBE_CHANNEL_ID_144 = "PL07B1DB028D800C8D" 	#PHIL COLLINS
YOUTUBE_CHANNEL_ID_145 = "PL12A3014F7B28F705" 	#ROD STEWART
YOUTUBE_CHANNEL_ID_146 = "PL804A8D8E31287555" 	#LIONEL RICHIE
YOUTUBE_CHANNEL_ID_147 = "PLV8LFZeK-sM_cDXpI-BX815xfEVQIUz8V" #PETER CETERA
YOUTUBE_CHANNEL_ID_148 = "PL1BDE43216C9BBAEF" 	#PETER GRABIEL
YOUTUBE_CHANNEL_ID_149 = "PLEp7LuAEi-SDw28kqXFaN5s8NZavRJHMf" 	#GUSTAVO CERATI
YOUTUBE_CHANNEL_ID_150 = "PL9AFA166F5CFB34A2" 	#SODA STEREO
YOUTUBE_CHANNEL_ID_151 = "PLJu1mQyIUo9vv7pr-_kAJhw8Zq7EpWnlC" 	#NEXT MUSIC CINE
YOUTUBE_CHANNEL_ID_152 = "PLF9IgOl8OobWqJltrQqpjy3AKF3LYEQhc" 	#TOM JONES
YOUTUBE_CHANNEL_ID_153 = "PLCF0F6B05B52AEB1C" 	#ELTON JOHN
YOUTUBE_CHANNEL_ID_154 = "PL8C6EEAE0ED065A70" 	#PINK
YOUTUBE_CHANNEL_ID_155 = "PL9BDB756C35363391" 	#MICHAEL JACKSON
YOUTUBE_CHANNEL_ID_156 = "PLqK1JpL0Zp64-ag74CbP4M5ua0LTKvPZX" 	#AZUCAR MORENO
YOUTUBE_CHANNEL_ID_157 = "PLY5QRSIgDTFYrOve0_b5KnCyEtkjqztpN" 	#PERET
YOUTUBE_CHANNEL_ID_158 = "PL849CBC8E6B3F67A2" 	#SEGURIDAD SOCIAL
YOUTUBE_CHANNEL_ID_159 = "PL2innewxz-3T30yle-pC2iYnKhSpA2AcS" 	#NO ME PISES QUE LLEVO CHANCLAS
YOUTUBE_CHANNEL_ID_160 = "PL4C60136402D71D4F" 	#LOS INHUMANOS
YOUTUBE_CHANNEL_ID_161 = "PL71A9E09DEF0CE017" 	#KISS
YOUTUBE_CHANNEL_ID_162 = "PLsutuIAyVp8wTARwkTmko-0jSRZv-wYea" 	#KIKO VENENO
YOUTUBE_CHANNEL_ID_163 = "PL2CD7050397E3895E" 	#ELVIS CRESPO
YOUTUBE_CHANNEL_ID_164 = "PL76AACB66F3694F93" 	#KATY PERRY
YOUTUBE_CHANNEL_ID_165 = "PL3346CA22E1572950" 	#LUIS FONSI
YOUTUBE_CHANNEL_ID_166 = "PL750CBD8C5C19084D" 	#MADONA
YOUTUBE_CHANNEL_ID_167 = "PL3F60FB8566CB97BB" 	#TINA TURNER
YOUTUBE_CHANNEL_ID_168 = "PL7C2B0E3933F8F6EE" 	#MARIAH CAREY
YOUTUBE_CHANNEL_ID_169 = "PL1F21709106B8CB0D" 	#ROXETTE
YOUTUBE_CHANNEL_ID_170 = "PLA70DDD2CB84B2FD7" 	#DEPECHE MODE
YOUTUBE_CHANNEL_ID_171 = "PL9DE5BA48FEBF5F53" 	#ABBA
YOUTUBE_CHANNEL_ID_172 = "PL3C4D7E1D4267BA5C" 	#BEE GEES
YOUTUBE_CHANNEL_ID_173 = "PLv9uDgeCR73XvzgGF_tRCl2NUsP5Y2Feo" 	#ONE DIRECTION
YOUTUBE_CHANNEL_ID_174 = "PLE5EEE5F64902A346" 	#LINKIN PARK
YOUTUBE_CHANNEL_ID_175 = "PL4EA4DF2B2926EDC8" 	#STING
YOUTUBE_CHANNEL_ID_176 = "PLE8E0CE1DD477FFC4" 	#RED HOT CHILI PEPPERS
YOUTUBE_CHANNEL_ID_177 = "PL2A70E0897EFD9FC5" 	#LA 5 ESTACION
YOUTUBE_CHANNEL_ID_178 = "PLF31711B2F35147F2" 	#THE PRODIGY
YOUTUBE_CHANNEL_ID_179 = "PLV4qtz56dfJTU5apFQ_TMKf4ZU_yCAfCj" 	#THE CHERMICAL BROTHERS
YOUTUBE_CHANNEL_ID_180 = "PLB050A119A7FFAC17" 	#TATU
YOUTUBE_CHANNEL_ID_181 = "PL0A4CE5CE620F96D8" 	#BACKSTREET BOYS
YOUTUBE_CHANNEL_ID_182 = "PL1E71A66C31D1CEA0" 	#SPICE GIRL
YOUTUBE_CHANNEL_ID_183 = "PL3BB5FBA1E8119137" 	#RAMONES
YOUTUBE_CHANNEL_ID_184 = "PL922784C582D594E0" 	#BLINK 182
YOUTUBE_CHANNEL_ID_185 = "PLC68673F19C82832B" 	#LED ZEPPELIN
YOUTUBE_CHANNEL_ID_186 = "PL425F29B46CA3B395" 	#OASIS
YOUTUBE_CHANNEL_ID_187 = "PLRVAmnwV_xPr19Bvuwnu-SRwrraChRECW" 	#CHINO Y NACHO
YOUTUBE_CHANNEL_ID_188 = "PLxgvkEADrKB1n4WqugPMKbIWlch0Tvdb4" 	#NEXT MUSIC HD
YOUTUBE_CHANNEL_ID_189 = "PLVS8L6lb4C1n0j6qQRTS5mP8bkwaRXL-Y" 	#NEXT CLASICOS DE AYER Y DE HOY
YOUTUBE_CHANNEL_ID_190 = "PLShKu0sRclF8Gj6GMzQ3LFjJYjI3ZEwbP" 	#TEMA DE LA SEMANA
YOUTUBE_CHANNEL_ID_191 = "PLVS8L6lb4C1n3ClZYnDK7fpD0ne6XdlQC" 	#NEXT - EVENTO ESPECIAL
YOUTUBE_CHANNEL_ID_192 = "RDQMstL9dbTqT2s" 	#MANA
YOUTUBE_CHANNEL_ID_193 = "PLBN78YJJvjRFtHOZ6TYVXQJUzPDHGnw7D" 	#MANOLO TENA
YOUTUBE_CHANNEL_ID_194 = "RDQMBOGG9PONv1Q" 	#MELENDI
YOUTUBE_CHANNEL_ID_195 = "RDUc9u__f6hxM" 	#SALVATORE GANACCI
YOUTUBE_CHANNEL_ID_196 = "PLe_ZtSe0ZjGmxpT95hZlejTde8YynHdy4" 	#SUPERSUBMARINA
YOUTUBE_CHANNEL_ID_197 = "RDQMBimud2NnKxY" 	#VETUSTA MORLA
YOUTUBE_CHANNEL_ID_198 = "RDQMOI78oB-40zU" 	#NEXT - CHRISTMAS SONGS
YOUTUBE_CHANNEL_ID_199 = "PLjt5ExlRCdaDCRHchgu-FKP7ZC3gclen1" 	#NEXT - POP LATINO MIX
YOUTUBE_CHANNEL_ID_200 = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI" 	#NEXT - VIDEOS POPULARES	PopularPopular Music Videos
YOUTUBE_CHANNEL_ID_201 = "PLFgquLnL59alW3xmYiWRaoz0oM3H17Lth" 	#NEXT - LO NUEVO DE LA SEMANA	New Music This Week
YOUTUBE_CHANNEL_ID_202 = "PLFgquLnL59akA2PflFpeQG9L01VFg90wS" 	#NEXT - LO MAS NUEVO	Latest Music Videos
YOUTUBE_CHANNEL_ID_203 = "PLFPg_IUxqnZNnACUGsfn50DySIOVSkiKI" 	#NEXT - MUSCIA ELECTRONICA	Electronic Music
YOUTUBE_CHANNEL_ID_204 = "PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ" 	#NEXT - HOUSE	Top Tracks - House Music
YOUTUBE_CHANNEL_ID_205 = "PLcfQmtiAG0X-fmM85dPlql5wfYbmFumzQ" 	#NEXT - LATINO	Top Tracks - Latin Music
YOUTUBE_CHANNEL_ID_206 = "PLFgquLnL59akXPIHrEZci0oouw4dArE0D" 	#NEXT - MUSICA ELECTRONICA - INDICE	The Electronic Index
YOUTUBE_CHANNEL_ID_207 = "PLhInz4M-OzRUsuBj8wF6383E7zm2dJfqZ" 	#NEXT - HOUSE	Top Tracks - House Music
YOUTUBE_CHANNEL_ID_208 = "PLFgquLnL59amBBTCULGWSotJu2CkioYkj" 	#NEXT - HIP HOP - INDICE 	The Hip-Hop Index
YOUTUBE_CHANNEL_ID_209 = "PLDcnymzs18LWrKzHmzrGH1JzLBqrHi3xQ" 	#NEXT - POP 	Top Tracks - Pop Music
YOUTUBE_CHANNEL_ID_210 = "PLH6pfBXQXHEC2uDmDy5oi3tHW6X8kZ2Jo" 	#NEXT - HIP HOP 	Top Tracks - Hip Hop Music
YOUTUBE_CHANNEL_ID_211 = "PL47oRh0-pTouthHPv6AbALWPvPJHlKiF7" 	#NEXT - ROCK ALTERNATIVO 	Top Tracks - Alternative Rock
YOUTUBE_CHANNEL_ID_212 = "PLYAYp5OI4lRLf_oZapf5T5RUZeUcF9eRO" 	#NEXT - REGGAE 	Top Tracks - Reggae
YOUTUBE_CHANNEL_ID_213 = "PLL4IwRtlZcbvbCM7OmXGtzNoSR0IyVT02" 	#NEXT - TRAP 	Top Tracks - Trap
YOUTUBE_CHANNEL_ID_214 = "PLvLX2y1VZ-tFJCfRG7hi_OjIAyCriNUT2" 	#NEXT - COUNTRY 	Top Tracks - Country
YOUTUBE_CHANNEL_ID_215 = "PLFgquLnL59amI45Go39kM7ha2evwjOxzs" 	#NEXT - COUNTRY - INDICE 	The Country Index
YOUTUBE_CHANNEL_ID_216 = "PLr8RdoI29cXIlkmTAQDgOuwBhDh3yJDBQ" 	#NEXT - POP ROCK 	Top Tracks - Pop Rock
YOUTUBE_CHANNEL_ID_217 = "PLFRSDckdQc1th9sUu8hpV1pIbjjBgRmDw" 	#NEXT - R&B 	Top Tracks - R&B
YOUTUBE_CHANNEL_ID_218 = "PL0zQrw6ZA60Z6JT4lFH-lAq5AfDnO2-aE" 	#NEXT - ASIA 	Top Tracks - Asian Music
YOUTUBE_CHANNEL_ID_219 = "PLXupg6NyTvTxw5-_rzIsBgqJ2tysQFYt5" 	#NEXT - MEXICO 	Top Tracks - Mexican Music
YOUTUBE_CHANNEL_ID_220 = "PLQog_FHUHAFUDDQPOTeAWSHwzFV1Zz5PZ" 	#NEXT - SOUL 	Top Tracks - Soul
YOUTUBE_CHANNEL_ID_221 = "PLFgquLnL59amVPzpNpN5bNLcZCld7JfI8" 	#NEXT - INDIE - INDICE 	The Indie Index
YOUTUBE_CHANNEL_ID_222 = "PLFgquLnL59ak5gmnz28ZiMd59ryeTPXjT" 	#NEXT - EN LA CIMA 	On the Rise
YOUTUBE_CHANNEL_ID_223 = "PLWNXn_iQ2yrKzFcUarHPdC4c_LPm-kjQy" 	#NEXT - RHYTHM & BLUES 	Top Tracks - Rhythm & Blues
YOUTUBE_CHANNEL_ID_224 = "PLLMA7Sh3JsOQQFAtj1no-_keicrqjEZDm" 	#NEXT - CRISTIANA 	Top Tracks - Christian Music
YOUTUBE_CHANNEL_ID_225 = "PL9NMEBQcQqlzwlwLWRz5DMowimCk88FJk" 	#NEXT - HARD ROCK 	Top Tracks - Hard Rock
YOUTUBE_CHANNEL_ID_226 = "PLfY-m4YMsF-OM1zG80pMguej_Ufm8t0VC" 	#NEXT - HEAVY METAL 	Top Tracks - Heavy Metal
YOUTUBE_CHANNEL_ID_227 = "PLVXq77mXV53-Np39jM456si2PeTrEm9Mj" 	#NEXT - CLASICA 	Top Tracks - Classical Music
YOUTUBE_CHANNEL_ID_228 = "PLrEnWoR732-D67iteOI6DPdJH1opjAuJt" 	#NEXT - RECIEN EDITADA 	Just-Released Music
YOUTUBE_CHANNEL_ID_229 = "PL55713C70BA91BD6E" 	#NEXT - BILLBOARD 2015
YOUTUBE_CHANNEL_ID_230 = "PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI" 	#NEXT - MUSICA POPULAR 	Popular Music
YOUTUBE_CHANNEL_ID_231 = "PL3485902CC4FB6C67" 	#NEXT - ROCK 80S - 90S 	80s & 90s Rock
YOUTUBE_CHANNEL_ID_232 = "PLGBuKfnErZlAkaUUy57-mR97f8SBgMNHh" 	#NEXT - 70S 	Greatest Hits Of The 70s
YOUTUBE_CHANNEL_ID_233 = "PLuK6flVU_Aj5EJ9Pp-C9N7XA0YJr_GrJI" 	#NEXT - 60S 	60s Classic Hits
YOUTUBE_CHANNEL_ID_234 = "PLuK6flVU_Aj45QZ_A5ld0-pP3CIkoNQDk" 	#NEXT - 50S 	50s Classic Hits
YOUTUBE_CHANNEL_ID_235 = "PLi7ihgkEws7RB7W89lEjK2qvItmbyLBLl" 	#NEXT - COUNTRY 2016 	Hottest Country Songs 2016
YOUTUBE_CHANNEL_ID_236 = "PLnpWcMv6bu2X0xfAD6Kt-MgIIFOCNb067" 	#NEXT - COUNTRY MIX 	Country Music Mix
YOUTUBE_CHANNEL_ID_237 = "PL2BN1Zd8U_MsyMeK8r9Vdv1lnQGtoJaSa" 	#NEXT - COUNTRY LO MEJOR 	Hot Country Songs
YOUTUBE_CHANNEL_ID_238 = "PLh__qJ1ro4JgQI6aAgk5dduKLZUGr1Tiw" 	#NEXT - COUNTRY 2000 - 2014 	Country Radio Mix 2000 - 2014
YOUTUBE_CHANNEL_ID_239 = "PLCEE7B2A4B9C9BCE7" 	#NEXT - COUNTRY 90S 	90s Country Music
YOUTUBE_CHANNEL_ID_240 = "PL04199B0AF6C7C9F8" 	#NEXT - COUNTRY 80S 	80s Country Music
YOUTUBE_CHANNEL_ID_241 = "PLFgquLnL59alFaD6qZtCpJgV2CB9L-Boq" 	#NEXT ON: LEONARD COHEN
YOUTUBE_CHANNEL_ID_242 = "PLFgquLnL59ansZbAyA-OqSvImU8yo9j5I" 	#NEXT ON: VISUALLY STUNNING
YOUTUBE_CHANNEL_ID_243 = "PLFgquLnL59amdobdR5OfC5OW3YoGtavfT" 	#NEXT ON: RECAPITULANDO OCTUBRE 	October Recap
YOUTUBE_CHANNEL_ID_244 = "PLFgquLnL59akYTGd40gT26IYoL2kuhQZO" 	#NEXT ON: BANDA SONORA DE LA SEMANA 	Weekend Soundtrack
YOUTUBE_CHANNEL_ID_245 = "PLFgquLnL59an78ZI25rXfkTnpkrLFVXJ8" 	#NEXT ON: DESCUBRIMIRENTO EN EL MUNDO 	Global Discoveries
YOUTUBE_CHANNEL_ID_246 = "PLFgquLnL59am3gKxgT7Tvw-CMAlT4lQiC" 	#NEXT ON: DANCE OFF
YOUTUBE_CHANNEL_ID_247 = "PLFgquLnL59akoZ1GetztyRuu1jtSwOvMi" 	#NEXT ON: SUBRREAL E IRREAL 	Surreal and Unreal
YOUTUBE_CHANNEL_ID_248 = "RDEMQCvwpRTcFnGMj6R-ck__8w" 	#DIEGO TORRES
YOUTUBE_CHANNEL_ID_2000 = "UCY14-R0pMrQzLne7lbTqRvA" 	#CHANNEL VEVO UK
YOUTUBE_CHANNEL_ID_2001 = "UC-7BJPPk_oQGTED1XQA_DTw" 	#CHANNEL VEVO DSCVR
YOUTUBE_CHANNEL_ID_2002 = "UC2TdeJmXTI34g5U13mxMsLA" 	#CHANNEL VEVO ITALY
YOUTUBE_CHANNEL_ID_2003 = "UClGZNNSnYzavv32-PptUTAA" 	#CHANNEL VEVO SPAIN
YOUTUBE_CHANNEL_ID_2004 = "UC-Eb73KoiLmtXnxkz6XLk-g" 	#CHANNEL VEVO NETHERLAND
YOUTUBE_CHANNEL_ID_2005 = "UC9Pbo1KXq5LRSV8yNTW6jtw" 	#CHANNEL VEVO POLSKA
YOUTUBE_CHANNEL_ID_2006 = "UC0t9HSnAFStdSrlHs5K7raA" 	#CHANNEL VEVO fRANCE
YOUTUBE_CHANNEL_ID_2007 = "UCWp8Rc0qh08RZKlWxNfQ6PQ" 	#CHANNEL HEXAGON
YOUTUBE_CHANNEL_ID_2008 = "UCvqvrS2l3R8QNP-3HqobqOw" 	#CHANNEL VEVO FAITHLESS
YOUTUBE_CHANNEL_ID_2009 = "UCB-7IEpKGIdXkgGUObE5D5A" 	#CHANNEL STMPD RCRDS
YOUTUBE_CHANNEL_ID_2010 = "UCIGzDgn6LlPzk3KMwVRP5Xg" 	#CHANNEL NEXT - TOP 40 CHARTS
YOUTUBE_CHANNEL_ID_2011 = "UCR85xzwE1PevoGId8HOnErw" 	#CHANNEL HÉROES DEL SILENCIO
YOUTUBE_CHANNEL_ID_4000 = "TomorrowlandChannel" 	#USER TOMORROWLAND
YOUTUBE_CHANNEL_ID_4001 = "DonDiablo" 	#USER DON DIABLO
YOUTUBE_CHANNEL_ID_4002 = "festivaldevinachile" 	#USER FESTIVAL VINA DEL MAR CHILE
YOUTUBE_CHANNEL_ID_4003 = "MartinGarrix" 	#USER MARTIN GARRIX
YOUTUBE_CHANNEL_ID_4004 = "UMFTV" 	#USER UMFTV
YOUTUBE_CHANNEL_ID_4005 = "jesseyjoyoficial" 	#USER JESSE Y JOY
# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT - EVENTO ESPECIAL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_191+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT CHRISTMAS SONGS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_198+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TEMITA DE LA SEMANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_190+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC LO MAS NUEVO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_202+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC LO NUEVO DE LA SEMANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_201+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC EN LA CIMA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_222+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC RECIEN EDITADA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_228+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS 40 PRINCIPALES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_101+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/Los40PrincipalesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]51 CHART MAXIMA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ChartMaximaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC ASIA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_218+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC BILLBOARD 2015[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_229+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC CHILL OUT[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_99+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC CINE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_151+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC CLASICA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_227+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC CLASICOS DE AYER Y DE HOY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_189+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_214+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY INDICE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_215+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY LO MEJOR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_237+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY MIX[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_236+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY 80S[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_240+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY 90S[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_239+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY 2000 - 2014[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_238+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC COUNTRY 2016[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_235+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC CRISTIANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_224+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC ELECTRONICA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_203+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC ELECTRONICA INDICE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_206+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HARD ROCK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_225+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_188+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HEAVY METAL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_226+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HIP HOP[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_210+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HIP HOP INDICE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_208+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HOUSE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HOUSE VOL. 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_207+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC HOUSE VOL. 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_204+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC INDIE INDICE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_221+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC LATINO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_205+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC LO MEJOR DEL ROCK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_139+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC MEXICO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_219+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC POP[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_209+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC POP ROCK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_216+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC MUSICA POPULAR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_230+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC R&B[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_217+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC RHYTHM & BLUES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_223+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC REGGAE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_212+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC REGGAETON[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC ROCK 80S 90S[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_231+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC ROCK ALTERNATIVO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_211+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC SOUL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_220+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC TRAP[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_213+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 30s-40s-50s[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_84+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 50S[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_234+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 60s[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_85+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 60S VOL. 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_233+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 70s[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_82+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 70S VOL. 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_232+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 70s VOL 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_86+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 80s[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_81+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 80s VOL2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_87+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 90s[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_83+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 90s VOL 2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_88+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2000-2003[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_89+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2004-2007[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_90+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2007-2009[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_91+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2010[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_92+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2011[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_93+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2012[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_94+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2013[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_95+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2014[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_96+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC 2017[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC MIX POP LATINO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_199+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC TOP 40 CHARTS[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2010+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT MUSIC VIDEOS POPULARES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_200+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: BANDA SONORA DE LA SEMANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_244+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: DANCE OFF[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_246+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: DESCUBRIMIRENTO EN EL MUNDO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_245+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: LEONARD COHEN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_241+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: RECAPITULANDO OCTUBRE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_243+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: SUBRREAL E IRREAL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_247+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NEXT ON: VISUALLY STUNNING[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_242+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NextThumbnail.png?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ABBA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_171+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AbbaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]AC-DC[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_122+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ACDCThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ADELE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_118+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AdeleThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]AEROSMITH[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_121+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AerosmithThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ALEJANDRO FERNÁNDEZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_123+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AlejandroFernandezThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ALEJANDRO SANZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AlejandroSanzThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]AMY WINEHOUSE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_143+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AmyWinehouseThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ANDY & LUCAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AndyYLucasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ANTONIO JOSE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AntonioJoseThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ANTONIO OROZCO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AntonioOrozcoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ARIANA GRANDE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_119+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ArianaGrandeThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]AVENTURA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_120+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AventuraThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]AZUCAR MORENO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_156+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/AzucarMorenoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BACKSTREET BOYS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_181+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BackstreetBoysThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BEE GEES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_172+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BeeGeesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BOB DYLAN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_117+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BobDylanThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BOB MARLEY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_113+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BobMarleyThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BON JOVI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_115+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BonJoviThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BECKY G[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BeckyGThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BEYONCÉ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_114+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BeyonceThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BLINK 182[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_184+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/Blink182Thumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]BRUNO MARS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_116+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BrunoMarsThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CALLE 13[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_78+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/Calle13Thumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CAMARÓN DE LA ISLA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CamaronDeLaIslaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CAMELA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_65+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CamelaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CAMILA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_77+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CamilaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CANELITA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CanelitaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CARLOS BAUTE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_74+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CarlosBauteThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CARLOS SANTANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_75+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CarlosSantanaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CARLOS VIVES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_76+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CarlosVivesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CELTAS CORTOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/CeltasCortosThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CHAMBAO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ChambaoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CHAYANNE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_72+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ChayanneThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]CHINO Y NACHO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_187+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ChinoYNachoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]COLDPLAY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_125+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ColdPlayThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DADDY YANKEE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_70+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DaddyYankeeThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAFT PUNK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_128+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DaftPunkThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DANI MARTIN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DaniMartinThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAVID BISBAL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DavidBisvalThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAVID BUSTAMANTE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DavidBustamanteThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAVID DE MARIA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DavidDeMariaThumbnail.jpg?raw=true",
        fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DAVID GUETTA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_127+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DavidGuettaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DEPECHE MODE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_170+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DepecheModeThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DIANA NAVARRO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DianaNavarroThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DIEGO TORRES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_248+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DiegoTorresThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DON DIABLO[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4001+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DonDiabloThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DON DIABLO HEXAGON[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2007+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HexagonThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DON OMAR[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_126+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DonOmarThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DRAKE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_129+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DrakeThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]DUNCAN DHU[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/DuncanDhuThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ED SHEERAN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_97+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EdSheeranThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL BARRIO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElBarrioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL BICHO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_67+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElBichoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL SUEÑO DE MORFEO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElSuenoDeMorfeoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EL ULTIMO DE LA FILA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElUltimoDeLaFilaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ELTON JOHN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_153+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EltonJohnThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ELVIS CRESPO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_163+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElvisCrespoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ELVIS PRESLEY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_130+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ElvisPresleyThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EMINEM[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_132+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EminemThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ENRIQUE IGLESIAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EnriqueIglesiasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ESTOPA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/EstopaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]EXTREMODURO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ExtremoduroThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]FAITHLESS[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2008+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/FaithlessThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]FITO & FITIPALDIS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/FitoYFitipaldisThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]FLAMENCO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/FlamencoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]GLORIA STEFAN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_73+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/GloriaEstefanThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]GLORIA TREVI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_135+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/GloriaTreviThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]GREEN DAY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_134+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/GreenDayThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]GUNS N ROSES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_133+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/GunsNRosesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]GUSTAVO CERATI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_149+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/GustavoCeratiThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HAZE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HazeThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HÉROES DEL SILENCIO[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2011+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HeroesDelSilencioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HOMBRES G[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HombresGThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]HUECO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/HuecoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]IL DIVO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/IlDivoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]INDIA MARTINEZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/IndiaMartinezThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JARABE DE PALO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JarabeDePaloThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]J BALVIN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_79+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JBalvinThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JESSE Y JOY[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4005+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JesseYJoyThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JOAN MANUEL SERRAT[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JoanManuelSerratThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JOAQUIN SABINA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JoaquinSabinaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JOSE MERCÉ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_66+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JoseMerceThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JUAN LUIS GUERRA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JuanLuisGuerraThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JUANES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_68+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JuanesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JULIO IGLESIAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JulioIglesiasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]JUSTIN BIEBER[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_98+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/JustinBieberThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]KATY PERRY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_164+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/KatyPerryThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]KIKO VENENO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_162+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/KikoVenenoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]KISS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_161+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/KissThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LA OREJA DE VAN GOGH[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LaOrejaDeVanGoghThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LA QUINTA ESTACION[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_177+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LaQuintaEstacionThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LED ZEPPELIN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_185+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LedZeppelinThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LINKIN PARK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_174+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LinkinParkThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LIONEL RICHIE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_146+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LionelRichieThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOQUILLO Y LOS TROGLODITAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LoquilloYLosTrogloditasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS DEL RÍO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosDelRioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS INHUMANOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_160+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosInhumanosThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS REBUJITOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosRebujitosThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS SECRETOS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosSecretosThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LOS SUAVES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LosSuavesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LUIS FONSI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_165+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LuisFonsiThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]LUIS MIGUEL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_100+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/LuisMiguelThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]M-CLAN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MclanThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MADONNA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_166+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MadonnaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MAGO DE OZ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MagoDeOzThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MAÍTA VENDE CÁ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MaitaVendeCaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MALÚ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MaluThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MALUMA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_80+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MalumaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_192+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ManaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MANOLO GARCIA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ManoloGarciaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MANOLO TENA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_193+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ManoloTenaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MANUEL CARRASCO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ManuelCarrascoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MARC ANTHONY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_71+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MarcAnthonyThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MARIA ARTES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MariaArtesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MARIAH CAREY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_168+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MariahCareyThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MAROON 5[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_136+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/Marron5Thumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MARTIN GARRIX (+x)[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4003+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MartinGarrixThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MECANO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MecanoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MELENDI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_194+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MelendiThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]METALLICA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_137+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MetallicaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MICHAEL JACKSON[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_155+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MichaelJacksonThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]MIGUEL BOSÉ[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/MiguelBoseThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NACHA POP[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NachaPopThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NAVAJITA PLATEADA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NavajitaPlateadaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NIÑA PASTORI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NinaPastoriThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NIRVANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_138+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NirvanaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]NO ME PISES QUE LLEVO CHANCLAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_159+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/NoMePisesQueLlevoChanclasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]OASIS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_186+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/OasisThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]OBK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ObkThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ONE DIRECTION[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_173+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/OneDirectionThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PABLO ALBORÁN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PabloAlboranThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PASTORA SOLER[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PastoraSolerThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PERET[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_157+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PeretThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PETER CETERA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_147+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PeterCeteraThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PETER GRABIEL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_148+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PeterGabrielThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PHIL COLLINS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_144+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PhilCollinsThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PINK[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_154+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PinkThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]PINK FLOYD[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_140+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/PinkFloydThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]QUEEN[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_112+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/QueenThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RADIO FUTURA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RadioFuturaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RAMONES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_183+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RamonesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RAPHAEL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RaphaelThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RED HOT CHILI PEPPERS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_176+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RedHotChiliPeppersThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]R.E.M[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_131+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RemThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]RICARDO ARJONA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_124+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RicardoArjonaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ROD STEWART[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_145+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RodStewartThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ROSARIO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RosarioThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]ROXETTE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_169+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/RoxetteThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SALVATORE GANACCI[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_195+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SalvatoreGanacciThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SEGURIDAD SOCIAL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_158+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SeguridadSocialThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SERGIO CONTRERAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SergioContrerasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SERGIO DALMA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SergioDalmaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SODA STEREO[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_150+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SodaStereoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SPICE GIRL[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_182+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SpiceGirlThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]STING[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_175+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/StingThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]STMPD RCRDS[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2009+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/StmpdRcrdsThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SHAKIRA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_69+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ShakiraThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]SUPERSUBMARINA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_196+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/SupersubmarinaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TATU[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_180+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TatuThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TAYLOR SWIFT[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_142+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TaylorSwiftThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE BEATLES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_102+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheBeatlesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE BLACK EYED PEAS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_110+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/BlackEyedPeasThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE CHAINSMOKERS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_105+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheChainsmokersThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE CHERMICAL BROTHERS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_179+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheChimicalBrothersThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE CORRS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_109+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheCorrsThumbnails.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE CRANBERRIES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_107+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheCranberriesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE DOORS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_104+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheDoorsThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE KILLERS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_103+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheKillersThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE POLICE[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_106+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/ThePoliceThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE PRODIGY[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_178+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheProdigyThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE ROLLING STONES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_111+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheRollingStonesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]THE SMITHS[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_108+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TheSmithsThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TINA TURNER[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_167+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TinaTurnerThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TOM JONES[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_152+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TomJonesThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TRIANA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TrianaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]U2[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_141+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/U2Thumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VETUSTA MORLA[/COLOR]",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_197+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VetustaMorlaThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]FESTIVAL VINA DEL MAR CHILE[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4002+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VinaDelMarThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO UK[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2000+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO DSCVR[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2001+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO ITALY[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2002+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO SPAIN[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2003+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO NETHERLAND[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2004+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO POLSKA[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2005+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]VEVO FRANCE[/COLOR]",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2006+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/VevoThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]TOMORROWLAND[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4000+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/TomorrowlandThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="[COLOR gold]UMFTV[/COLOR]",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4004+"/",
        thumbnail="https://github.com/djliptv/NEXT/blob/master/Pics/UmfTvThumbnail.jpg?raw=true",
		fanart="https://github.com/djliptv/NEXT/blob/master/Pics/NextFanart.jpg?raw=true",
        folder=True )
run()