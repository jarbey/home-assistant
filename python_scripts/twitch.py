streamInput = data.get('stream_name').split(' ', 1)[0].lower()
chromecast = data.get('chromecast');

streams = {
    "gaming": "ogamingsc2",
    "ogaming": "ogamingsc2",
    "starcraft": "ogamingsc2",
    "yogo": "docteuryogo",
    "yugo": "docteuryogo",
    "logo": "docteuryogo",
}

if streamInput in streams:
    streamToCast = streams[streamInput]
else:
    streamToCast = streamInput

url = "https://twitch.tv/"+streamToCast

logger.warning("Streaming {} on {}".format(url, chromecast))
hass.services.call("media_extractor", "play_media", {"entity_id": "media_player.{}".format(chromecast), "media_content_id": url, "media_content_type": "video"})

