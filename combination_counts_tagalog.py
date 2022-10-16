import random

#could so-called secondary composition cases in native vocabulary (McCone 1997:90-1) be burps from a bigrammatic grammar? 
#should make separate lists of native/loan secondary orderings

combination_cnt = (
    [('RED',),('RED',), None],
    [('ma',),('ma',), 934762],#Ryan doesn't give freqs for prefixes without RED in table 2, just using total
    [('Pi',),('Pi',), None],
    [('mag',),('mag',), None],
    [('ka',),('ka',), 165043], 
    [('si',),('si',), None],
    [('pag',),('pag',), 527618],
    [('pa',),('pa',), 510090],
    [('ki',),('ki',), None],
    [('RED', 'ma'),('RED', 'ma'), 0],
    [('RED', 'ma'),('ma', 'RED'), 934762],
    [('RED', 'Pi'),('RED', 'Pi'), None],
    [('RED', 'mag'),('RED', 'mag'), None],
    [('RED', 'ka'),('RED', 'ka'), 52648.717],
    [('RED', 'ka'),('ka', 'RED'), 112394.283], 
    [('RED', 'si'),('RED', 'si'), None],
    [('RED', 'pag'),('RED', 'pag'), 3165.708],
    [('RED', 'pag'),('pag', 'RED'), 524452.292],
    [('RED', 'pa'),('RED', 'pa'), 181081.95],
    [('RED', 'pa'),('pa', 'RED'), 329008.05],
    [('RED', 'ki'),('RED', 'ki'), None],
    [('ma', 'Pi'),('ma', 'Pi'), 653862],
    [('ma', 'mag'),('ma', 'mag'), None],
    [('ma', 'ka'),('ma', 'ka'), 6053626],
    [('ma', 'si'),('ma', 'si'), None],
    [('ma', 'pag'),('ma', 'pag'), 73100],
    [('ma', 'pa'),('ma', 'pa'), 706361],
    [('ma', 'ki'),('ma', 'ki'), 275096],
    [('Pi', 'ka'),('Pi', 'ka'), 274986],
    [('Pi', 'si'),('Pi', 'si'), None],
    [('mag', 'ka'),('mag', 'ka'), 559113],
    [('mag', 'si'),('mag', 'si'), 14429],
    [('Pi', 'pag'),('Pi', 'pag'), 306153],
    [('mag', 'pag'),('mag', 'pag'), None],
    [('Pi', 'pa'),('Pi', 'pa'), 951363],
    [('mag', 'pa'),('mag', 'pa'), 970285],
    [('Pi', 'ki'),('Pi', 'ki'), None],
    [('mag', 'ki'),('mag', 'ki'), None],
    [('ka', 'pag'),('ka', 'pag'), 15612],
    [('si', 'pag'),('si', 'pag'), None],
    [('ka', 'pa'),('ka', 'pa'), None],
    [('si', 'pa'),('si', 'pa'), None],
    [('ka', 'ki'),('ka', 'ki'), None],
    [('si', 'ki'),('si', 'ki'), None],
    [('pag', 'pa'),('pag', 'pa'), 883858],
    [('pag', 'ki'),('pag', 'ki'), None],
    [('pa', 'ki'),('pa', 'ki'), 125622],
    [('RED', 'ma', 'Pi'),('RED', 'ma', 'Pi'), 0],
    [('RED', 'ma', 'Pi'),('ma', 'RED', 'Pi'), 88271.37],
    [('RED', 'ma', 'Pi'),('ma', 'Pi', 'RED'), 565590.63],
    [('RED', 'ma', 'mag'),('RED', 'ma', 'mag'), None],
    [('RED', 'ma', 'ka'),('RED', 'ma', 'ka'), 0],
    [('RED', 'ma', 'ka'),('ma', 'RED', 'ka'), 5884124.472],
    [('RED', 'ma', 'ka'),('ma', 'ka', 'RED'), 1695015.28],
    [('RED', 'ma', 'si'),('RED', 'ma', 'si'), None],
    [('RED', 'ma', 'pag'),('RED', 'ma', 'pag'), 0],
    [('RED', 'ma', 'pag'),('ma', 'RED', 'pag'), 4166.7],
    [('RED', 'ma', 'pag'),('ma', 'pag', 'RED'), 68933.3],
    [('RED', 'ma', 'pa'),('RED', 'ma', 'pa'), 0],
    [('RED', 'ma', 'pa'),('ma', 'RED', 'pa'), 678106.56],
    [('RED', 'ma', 'pa'),('ma', 'pa', 'RED'), 28254.44],
    [('RED', 'ma', 'ki'),('RED', 'ma', 'ki'), 0],
    [('RED', 'ma', 'ki'),('ma', 'RED', 'ki'), 262716.68],
    [('RED', 'ma', 'ki'),('ma', 'ki', 'RED'), 12379.32],
    [('RED', 'Pi', 'ka'),('RED', 'Pi', 'ka'), 0],
    [('RED', 'Pi', 'ka'),('Pi', 'RED', 'ka'), 78371.01],
    [('RED', 'Pi', 'ka'),('Pi', 'ka', 'RED'), 196614.99],
    [('RED', 'Pi', 'si'),('RED', 'Pi', 'si'), None],
    [('RED', 'mag', 'ka'),('RED', 'mag', 'ka'), 0],
    [('RED', 'mag', 'ka'),('mag', 'RED', 'ka'), 558553.887],
    [('RED', 'mag', 'ka'),('mag', 'ka', 'RED'), 559.113],
    [('RED', 'mag', 'si'),('RED', 'mag', 'si'), 0],
    [('RED', 'mag', 'si'),('mag', 'RED', 'si'), 14414.571],
    [('RED', 'mag', 'si'),('mag', 'si', 'RED'), 14.429],
    [('RED', 'Pi', 'pag'),('RED', 'Pi', 'pag'), 0],
    [('RED', 'Pi', 'pag'),('Pi', 'RED', 'pag'), 4592.295],
    [('RED', 'Pi', 'pag'),('Pi', 'pag', 'RED'), 301560.705],
    [('RED', 'mag', 'pag'),('RED', 'mag', 'pag'), None],
    [('RED', 'Pi', 'pa'),('RED', 'Pi', 'pa'), 0],
    [('RED', 'Pi', 'pa'),('Pi', 'RED', 'pa'), 798193.557],
    [('RED', 'Pi', 'pa'),('Pi', 'pa', 'RED'), 153169.443], #made it through Pi pa
    [('RED', 'mag', 'pa'),('RED', 'mag', 'pa'), 0],
    [('RED', 'mag', 'pa'),('mag', 'RED', 'pa'), 970285],
    [('RED', 'mag', 'pa'),('mag', 'pa', 'RED'), 0],
    [('RED', 'Pi', 'ki'),('RED', 'Pi', 'ki'), None],
    [('RED', 'mag', 'ki'),('RED', 'mag', 'ki'), None],
    [('RED', 'ka', 'pag'),('RED', 'ka', 'pag'), 4277.688],
    [('RED', 'ka', 'pag'),('ka', 'RED', 'pag'), 0],
    [('RED', 'ka', 'pag'),('ka', 'pag', 'RED'), 9773.112],
    [('RED', 'si', 'pag'),('RED', 'si', 'pag'), None],
    [('RED', 'ka', 'pa'),('RED', 'ka', 'pa'), None],
    [('RED', 'si', 'pa'),('RED', 'si', 'pa'), None],
    [('RED', 'ka', 'ki'),('RED', 'ka', 'ki'), None],
    [('RED', 'si', 'ki'),('RED', 'si', 'ki'), None],
    [('RED', 'pag', 'pa'),('RED', 'pag', 'pa'), 0],
    [('RED', 'pag', 'pa'),('pag', 'RED', 'pa'), 883858],
    [('RED', 'pag', 'pa'),('pag', 'pa', 'RED'), 0],
    [('RED', 'pag', 'ki'),('RED', 'pag', 'ki'), None],
    [('RED', 'pa', 'ki'),('RED', 'pa', 'ki'), 753.732],
    [('RED', 'pa', 'ki'),('pa', 'RED', 'ki'), 115823.484],
    [('RED', 'pa', 'ki'),('pa', 'ki', 'RED'), 9044.784], 
    [('ma', 'Pi', 'ka'),('ma', 'Pi', 'ka'), None],
    [('ma', 'Pi', 'si'),('ma', 'Pi', 'si'), None],
    [('ma', 'mag', 'ka'),('ma', 'mag', 'ka'), None],
    [('ma', 'mag', 'si'),('ma', 'mag', 'si'), None],
    [('ma', 'Pi', 'pag'),('ma', 'Pi', 'pag'), None],
    [('ma', 'mag', 'pag'),('ma', 'mag', 'pag'), None],
    [('ma', 'Pi', 'pa'),('ma', 'Pi', 'pa'), None],
    [('ma', 'mag', 'pa'),('ma', 'mag', 'pa'), None],
    [('ma', 'Pi', 'ki'),('ma', 'Pi', 'ki'), None],
    [('ma', 'mag', 'ki'),('ma', 'mag', 'ki'), None],
    [('ma', 'ka', 'pag'),('ma', 'ka', 'pag'), None],
    [('ma', 'si', 'pag'),('ma', 'si', 'pag'), None],
    [('ma', 'ka', 'pa'),('ma', 'ka', 'pa'), None],
    [('ma', 'si', 'pa'),('ma', 'si', 'pa'), None],
    [('ma', 'ka', 'ki'),('ma', 'ka', 'ki'), None],
    [('ma', 'si', 'ki'),('ma', 'si', 'ki'), None],
    [('ma', 'pag', 'pa'),('ma', 'pag', 'pa'), None],
    [('ma', 'pag', 'ki'),('ma', 'pag', 'ki'), None],
    [('ma', 'pa', 'ki'),('ma', 'pa', 'ki'), None],
    [('Pi', 'ka', 'pag'),('Pi', 'ka', 'pag'), 386],
    [('Pi', 'si', 'pag'),('Pi', 'si', 'pag'), None],
    [('mag', 'ka', 'pag'),('mag', 'ka', 'pag'), None],
    [('mag', 'si', 'pag'),('mag', 'si', 'pag'), 2724],
    [('Pi', 'ka', 'pa'),('Pi', 'ka', 'pa'), None],
    [('Pi', 'si', 'pa'),('Pi', 'si', 'pa'), None],
    [('mag', 'ka', 'pa'),('mag', 'ka', 'pa'), None],
    [('mag', 'si', 'pa'),('mag', 'si', 'pa'), None],
    [('Pi', 'ka', 'ki'),('Pi', 'ka', 'ki'), None],
    [('Pi', 'si', 'ki'),('Pi', 'si', 'ki'), None],
    [('mag', 'ka', 'ki'),('mag', 'ka', 'ki'), None],
    [('mag', 'si', 'ki'),('mag', 'si', 'ki'), None],
    [('Pi', 'pag', 'pa'),('Pi', 'pag', 'pa'), 51776],
    [('mag', 'pag', 'pa'),('mag', 'pag', 'pa'), None],
    [('Pi', 'pag', 'ki'),('Pi', 'pag', 'ki'), None],
    [('mag', 'pag', 'ki'),('mag', 'pag', 'ki'), None],
    [('Pi', 'pa', 'ki'),('Pi', 'pa', 'ki'), 762],
    [('mag', 'pa', 'ki'),('mag', 'pa', 'ki'), None],
    [('ka', 'pag', 'pa'),('ka', 'pag', 'pa'), None],
    [('si', 'pag', 'pa'),('si', 'pag', 'pa'), None],
    [('ka', 'pag', 'ki'),('ka', 'pag', 'ki'), None],
    [('si', 'pag', 'ki'),('si', 'pag', 'ki'), None],
    [('ka', 'pa', 'ki'),('ka', 'pa', 'ki'), None],
    [('si', 'pa', 'ki'),('si', 'pa', 'ki'), None],
    [('pag', 'pa', 'ki'),('pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'ka'),('RED', 'ma', 'Pi', 'ka'), None],
    [('RED', 'ma', 'Pi', 'si'),('RED', 'ma', 'Pi', 'si'), None],
    [('RED', 'ma', 'mag', 'ka'),('RED', 'ma', 'mag', 'ka'), None],
    [('RED', 'ma', 'mag', 'si'),('RED', 'ma', 'mag', 'si'), None],
    [('RED', 'ma', 'Pi', 'pag'),('RED', 'ma', 'Pi', 'pag'), None],
    [('RED', 'ma', 'mag', 'pag'),('RED', 'ma', 'mag', 'pag'), None],
    [('RED', 'ma', 'Pi', 'pa'),('RED', 'ma', 'Pi', 'pa'), None],
    [('RED', 'ma', 'mag', 'pa'),('RED', 'ma', 'mag', 'pa'), None],
    [('RED', 'ma', 'Pi', 'ki'),('RED', 'ma', 'Pi', 'ki'), None],
    [('RED', 'ma', 'mag', 'ki'),('RED', 'ma', 'mag', 'ki'), None],
    [('RED', 'ma', 'ka', 'pag'),('RED', 'ma', 'ka', 'pag'), None],
    [('RED', 'ma', 'si', 'pag'),('RED', 'ma', 'si', 'pag'), None],
    [('RED', 'ma', 'ka', 'pa'),('RED', 'ma', 'ka', 'pa'), None],
    [('RED', 'ma', 'si', 'pa'),('RED', 'ma', 'si', 'pa'), None],
    [('RED', 'ma', 'ka', 'ki'),('RED', 'ma', 'ka', 'ki'), None],
    [('RED', 'ma', 'si', 'ki'),('RED', 'ma', 'si', 'ki'), None],
    [('RED', 'ma', 'pag', 'pa'),('RED', 'ma', 'pag', 'pa'), None],
    [('RED', 'ma', 'pag', 'ki'),('RED', 'ma', 'pag', 'ki'), None],
    [('RED', 'ma', 'pa', 'ki'),('RED', 'ma', 'pa', 'ki'), None],
    [('RED', 'Pi', 'ka', 'pag'),('RED', 'Pi', 'ka', 'pag'), 0],
    [('RED', 'Pi', 'ka', 'pag'),('Pi', 'RED', 'ka', 'pag'), 10.808],
    [('RED', 'Pi', 'ka', 'pag'),('Pi', 'ka', 'RED', 'pag'), 1.158],
    [('RED', 'Pi', 'ka', 'pag'),('Pi', 'ka', 'pag', 'RED'), 374.034],
    [('RED', 'Pi', 'si', 'pag'),('RED', 'Pi', 'si', 'pag'), None],
    [('RED', 'mag', 'ka', 'pag'),('RED', 'mag', 'ka', 'pag'), None],
    [('RED', 'mag', 'si', 'pag'),('RED', 'mag', 'si', 'pag'), 0],
    [('RED', 'mag', 'si', 'pag'),('mag', 'RED', 'si', 'pag'), 2724],
    [('RED', 'mag', 'si', 'pag'),('mag', 'si', 'RED', 'pag'), 0],
    [('RED', 'mag', 'si', 'pag'),('mag', 'si', 'pag', 'RED'), 0], #UNTIL THIS FAR
    [('RED', 'Pi', 'ka', 'pa'),('RED', 'Pi', 'ka', 'pa'), None],
    [('RED', 'Pi', 'si', 'pa'),('RED', 'Pi', 'si', 'pa'), None],
    [('RED', 'mag', 'ka', 'pa'),('RED', 'mag', 'ka', 'pa'), None],
    [('RED', 'mag', 'si', 'pa'),('RED', 'mag', 'si', 'pa'), None],
    [('RED', 'Pi', 'ka', 'ki'),('RED', 'Pi', 'ka', 'ki'), None],
    [('RED', 'Pi', 'si', 'ki'),('RED', 'Pi', 'si', 'ki'), None],
    [('RED', 'mag', 'ka', 'ki'),('RED', 'mag', 'ka', 'ki'), None],
    [('RED', 'mag', 'si', 'ki'),('RED', 'mag', 'si', 'ki'), None],
    [('RED', 'Pi', 'pag', 'pa'),('RED', 'Pi', 'pag', 'pa'), 0],
    [('RED', 'Pi', 'pag', 'pa'),('Pi', 'RED', 'pag', 'pa'), 3520.768],
    [('RED', 'Pi', 'pag', 'pa'),('Pi', 'pag', 'RED', 'pa'), 48255.232],
    [('RED', 'Pi', 'pag', 'pa'),('Pi', 'pag', 'pa', 'RED'), 0],
    [('RED', 'mag', 'pag', 'pa'),('RED', 'mag', 'pag', 'pa'), None],
    [('RED', 'Pi', 'pag', 'ki'),('RED', 'Pi', 'pag', 'ki'), None],
    [('RED', 'mag', 'pag', 'ki'),('RED', 'mag', 'pag', 'ki'), None],
    [('RED', 'Pi', 'pa', 'ki'),('RED', 'Pi', 'pa', 'ki'), 0],
    [('RED', 'Pi', 'pa', 'ki'),('Pi', 'RED', 'pa', 'ki'), 136.398],
    [('RED', 'Pi', 'pa', 'ki'),('Pi', 'pa', 'RED', 'ki'), 477.012],
    [('RED', 'Pi', 'pa', 'ki'),('Pi', 'pa', 'ki', 'RED'), 148.59],
    [('RED', 'mag', 'pa', 'ki'),('RED', 'mag', 'pa', 'ki'), None],
    [('RED', 'ka', 'pag', 'pa'),('RED', 'ka', 'pag', 'pa'), None],
    [('RED', 'si', 'pag', 'pa'),('RED', 'si', 'pag', 'pa'), None],
    [('RED', 'ka', 'pag', 'ki'),('RED', 'ka', 'pag', 'ki'), None],
    [('RED', 'si', 'pag', 'ki'),('RED', 'si', 'pag', 'ki'), None],
    [('RED', 'ka', 'pa', 'ki'),('RED', 'ka', 'pa', 'ki'), None],
    [('RED', 'si', 'pa', 'ki'),('RED', 'si', 'pa', 'ki'), None],
    [('RED', 'pag', 'pa', 'ki'),('RED', 'pag', 'pa', 'ki'), None],
    [('ma', 'Pi', 'ka', 'pag'),('ma', 'Pi', 'ka', 'pag'), None],
    [('ma', 'Pi', 'si', 'pag'),('ma', 'Pi', 'si', 'pag'), None],
    [('ma', 'mag', 'ka', 'pag'),('ma', 'mag', 'ka', 'pag'), None],
    [('ma', 'mag', 'si', 'pag'),('ma', 'mag', 'si', 'pag'), None],
    [('ma', 'Pi', 'ka', 'pa'),('ma', 'Pi', 'ka', 'pa'), None],
    [('ma', 'Pi', 'si', 'pa'),('ma', 'Pi', 'si', 'pa'), None],
    [('ma', 'mag', 'ka', 'pa'),('ma', 'mag', 'ka', 'pa'), None],
    [('ma', 'mag', 'si', 'pa'),('ma', 'mag', 'si', 'pa'), None],
    [('ma', 'Pi', 'ka', 'ki'),('ma', 'Pi', 'ka', 'ki'), None],
    [('ma', 'Pi', 'si', 'ki'),('ma', 'Pi', 'si', 'ki'), None],
    [('ma', 'mag', 'ka', 'ki'),('ma', 'mag', 'ka', 'ki'), None],
    [('ma', 'mag', 'si', 'ki'),('ma', 'mag', 'si', 'ki'), None],
    [('ma', 'Pi', 'pag', 'pa'),('ma', 'Pi', 'pag', 'pa'), None],
    [('ma', 'mag', 'pag', 'pa'),('ma', 'mag', 'pag', 'pa'), None],
    [('ma', 'Pi', 'pag', 'ki'),('ma', 'Pi', 'pag', 'ki'), None],
    [('ma', 'mag', 'pag', 'ki'),('ma', 'mag', 'pag', 'ki'), None],
    [('ma', 'Pi', 'pa', 'ki'),('ma', 'Pi', 'pa', 'ki'), None],
    [('ma', 'mag', 'pa', 'ki'),('ma', 'mag', 'pa', 'ki'), None],
    [('ma', 'ka', 'pag', 'pa'),('ma', 'ka', 'pag', 'pa'), None],
    [('ma', 'si', 'pag', 'pa'),('ma', 'si', 'pag', 'pa'), None],
    [('ma', 'ka', 'pag', 'ki'),('ma', 'ka', 'pag', 'ki'), None],
    [('ma', 'si', 'pag', 'ki'),('ma', 'si', 'pag', 'ki'), None],
    [('ma', 'ka', 'pa', 'ki'),('ma', 'ka', 'pa', 'ki'), None],
    [('ma', 'si', 'pa', 'ki'),('ma', 'si', 'pa', 'ki'), None],
    [('ma', 'pag', 'pa', 'ki'),('ma', 'pag', 'pa', 'ki'), None],
    [('Pi', 'ka', 'pag', 'pa'),('Pi', 'ka', 'pag', 'pa'), None],
    [('Pi', 'si', 'pag', 'pa'),('Pi', 'si', 'pag', 'pa'), None],
    [('mag', 'ka', 'pag', 'pa'),('mag', 'ka', 'pag', 'pa'), None],
    [('mag', 'si', 'pag', 'pa'),('mag', 'si', 'pag', 'pa'), None],
    [('Pi', 'ka', 'pag', 'ki'),('Pi', 'ka', 'pag', 'ki'), None],
    [('Pi', 'si', 'pag', 'ki'),('Pi', 'si', 'pag', 'ki'), None],
    [('mag', 'ka', 'pag', 'ki'),('mag', 'ka', 'pag', 'ki'), None],
    [('mag', 'si', 'pag', 'ki'),('mag', 'si', 'pag', 'ki'), None],
    [('Pi', 'ka', 'pa', 'ki'),('Pi', 'ka', 'pa', 'ki'), None],
    [('Pi', 'si', 'pa', 'ki'),('Pi', 'si', 'pa', 'ki'), None],
    [('mag', 'ka', 'pa', 'ki'),('mag', 'ka', 'pa', 'ki'), None],
    [('mag', 'si', 'pa', 'ki'),('mag', 'si', 'pa', 'ki'), None],
    [('Pi', 'pag', 'pa', 'ki'),('Pi', 'pag', 'pa', 'ki'), None],
    [('mag', 'pag', 'pa', 'ki'),('mag', 'pag', 'pa', 'ki'), None],
    [('ka', 'pag', 'pa', 'ki'),('ka', 'pag', 'pa', 'ki'), None],
    [('si', 'pag', 'pa', 'ki'),('si', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'ka', 'pag'),('RED', 'ma', 'Pi', 'ka', 'pag'), None],
    [('RED', 'ma', 'Pi', 'si', 'pag'),('RED', 'ma', 'Pi', 'si', 'pag'), None],
    [('RED', 'ma', 'mag', 'ka', 'pag'),('RED', 'ma', 'mag', 'ka', 'pag'), None],
    [('RED', 'ma', 'mag', 'si', 'pag'),('RED', 'ma', 'mag', 'si', 'pag'), None],
    [('RED', 'ma', 'Pi', 'ka', 'pa'),('RED', 'ma', 'Pi', 'ka', 'pa'), None],
    [('RED', 'ma', 'Pi', 'si', 'pa'),('RED', 'ma', 'Pi', 'si', 'pa'), None],
    [('RED', 'ma', 'mag', 'ka', 'pa'),('RED', 'ma', 'mag', 'ka', 'pa'), None],
    [('RED', 'ma', 'mag', 'si', 'pa'),('RED', 'ma', 'mag', 'si', 'pa'), None],
    [('RED', 'ma', 'Pi', 'ka', 'ki'),('RED', 'ma', 'Pi', 'ka', 'ki'), None],
    [('RED', 'ma', 'Pi', 'si', 'ki'),('RED', 'ma', 'Pi', 'si', 'ki'), None],
    [('RED', 'ma', 'mag', 'ka', 'ki'),('RED', 'ma', 'mag', 'ka', 'ki'), None],
    [('RED', 'ma', 'mag', 'si', 'ki'),('RED', 'ma', 'mag', 'si', 'ki'), None],
    [('RED', 'ma', 'Pi', 'pag', 'pa'),('RED', 'ma', 'Pi', 'pag', 'pa'), None],
    [('RED', 'ma', 'mag', 'pag', 'pa'),('RED', 'ma', 'mag', 'pag', 'pa'), None],
    [('RED', 'ma', 'Pi', 'pag', 'ki'),('RED', 'ma', 'Pi', 'pag', 'ki'), None],
    [('RED', 'ma', 'mag', 'pag', 'ki'),('RED', 'ma', 'mag', 'pag', 'ki'), None],
    [('RED', 'ma', 'Pi', 'pa', 'ki'),('RED', 'ma', 'Pi', 'pa', 'ki'), None],
    [('RED', 'ma', 'mag', 'pa', 'ki'),('RED', 'ma', 'mag', 'pa', 'ki'), None],
    [('RED', 'ma', 'ka', 'pag', 'pa'),('RED', 'ma', 'ka', 'pag', 'pa'), None],
    [('RED', 'ma', 'si', 'pag', 'pa'),('RED', 'ma', 'si', 'pag', 'pa'), None],
    [('RED', 'ma', 'ka', 'pag', 'ki'),('RED', 'ma', 'ka', 'pag', 'ki'), None],
    [('RED', 'ma', 'si', 'pag', 'ki'),('RED', 'ma', 'si', 'pag', 'ki'), None],
    [('RED', 'ma', 'ka', 'pa', 'ki'),('RED', 'ma', 'ka', 'pa', 'ki'), None],
    [('RED', 'ma', 'si', 'pa', 'ki'),('RED', 'ma', 'si', 'pa', 'ki'), None],
    [('RED', 'ma', 'pag', 'pa', 'ki'),('RED', 'ma', 'pag', 'pa', 'ki'), None],
    [('RED', 'Pi', 'ka', 'pag', 'pa'),('RED', 'Pi', 'ka', 'pag', 'pa'), None],
    [('RED', 'Pi', 'si', 'pag', 'pa'),('RED', 'Pi', 'si', 'pag', 'pa'), None],
    [('RED', 'mag', 'ka', 'pag', 'pa'),('RED', 'mag', 'ka', 'pag', 'pa'), None],
    [('RED', 'mag', 'si', 'pag', 'pa'),('RED', 'mag', 'si', 'pag', 'pa'), None],
    [('RED', 'Pi', 'ka', 'pag', 'ki'),('RED', 'Pi', 'ka', 'pag', 'ki'), None],
    [('RED', 'Pi', 'si', 'pag', 'ki'),('RED', 'Pi', 'si', 'pag', 'ki'), None],
    [('RED', 'mag', 'ka', 'pag', 'ki'),('RED', 'mag', 'ka', 'pag', 'ki'), None],
    [('RED', 'mag', 'si', 'pag', 'ki'),('RED', 'mag', 'si', 'pag', 'ki'), None],
    [('RED', 'Pi', 'ka', 'pa', 'ki'),('RED', 'Pi', 'ka', 'pa', 'ki'), None],
    [('RED', 'Pi', 'si', 'pa', 'ki'),('RED', 'Pi', 'si', 'pa', 'ki'), None],
    [('RED', 'mag', 'ka', 'pa', 'ki'),('RED', 'mag', 'ka', 'pa', 'ki'), None],
    [('RED', 'mag', 'si', 'pa', 'ki'),('RED', 'mag', 'si', 'pa', 'ki'), None],
    [('RED', 'Pi', 'pag', 'pa', 'ki'),('RED', 'Pi', 'pag', 'pa', 'ki'), None],
    [('RED', 'mag', 'pag', 'pa', 'ki'),('RED', 'mag', 'pag', 'pa', 'ki'), None],
    [('RED', 'ka', 'pag', 'pa', 'ki'),('RED', 'ka', 'pag', 'pa', 'ki'), None],
    [('RED', 'si', 'pag', 'pa', 'ki'),('RED', 'si', 'pag', 'pa', 'ki'), None],
    [('ma', 'Pi', 'ka', 'pag', 'pa'),('ma', 'Pi', 'ka', 'pag', 'pa'), None],
    [('ma', 'Pi', 'si', 'pag', 'pa'),('ma', 'Pi', 'si', 'pag', 'pa'), None],
    [('ma', 'mag', 'ka', 'pag', 'pa'),('ma', 'mag', 'ka', 'pag', 'pa'), None],
    [('ma', 'mag', 'si', 'pag', 'pa'),('ma', 'mag', 'si', 'pag', 'pa'), None],
    [('ma', 'Pi', 'ka', 'pag', 'ki'),('ma', 'Pi', 'ka', 'pag', 'ki'), None],
    [('ma', 'Pi', 'si', 'pag', 'ki'),('ma', 'Pi', 'si', 'pag', 'ki'), None],
    [('ma', 'mag', 'ka', 'pag', 'ki'),('ma', 'mag', 'ka', 'pag', 'ki'), None],
    [('ma', 'mag', 'si', 'pag', 'ki'),('ma', 'mag', 'si', 'pag', 'ki'), None],
    [('ma', 'Pi', 'ka', 'pa', 'ki'),('ma', 'Pi', 'ka', 'pa', 'ki'), None],
    [('ma', 'Pi', 'si', 'pa', 'ki'),('ma', 'Pi', 'si', 'pa', 'ki'), None],
    [('ma', 'mag', 'ka', 'pa', 'ki'),('ma', 'mag', 'ka', 'pa', 'ki'), None],
    [('ma', 'mag', 'si', 'pa', 'ki'),('ma', 'mag', 'si', 'pa', 'ki'), None],
    [('ma', 'Pi', 'pag', 'pa', 'ki'),('ma', 'Pi', 'pag', 'pa', 'ki'), None],
    [('ma', 'mag', 'pag', 'pa', 'ki'),('ma', 'mag', 'pag', 'pa', 'ki'), None],
    [('ma', 'ka', 'pag', 'pa', 'ki'),('ma', 'ka', 'pag', 'pa', 'ki'), None],
    [('ma', 'si', 'pag', 'pa', 'ki'),('ma', 'si', 'pag', 'pa', 'ki'), None],
    [('Pi', 'ka', 'pag', 'pa', 'ki'),('Pi', 'ka', 'pag', 'pa', 'ki'), None],
    [('Pi', 'si', 'pag', 'pa', 'ki'),('Pi', 'si', 'pag', 'pa', 'ki'), None],
    [('mag', 'ka', 'pag', 'pa', 'ki'),('mag', 'ka', 'pag', 'pa', 'ki'), None],
    [('mag', 'si', 'pag', 'pa', 'ki'),('mag', 'si', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'ka', 'pag', 'pa'),('RED', 'ma', 'Pi', 'ka', 'pag', 'pa'), None],
    [('RED', 'ma', 'Pi', 'si', 'pag', 'pa'),('RED', 'ma', 'Pi', 'si', 'pag', 'pa'), None],
    [('RED', 'ma', 'mag', 'ka', 'pag', 'pa'),('RED', 'ma', 'mag', 'ka', 'pag', 'pa'), None],
    [('RED', 'ma', 'mag', 'si', 'pag', 'pa'),('RED', 'ma', 'mag', 'si', 'pag', 'pa'), None],
    [('RED', 'ma', 'Pi', 'ka', 'pag', 'ki'),('RED', 'ma', 'Pi', 'ka', 'pag', 'ki'), None],
    [('RED', 'ma', 'Pi', 'si', 'pag', 'ki'),('RED', 'ma', 'Pi', 'si', 'pag', 'ki'), None],
    [('RED', 'ma', 'mag', 'ka', 'pag', 'ki'),('RED', 'ma', 'mag', 'ka', 'pag', 'ki'), None],
    [('RED', 'ma', 'mag', 'si', 'pag', 'ki'),('RED', 'ma', 'mag', 'si', 'pag', 'ki'), None],
    [('RED', 'ma', 'Pi', 'ka', 'pa', 'ki'),('RED', 'ma', 'Pi', 'ka', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'si', 'pa', 'ki'),('RED', 'ma', 'Pi', 'si', 'pa', 'ki'), None],
    [('RED', 'ma', 'mag', 'ka', 'pa', 'ki'),('RED', 'ma', 'mag', 'ka', 'pa', 'ki'), None],
    [('RED', 'ma', 'mag', 'si', 'pa', 'ki'),('RED', 'ma', 'mag', 'si', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'pag', 'pa', 'ki'),('RED', 'ma', 'Pi', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'mag', 'pag', 'pa', 'ki'),('RED', 'ma', 'mag', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'ka', 'pag', 'pa', 'ki'),('RED', 'ma', 'ka', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'si', 'pag', 'pa', 'ki'),('RED', 'ma', 'si', 'pag', 'pa', 'ki'), None],
    [('RED', 'Pi', 'ka', 'pag', 'pa', 'ki'),('RED', 'Pi', 'ka', 'pag', 'pa', 'ki'), None],
    [('RED', 'Pi', 'si', 'pag', 'pa', 'ki'),('RED', 'Pi', 'si', 'pag', 'pa', 'ki'), None],
    [('RED', 'mag', 'ka', 'pag', 'pa', 'ki'),('RED', 'mag', 'ka', 'pag', 'pa', 'ki'), None],
    [('RED', 'mag', 'si', 'pag', 'pa', 'ki'),('RED', 'mag', 'si', 'pag', 'pa', 'ki'), None],
    [('ma', 'Pi', 'ka', 'pag', 'pa', 'ki'),('ma', 'Pi', 'ka', 'pag', 'pa', 'ki'), None],
    [('ma', 'Pi', 'si', 'pag', 'pa', 'ki'),('ma', 'Pi', 'si', 'pag', 'pa', 'ki'), None],
    [('ma', 'mag', 'ka', 'pag', 'pa', 'ki'),('ma', 'mag', 'ka', 'pag', 'pa', 'ki'), None],
    [('ma', 'mag', 'si', 'pag', 'pa', 'ki'),('ma', 'mag', 'si', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'ka', 'pag', 'pa', 'ki'),('RED', 'ma', 'Pi', 'ka', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'Pi', 'si', 'pag', 'pa', 'ki'),('RED', 'ma', 'Pi', 'si', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'mag', 'ka', 'pag', 'pa', 'ki'),('RED', 'ma', 'mag', 'ka', 'pag', 'pa', 'ki'), None],
    [('RED', 'ma', 'mag', 'si', 'pag', 'pa', 'ki'),('RED', 'ma', 'mag', 'si', 'pag', 'pa', 'ki'), None],
)
