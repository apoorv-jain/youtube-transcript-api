import sys

import os


class SrtFormatter():
    def _secs_to_minutes_hours(self , time):
        add_formatting = lambda a: '0' + a if len(a) == 1 else a
        milli_secs = time - int(time)
        secs = add_formatting(str(int(time)%60))
        mins = add_formatting((int(time)//60).__str__())
        hours = add_formatting((int(time)//3600).__str__())

        return f"{hours}:{mins}:{secs},{int(milli_secs*1000)}"
    def _format(self, transcript_data):
        prev_time = 0
        final_srt = ''
        for index,each in enumerate(transcript_data) :
            start_time = each['start']
            end_time = each['start'] + each['duration']
            final_srt += f"{index+1}\n"
            final_srt += f'{self._secs_to_minutes_hours(start_time)} --> {self._secs_to_minutes_hours(end_time)}\n'
            final_srt += each['text'] + '\n\n'
        return final_srt
    def format_and_save(self , transcript_data , location = os.getcwd() , file_name = r'Transcript'):
        file_name +=r'.srt'
        path_list = location.split(os.sep)
        final_path = os.sep.join(path_list) + "/" + file_name
        with open(final_path, 'w', encoding = "utf-8") as srt_file:
            final_srt = self._format(transcript_data)
            srt_file.write(final_srt)
            srt_file.close()
