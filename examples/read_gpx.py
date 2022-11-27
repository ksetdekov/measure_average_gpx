import gpxpy.gpx

gpx_file = open("data/activity_10044912854.gpx", 'r')

gpx = gpxpy.parse(gpx_file)
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print(
                f'Point at with time {point.time} at ({point.latitude},{point.longitude}) elevation {point.elevation}')
