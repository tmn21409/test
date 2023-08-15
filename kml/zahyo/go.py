import pyproj
 

# 平面直角座標系の座標を取得


point = [
 "30000, -155700", # 左下
 "45000, -155700", # 右下
 "45000, -143700", # 右上
 "30000, -143700"  # 左上
]



# 座標変換を行う
with open('a.out','w') as f:
    for a in point : 
        x,y = a.split(',')
    
        transformer = pyproj.Transformer.from_crs("epsg:6676", "epsg:4326", always_xy=True)
        lon,lat = transformer.transform(x, y)
    
        f.write("{0},{1}\n".format(lon, lat))
