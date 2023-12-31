import simplekml
import pandas as pd
import datetime




# coordinates
# ↓Cesiumに乗せると少しずれる.GoogleEearthだとずれない
p1 = 138.82706266806662,34.59603674056423 # lower left
p2 = 138.99058958779398,34.595488882483906 # lower right
p3 = 138.99122728802018,34.70366797605449 # upper right
p4 = 138.8274878169426,34.704218037168786 # upper left

# p1 = 138.82706,34.596036 # lower left
# p2 = 138.99058,34.595488 # lower right
# p3 = 138.99110,34.703400 # upper right
# p4 = 138.82748,34.704018 # upper left

output_file='./01_main_pres-10y_v005_dslip1.04.kml'
path_fig = './png/01_main_pres-10y_v005_dslip1.04/'

csv_file='filelist.csv'
df = pd.read_csv(csv_file,header=0,encoding='shift-jis')
df['time_start'] = pd.to_datetime(df['time_start'])
df['time_end'] = pd.to_datetime(df['time_end'])
df['time_start']=df['time_start'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')
df['time_end']=df['time_end'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')

# make kmloverlay
kml = simplekml.Kml()
for n,fig in enumerate(df['fig']):
    ground = kml.newgroundoverlay(name='Image')
    ground.icon.href = path_fig + df.loc[n,'fig']

    ground.gxlatlonquad.coords = [(p1),(p2),(p3),(p4)]
    ground.timespan.begin = df.loc[n,'time_start']
    ground.timespan.end   = df.loc[n,'time_end']

    ground.altitudemode = 'relativeToGround'
   #ground.altitudemode = 'absolute'
   #ground.altitudemode = 'clampToGround'

kml.save(output_file)
print(output_file)

