from formatting import SrtFormatter

from youtube_transcript_api import YouTubeTranscriptApi
import os

video_id = "8W32z8Xq-dA"
# trans = YouTubeTranscriptApi.get_transcripts([video_id], languages=['es'])
# print(trans)
trans = YouTubeTranscriptApi.get_transcripts([video_id], languages=['en'])
print(trans)
print(SrtFormatter()._format(trans[0][video_id]))
SrtFormatter().format_and_save(trans[0][video_id] , location = r'C:\Users\User\Desktop' , file_name=r'subt')
