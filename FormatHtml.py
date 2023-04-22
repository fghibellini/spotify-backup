
import dominate
from dominate.tags import *
from datetime import datetime

def outputAsHtml(file, playlists):
	backup_time = datetime.now()
	title = 'Spotify backup from %s' % backup_time.strftime("%d/%m/%Y %H:%M:%S")
	doc = dominate.document(title=title)

	with doc.head:
	    link(rel='stylesheet', href='style.css')
	    script(type='text/javascript', src='script.js')

	with doc:
	    with div(id='header'):
	        h1(title)

	    with div():
	        attr(cls='playlists')
	        for playlist in playlists:
	            with div():
	                attr(cls='playlist')
	                h2(playlist['name'])
	                for track in [ t for t in playlist['tracks'] if not (t['track'] is None) ]:
	                    with div():
	                        attr(cls='track')
	                        with div():
	                            attr(cls='thumbnail')
	                            thumbnail_image = getTrackThumbnail(track['track'])
	                            if not (thumbnail_image is None):
	                                img(src = thumbnail_image['url'])
	                        with div():
	                            attr(cls='track-name-column')
	                            external_url = track['track']['external_urls'].get('spotify', None)
	                            a(track['track']['name'], href=external_url)
	                        with div():
	                            attr(cls='artists')
	                            for artist in track['track']['artists']:
	                                span(artist['name'], cls='artist')
	                        with div():
	                            attr(cls='album')
	                            span(track['track']['album']['name'])

	file.write(str(doc))


def getTrackThumbnail(track):
	images = track.get('album', {}).get('images', [])
	return sorted(images, key=lambda x: x['width'], reverse=False)[0] if len(images) > 0 else None
