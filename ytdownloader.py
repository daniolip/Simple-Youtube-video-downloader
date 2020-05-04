import sys
from pytube import YouTube

def SelectResolution(yt_list):
    # Function to select resolution of yt video

    # Listing resolutions
    res_list = []
    for item in yt_list:
        if((item.resolution not in res_list) and (item.resolution is not None)):
            res_list.append(item.resolution)
    res_list.sort()
    # print(res_list)

    # Prompting which resolution to use
    selected_resolution  = -1
    if(len(res_list) > 1):
        print("Which resolution do you want?")
        x = 1
        for item in res_list:
            print(f'{x} = {item}')
            x=x+1
        selected_resolution = int(input()) - 1
        if(selected_resolution < 0 or selected_resolution > len(res_list)):
            print("Invalid option")
            sys.exit(0)
    elif(len(res_list) == 1):
        print("Resolution selected:",res_list[0])
        selected_resolution = 0
    else:
        print("Something is wrong (no resolution available)")
        sys.exit(0)

    return yt_list.filter(resolution=res_list[selected_resolution]), res_list[selected_resolution]
    
def SelectType(yt_list):
    type_list = []
    for item in yt_list:
        if(item.type not in type_list):
            type_list.append(item.type)
    type_list.sort()
    

    # Which type to use
    if(len(type_list) > 1):
        print("Which type do you want?")
        x = 1
        for item in type_list:
            print(f'{x}. {item}')
            x = x + 1
        selected_type = int(input()) - 1
        if(selected_type < 0 or selected_type > len(type_list)):
            print("Invalid type")
            sys.exit(0)
    elif(len(type_list) == 1):
        print(f'Selected type:{type_list[0]}')
        selected_type = 0
    else:
        print("Something is wrong (no type available)")
        sys.exit(0)
    
    return yt_list.filter(type=type_list[selected_type]) , type_list[selected_type]

def SelectAbr(yt_list):

    # Getting all abrs
    abr_list = []
    for item in yt_list:
        if(item.abr not in abr_list):
            abr_list.append(item.abr)
    abr_list.sort()

    # Selecting Abr
    selected_abr = -1
    if(len(abr_list) > 1):
        print("What bitrate you want?")
        x = 1
        for item in abr_list:
            print(f'{x}. {item}')
            x = x + 1
        selected_abr = int(input()) - 1
        if(selected_abr < 0 or selected_abr > len(abr_list)):
            print("Invalid option")
            sys.exit(0)
    elif(len(abr_list) == 1):
        print(f'Format: {abr_list[0]}')
        selected_abr = 0
    else:
        print("Something is wrong (no abr available)")
        sys.exit(0)

    return yt_list.filter(abr=abr_list[selected_abr]), abr_list[selected_abr]

def SelectFormat(yt_list):

    # Getting all formats
    format_list = []
    for item in yt_list:
        if(item.mime_type not in format_list):
            format_list.append(item.mime_type)
    
    # Selecting format
    selected_format = -1
    if(len(format_list) > 1):
        print("What format you want?")
        x = 1
        for item in format_list:
            print(f'{x}. {item}')
            x = x + 1
        selected_format = int(input()) - 1
        if(selected_format < 0 or selected_format > len(format_list)):
            print("Invalid option")
            sys.exit(0)
    elif(len(format_list) == 1):
        print(f'Format: {format_list[0]}')
        selected_format = 0
    else:
        print("Something is wrong (no format available)")
        sys.exit(0)

    return yt_list.filter(mime_type=format_list[selected_format]), format_list[selected_format]

x = input("Please insert the video URL:")

# Example of URL
# x = "https://www.youtube.com/watch?v=PC19-Y-Mrg0"

# Getting the video from youtube
try:
    yt = YouTube(x).streams
except:
    print("Error on finding the video :(")
    sys.exit(0)

# Selecting video or audio
yt, type_selected = SelectType(yt)

# Selecting params for stream
if(type_selected == 'audio'):
    yt, selected_format = SelectFormat(yt)
    yt, selected_abr = SelectAbr(yt)
elif(type_selected == 'video'):
    yt, selected_resolution = SelectResolution(yt)
    yt, selected_format = SelectFormat(yt)    
else:
    print("Type unknown")
    sys.exit(0)

print(f"Filesize of selected stream: {yt.first().filesize/(10**6):.2f} MBs")
try:        
    if(input("Are you sure you want to download this? (y/n)") is 'y'):
        yt.first().download()
        print("Download finished")
    else:
        print("Download aborted")
except:
    print("Download failed :(")